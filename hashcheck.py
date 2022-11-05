#!/usr/bin/python3
import hashlib
import sys
from collections import Counter
import os

def hash_file(filename):
   """"This function returns the MD5 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.md5()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()


def count_hashes(dir, delete=False):
    """This functions counts the number of
    duplicated files in a directory (recursive)"""
    l = []
    dup = 0
    for r, d, f in os.walk(dir):
        for file in f:
            #if file.endswith(".jpg"):
            fullp = os.path.join(r, file)
            hash = hash_file(fullp)
            if hash in l:
                dup +=1
                print(f"Duplicate file {fullp}")
                if delete:
                    os.remove(fullp)

            else:
                l.append(hash)
    return dup



if __name__ == "__main__":
    hc = count_hashes(sys.argv[1], len(sys.argv) > 2)
    print(f"Total Dups: {hc}")
