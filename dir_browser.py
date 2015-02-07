import os
from Tkinter import Tk
import tkFileDialog
toplevel = Tk()
toplevel.withdraw()
dirname = tkFileDialog.askdirectory(title="Whitelist directories")
if os.path.isdir(dirname):
    print os.path.abspath(dirname)
else: print 'No file chosen'
raw_input('Ready, push Enter')
