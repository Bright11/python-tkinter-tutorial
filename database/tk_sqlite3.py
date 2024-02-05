from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title("Tkinter sqlite3")
# adding logo
root.iconbitmap("img/logo.ico")
root.geometry("400x400")


# creating database or connection to database
conn=sqlite3.connect('address_book.db')

# creat cursor
c=conn.cursor()

# creating database tables
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)
          
          
          """)


# commit changes
conn.commit()

# close connection
conn.close()





root.mainloop()