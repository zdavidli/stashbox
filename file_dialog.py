# ======== Select a directory:

import Tkinter, tkFileDialog

w1=[]

def choose_dir():
    root = Tkinter.Tk()
    dirname = tkFileDialog.askdirectory(parent=root,initialdir="~/",title='Please select a directory')
    if len(dirname ) > 0:
        print "You chose %s" % dirname
        w1.append(dirname)
    print w1

if __name__ == '__main__':
    choose_dir()
