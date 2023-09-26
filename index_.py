from tkinter import*
from dbo import get,optionMenu
window =Tk()
window.title("Snipper")
window.geometry('800x500')
window.resizable(FALSE,FALSE)

options=get.list()
clicked = StringVar()
clicked.set("Select")
commnadClicked =StringVar()
commnadClicked.set("Select Command")
commandList ={"Add New":0}

def getDropdown(selected):
    global commandList
    commandList = get.commandlist(selected,options,clicked)
    print(commandList)
    selected = clicked.get()
   

                
# def getCommand(command_id):
#     command_id = commnadClicked.get()
#     print(command_id)
    

# command_list_label = Label(window,text="Command List",fg="#000",font=('Aerial 10 '))
# command_list_label.place(x=90, y=2)
# commandDropdown=OptionMenu(window,commnadClicked,*commandList.keys(),command=getCommand)
# commandDropdown.place(x=90,y=20)
# commandDropdown.configure(borderwidth=2)

select_command_listLabel = Label(window,text="Select List",fg='#000', font=('Aerial 10 '))
select_command_listLabel.place(x=10,y=2)

techniqueDropdown =  OptionMenu(window,clicked,*options.keys(),command=getDropdown)
techniqueDropdown.grid(row=0,sticky=EW,pady=20,padx=2,columnspan=2)
techniqueDropdown.place(x=10,y=20)
techniqueDropdown.configure(borderwidth=2)

commandDescription =Text(window,bd=2, width=95,height=18,borderwidth=2,)
commandDescription.place(x=10,y=60)




window.mainloop()