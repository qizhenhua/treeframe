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
        self.datatitle=list(datafield)
        self.grid()
        self.treetitle=["level"]+list(datafield)
        self.createFrames()

    def createFrames(self):
        self.frame_tree=ttk.Frame(self,width=500,height=300)
        #self.frame_tree.grid_propagate(0) # make width and height effect
        self.tree=ttk.Treeview(self.frame_tree,height=20)
        self.tree.grid()    #tree must put in a frame, otherwise it can't adjust dimension
        self.frame_info=ttk.Frame(self,width=400,height=300)
        self.frame_info.grid_propagate(0)
        self.frame_button=ttk.Frame(self)
        self.frame_tree.grid(row=0,column=0)
        self.frame_info.grid(row=0,column=1)
        self.frame_button.grid(row=1,column=0,columnspan=2)

        self.createButtons(self.frame_button)
        self.createTree()

    def createButtons(self,parentframe):
        buttonnamelist=["Insert","Append","Delete","Addchild","Copy","Cut","Paste",\
                         "Import","Export"]
        buttonlist=[]
        for i in range(len(buttonnamelist)):
            tempbutton=ttk.Button(parentframe,text=buttonnamelist[i])
            tempbutton.grid(row=0,column=i)
            buttonlist.append(tempbutton)
        self.buttons=dict(zip(buttonnamelist,buttonlist))

        self.buttons["Insert"].config(command=self.insertItem)
        pass    #bind others command in buttons

    def createTree(self):

        self.tree.configure(columns=self.datatitle)
        self.tree.column('#0',width=50)
        for i in self.datatitle:
            self.tree.heading(i,text=i)
            self.tree.column(i,width=100)


    def insertItem(self):
        self.inputframe=InputDataDialog(self,*self.datatitle)
        self.inputframe.wait_window()
        print(self.inputframe.mydata)

        # self.tree.insert('','end',text="test")

class InputDataDialog(Toplevel):
    mydata=[]   #exchange data with others modules
    def __init__(self,parent,*datatitle):
        Toplevel.__init__(self,parent)
        self.title("Input Data:")
        self.grab_set()     # make the main window unvaliable
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
        self.quitButton=ttk.Button(self.frame, text="Quit",command=self.getdata)
        self.quitButton.grid()

    def getdata(self):
        self.mydata=[1,3,5,7]
        self.destroy()



#a=["Part","description","Number","qty","sequence","status"]
a=["sequence","*agrv","**kw"]

mainapp=TreeFrame(*a)
mainapp.title("Treeview window")
mainapp.mainloop()

