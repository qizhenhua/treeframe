#!/usr/bin/env python3
"""
This program is a test for data with level
It written by QiZhenHua in 20190316
"""

from tkinter import *
from tkinter import ttk


class TreeFrame(Tk):
    def __init__(self,*datafield):
        Tk.__init__(self)
        self.grid()
        self.treetitle=["level"]+list(datafield)
        self.createWidgets()

    def createWidgets(self):
        self.frame_tree=ttk.Frame(self)
        self.frame_button=ttk.Frame(self)
        self.frame_tree.grid(row=0,column=1)
        self.frame_button.grid(row=1,column=1)

        self.tree=ttk.Treeview(self.frame_tree)
        self.button_add=ttk.Button(self.frame_button,text="Add",command=self.addItem)
        self.button_del=ttk.Button(self.frame_button,text="Delete")

        self.tree.grid()
        self.button_add.grid()
        self.button_del.grid()

        self.tree.configure(columns=self.treetitle)
        self.tree.column('#0',width=50)
        for i in self.treetitle:
            self.tree.heading(i,text=i)


    def addItem(self):
        self.inputframe=InputDataDialog(self,*self.treetitle)

        # self.tree.insert('','end',text="test")

class InputDataDialog(Toplevel):
    def __init__(self,parent,*datatitle):
        Toplevel.__init__(self,parent)
        self.title("Input Data:")
        self.grab_set()
        self.frame=ttk.Frame(self)
        self.frame.grid()
        self.createWidgets(*list(datatitle))

    def createWidgets(self,*datatitle):
        self.entrylist=[]
        currentrow=0
        for i in datatitle:
            a=ttk.Label(self.frame,text=i)
            b=ttk.Entry(self.frame)
            self.entrylist.append(a)
            a.grid(row=currentrow,column=0)
            b.grid(row=currentrow,column=1)
            currentrow +=1
        self.quitButton=ttk.Button(self.frame, text="Quit",command=self.destroy)
        self.quitButton.grid()



a=["Part","description","Number","qty","sequence","status"]
#a=["sequence","*agrv","**kw"]

mainapp=TreeFrame(*a)
mainapp.title("Treeview window")
mainapp.mainloop()

