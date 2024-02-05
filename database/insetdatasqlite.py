from tkinter import *
from PIL import ImageTk,Image
import sqlite3
import connection

root=Tk()
root.title("Tkinter sqlite3")
# adding logo
root.iconbitmap("img/logo.ico")
root.geometry("400x400")

# creating submit function
def submit():
    # connection to db
    #database_file = 'address_book.db'
    conn = sqlite3.connect(connection.database_file)
  
    #connection.conn
    # getting the cursor
    c = conn.cursor()
    
    # insert data
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                         
                         {
                             "f_name":f_name.get(),
                             "l_name":l_name.get(),
                             "address":address.get(),
                             "city":city.get(),
                             "state":state.get(),
                             "zipcode":zipcode.get(),
                         }
                         )
    # the end
    
    conn.commit()
    conn.close()
    
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

# dcreate query function
def query():
     conn = sqlite3.connect(connection.database_file)
     c = conn.cursor()
     
     c.execute("SELECT *, oid FROM addresses")
     records=c.fetchall()
     print(records)
     print_recordes=""
     #c.fetchall() #fetching all the data
    # c.fetchmany(5) #fetching 5 data
     #c.fetchone() #fetching one data
     print_recordes=""
    #  for record in records[0]:
     for record in records:
         print(record)
        #  print_recordes+=str(record)+"\n"
         print_recordes+=str(record[0])+ " " +str(record[1])+ " " +str(record[2])+ " " +str(record[3])+ " " +str(record[4])+ " " +str(record[5])+ " " +str(record[6])+  "\n"
         query_label=Label(root, text=print_recordes)
         query_label.grid(row=8, column=0, columnspan=2)
         
         
         conn.commit()
     conn.close()
    


# creating our text entrys
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)

address=Entry(root,width=30)
address.grid(row=2,column=1,padx=20)

city=Entry(root,width=30)
city.grid(row=3,column=1,padx=20)

state=Entry(root,width=30)
state.grid(row=4,column=1,padx=20)

zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20)

# entry labels
f_name_label=Label(root,text="Enter first name")
f_name_label.grid(row=0,column=0)

l_name_label=Label(root,text="Enter last name")
l_name_label.grid(row=1,column=0)

addres_label=Label(root,text="Enter address")
addres_label.grid(row=2,column=0)

city_label=Label(root,text="Enter City name")
city_label.grid(row=3,column=0)

state_label=Label(root,text="Enter state name")
state_label.grid(row=4,column=0)

zipcode_label=Label(root,text="Enter zipcode")
zipcode_label.grid(row=5,column=0)

# creating submit button
submit_btn=Button(root, text="Add data to database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

# query button
#query_btn=Button(root, text="Show data", command=lambda: connection.query())
query_btn=Button(root, text="Show data", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


root.mainloop()