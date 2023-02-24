from firebase import firebase
from tkinter import *

firebase = firebase.FirebaseApplication("https://itsthere-be0c6.firebaseio.com/", None)

nameS = {}


def senddatas(entry1):
    nameS['Name'] = entry1
    data = {
        'Name' : nameS['Name'],
        'Email' : 'confusing@gmail.com',
        'Other detail' : '555'
    }
    result = firebase.post('https://itsthere-be0c6.firebaseio.com/Contact', data)
    print(result)
    return nameS['Name']

def exitProgram():
    root.destroy()

root = Tk()
entry1 = Entry(root).pack()
bnt1 = Button(root, text="Send", command=senddatas).pack()
exitbut = Button(root, text="EXIT", command=exitProgram).pack()
root.mainloop()