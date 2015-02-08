

'''
Created on Jan 26, 2015
'''

import os, time, datetime, pickle, shutil, dropbox
import zipfile

global FILE_PREFIX
FILE_PREFIX = "/StashBox"

#data
global WhiteList_zip
global WhiteList_del 
global BlackList 

global curTime 
global ZIP_AGE 
global DEl_AGE 

global ZipFileEndings 
global DelFileEndings

global RunInterval

global client
global __RUN

def DelDir(curDir):
    #print "directory = " + curDir
    #for root, directories, files in walklevel(curDir, 1):
    for item in os.listdir(curDir):
        filename = item
        if os.path.isfile(os.path.join(curDir, item)):
            #print filename
            if(shouldDel(curDir+"/"+item)):
                #delete it!
                #print("should be deleting!")
                dropboxFilename= ""
                words = os.path.join(curDir, filename).split("/")
                shouldAdd = False
                for idx in range(0,len(words)):
                    word = words[idx]
                    #print word
                    if word == "Dropbox":
                        shouldAdd = True
                        continue
                    if shouldAdd:
                        dropboxFilename+= "/"
                        #if idx == len(words)-1:
                            #dropboxFilename+= FILE_PREFIX
                        dropboxFilename+= word
                if shouldAdd:
                    #print "pre-save to dropbox"
                    saveToDropbox(os.path.join(curDir, filename), FILE_PREFIX+dropboxFilename)
                    print "dropboxFilename =  "+FILE_PREFIX+dropboxFilename
                    os.remove(os.path.join(curDir, filename))
                    with open(os.path.join(curDir, filename + "_inDropbox"), 'w') as fout:
                        fout.write('')
        #for dirname in directories:
        if os.path.isdir(os.path.join(curDir, item)):
            dirname = item
            if(dirname in WhiteList_del):
                WhiteList_del.remove(dirname)
            if((os.path.join(curDir, dirname) not in BlackList) and (os.path.join(curDir, dirname) not in WhiteList_zip)):
                DelDir(os.path.join(curDir, dirname))

def ZipDir(curDir):
    #for root, directories, files in os.walk(curDir):
    ZipFiles = []
    for item in os.listdir(curDir):
    	filename = item        
    	if os.path.isfile(os.path.join(curDir, filename)):
            if (item in WhiteList_zip):
                WhiteList_zip.remove(item)
            if(shouldZip(curDir + "/" + filename)):
                #shutil.make_archive(filename, "zip", os.getcwd()) # creates a zip file
                #print "shouldzip"
                #os.remove(curDir + "/" + filename) # deletes original copy of files
                ZipFiles.append(filename)

        dirname = item
        if os.path.isdir(os.path.join(curDir, dirname)):
            if(dirname in WhiteList_zip):
                WhiteList_zip.remove(dirname)
            if((os.path.join(curDir, dirname) not in BlackList) and (os.path.join(curDir, dirname) not in WhiteList_del)):
                #if (dirname == curDir):
                    #print "the directories are equal"
                ZipDir(os.path.join(curDir, dirname))

    #ZIP ALL FILES IN 'ZipFiles'
    if (len(ZipFiles) == 0):
        return
    zip = zipfile.ZipFile(os.path.join(curDir, '_archive.zip'), 'w') #creates zip file
    for item in ZipFiles: #iterates through ZipFile list
    	zip.write(os.path.join(curDir, item), item) #writes each one in the zip file
    zip.close(); #closes the zipfile
    for item in ZipFiles:
        os.remove(os.path.join(curDir, item))


#checks if the file should be deleted, default is True
#False if: not a recognized file ending, or on a list other than WhiteList_Del
def shouldDel(file):
    #print "shouldDel("+file+")"
    global curTime
    global DEL_AGE
    accessTime = os.stat(file).st_atime
    print "age of " + file + "  = " + repr(curTime - accessTime) + "<" 
    print DEL_AGE
    if (curTime - accessTime < DEL_AGE):
        return False
    if ((file in BlackList) or (file in WhiteList_zip)):
        return False
    
    validEnding = False
    for ending in DelFileEndings:
        if file.endswith(ending):
            validEnding = True
            break
    if (not validEnding):
        return False

    return True

def shouldZip(file):
    accessTime = os.stat(file).st_atime
    if (curTime - accessTime < ZIP_AGE):
        return False
    elif (file.endswith(".zip")): # we don't want to look at already zipped files!
        return False
    elif ((file in BlackList) or (file in WhiteList_del)):
        return False

    validEnding = False
    for ending in ZipFileEndings:
        if file.endswith(ending):
            validEnding = True
            break
    if (not validEnding):
        return False

    return True

def loadData():
    #load each global var from disk
    global WhiteList_del
    global WhiteList_zip
    global BlackList
    global ZipFileEndings
    global DelFileEndings
    global curTime
    global ZIP_AGE
    global DEL_AGE
    global __RUN
    WhiteList_del = loadObject(".file_compress.data/.WhiteList_del.p")
    WhiteList_zip = loadObject(".file_compress.data/.WhiteList_zip.p")
    BlackList = loadObject(".file_compress.data/.BlackList.p")

    #THIS PART WILL BE TAKEN OUT IN THE FINAL VERSION
    ''' for item in WhiteList_del:
        item = os.path.join(os.getcwd(), item)
    for item in WhiteList_zip:
        item = os.path.join(os.getcwd(), item)
    for item in BlackList:
        item = os.path.join(os.getcwd(), item)'''

    ZipFileEndings = loadObject(".file_compress.data/.ZipFileEndings.p")
    DelFileEndings = loadObject(".file_compress.data/.DelFileEndings.p")

    curTime = time.mktime(datetime.datetime.now().timetuple())
    #print curTime

    ZIP_AGE = loadObject(".file_compress.data/.ZIP_AGE.p")
    DEL_AGE = loadObject(".file_compress.data/.DEL_AGE.p")

    __RUN = loadObject(".file_compress.data/.__RUN.p")
    #print WhiteList_del


def loadObject(filename):
    try:        
        with open(filename, 'r+') as input:
            return pickle.load(input)
    except IOError:
        print "File does not exist yet"  

def saveObject(obj, filename):
    with open(filename, 'w+') as output:
        pickle.dump(obj,output,-1) 

def saveToDropbox(obj, uploadPath):
    global client
    with open(obj, 'rb') as f:
        response = client.put_file(uploadPath, f)
    #print response


def setupAuthentication():
    global client
    #app_key = "9s7hb21rv9udehc"
    #app_secret = "d0grqcxuf3rnzmb"

    app_key = "ht7nrglcmelcuhu"
    app_secret = "rmjtru5i7es7reu"

    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
    # Have the user sign in and authorize this token
    authorize_url = flow.start()
    print '1. Go to: ' + authorize_url
    print '2. Click "Allow" (you might have to log in first)'
    print '3. Copy the authorization code.'
    code = raw_input("Enter the authorization code here: ").strip()
    access_token, user_id = flow.finish(code)
    client = dropbox.client.DropboxClient(access_token)
    print 'linked account: ', client.account_info()
    saveObject(client, ".file_compress.data/.client.p")



loadData()
global client
authenticated = False;
authenticated = loadObject("./.file_compress.data/.authenticated.p")
#print authenticated
if (not authenticated):
    setupAuthentication()
    authenticated = True;
    saveObject(authenticated, "./.file_compress.data/.authenticated.p")
client = loadObject("./.file_compress.data/.client.p")

#print len(WhiteList_del)
for entry in WhiteList_del:
    #print os.getcwd()+"/"+entry
    DelDir(entry)
for entry in WhiteList_zip:
    ZipDir(entry)

