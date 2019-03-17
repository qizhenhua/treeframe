from tkinter import *
from tkinter import ttk

""" 
This program is a test for data with level 
It written by QiZhenHua in 20190316
"""

class TreeFrame():
    root=Tk()
    root.title("TreeFrame")
    frame_tree=ttk.Frame(root)
    frame_button=ttk.Frame(root)

    tree=ttk.Treeview(frame_tree)
    button_add=ttk.Button(frame_button,text="Add")
    button_del=ttk.Button(frame_button,text="Delte")

    def __init__(self,*datafield):
        self.tree.configure(columns=["level"]+list(datafield))
        self.frame_tree.grid(row=0,column=1)
        self.frame_button.grid(row=0,column=2)
        self.tree.grid()
        self.button_add.grid()
        self.button_del.grid()
        self.root.mainloop()



a=["Part","Number","qty"]

myFrame=TreeFrame(*a)


