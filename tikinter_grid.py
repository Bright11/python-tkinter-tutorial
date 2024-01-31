from tkinter import *

from tkinter import ttk

root = Tk()
root.geometry("400x400")
root.title("Calculator")


myframe=Frame(root,width=400,height=400,bg="blue",relief=SUNKEN)
myframe.pack(side=TOP)

mylabel=Label(myframe,text="Calculator",font=("Arial",20),bg="blue",fg="white").grid(row=0,column=0)
mylabe2=Label(myframe,text="Calculator",font=("Arial",20),bg="blue",fg="white").grid(row=0,column=1)
mylabel3=Label(myframe,text="Calculator",font=("Arial",20),bg="blue",fg="white").grid(row=1,column=0)
mylabel4=Label(myframe,text="Calculator",font=("Arial",20),bg="blue",fg="white").grid(row=1,column=1)
root.mainloop()