from tkinter import *
from PIL import ImageTk, Image
from tkinter import Toplevel
from tkinter import filedialog


root=Tk()
root.title("Bright C Developer Window")
# adding logo
root.iconbitmap("img/logo.ico")
root.geometry("400x400")

vertical=Scale(root,from_=0,to=200)
vertical.pack()

horizontal=Scale(root,from_=0,to=400,orient=HORIZONTAL)
horizontal.pack()

def slide():
    my_label=Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())  + "x400")
    


my_label=Label(root,text=horizontal.get()).pack()

my_btn=Button(root,text="click me", command=slide).pack()



root.mainloop()
