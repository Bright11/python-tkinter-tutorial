from tkinter import *

from tkinter import ttk
import math

root = Tk()
root.geometry("400x500")
root.title("Calculator")


myframe=Frame(root,width=100,height=200,relief=SUNKEN)
myframe.pack(side=TOP)

# text entry
e=Entry(myframe,width=20,borderwidth=5, bg="gray",fg="white",font=("Arial",20))
e.grid(row=0,column=0,columnspan=3)
# e.grid(row=0,column=0,columnspan=3,padx=20,pady=20)
# calculators button

# we use lambda to pass value initkinter
# def button_click(number):
#    #e.delete(0,END) we use it to delete
#     current=e.get() 
#     e.delete(0,END)
#     e.insert(0,str(current)+str(number))

def button_click(number):
    current = e.get()

    # Check if current input contains a decimal point
    if '.' in current:
        # If it does, keep it as a float
        e.delete(0, END)
        e.insert(0, current + float(number))
    else:
        # If it doesn't, treat it as an integer
        e.delete(0, END)
        e.insert(0, int(current + str(number)))




# deleting 
def button_clear():
    e.delete(0,END)
    
# addition
def button_add():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    e.delete(0,END)
    
# button_minus
def button_minus():
    first_number=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(first_number)
    e.delete(0,END)

# button_multiply

def button_multiply():
    first_number=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_number)
    e.delete(0,END)

#button_didvision
def button_didvision():
    first_number=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first_number)
    e.delete(0,END)
    
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+int(second_number))
    if math=="subtraction":
        e.insert(0,f_num-int(second_number))
    if math=="multiplication":
        e.insert(0,f_num*int(second_number))
    if math=="division":
        e.insert(0,f_num/int(second_number))




button_1=Button(myframe,text="1",padx=40,pady=20,command=lambda:button_click(1))
button_2=Button(myframe,text="2",padx=40,pady=20,command=lambda:button_click(2))
button_3=Button(myframe,text="3",padx=40,pady=20,command=lambda:button_click(3))
button_4=Button(myframe,text="4",padx=40,pady=20,command=lambda:button_click(4))
button_5=Button(myframe,text="5",padx=40,pady=20,command=lambda:button_click(5))
button_6=Button(myframe,text="6",padx=40,pady=20,command=lambda:button_click(6))
button_7=Button(myframe,text="7",padx=40,pady=20,command=lambda:button_click(7))
button_8=Button(myframe,text="8",padx=40,pady=20,command=lambda:button_click(8))
button_9=Button(myframe,text="9",padx=40,pady=20,command=lambda:button_click(9))
button_0=Button(myframe,text="0",padx=40,pady=20,command=lambda:button_click(0))
button_add=Button(myframe,text="+",padx=40,pady=20,background="#FF9F0A",fg="white",command=button_add)
button_point=Button(myframe,text=".",padx=40,pady=20,command=lambda:button_click("."))
button_minus=Button(myframe,text="-",padx=40,pady=20,background="#FF9F0A",fg="black",command=button_minus)
button_multiply=Button(myframe,text="*",padx=40,pady=20,background="#FF9F0A",fg="black",command=button_multiply)
button_didvision=Button(myframe,text="/",padx=40,pady=20,background="#FF9F0A",fg="black",command=button_didvision)
button_equal=Button(myframe,text="=",padx=91,pady=20,background="#FF9F0A",fg="white",command=button_equal)
button_clear=Button(myframe,text="c",padx=40,pady=20,background="red",fg="white",command=button_clear)



# pat the button on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_point.grid(row=4,column=1)
button_minus.grid(row=4,column=2)
button_add.grid(row=5,column=1)
button_multiply.grid(row=5,column=0)
# button_clear.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=5,column=2)

button_didvision.grid(row=6,column=0)
button_equal.grid(row=6,column=1,columnspan=2)

root.mainloop()