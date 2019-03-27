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
        self.treetitle=["level"]+list(datafield)
        self.currentitem=''
        self.frame_tree=ttk.Frame(self,width=500,height=300)
        #self.frame_tree.grid_propagate(0) # make width and height effect
        self.tree=ttk.Treeview(self.frame_tree,height=20)
        self.frame_info=ttk.Frame(self,width=400,height=200)
        self.frame_button=ttk.Frame(self)

        self.grid()
        self.createFrames()

    def createFrames(self):

        self.tree.grid()    #tree must put in a frame, otherwise it can't adjust dimension
        self.frame_info.grid_propagate(0)
        self.frame_tree.grid(row=0,column=0)
        self.frame_info.grid(row=0,column=1)
        self.frame_button.grid(row=1,column=0,columnspan=2)

        self.createButtons(self.frame_button)
        self.createTree()
        self.showdata(self.frame_info)

    def createTree(self):

        self.tree.configure(columns=self.datatitle)
        self.tree.column('#0',width=150)
        for i in self.datatitle:
            self.tree.heading(i,text=i)
            self.tree.column(i,width=80)

    def showdata(self,parentframe):
        datalist=[]
        for i in range(len(self.datatitle)):
            temptitle=ttk.Label(parentframe,text=self.datatitle[i])
            tempinfo= ttk.Label(parentframe,text="test....")
            temptitle.grid(row=i,column=0)
            tempinfo.grid(row=i,column=1)
            datalist.append(tempinfo)
        datas=dict(zip(self.datatitle,datalist))
        print(datas)

    def createButtons(self,parentframe):
        buttonnamelist=["Add After","Add Into","Delete","Copy","Cut","Paste",\
                         "Import","Export"]
        buttonlist=[]
        for i in range(len(buttonnamelist)):
            tempbutton=ttk.Button(parentframe,text=buttonnamelist[i])
            tempbutton.grid(row=0,column=i)
            buttonlist.append(tempbutton)
        self.buttons=dict(zip(buttonnamelist,buttonlist))

        self.buttons["Add After"].config(command=self.addItemAfter)
        self.buttons["Add Into"].config(command=self.addItemInto)
        pass    #bind others command in buttons


    def addItemAfter(self):
        self.currentitem=self.tree.focus()
        self.inputframe=InputDataDialog(self,*self.datatitle)
        self.inputframe.wait_window()
        mydata=self.inputframe.data

        if self.currentitem=="":
            parentitem=""
        else:
            parentitem=self.tree.parent(self.currentitem)
        self.tree.insert(parentitem,'end',text=mydata[0],values=mydata)

    def addItemInto(self):
        self.currentitem=self.tree.focus()
        self.inputframe=InputDataDialog(self,*self.datatitle)
        self.inputframe.wait_window()
        mydata=self.inputframe.data

        self.tree.insert(self.currentitem,'end',text=mydata[0],values=mydata)

class InputDataDialog(Toplevel):
    data=[]   #exchange data with others modules
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
            self.entrylist.append(b)
            a.grid(row=currentrow,column=0)
            b.grid(row=currentrow,column=1)
            currentrow +=1
        self.okButton=ttk.Button(self.frame, text="Ok",command=self.getdata)
        self.okButton.grid()

    def getdata(self):
        self.data=[]
        for i in self.entrylist:
            self.data.append(i.get())
        self.destroy()



a=["Part","description","Number","qty","sequence","status"]
#a=["sequence","*agrv","**kw"]

mainapp=TreeFrame(*a)
mainapp.title("Treeview window")
mainapp.mainloop()

