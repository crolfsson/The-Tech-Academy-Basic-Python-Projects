#
#Python:   3.7.2
#
#Author:   Cheyanne Rolfsson
#
#Purpose:  The Tech Academy - Python course, Creating script that creates a
#          database and adds new data into that database. 
#
#          Requirement 1:  Your script will need to use Python 3 and the Tkinter module.
#          Requirement 2:  Your script will need to re-create an exact copy of a GUI  
#          from the supplied image at the bottom of this page.


from tkinter import *
import tkinter as tk
import sqlite3


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
        self.btn_browse1 = tk.Button(self.master,width=15,height=1,text='Browse...')
        self.btn_browse1.grid(row=1,column=0,padx=(25,0),pady=(60,5),sticky=W)
        self.btn_browse2 = tk.Button(self.master,width=15,height=1,text='Browse...')
        self.btn_browse2.grid(row=2,column=0,padx=(25,0),pady=(10,5),sticky=W)
        self.btn_check = tk.Button(self.master,width=15,height=2,text='Check for files...')
        self.btn_check.grid(row=3,column=0,padx=(25,0),pady=(10,10),sticky=W)
        self.btn_close = tk.Button(self.master,width=15,height=2,text='Close Program')
        self.btn_close.grid(row=3,column=4,padx=(25,0),pady=(10,10),sticky=E)





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root) 
    root.mainloop()
