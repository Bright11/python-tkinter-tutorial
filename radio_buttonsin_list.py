from tkinter import *
from PIL import ImageTk, Image
from tkinter import Radiobutton
from tkinter import StringVar


root=Tk()
root.title("Bright C Developer radio buttons")
# adding logo
root.iconbitmap("img/logo.ico")

# radio buttions using python list
mypizza=[
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]
# getting the variable from the radio buttons
pizza=StringVar()

pizza.set("Pepperoni")
#  making the radio buttion using for loop
for text, p in mypizza:
    Radiobutton(root, text=text, variable=pizza, value=p).pack(anchor=W)
# dsiplaying the value of the radio buttons on click event
def clicked(value):
    mylable=Label(root, text=value)
    mylable.pack()
    


# displaying the value of the radio buttons


# we can also use button to get the value on clicked

mybutton=Button(root, text="Click me", command=lambda:clicked(pizza.get()))

mybutton.pack()


root.mainloop()