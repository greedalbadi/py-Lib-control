import os
import tkinter
import sys
from tkinter import filedialog
import json




class _data:

    file = "data.json"




def msgbox(message, Title="Lib builder"):

    cmd = f'mshta vbscript:Execute("MsgBox ""{message}"", vbOkOnly, ""{Title}""")(window.close)'


    return os.system(cmd)


def getpy():

    line = sys.version

    return line.split()[0]

def getfolder():
    root = tkinter.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    root.destroy()
    return path


def _alldata():

    return json.load(open(_data.file))


def editvalue(key, value):

    data = _alldata()
    data[0][key] = value

    return json.dump(data, open(_data.file, "w"))




def getdata(key):

    return _alldata()[0][key]


def openfolder(path):


    path = path.replace("/", "\\")
    cmd = f'explorer {path}'
    return os.system(cmd)


def writelog(username, password):

    editvalue("username", username)
    editvalue("password", password)

def getlogdata(username, password):
    try:
        return getdata("username"), getdata("password")
    except:
        pass

