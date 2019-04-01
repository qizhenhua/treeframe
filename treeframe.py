#!/usr/bin/env python3
"""
This program is a test for data with level
It written by QiZhenHua in 20190316
"""

from tkinter import *
from tkinter import ttk

class Treewithlevel(ttk.Treeview):
    """
    This module use level (an int) to set relationship of items, level will
    store to values[0], the set will make the data can readed by human.
    """
    def __init__(self,master=None):
        ttk.Treeview.__init__(self,master)
        self.treeitemlist=[]

    def deleteAllitems(self):
        for i in self.get_children(''):
            self.delete(i)
   
    def exportTreetofile(self,filename):
        self.treeitemlist=[]
        self.getTreeitems('',0) #get the whole tree's items
        myfile=open(filename,"w")
        for i in self.treeitemlist:
            myfile.writelines(str(i)+'\n')
        myfile.close()
 
    def getTreeitems(self,iid,level):
        #get children items and put it in treeitemlist
        for i in self.get_children(iid):
            a=self.item(i,"values")
            a=(level+1,)+a
            self.treeitemlist.append(a)
            if self.get_children(i):
                self.getTreeitems(i,level+1)

    def importTreefromfile(self,filename):
        treeitemlist=[]
        myfile=open(filename,'r')
        a=myfile.readlines()
        myfile.close()
        for i in a:
            treeitemlist.append(list(eval(i)))
        return treeitemlist

    def writeItemlisttotree(self,treeitemlist):
        previousiid=''
        previouselevel=''
        for i in treeitemlist:
            if i[0]==1:
                previousiid=self.insert('','end',text=i[1],values=i[1:])
                previouslevel=i[0]
            else:
                parent=self.whoisparent(previousiid,previouslevel,i[0])
                previousiid=self.insert(parent,'end',text=i[1],values=i[1:])
                previouslevel=i[0]

    def whoisparent(self,previid=None,prevlevel=None,mylevel=None):
        #This function will find the current items parent
        if mylevel==prevlevel:  #same level
            return self.parent(previid)
        elif mylevel > prevlevel:   #child
            return previid
        else:   #level is same as father or top
            return self.whoisparent(self.parent(previid),prevlevel-1,mylevel)
 
