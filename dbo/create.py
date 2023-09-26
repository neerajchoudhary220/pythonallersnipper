from dbo import conn
connection = conn.dbconn()
cursor = connection.cursor()
def newListItem(value,msgbox):
    
    try:
        cursor.execute(f'''insert into technique (name,description) values('{value}',"");''')
        connection.commit()
    except:
       return msgbox.showerror("Error","This item is already exist")
    else:
       return  msgbox.showinfo("Success","New item has been added")


def newCommand(technique_id,name,command,msgbox,clear,refresh,container):
    try:
        cursor.execute(f'''insert into commandlist (technique_id,name,command) values({technique_id},'{name}','{command.strip()}');''')
        connection.commit()
    except:
        return msgbox.showerror("Error","This command is already exist")
    else:
        clear()
        refresh()
        container.place_forget()
        return msgbox.showinfo("Success","New command add successfully")