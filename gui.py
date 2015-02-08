from Tkinter import *
from ttk import *


w1 = ["/home/dli/", "/home/dli/git_web/"]
root = Tk() # create a top-level window

master = Frame(root, name='master') # create Frame in "root"
master.pack(fill=BOTH) # fill both sides of the parent

root.title('EZ') # title for top-level window
# quit if the window is deleted
root.protocol("WM_DELETE_WINDOW", master.quit)

nb = Notebook(master, name='nb') # create Notebook in "master"
nb.pack(fill=BOTH, padx=2, pady=3) # fill "master" but pad sides

# create each Notebook tab in a Frame
master_wl1 = Frame(nb, name='wl1')
Label(master_wl1, text="These are the whitelisted directories for cloud storage\n").pack(side=LEFT)
# Button to quit app on right
btn = Button(master_wl1, text="Edit", command=lambda arg1 = w1: edit_list(w1))
btn.pack(side=RIGHT)
nb.add(master_wl1, text="Whitelist 1") # add tab to Notebook

# repeat for each tab
master_wl2 = Frame(master, name='wl2')
Label(master_wl2, text="These are the whitelisted directories for compression").pack(side=LEFT)
btn = Button(master_wl2, text="Edit", command=master.quit)
btn.pack(side=RIGHT)
nb.add(master_wl2, text="Whitelist 2") #add tab

# one more
master_bl = Frame(master, name='bl')
Label(master_bl, text="These are the blacklisted directories for StashBox").pack(side=LEFT)
btn = Button(master_bl, text="Edit", command=master.quit)
btn.pack(side=RIGHT)
nb.add(master_bl, text="Blacklist")

def edit_list(mylist):
    top = Toplevel() 
    top.title("about this app")
    msg = Message(top, text="more about this app")
    msg.pack(side=LEFT)
    btn = Button(top, text="Dismiss", command=top.destroy)
    btn.pack(side=RIGHT)

# start the app
if __name__ == "__main__":
    master.mainloop() # call master's Frame.mainloop() method.
    #root.destroy() # if mainloop quits, destroy window
