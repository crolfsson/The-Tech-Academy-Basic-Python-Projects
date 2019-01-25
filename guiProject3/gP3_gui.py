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
import tkinter as tk
import gP3_main
import gP3_functions


def load_gui(self):
    # Labels
    self.lbl_source = tk.Label(self.master,text='Source Directory:',bg="#f0f7f9")
    self.lbl_source.grid(row=1,column=0,padx=(57,0),pady=(65,20),sticky=N+W)
    self.lbl_destination = tk.Label(self.master,text='Destination Directory:',bg="#f0f7f9")
    self.lbl_destination.grid(row=3,column=0,padx=(27,0),pady=(10,0),sticky=N+W)


    # Text boxes
    self.txt_source = tk.Entry(self.master,text='',width=60)
    self.txt_source.grid(row=1,column=1,columnspan=4,padx=(10,0),pady=(65,10),sticky='NSEW')
    self.txt_destination = tk.Entry(self.master,text='',width=60)
    self.txt_destination.grid(row=3,column=1,columnspan=4,padx=(10,0),pady=(5,5),sticky='NSEW')


    #Buttons
    self.btn_source = tk.Button(self.master,width=15,height=1,text='Browse...',command=lambda: gP3_functions.onBrowse1(self))
    self.btn_source.grid(row=1,column=6,padx=(10,0),pady=(60,5),sticky=E)
    self.btn_destination = tk.Button(self.master,width=15,height=1,text='Browse...',command=lambda: gP3_functions.onBrowse2(self))
    self.btn_destination.grid(row=3,column=6,padx=(10,0),pady=(5,5),sticky=E)
    self.btn_move = tk.Button(self.master,width=15,height=1,text='Move files',command=lambda: gP3_functions.onMove(self))
    self.btn_move.grid(row=5,column=6,padx=(10,0),pady=(20,5),sticky=E)


    # Addtional functions
    gP3_functions.create_db(self)




if __name__ == "__main__":
    pass
