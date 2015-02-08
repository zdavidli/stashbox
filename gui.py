import file_dialog
import sys
import file_compressor

from Tkinter import *
import tkMessageBox
# TODO Make sure zip_list, del_list, blacklist have no conflicts
# TODO KNOWN ISSUE: Message boxes don't close and leave some "residue"


# <<<Set ZipList>>>
zip_list = []
del_list = []
blacklist = []
dir_selected = ""
def set_ziplist():
    tkMessageBox.showinfo("Choose directories", "Choose directories to be compressed by stashBox")
    while True:
        dir_selected = file_dialog.choose_dir("Choose directories for compression")
        try:
            len(dir_selected) != 0
            zip_list.append(dir_selected)
        except TypeError,ValueError:
            if tkMessageBox.askyesno("Continue", "Continue selecting directories?"):
                continue
            else:
                break

def set_dellist():
    tkMessageBox.showinfo("Choose directories", "Choose directories for cloud storage by stashBox")
    while True:
        dir_selected = file_dialog.choose_dir("Choose directories for cloud storage")
        try:
            len(dir_selected) != 0
            del_list.append(dir_selected)
        except TypeError,ValueError:
            if tkMessageBox.askyesno("Continue", "Continue selecting directories?"):
                continue
            else:
                break

def set_blacklist():
    tkMessageBox.showinfo("Choose directories", "Choose directories to be ignored by Stashbox")
    while True:
        dir_selected = file_dialog.choose_dir("Choose directories to ignore")
        try:
            len(dir_selected) != 0
            blacklist.append(dir_selected)
        except TypeError,ValueError:
            if tkMessageBox.askyesno("Continue", "Continue selecting directories?"):
                continue
            else:
                break

def get_ziplist():
    return zip_list

def get_dellist():
    return del_list

def get_blacklist():
    return blacklist

def save_lists():
    file_compressor.saveObject(zip_list, ".file_compress.data/.WhiteList_zip.p")
    file_compressor.saveObject(del_list, ".file_compress.data/.WhiteList_del.p")
    file_compressor.saveObject(blacklist, ".file_compress.data/.BlackList.p")


if __name__ == "__main__":
    set_ziplist()
    set_dellist()
    set_blacklist()
    print get_ziplist()
    print get_dellist()
    print get_blacklist()
    save_lists()


