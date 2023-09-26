from dbo import conn
def list():
    list = conn.dbconn().execute('select * from technique order by id desc;')
    lists = {0:"Add New"}
    for row in list:
        lists[row[0]] = row[1]

    return lists


def commandlist(technique_id):
   
    query = f"""select technique.id, technique.name,commandlist.id,commandlist.name, commandlist.command from commandlist INNER join technique
    on commandlist.technique_id=technique.id where technique_id={technique_id} order by commandlist.id desc;"""
    commandlists= conn.dbconn().execute(query)
    command ={0:"Add New"}
    for row in commandlists:
        command[row[2]]=row[3]

    return command

def command(id):
    cursor = conn.dbconn().execute(f'''select*from commandlist where id={id};''')
    data ={}
    for row in cursor:
        data["name"]=row[2]
        data["command"]=row[3]

    return data

def Id(indexVal,list_):
    return list_[indexVal]

def item(id):
    data = conn.dbconn().execute(f"select * from technique where id={id};")
    item_={}
    for row in data:
        item_["command"]=row[1]
        item_["description"]=row[2]
    
    return item_
        


    