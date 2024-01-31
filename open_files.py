from tkinter import *
from PIL import ImageTk, Image
from tkinter import Toplevel
from tkinter import filedialog


root=Tk()
root.title("Bright C Developer Window")
# adding logo
root.iconbitmap("img/logo.ico")

def opefile():
    global my_image
    root.filename=filedialog.askopenfilename(initialdir="/",title="Open file", filetypes=(("jpg files","*.jpg"),("all files", "*.*")))
    my_label=Label(root,text=root.filename).pack()
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label=Label(image=my_image).pack()
# root.filename=filedialog.askopenfilename(initialdir="/",title="Open file", filetypes=(("jpg files","*.jpg"),("all files", "*.*")))






Button(text="open file",command=opefile).pack()




root.mainloop()