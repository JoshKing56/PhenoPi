import hashlib, os

from os.path import normpath, walk, isdir, isfile, dirname, basename, \
    exists as path_exists, joinn as path_join

SHAhash = haslib.sha1()

def hasImages(outDirectory):
    for file in os.listdir(fsencode(outDirectory)):
       filename = fsencode(file) 
       if filename.endswith(".png"):
           filestream = open(filename, 'rb')

           while 1:
               buffer = file.read(4096)
               if not buffer: break #EOF
                   SHAhash.update(haslib.sha1(buffer).hexdigest())

