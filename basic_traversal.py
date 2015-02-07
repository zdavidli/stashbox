# We only need to import this module
import os.path
 
# The top argument for walk. The
# Python27/Lib/site-packages folder in my case

topdir= raw_input("Choose a directory: ")

# The arg argument for walk, and subsequently ext for step

exten = raw_input("Choose an extension (include the .): ")
 
def step(ext, dirname, names):
    ext = ext.lower()
 
    for name in names:
        if name.lower().endswith(ext):
            print(os.path.join(dirname, name))
 
# Start the walk
os.path.walk(topdir, step, exten)
