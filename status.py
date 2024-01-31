from tkinter import *
# from PIL import ImageTk, Image
from PIL import ImageTk, Image

root=Tk()
root.title("Bright C Developer Status")
# adding logo
root.iconbitmap("img/logo.ico")

# adding an image into a lable
my_img1=ImageTk.PhotoImage(Image.open("img/IMG1.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("img/img.jpg"))
my_img3=ImageTk.PhotoImage(Image.open("img/img.jpg"))
my_img4=ImageTk.PhotoImage(Image.open("img/img2.jpg"))
my_img5=ImageTk.PhotoImage(Image.open("img/img3.jpg"))
my_img6=ImageTk.PhotoImage(Image.open("img/img4.png"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5,my_img6]

status=Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN,anchor=E)
my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward=Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda:back(image_number-1))
    
    #if image_list and image_number==image_list[-1]:
    if image_number==6:
        button_forward=Button(root,text=">>",state=DISABLED)
    
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    
    # update status bar
    status=Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)
    

def back(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward=Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda:back(image_number-1))
    if image_number==1:
        button_back=Button(root,text="<<",state=DISABLED)
    
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    
    # update status bar
    status=Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)


button_back=Button(root,text="<<",command=back, state=DISABLED)
button_forward=Button(root,text=">>",command=lambda:forward(2))

# to quit, exit or close the window
button_quit=Button(root, text="Exit program", command=root.quit)


button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,padx=4)
status.grid(row=2,column=0,columnspan=3, sticky=W+E)


# north is up N
# south is down S
# west is left W
# east is right E
# We use anchor to align text or data to any direction

root.mainloop()