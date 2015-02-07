 
'''
Created on Jan 26, 2015
'''

import os, time, datetime, pickle, shutil

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

__RUN = True


def DelDir(curDir):
    print "Hi"
    for root, directories, files in os.walk(curDir):
        print "hi"
        for filename in files:
            print filename
            if(shouldDel(curDir+"/"+filename)):
                #delete it!
                print("should be deleting!")
                dropboxFilename= ""
                words = filename.split("/")
                shouldAdd = False
                for word in words:
                    if word == "Dropbox":
                        shouldAdd = True
                        continue
                    if shouldAdd:
                        dropboxFilename+= "/" + word
                #saveToDropbox(file, dropboxFilename)
                os.remove(curDir + "/" + filename)
            else:
                print "should not delete " + filename
        for dirname in directories:
            if(dirname in WhiteList_del):
                WhiteList_del.remove(dirname)
            if(dirname not in BlackList and dirname not in WhiteList_zip):
                DelDir(dirname)

#similar method for ZipDir
def ZipDir(curDir):
    for root, directories, files in os.walk(curDir):
        for filename in files:
            if(shouldZip(filename) && !filename.endswith("zip")):
                shutil.make_archive(filename, "zip", os.getcwd())
                print "shouldzip"
                os.remove(filename)
        for dirname in directories:
            if(dirname in WhiteList_zip):
                WhiteList_zip.remove(dirname)
            if(dirname not in BlackList and dirname not in WhiteList_del):
                ZipDir(dirname)

#checks if the file should be deleted, default is True
#False if: not a recognized file ending, or on a list other than WhiteList_Del
def shouldDel(file):
    global curTime
    accessTime = os.stat(file).st_atime
    if (curTime - accessTime < DEL_AGE):
        return False
    elif ((file in BlackList) or (file in WhiteList_zip)):
        return False
    return True

def shouldZip(file):
    accessTime = os.stat(file).st_atime
    if (curTime - accessTime < ZIP_AGE):
        return False
    elif ((BlackList.contains(file)) or (WhiteList_del.contains(file))):
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

    ZipFileEndings = loadObject(".file_compress.data/.ZipFileEndings.p")
    DelFileEndings = loadObject(".file_compress.data/.DelFileEndings.p")

    curTime = time.mktime(datetime.datetime.now().timetuple())
    print curTime

    ZIP_AGE = loadObject(".file_compress.data/.ZIP_AGE.p")
    DEL_AGE = loadObject(".file_compress.data/.DEL_AGE.p")

    __RUN = loadObject(".file_compress.data/.__RUN.p")
    print WhiteList_del
def loadObject(filename):
    #will this correctly load the object?
    try:        
        with open(filename, 'r+') as input:
            return pickle.load(input)
    except IOError:
        print "File does not exist yet"   





loadData()
print len(WhiteList_del)
for entry in WhiteList_del:
    print os.getcwd()+"/"+entry
    DelDir(os.getcwd()+"/"+entry)
for entry in WhiteList_zip:
    ZipDir(entry)

