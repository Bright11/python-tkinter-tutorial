from tkinter import *

from tkinter import ttk

root = Tk()
root.geometry("400x400")
root.title("Calculator")


myframe=Frame(root,width=400,height=400,bg="blue",relief=SUNKEN)
myframe.pack(side=TOP)

mybutton=Button(myframe,text="Click Me",bg="red",fg="white",state=DISABLED)
mybutton.pack()

def changtext():
    mylable=Label(myframe,text="Hello World",bg="red",fg="white",font=("Arial",20)).pack()



# for padding just link in css
# we say padyx which us left and right and pady which is top and bottom
mybutton=Button(myframe,text="Click Me now",bg="green",fg="white",padx=20,pady=20,command=changtext).pack()



root.mainloop()