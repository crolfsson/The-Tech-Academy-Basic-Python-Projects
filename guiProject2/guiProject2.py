#
#Python:   3.7.2
#
#Author:   Cheyanne Rolfsson
#
#Purpose:  The Tech Academy - Python course, write a script that creates a GUI with a
#          button widget and a text widget. Your script will also include a function
#          that when it is called will invoke a dialog modal which will allow users
#          with the ability to select a folder directory from their system.  Finally,
#          your script will show the user’s selected directory path into the text field.
#
#          Requirement 1:  Your script will need to use Python 3 and the Tkinter module.
#          Requirement 2:  Your script will need to use the askdirectory() method from   
#          the Tkinter module.
#          Requirement 3:  Your script will need have a function linked to the button
#          widget so that once the button has been clicked will take the user’s selected
#          file path retained by the askdirectory() method and print it within your GUI’s
#          text widget.



from tkinter import *
from tkinter import filedialog
import tkinter as tk
import sqlite3
import os



class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        #  Window configuration
        self.master = master
        self.master.resizable(width=False,height=False)
        self.master.geometry("{}x{}".format(700,250))
        self.master.title("Check files")
        self.master.config(bg="#f0f7f9")

        
        # Text boxes
        self.txt_browse1 = tk.Entry(self.master,text='',width=60)
        self.txt_browse1.grid(row=1,column=1,columnspan=4,padx=(30,0),pady=(60,5),sticky='NSEW')
        self.txt_browse2 = tk.Entry(self.master,text='',width=60)
        self.txt_browse2.grid(row=2,column=1,columnspan=4,padx=(30,0),pady=(10,5),sticky='NSEW')


        #Buttons
        self.btn_browse1 = tk.Button(self.master,width=15,height=1,text='Browse...',command=self.ask_dir1)
        self.btn_browse1.grid(row=1,column=0,padx=(25,0),pady=(60,5),sticky=W)
        self.btn_browse2 = tk.Button(self.master,width=15,height=1,text='Browse...',command=self.ask_dir2)
        self.btn_browse2.grid(row=2,column=0,padx=(25,0),pady=(10,5),sticky=W)
        self.btn_check = tk.Button(self.master,width=15,height=2,text='Check for files...')
        self.btn_check.grid(row=3,column=0,padx=(25,0),pady=(10,10),sticky=W)
        self.btn_close = tk.Button(self.master,width=15,height=2,text='Close Program')
        self.btn_close.grid(row=3,column=4,padx=(25,0),pady=(10,10),sticky=E)


    # Browse1-Ask the user to select a folder.
    def ask_dir1(self):
        dir1 = filedialog.askdirectory(initialdir=os.getcwd())
        if len(dir1) > 0:
            self.txt_browse1.insert(0,dir1)


    # Browse2-Ask the user to select a folder.
    def ask_dir2(self):
        dir2 = filedialog.askdirectory(initialdir=os.getcwd())
        if len(dir2) > 0:
            self.txt_browse2.insert(0,dir2)



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root) 
    root.mainloop()
