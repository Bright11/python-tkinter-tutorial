from tkinter import *
from PIL import ImageTk, Image
from tkinter import Toplevel


root=Tk()
root.title("Bright C Developer Window")
# adding logo
root.iconbitmap("img/logo.ico")

def opennewwindow():
    top=Toplevel()
    global my_img
    top.title("Bright C Developer Window 2")
    top.iconbitmap("img/logo.ico")
    my_img=ImageTk.PhotoImage(Image.open("img/IMG1.jpg"))
    my_label=Label(top,image=my_img).pack()
    # Label(top, text="Hello World",padx=10,pady=10).pack(padx=10,pady=10)
    
    # close window
    Button(top,text="Close Window",command=top.destroy).pack(padx=10,pady=10)
    
    
    
    
Button(root,text="Open Second Window",command=opennewwindow).pack(padx=10,pady=10)














root.mainloop()