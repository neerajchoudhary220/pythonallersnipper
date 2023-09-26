import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkinter import messagebox as msgbox
from dbo import get,create,icons,delete,update,runcommand

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title("Snippers")
        self.resizable(FALSE,FALSE)
        self.configure(background="#23383f")
        self.customStyle()
        self.frameHeight = 30
        self.paddingValue=10
        self.widgetHeightValue=18
        self.fontFamily ="Modern"
        self.fontSize=18
        self.menubar = Menu()
        self.file = Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.file)
        self.file.add_command(label="Save",command=self.saveClick)
        self.config(menu=self.menubar)

        
        self.optionFrame = ttk.Frame(border=1,width=240,height=self.frameHeight)
        self.optionFrame.place(x=5,y=10)

        self.optionFrame1 = ttk.Frame(width=300,height=self.frameHeight)
        self.optionFrame1.place(x=340,y=10)

        self.newOptionCreateFrame = ttk.Frame(width=250,height=self.frameHeight)
        self.newOptionCreateFrame.place(x=340,y=10)

        
        self.EditAreaFrame=ttk.Frame(width= 780,height=450)
        self.EditAreaFrame.place_forget()

        self.CommandEditAreaFrame= ttk.Frame(width= 780,height=450)
        self.CommandEditAreaFrame.place_forget()

        self.commandNewAraFrame=ttk.Frame(width=780,height=450)
        self.commandNewAraFrame.place_forget()



        
        # self.text
        self.newOptionCreateFrame.place_forget()
        self.optionFrame1.place_forget()
        self.commndList=''
        
        self.createList()
        self.itemListDltBtn()
        self.inputAndAddBtnForOption()
        self.refreshList()
        self.itemListEdtBtn()
        self.itemEditText()
        self.CommandNewText()
        self.CommandEditText()

        self.protocol('WM_DELETE_WINDOW',self.exitWindow)
        # self.
      
    def saveClick(self):
        runcommand.save(msgbox,self)

    def exitWindow(self):
        q = msgbox.askokcancel("Quit","Are you sure ?")
        
        if q:
            runcommand.close(self)
        else:
            return False

        

    def customStyle(self):
        self.s = ttk.Style()
        all_theme = self.s.theme_names()
        # print(all_theme)
        self.s.theme_use('alt')
        self.s.configure("TMenubutton")
        self.s.configure("TFrame",background="#23383f")
        # self.s.configure("TFrame",background="green")

        self.s.configure('TButton',background="#DC3545", foreground="#fff", borderwidth=2, focusthickness=0)
        self.s.map('TButton', background=[('active','#DC3545')])
        

    def createList(self):
        self.listClicked = StringVar()
        self.list = get.list()
        self.listMenu = ttk.Combobox(self.optionFrame,values=list(self.list.values()),state="readonly",
                                     height=self.widgetHeightValue)
        self.listMenu.bind("<<ComboboxSelected>>",self.commandListAction)
        self.defaultItemSelect()
        self.listMenu.pack(side=LEFT, pady=3)

   
    def defaultItemSelect(self):
        self.listMenu.set("Select ")

    def refreshList(self):
        self.listMenu.configure(values=list(get.list().values()))
    
   
        

    def ItemEditBtnClick(self,*args):
        self.item_list = get.item(self.technique_id)
        self.clearItemUpdateField()
        self.EditAreaFrame.place(x=10,y=100)
        self.ItemName.set(self.item_list["command"])
        self.ItemDescriptionField.insert(INSERT,self.item_list["description"])
        self.ItemUpdateBtn.configure(state="enabled")
    
    def ItemUpdateBtnClick(self):
        name = self.ItemName.get()
        description = self.ItemDescriptionField.get('1.0', 'end -1c')
        update.item(name,description,self.technique_id,msgbox)
        self.refreshList()
        self.defaultItemSelect()
        self.hideItemUpdateArea()
    
    def itemCancelBtnClick(self):
        self.hideItemUpdateArea()
       

    def hideItemUpdateArea(self):
        self.clearItemUpdateField()
        self.EditAreaFrame.place_forget()
    
    def hideCommandUpdateArea(self):
        self.clearCommandUpdateField()
        self.CommandEditAreaFrame.place_forget()
    
    def ChangeItemUpdateField(self,*args):
        if len(self.ItemName.get())>1:
            self.ItemUpdateBtn.configure(state="enabled")
        else:
            self.ItemUpdateBtn.configure(state="disabled")
    
    def clearItemUpdateField(self):
        self.ItemName.set('')
        self.ItemDescriptionField.delete('1.0', 'end -1c')
    def clearCommandUpdateField(self):
        self.commandName.set('')
        self.CommandDescriptionField.delete('1.0', 'end -1c')

    def clearNewCommandField(self):
        self.newCommand.set('')
        self.commandDetials.delete('1.0', 'end -1c')
        # return get.list()
  
