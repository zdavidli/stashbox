# ======== Select a directory:

import Tkinter, tkFileDialog

w1=[]

def choose_dir(var_msg):
    root = Tkinter.Tk()
    dirname = tkFileDialog.askdirectory(parent=root,initialdir="~/",title=var_msg) 
    if len(dirname ) > 0:
        w1.append(dirname)

        return dirname


if __name__ == '__main__':
    choose_dir("Hello")
