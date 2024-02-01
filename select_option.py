from tkinter import *
from PIL import ImageTk, Image
from tkinter import Toplevel
from tkinter import filedialog


root=Tk()
root.title("Bright C Developer Window")
# adding logo
root.iconbitmap("img/logo.ico")
root.geometry("400x400")


# drop down menu

options=[
     "Monday",
     "Tuesday",
     "Wedsday",
     "Thursday",
     "Friday",
     "Saturday",
     "Sunday"
]



def getdropdown():
    Label(root, text=clicked.get()).pack()
    
clicked = StringVar()
#clicked.set("Monday")
clicked.set(options[0])
# drop=OptionMenu(root, clicked, "Monday","Tuesday","Wedsday","Thursday","Friday","Satuday","Sunday")
# drop.pack()

# using python list
drop=OptionMenu(root, clicked, *options)
drop.pack()



btn_drop=Button(root,text="get value of drop down",command=getdropdown)
btn_drop.pack()








root.mainloop()