#   item list change action
    def commandListAction(self,e,*args):
        self.clearItemUpdateField()
        self.technique_id = get.Id(e.widget.current(),list(get.list()))

        if self.technique_id!=0:
            self.optionFrame1.place(x=340,y=10)
            self.newOptionCreateFrame.place_forget()
            commandlist = get.commandlist(self.technique_id)
            self.commandlist = commandlist
            self.createCommandList()
            self.trashBtn.configure(state="enabled")
            self.itemEdtBtn.configure(state="enabled")
        else:
            self.optionFrame1.place_forget()
            self.newOptionCreateFrame.place(x=340,y=10)
            self.trashBtn.configure(state="disabled")
            self.itemEdtBtn.configure(state="disabled")


   
    def selectCommand(self,e,*args):
        commandList = get.commandlist(self.technique_id)

        self.commandId = get.Id(e.widget.current(),list(commandList))
        self.clearCommandUpdateField()
       
     
        if self.commandId >0:
            self.commandDltBtn.configure(state="enabled")
            self.commandNewAraFrame.place_forget()
            self.commandEditBtn.configure(state="enabled")

        else:
            self.commandDltBtn.configure(state="disabled")
            self.commandEditBtn.configure(state="disabled")
            self.commandNewAraFrame.place(x=10,y=100)


    def onchangeUpdateCommandEntry(self,e,*args):
        desc = self.CommandDescriptionField.get('1.0', 'end -1c')
        commandName = self.commandName.get()
        if len(desc)>1 and len(commandName)>1:
            self.commandItemUpdateBtn.configure(state="enabled")
        else:
            self.commandItemUpdateBtn.configure(state="disabled")

    def onchangeNewCommandInput(self,e,*args):
        desc = self.commandDetials.get('1.0', 'end -1c')

        if len(desc)>1 and len(self.newCommand.get())>1:
            self.commandSaveBtn.configure(state="enabled")
        else:
            self.commandSaveBtn.configure(state="disabled")

    def onchangeCommandNewDescription(self,*args):
        desc = self.commandDetials.get('1.0', 'end -1c')
        if len(desc)>1 and len(self.newCommand.get()):
            self.commandSaveBtn.configure(state="enabled")
        else:
            self.commandSaveBtn.configure(state="disabled")

    def commandSaveBtnClick(self,*args):
        create.newCommand(self.technique_id,self.newCommand.get(),self.commandDetials.get('1.0', 'end -1c'),msgbox,
                          self.clearNewCommandField, self.commandListRefresh,self.commandNewAraFrame)
        # create.newCommand(self.technique_id,self.newCommand.get(),self.commandDetials.get('1.0', 'end -1c'),msgbox,
        #                   self.clearNewCommandField, self.commandListRefresh,self.commandNewAraFrame)               
       

    def inputAndAddBtnForOption(self):
        self.techniqueName = StringVar()
        self.techniqueEntry = ttk.Entry(self.newOptionCreateFrame,textvariable=self.techniqueName,font=('calibre',10,'normal'),
                                        validatecommand=self.getTextValue, validate="focusout")
        self.techniqueName.trace("w",self.getTextValue)
        self.techniqueEntry.place(x=2,y=3)

        self.techniqueBtn = ttk.Button(self.newOptionCreateFrame,text="Add New", command=self.CreateNewTechnique,state="disabled")
        self.techniqueBtn.place(x=160,y=3)
        
    def itemEditText(self):
        self.ItemName=StringVar()
        self.ItemEditField = ttk.Entry(self.EditAreaFrame,textvariable=self.ItemName)
        self.ItemName.trace('w',self.ChangeItemUpdateField)
        self.ItemEditField.place(x=5,y=15)

        self.ItemUpdateBtn = ttk.Button(self.EditAreaFrame,text="Update",state="disabled",command=self.ItemUpdateBtnClick)
        self.ItemUpdateBtn.place(x=135,y=15)

        self.itemCancelBtn = ttk.Button(self.EditAreaFrame,text="Cancel",command=self.itemCancelBtnClick)
        self.itemCancelBtn.place(x=215,y=15)
    
        self.ItemDescriptionField = Text(self.EditAreaFrame,height=24,width=95,bd=2)
        self.ItemDescriptionField.place(x=5,y=50)

    

    def CommandEditText(self):
        self.commandName=StringVar()
        self.commandNameEdit = ttk.Entry(self.CommandEditAreaFrame,textvariable=self.commandName)
        self.commandName.trace('w',self.onchangeUpdateCommandEntry)
        self.commandNameEdit.place(x=5,y=15)
    
        self.commandItemUpdateBtn = ttk.Button(self.CommandEditAreaFrame,text="Update",state="disabled",
                                               command=self.commandUpdateBtnclick)
        self.commandItemUpdateBtn.place(x=135,y=15)

        self.commandCancelBtn = ttk.Button(self.CommandEditAreaFrame,text="Cancel",command=self.hideCommandUpdateArea)
        self.commandCancelBtn.place(x=215,y=15)

        self.CommandDescriptionField = Text(self.CommandEditAreaFrame,height=24,width=95,bd=2)
        self.CommandDescriptionField.place(x=5,y=50)


    
    def CommandNewText(self):
        self.newCommand=StringVar()
        self.newCommandEdit = ttk.Entry(self.commandNewAraFrame,textvariable=self.newCommand)
        self.newCommandEdit.place(x=5,y=15)
        self.newCommand.trace('w',self.onchangeNewCommandInput)
    
        self.commandSaveBtn = ttk.Button(self.commandNewAraFrame,text="Save",state="disabled",
                                         command=self.commandSaveBtnClick)
        self.commandSaveBtn.place(x=135,y=15)

        self.commandDetials = Text(self.commandNewAraFrame,height=24,width=95,bd=2)
        self.commandDetials.place(x=5,y=50)
        self.commandDetials.bind('<KeyRelease>',self.onchangeCommandNewDescription)

   

    def itemListDltBtn(self):
        self.trashBtnIcon = PhotoImage(file=icons.deleteBtn())
        self.trashBtn = ttk.Button(self.optionFrame,text="Delete",command=self.itemDelete,state="disabled")
        self.trashBtn.pack(side=LEFT,pady=3,padx=2)
        
    def itemListEdtBtn(self):
        self.itemEdtBtn = ttk.Button(self.optionFrame,text="Edit",state="disabled",
                                     command=self.ItemEditBtnClick)
        self.itemEdtBtn.pack(side=LEFT,pady=3,padx=2)
    
        

    def itemDelete(self,*args):
        q = msgbox.askquestion("Delete Item","Are you sure ?")
        if q=='yes':
            delete.ItemDelete(self.technique_id)
            self.refreshList()
            self.defaultItemSelect()
            self.optionFrame1.place_forget()
            self.hideCommandUpdateArea()
            msgbox.showinfo('Success',"Item has been deleted")
            
        else:
            return False

        
        
        
    
    def getTextValue(self, *args):
        value = self.techniqueName.get()
        if len(value)>1:
            self.techniqueBtn.configure(state="enabled")
        else:
            self.techniqueBtn.configure(state="disabled")


    
    def CreateNewTechnique(self):
        value = self.techniqueName.get()
        result = create.newListItem(value,msgbox)
        self.techniqueName.set('')
        self.refreshList()
        

    def createCommandList(self):
        self.commandListMenu = ttk.Combobox(self.optionFrame1,values=list(self.commandlist.values()),state="readonly")
        self.commandListMenu.set("Select")
        self.commandListMenu.bind("<<ComboboxSelected>>",self.selectCommand)
        self.commandListMenu.place(x=5,y=5)

        self.commandDltBtn = ttk.Button(self.optionFrame1,text="Delete",state="disabled",command=self.commandDelete)
        self.commandDltBtn.place(x=148,y=5)

        self.commandEditBtn  =ttk.Button(self.optionFrame1,text="Edit",state="disabled",
                                         command=self.commnadEditBtnClick)
        self.commandEditBtn.place(x=224,y=5)
    
    def commandListRefresh(self):
        self.commandListMenu.set("Select")
        commandList = get.commandlist(self.technique_id)
        self.commandListMenu.configure(values=list(commandList.values()))

    def commandUpdateBtnclick(self):
        update.command(self.commandName.get(),self.CommandDescriptionField.get('1.0', 'end -1c'),
                       self.commandId,msgbox)
        # self.hideCommandUpdateArea()
        
    
    def commnadEditBtnClick(self):
        if self.commandId>0:
            self.CommandEditAreaFrame.place(x=10,y=100)
            command = get.command(self.commandId)
            self.commandName.set(command['name'])
            self.CommandDescriptionField.delete('1.0', 'end -1c')
            self.CommandDescriptionField.insert(1.0,command['command'])
            self.commandItemUpdateBtn.configure(state="enabled")
            
        else:
            self.clearCommandUpdateField()
            self.CommandEditAreaFrame.place_forget()
            self.commandItemUpdateBtn.configure(state="disabled")

           


    def commandDelete(self,*args):
        q =msgbox.askquestion("Delete Command","Are you sure ?")
        if q=='yes':
            delete.CommandDelete(self.commandId)
    
            self.commandListRefresh()
            msgbox.showinfo("Success","Command has been deleted successfully")
            self.hideCommandUpdateArea()
            
        else:
            return False
        
 
    


   
  


        
        
if __name__=="__main__":
    app =App()
    app.mainloop()