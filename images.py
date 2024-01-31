from tkinter import *
# from PIL import ImageTk, Image
from PIL import ImageTk, Image

root=Tk()
root.title("Bright C Developer")
# adding logo
root.iconbitmap("img/logo.ico")

# adding an image into a lable
my_img=ImageTk.PhotoImage(Image.open("img/IMG1.jpg"))
my_label=Label(image=my_img)
my_label.pack()

# to quit, exit or close the window
button_quit=Button(root, text="Exit program", command=root.quit)
button_quit.pack()




root.mainloop()