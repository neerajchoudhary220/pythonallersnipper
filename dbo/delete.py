from dbo import conn
connection = conn.dbconn()
# conn.dbconn().cursor().execute('PRAGMA foreign_keys = ON')

def ItemDelete(id):
    connection.cursor().execute('PRAGMA foreign_keys = ON')
    connection.cursor().execute(f"delete from technique where id ={id}")
    connection.commit()
    

def CommandDelete(id):
    connection.cursor().execute(f"delete from commandlist where id={id};")
    connection.commit()
    return print("Data has been deleted")