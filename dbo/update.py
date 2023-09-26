from dbo import conn
connection = conn.dbconn()

def item(name,description,id,msgbox):
    try:
        connection.execute(f'''update technique set name="{name}", description="{description}" where id={id};''')
        connection.commit()
    except:
       return msgbox.showerror("Error","This item is already exit")
    else:
       return  msgbox.showinfo("Success","Item has been successfully updated")

def command(name,command,id,msgbox):
   try:
      connection.execute(f'''update commandlist set name="{name}", command="{command}" where id={id};''')
      connection.commit()
   except:
      return msgbox.showerro("Error","This command is already exist")
   else:
      return msgbox.showinfo("Success","Command has been successfully updated")