class TreeFrame(Tk):
    def __init__(self,*datafield):
        Tk.__init__(self)
        self.datatitle=list(datafield)
        #self.treetitle=["level"]+list(datafield)
        self.currentitem=''
        self.treeitemlist=[]
        self.frame_tree=ttk.Frame(self,width=500,height=300)
        #self.frame_tree.grid_propagate(0) # make width and height effect
        self.tree=Treewithlevel(self.frame_tree)
        self.frame_info=ttk.Frame(self,width=400,height=200)
        self.frame_button=ttk.Frame(self)

        self.grid()
        self.createFrames()

    def createFrames(self):
        self.tree.grid()    #tree must put in a frame, otherwise it can't adjust dimension
        ysb=ttk.Scrollbar(self.frame_tree,
                orient='vertical',command=self.tree.yview)
        xsb=ttk.Scrollbar(self.frame_tree,
                orient='horizontal',command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set,xscroll=xsb.set)
        ysb.grid(row=0,column=1,sticky='ns')
        xsb.grid(row=1,column=0,sticky='ew')
       
        self.frame_info.grid_propagate(0)
        self.frame_tree.grid(row=0,column=0)
        self.frame_info.grid(row=0,column=1)
        self.frame_button.grid(row=1,column=0,columnspan=2)

        self.createButtons(self.frame_button)
        self.createTree()
        self.showdata(self.frame_info)

    def createTree(self):
        self.tree.configure(height=20)
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

    def createButtons(self,parentframe):
        buttonnamelist=["Add After","Add Into","Modify","Move to","Delete","Copy","Cut","Paste", "Import","Export","Info"]
        buttonlist=[]
        for i in range(len(buttonnamelist)):
            tempbutton=ttk.Button(parentframe,text=buttonnamelist[i])
            tempbutton.grid(row=0,column=i)
            buttonlist.append(tempbutton)
        self.buttons=dict(zip(buttonnamelist,buttonlist))

        self.buttons["Add After"].config(command=self.addItemAfter)
        self.buttons["Add Into"].config(command=self.addItemInto)
        self.buttons["Modify"].config(command=self.modifyItem)
        self.buttons["Delete"].config(command=self.deleteItem)
        self.buttons["Export"].config(command=self.exportTree)
        self.buttons["Import"].config(command=self.importTree)
        pass    #bind others command in buttons
        self.buttons["Info"].config(command=self.getTreeinfo)

    def addItemAfter(self):
        self.currentitem=self.tree.focus()
        self.inputframe=InputDataDialog(self,self.datatitle,'')
        self.inputframe.wait_window()
        mydata=self.inputframe.data

        if self.currentitem=="":
            parentitem=""
        else:
            parentitem=self.tree.parent(self.currentitem)
        self.tree.insert(parentitem,'end',text=mydata[0],values=mydata)

    def addItemInto(self):
        self.currentitem=self.tree.focus()
        self.inputframe=InputDataDialog(self,self.datatitle,'')
        self.inputframe.wait_window()
        mydata=self.inputframe.data

        self.tree.insert(self.currentitem,'end',text=mydata[0],values=mydata)

    def modifyItem(self):
        myitem=self.tree.focus()
        a=list(self.tree.item(myitem,"values"))
        self.modifyframe=InputDataDialog(self,self.datatitle,a)
        self.modifyframe.wait_window()
        mydata=self.modifyframe.data
        self.tree.item(myitem,text=mydata[0],values=mydata)

    def deleteItem(self):
        myitem=self.tree.focus()
        self.tree.delete(myitem)

    def exportTree(self):
        filename=input("File name?: ")
        if filename:
            self.tree.exportTreetofile(filename)
                
    def importTree(self):
        filename=input("Which file?: ")
        if filename:
            self.tree.deleteAllitems()
            treeitemlist=self.tree.importTreefromfile(filename)
            self.tree.writeItemlisttotree(treeitemlist)
        
    def getTreeinfo(self):
        #This function is for debug.
        self.currentitem=self.tree.focus()
        code=input("What you want to show? ")
        eval("print(self."+code+")")

class InputDataDialog(Toplevel):
    data=[]   #exchange data with others modules
    def __init__(self,parent,datatitle,itemdata):
        Toplevel.__init__(self,parent)
        self.title("Input Data:")
        self.grab_set()     # make the main window unvaliable
        self.frame=ttk.Frame(self)
        self.frame.grid()
        self.createWidgets(datatitle,itemdata)

    def createWidgets(self,datatitle,itemdata):
        self.entrylist=[]
        currentrow=0
        for i in datatitle:
            a=ttk.Label(self.frame,text=i)
            b=ttk.Entry(self.frame)
            self.entrylist.append(b)
            a.grid(row=currentrow,column=0)
            b.grid(row=currentrow,column=1)
            currentrow +=1
        print(self.entrylist)
        print(itemdata)
        if itemdata:
            self.setData(itemdata)
        self.entrylist[0].focus_force()
        self.okButton=ttk.Button(self.frame, text="Ok",command=self.getData)
        self.okButton.grid()

    def setData(self,datalist):
        for i in range(len(self.entrylist)):
            self.entrylist[i].insert(0,datalist[i])

    def getData(self):
        self.data=[]
        for i in self.entrylist:
            self.data.append(i.get())
        self.destroy()

a=["Part","description","qty","sequence","status"]
#a=["sequence","*agrv","**kw"]

mainapp=TreeFrame(*a)
mainapp.title("Treeview window")
mainapp.mainloop()

