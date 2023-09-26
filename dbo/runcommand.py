import os,time


def save(msgbox,window):
    os.system('taskkill /f /im pythonw.exe')
    msgbox.showinfo("Saved","saved successfully")
    window.destroy()
    os.system('pythonw command.py')

def close(window):
    os.system('taskkill /f /im pythonw.exe')
    window.destroy()
    os.system('pythonw command.py')




