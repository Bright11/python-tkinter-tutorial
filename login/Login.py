from tkinter import *
from PIL import ImageTk, Image
import Register
import sqlite3
import hashlib
# messagebox
from tkinter import messagebox

class Login:
     def __init__(self,window):
        self.window=window
        width=400
        height=300
        self.window.config(bg="black")
        screen_width=self.window.winfo_screenwidth()
        screen_height=self.window.winfo_screenheight()
        x=int((screen_width/2)-(width/2))
        y=int((screen_height/2)-(height/2))
        self.window.geometry(f"{width}x{height}+{x}+{y}")  # Make window size dynamic
        # self.window.state("zoomed")
        self.window.title("Registration")
        # font=("Helvetica,32")
        # self.window.iconbitmap("logo/me.ico")
        font="Helvetica, 15"
        
        loginframe=Frame(self.window, width=width,pady=50)
        # loginframe.place(relx=0.5,rely=0.5,anchor=CENTER )
        loginframe.pack(expand=True, fill="both",padx=20,)
        # loginframe.grid(row=0,column=0,padx=20,sticky="ew")
        global btnimg_btn
        btnimg=Image.open("icons/icons8-done.gif").resize((20,20))
        btnimg_btn=ImageTk.PhotoImage(btnimg)
        
    
        def loginnow():
            getuser=entry_name.get()
            print(getuser)
            self.login()
         
           
        
        # login labes
        label_user=Label(loginframe,text="User Name",font=font,width=10 )
        label_user.grid(row=0,column=0)
        # sticky="nsew"
        entry_name=Entry(loginframe,text="User  Name",fg="black",font=font)
        entry_name.grid(row=0,column=1,padx=10,pady=10)
        
        # login labes
        label_email=Label(loginframe,text="User Email",font=font,width=10 )
        label_email.grid(row=1,column=0)
        # sticky="nsew"
        entry_email=Entry(loginframe,text="User Email",fg="black",font=font)
        entry_email.grid(row=1,column=1,padx=10,pady=10)
        
        
        label_password=Label(loginframe,text="Paassword",font=font,width=10 )
        label_password.grid(row=2,column=0)
        # sticky="nsew"
        entry_password=Entry(loginframe,text="User Password",fg="black",font=font)
        entry_password.grid(row=2,column=1,padx=10,pady=10)
        
        submit_btn=Button(loginframe,text="Register",bg="purple",fg="white" ,command=loginnow,image=btnimg_btn, compound="left",padx=20, font="Helvetica, 15")
        submit_btn.grid(row=3,column=0,columnspan=3)
        
        footer_btn=Label(self.window,text="Bright C Web Developer", compound="left",padx=20)
        footer_btn.pack()
        

        
        
     def login(self):
        #  check if entrybox is empty
            win=Toplevel()
            Register.Register(win)
            self.window.withdraw()
            
            win.deiconify()
        
    
        
        
def page():
    window=Tk()
    Login(window)
    window.mainloop()
    
    
    
if __name__ =='__main__':
    page()