#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Python:   3.7.2
#
#Author:   Cheyanne Rolfsson
#
#Purpose:  The Tech Academy - For this drill, you will need to gather all of the drills
#          that you have previously completed for this course and write a new script that
#          will use each of the concepts that you had previously used to complete this
#          drill assignment.
#
#          Requirement 1:  Your script will need to use Python 3 and the Tkinter module.
#          Requirement 2:  Your script will need to use the listdir() method from the OS
#          module to iterate through all files within a specific directory.   
#          Requirement 3:  Your script will need to use the path.join() method from the
#          OS module to concatenate the file name to its file path, forming an absolute path.
#          Requirement 4:  Your script will need to use the getmtime() method from the OS
#          module to find out the latest date the file has been created or last modified.
#          Requirement 5:  Your script will need to create a database to record the
#          qualifying file and corresponding modified time-stamp
#          Requirement 6:  Your script will need print each file ending with a “.txt” file
#          extension and its corresponding mtime to the console.
#          Requirement 7:  Your script will need to use the move() method from the Shutil
#          module to cut all qualifying files and paste them within the destination directory.




from tkinter import *
from tkinter import filedialog
import tkinter as tk
import sqlite3
import shutil
import os
import datetime
import gP3_gui
import gP3_main


#=========================Window Functions================================

def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)



#=========================Database Functions=============================

def create_db(self):
    conn = sqlite3.connect('db_files.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname VARCHAR(255), \
            col_mdate TEXT \
            );")
        conn.commit()
    conn.close()


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_files""")
    count = cur.fetchone()[0]
    return cur,count


    
#======================Source Button Function==============================

# Ask the user to select a folder in source directory.
def onBrowse1(self):
    dir1 = filedialog.askdirectory(initialdir=os.getcwd())
    if len(dir1) > 0:
        source = self.txt_source.insert(0,dir1)



#====================Destination Button Function===========================

# Ask the user to select a folder in destination directory.
def onBrowse2(self):
    dir2 = filedialog.askdirectory(initialdir=os.getcwd())
    if len(dir2) > 0:
        destination = self.txt_destination.insert(0,dir2)



#====================Move Files Button Functions==========================

# Search source directory for .txt files and move to destination directory
def onMove(self):
    var_source = self.txt_source.get()
    var_destination = self.txt_destination.get()
    if (len(var_source) > 0) and (len(var_destination) > 0):
        for filename in os.listdir(var_source):
            if filename.endswith(".txt"):
                shutil.move(os.path.join(var_source,filename),var_destination)
                onClear(self)
    else:
        messagebox.showerror("Directory missing. Please select a Source or Destination directory.")
        onClear(self)



# Clears text in browse text boxes
def onClear(self):
    self.txt_source.delete(0,END)
    self.txt_destination.delete(0,END)



# Add time stamp, insert to database and print
def addFile(Self):
    var_destination = self.txt_destination.get()
    modTime = datetime.datetime.fromtimestamp(os.path.getmtime(var_destination))
    
    conn = sqlite3.connect('db_files.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(col_fname) FROM tbl_files WHERE col_fname = '{}'""".format(var_destination))
        count = cursor.fetchone()[0]
        chkFname = count
        if chkFname == 0:
            for i in var_destination:
                cursor.execute("""INSERT INTO tbl_files (col_fname,col_mdate) VALUES (?,?)""",(var_destination,modTime))
                print("File name: {}".format(var_destination))
                print("Modification date: {}".format(modTime))
    conn.commit()
    conn.close()




if __name__ == "__main__":
    pass
