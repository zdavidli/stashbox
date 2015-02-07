# file_zip.py

import os, zipfile, shutil

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
