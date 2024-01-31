from tkinter import *
from PIL import ImageTk, Image
from tkinter import Radiobutton
from tkinter import StringVar
from tkinter import messagebox


root=Tk()
root.title("Bright C Developer message box")
# adding logo
root.iconbitmap("img/logo.ico")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response=messagebox.askyesno("This is my popup","Hello World")
    Label(root,text=response).pack()
    if response==1:
        Label(root,text=response).pack()
    if response==0:
        response="You clicked no"
        Label(root,text=response).pack()

Button(root,text="Popup",command=popup).pack()

# show showinfo message
def popup2():
    response=messagebox.showinfo("This is my popup","Hello World")
    Label(root,text=response).pack()
    
Button(root,text="Show Info",command=popup2).pack()

# show warning message

def popup3():
    response=messagebox.showwarning("This is my popup","Hello World")
    Label(root,text=response).pack()

Button(root,text="Warning",command=popup3).pack()

# show error message
def popup4():
    response=messagebox.showerror("This is my popup","Hello World")
    Label(root,text=response).pack()
    
Button(root,text="Error",command=popup4).pack()


# ask question message
def popup5():
    response=messagebox.askquestion("This is my popup","Hello World")
    if response=="yes":
        response="You clicked yes"
        Label(root,text=response).pack()
    if response=="no":
        response="You clicked no"
        Label(root,text=response).pack()
    #Label(root,text=response).pack()
    
Button(root,text="Ask Question",command=popup5).pack()

# ask okaycancel
def popup6():
    response=messagebox.askokcancel("This is my popup","Hello World")
    if response==True:
        response="You clicked yes"
        Label(root,text=response).pack()
    if response==False:
        response="You clicked no"
        Label(root,text=response).pack()
    #Label(root,text=response).pack()

Button(root,text="Ask Ok Cancel",command=popup6).pack()

root.mainloop()