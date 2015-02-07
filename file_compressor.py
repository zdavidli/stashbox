 
'''
Created on Jan 26, 2015
'''

#data

loadData()
for each entry in WhiteList_delete:
    DeleteDir(entry)
for each entry in WhiteList_zip:
    ZipDir(entry)

def DelDir(curDir):
    for each file in curDir: #NEED SOME WAY OF ITERATING HERE
        if (shouldDel(file)):
            #delete the file

        if (!BlackList.contains(dir) and !WhiteList_zip.contains(dir)):
            DelDir(dir)

#similar method for ZipDir
def ZipDir(curDir):


def shouldDel(file):
    

def shouldZip(file):


def loadData():
