from tkinter import *
root=Tk()

e=Entry(root,width=50)
e.pack()
e.insert(0,"Enter your name:")


def Msg():
    msg="Hello "+e.get()
    myTitle=Label(root,text=msg)
    myTitle.pack()

mybutt=Button(root,text="Enter: ",command=Msg,fg="blue")
mybutt.pack()
root.mainloop()