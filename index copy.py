import tkinter as tk
from tkinter import*
from tkinter import ttk
from dbo import get

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Snippers")
        self.resizable(FALSE,FALSE)
        self.customStyle()
        
        self.optionFrame = ttk.Frame(border=1,width=790,height=30)
        self.optionFrame.place(x=2,y=1)
        self.commndList=''
        self.createList()
        self.testOption()
        # self.createCommandList()

        
    def customStyle(self):
        self.s = ttk.Style()
        self.s.configure("TMenubutton",background="#dee1e6")

    def createList(self):
        self.listClicked = StringVar()
        self.listClicked.set("Select")
        self.list = get.list()
        self.listMenu = ttk.OptionMenu(self.optionFrame,self.listClicked,*self.list.keys(),command=self.commandListAction)
        self.listMenu.place(x=10,y=3)

   
    # def createList
    def commandListAction(self,selected):
       self.commndList= get.commandlist(selected,self.list,self.listClicked)
       self.createCommandList()
       

       

    def createCommandList(self):
        self.commandListClicked=StringVar()
        self.commandListClicked.set("Select")
        self.commandListMenu = ttk.OptionMenu(self.optionFrame,self.commandListClicked,*self.commndList.keys(),
                                              command=self.selectCommandAction)
        self.commandListMenu.place(x=110,y=3)

    def selectCommandAction(self,*args):
        select_=self.commandListClicked.get()
        print(select_)

    def testOption(self):
        self.optionsList = {10:"Mango",11:"Apple",12:"Orange"}
        
        self.opt =ttk.Combobox(self.optionFrame,values=list(self.optionsList.values()),state="readonly")
        self.opt.set("selctct any")
        self.opt.bind("<<ComboboxSelected>>",self.my_show)
        self.opt.place(x=300,y=3)

    
    def my_show(self,e,*args):
        selectedVal = e.widget.get()
        indexVal = e.widget.current()
        idlist= list(self.optionsList)
        print(f"selcted id:{idlist[indexVal]} selcted value:{selectedVal}")




if __name__=="__main__":
    app =App()
    app.mainloop()