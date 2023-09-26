import sqlite3
def dbconn():
    return sqlite3.connect('commands.db')
    

