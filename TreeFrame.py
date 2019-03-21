#!/usr/bin/env python3
"""
This program is a test for data with level
It written by QiZhenHua in 20190316
"""

from tkinter import *
from tkinter import ttk


class TreeFrame(ttk.Frame):
    def __init__(self,myparent,*datafield):
        ttk.Frame.__init__(self,master=None)
        self.grid()
        self.treetitle=["level"]+list(datafield)
        self.createWidgets(myparent)

    def createWidgets(self,myparent):
        self.frame_tree=ttk.Frame(myparent)
        self.frame_button=ttk.Frame(myparent)
        self.frame_tree.grid(row=0,column=1)
        self.frame_button.grid(row=0,column=2)

        self.tree=ttk.Treeview(self.frame_tree)
        self.button_add=ttk.Button(self.frame_button,text="Add",command=self.addItem)
        self.button_del=ttk.Button(self.frame_button,text="Delte")

        self.tree.grid()
        self.button_add.grid()
        self.button_del.grid()

        self.tree.configure(columns=self.treetitle)
        self.tree.column('#0',width=50)
        for i in self.treetitle:
            self.tree.heading(i,text=i)


    def addItem(self):
        self.grid_remove()
        inputframe=InputDataFrame()
        inputframe.grid()
        # self.tree.insert('','end',text="test")

class InputDataFrame(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.frame=ttk.Frame(self)
        self.frame.grid()
        self.createWidgets()
        #self.mainloop()

    def createWidgets(self):
        self.quitButton=ttk.Button(self.frame, text="Quit",command=self.quit)
        self.quitButton.grid()

root=Tk()
root.title("TreeFrame")
a=["Part","Number","qty"]

myFrame=TreeFrame(root,*a)

root.mainloop()

