import file_dialog
import sys
from Tkinter import *
import tkMessageBox

# <<<Set ZipList>>>
zip_list = []
del_list = []
black_list = []
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

if __name__ == "__main__":
    print "start"
    set_ziplist()
    set_dellist()
    set_blacklist()
    print "done"



