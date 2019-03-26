#!/usr/bin/env python
"""
HashComp v0.7
Author:@V1K1NG (Brandon Schwandt)
Date:3/25/2019
Tested with Python 2.7.16 and 3.7.3 on Win7 and Kali Linux

Program iterates through a file structure starting at the given directory and hashes files.
Hashes are compared to dictionary and entered if not found.
If matching hash is found filepath is added to the list of files matching the hash.
*********************************************************************************************************
"""

import hashlib										#pulls in the hashing lib
import os											#pulls in os interaction lib
import sys											#pulls in sys lib to get command line args

filenames = []										#data structure/variable declarations
hashes = {}
path = ""
filehash = ""
BLOCKSIZE = 65535 									#limits blocksize to keep RAM usage in check

try:												#map v3 input to raw input so all python works
    input = raw_input
except NameError:
    pass

if len(sys.argv) == 1:								#checking command line for root dir or prompt for it
	path = input("Please input the root directory to scan:")
elif len(sys.argv) > 2:
	print("This probably won't work quite right, only 1 argument expected. \nLets try! Using the first argument...")
	path = sys.argv[1]
else:
	path = sys.argv[1]

print("Scanning root directory:" + path)			#originally debugging but good output so left this in

for root, dir_names, file_names in os.walk(path):	#populates filenames[] with the filepaths from os.walk output
	for files in file_names:
		filenames.append(os.path.join(root, files))

for item in filenames:								#iterates through files
	try:
		with open(item, 'rb') as afile:				#opens file as bitstream
			hasher = hashlib.md5()					#preps hashing construct
			buf = afile.read(BLOCKSIZE)
			while len(buf) > 0:						#reads file while data still present
				hasher.update(buf)
				buf = afile.read(BLOCKSIZE)
			filehash = hasher.hexdigest()			#performs hash and stores 
			if filehash in hashes:					#checks if hash is in dict and appends file path if so
				hashes[filehash].append(item)
			else:									#if not in dict creates entry based on hash value
				hashes[filehash] = [item]
			afile.close()							#closes file to keep RAM usage down
	except IOError as err:							#error catching and mildly verbose output
		print("I/O error({0}: {1} ".format(err.errno, err.strerror) + item + " had bad chars and was not processed")
for hashval, files in hashes.items():
	print(hashval, files)							#prints output to screen as a hash value and a list of files. Can be CSV'd to analyze