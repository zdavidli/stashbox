 
'''
Created on Jan 26, 2015
'''

import os, time, datetime, pickle

#data
WhiteList_zip = []
WhiteList_del = []
BlackList = []

curTime = datetime.datetime.now()
ZIP_AGE = 120
DEl_AGE = 300

ZipFileEndings = []
DelFileEndings = []

RunInterval = 600

__RUN = True


def DelDir(curDir):
    for root, directories, files in os.walk(curDir):
        for filename in files:
            if(shouldDel(filename)):
                #delete it!
                dropboxFilename= ""
                words = file.split("/")
                shouldAdd = false
                for word in words:
                    if word == "Dropbox":
                        shouldAdd = true
                        continue
                    if shouldAdd:
                        dropboxFilename+= "/" + word
                saveToDropbox(file, dropboxFilename)
                os.remove(file)
        for dirname in directories:
            if(dirname in WhiteList_del):
                WhiteList_del.remove(dirname)
            if(dirname not in BlackList and dirname not in WhiteList_zip):
                DelDir(dirname)

#similar method for ZipDir
def ZipDir(curDir):
    for root, directories, files in os.walk(curDir):
        for filename in files:
            if(shouldZip(filename)):
                #zip it
                print "shouldzip"
        for dirname in directories:
            if(dirname in WhiteList_zip):
                WhiteList_zip.remove(dirname)
            if(dirname not in BlackList and dirname not in WhiteList_del):
                ZipDir(dirname)

#checks if the file should be deleted, default is True
#False if: not a recognized file ending, or on a list other than WhiteList_Del
def shouldDel(file):
    accessTime = os.stat(file).st_atime
    if (curTime - accessTime < DEL_AGE):
        return False
    elif ((BlackList.contains(file)) or (WhiteList_zip.contains(file))):
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
    WhiteList_del = loadObject(".file_compress.data/.WhiteList_del.p")
    WhiteList_zip = loadObject(".file_compress.data/.WhiteList_zip.p")
    BlackList = loadObject(".file_compress.data/.BlackList.p")

    ZipFileEndings = loadObject(".file_compress.data/.ZipFileEndings.p")
    DelFileEndings = loadObject(".file_compress.data/.DelFileEndings.p")

    ZIP_AGE = loadObject(".file_compress.data/.ZIP_AGE.p")
    DEL_AGE = loadObject(".file_compress.data/.DEL_AGE.p")

    __RUN = loadObject(".file_compress.data/.__RUN.p")

def loadObject(filename):
    #will this correctly load the object?
    try:        
        with open(filename, 'r+') as input:
            return pickle.load(input)
    except IOError:
        print "File does not exist yet"   





loadData()
'''
for each entry in WhiteList_delete:
    DelDir(entry)
for each entry in WhiteList_zip:
    ZipDir(entry)
'''
