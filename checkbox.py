from tkinter import *
from PIL import ImageTk, Image
from tkinter import Toplevel
from tkinter import filedialog


root=Tk()
root.title("Bright C Developer Window")
# adding logo
root.iconbitmap("img/logo.ico")
root.geometry("400x400")

var=StringVar()
#var=IntVar()

# c=Checkbutton(root,text="Check this box, I dare you!", variable=var)
c=Checkbutton(root,text="Check this box, I dare you!", variable=var, onvalue="On",offvalue="Of")
c.deselect()
c.pack()

def checked():
    Label(root,text=var.get()).pack()

mylabel=Label(root,text=var.get()).pack()


Button(root,text="see check box", command=checked).pack()



root.mainloop()