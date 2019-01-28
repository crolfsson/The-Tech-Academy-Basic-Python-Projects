#
#Python:   3.7.2
#
#Author:   Cheyanne Rolfsson
#
#Purpose:  The Tech Academy - Python course, Creating script that will check
#          a specific folder on the hard drive, verify the ".txt" file extension,
#          and print those files names and time-stamps to the console. 
#
#          Requirement 1:  Your script will need to use Python 3 and the OS module.
#          Requirement 2:  Your script will need to use the listdir() method from the 
#          OS module to iterate through all files within a specific directory.
#          Requirement 3:  Your script will need to use the path.join() method from 
#          the OS module to concatenate the file name to its file path, forming an absolute path.
#          Requirement 4:  Your script will need to use the getmtime() method from the 
#          OS module to find the latest date that each text file has been created or modified.
#          Requirement 5:  Your script will need to print each file ending with a
#          “.txt” file extension and its corresponding mtime to the console.


import datetime
import os


fPath = "C:\\Users\\rolfsson\\Documents\\GitHub\\PyProjects\\python_projects\\fileProject"



def getFileList():
    for f in os.listdir(fPath):
        if f.endswith(".txt"):
            newPath = os.path.join(fPath,f)
            modTime = datetime.datetime.fromtimestamp(os.path.getmtime(newPath))
            print("File name: ", newPath)
            print("Date last modified: ", modTime)



if __name__ == '__main__':
    getFileList()





