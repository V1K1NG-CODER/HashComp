HashComp v0.7
Author:@V1K1NG (Brandon Schwandt)
Date:3/25/2019
Tested with Python 2.7.16 and 3.7.3 on Win7 and Kali Linux

The main function of this code is to take and input directory, traverse it for all files, hash the files and compare the hashes for duplicate files. 

Use case: Many flash drives with identical images with different names were copied into a common folder. 
Going through these manually to find duplicates was time intensive and prone to errors.
Coded this to create a quick output I could used to speed up the de-duplication process. 
Output is normally piped into a file and treated as a CSV for analysis.
Output is not 100% clean yet but the paths are there and things are functional. 

This is a quick project to familiarize myself with github using a project I've wanted to tackle for a while. 
I have not looked into security implications of accepting files or any other aspect of code yet, USE AT YOUR OWN RISK. 

Tested in Windows and Linux for compatibility with current Python v2 and v3. Tested against both internal and external drives. Ran against 3TB on each and code ran to completion and created expected output. While viewing file noticed 232600 items exactly, may look into to make sure this is a coincidence or an issue importing large amounts of data into the viewing tool. 

Early development:
Error handling of bad chars in filenames and directories
Used BLOCKSIZE to limit RAM usage
Remapped raw_input so that code is usable in v2 and v3 without changes
Added command line functionality

Improvements envisioned:
Better input handling
-Multiple directories
-Omit directories
Automated deletion of duplicates (EXTREME CAUTION)
-Ability to select primary files tree to keep
Print output as processing so if program stops running data is stored in file and not lost in memory
Output to file instead of stdout(file redirection working fine at the moment)
Introduce functions to reduce visible nesting and increase modularization
Limit the scope of the error catching to just the file open 
Investigate processing overhead to change from md5
Clean up output starting with removing the 'list' chars 