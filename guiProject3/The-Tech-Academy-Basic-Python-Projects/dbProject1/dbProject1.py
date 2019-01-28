#
#Python:   3.7.2
#
#Author:   Cheyanne Rolfsson
#
#Purpose:  The Tech Academy - Python course, Creating script that creates a
#          database and adds new data into that database. 
#
#          Requirement 1:  Your script will need to use Python 3 and the sqlite3 module.
#          Requirement 2:  Your database will require 2 fields, an auto-increment primary 
#          integer field and a field with the datatype string.
#          Requirement 3:  Your script will need to read from the supplied list of file   
#          names at the bottom of this page and determine only the files from the list 
#          which ends with a “.txt” file extension.
#          Requirement 4:  Your script should add those file names from the list ending  
#          with “.txt” file extension within your database.
#          Requirement 5:  Your script should legibly print the qualifying text files to
#          the console.



import sqlite3


fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

textList = []


#  Create database and table 
conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_misc(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        files VARCHAR(255))")
    conn.commit



# Query .txt filenames
def getTextFile():
    for f in fileList:
        if f.endswith(".txt"):
            textList.append(f)
        
getTextFile()



# Insert .txt filenames into table
def dataEntry():
    for i in textList:
        cur.execute("INSERT INTO tbl_misc(col_files) VALUES(?)", (i,))
        conn.commit

dataEntry()



# Query database and print to console
with conn:
    cur.execute("SELECT * FROM tbl_misc")
    rows = cur.fetchall()
    for row in rows:
        msg = "File ID: {}, File Name: {}".format(row[0],row[1])
        print(msg)
    










