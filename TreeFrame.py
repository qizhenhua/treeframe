from tkinter import *
from tkinter import ttk

""" 
This program is a test for data with level 
It written by QiZhenHua in 20190316
"""

class TreeFrame():
   def __init__(self,myparent,*datafield):
         
        self.frame_tree=ttk.Frame(myparent)
        self.frame_button=ttk.Frame(myparent)

        self.tree=ttk.Treeview(self.frame_tree)
        self.button_add=ttk.Button(self.frame_button,text="Add")
        self.button_del=ttk.Button(self.frame_button,text="Delte")

        self.tree.configure(columns=["level"]+list(datafield))

        self.frame_tree.grid(row=0,column=1)
        self.frame_button.grid(row=0,column=2)
        self.tree.grid()
        self.button_add.grid()
        self.button_del.grid()
        



root=Tk()
root.title("TreeFrame")
a=["Part","Number","qty"]

myFrame=TreeFrame(root,*a)

root.mainloop()

