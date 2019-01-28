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




from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import sqlite3
import os
import datetime
import gP3_gui
import gP3_functions


class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self, master, *args, **kwargs)

        #  Window configuration
        self.master = master
        self.master.resizable(width=False,height=False)
        self.master.geometry("{}x{}".format(850,250))
        gP3_functions.center_window(self,850,250)
        self.master.title("Move Text Files")
        self.master.config(bg="#f0f7f9")


        # Delete Window 
        self.master.protocol("WM_DELETE_WINDOW", lambda: gP3_functions.ask_quit(self))
        arg = self.master


        # GUI Widgets
        gP3_gui.load_gui(self)



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root) 
    root.mainloop()
