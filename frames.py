from tkinter import *
from PIL import ImageTk, Image


root=Tk()
root.title("Bright C Developer Frame")
# adding logo
root.iconbitmap("img/logo.ico")

# frames
frame=LabelFrame(root, text="This is my frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)
# the frame.pack(padx=10, pady=10) is for x axis and pady is for y axis which is for outside of the frame
# and this (root, text="This is my frame", padx=5, pady=5) is for inside of the frame

# adding buttons into frames

b=Button(frame, text="Don't click here")
b2=Button(frame, text="or here")
b3=Button(frame, text="Don't click here")
b4=Button(frame, text="or here")

b.grid(row=0,column=0)
b2.grid(row=0,column=1,padx=5,pady=5)
b3.grid(row=1,column=0)
b4.grid(row=1,column=1)




root.mainloop()