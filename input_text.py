from tkinter import *

from tkinter import ttk

root = Tk()
root.geometry("400x400")
root.title("Calculator")


myframe=Frame(root,width=400,height=400,bg="blue",relief=SUNKEN)
myframe.pack(side=TOP)

# text entry
e=Entry(myframe,width=50,borderwidth=5, bg="blue",fg="white",font=("Arial",20))
e.pack()

c=Entry(myframe,width=50,borderwidth=5, bg="blue",fg="white",font=("Arial",20))
c.insert(0,"Enter your name")
c.pack()


def changtext():
    #mylable=Label(myframe,text=c.get(),bg="red",fg="white",font=("Arial",20)).pack()
    hello="hello", c.get()
    mylable=Label(myframe,text=hello,bg="red",fg="white",font=("Arial",20)).pack()



# for padding just link in css
# we say padyx which us left and right and pady which is top and bottom
mybutton=Button(myframe,text="Submit data",bg="green",fg="white",padx=20,pady=20,command=changtext).pack()



root.mainloop()