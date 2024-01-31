from tkinter import *
from PIL import ImageTk, Image
from tkinter import Radiobutton


root=Tk()
root.title("Bright C Developer radio buttons")
# adding logo
root.iconbitmap("img/logo.ico")

# getting the variable from the radio buttons
# if is a string, we can use  StrVar, in the value, we can use value="1"
r=IntVar()
r.set("2")

# dsiplaying the value of the radio buttons on click event
def clicked(value):
    mylable=Label(root, text=value)
    mylable.pack()
    
Radiobutton(root, text="Option 1", variable=r, value=1,command=lambda:clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2,command=lambda:clicked(r.get())).pack()

# displaying the value of the radio buttons
mylable=Label(root, text=r.get())
mylable.pack()

# we can also use button to get the value on clicked

mybutton=Button(root, text="Click me", command=lambda:clicked(r.get()))

mybutton.pack()


root.mainloop()