import keyboard
from dbo import conn
commandlist = conn.dbconn().execute("select * from commandList")
for row in commandlist:
    commandName = row[2]
    command = row[3]
    keyboard.add_abbreviation(commandName,command)


keyboard.wait()

