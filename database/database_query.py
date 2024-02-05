from tkinter import *
from PIL import ImageTk,Image
import sqlite3
import connection

root=Tk()
root.title("Tkinter sqlite3")
# adding logo
root.iconbitmap("img/logo.ico")
root.geometry("400x600")

# update record
def update():
   
    Label(editor,text=f_name_edit.get()).grid(row=0, column=2)
    conn = sqlite3.connect(connection.database_file)
    c = conn.cursor()
    record_id=select_box.get()
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {
            'first':f_name_edit.get(),
            'last':l_name_edit.get(),
            'address':address_edit.get(),
            'city':city_edit.get(),
            'state':state_edit.get(),
            'zipcode':zipcode_edit.get(),
            'oid':record_id
        })

    conn.commit()
    conn.close()

    editor.destroy()

def edit():
    global editor
    editor=Tk()
    editor.title("Edit data in sqlite")
    editor.iconbitmap("img/logo.ico")
    editor.geometry("400x400")
    
    conn = sqlite3.connect(connection.database_file)
    c = conn.cursor()
    recordes_id=select_box.get()
    c.execute("SELECT * FROM addresses WHERE oid = " + recordes_id)
    recordes=c.fetchall()
    
    global f_name_edit
    global l_name_edit
    global address_edit
    global city_edit
    global state_edit
    global zipcode_edit
    

    # conn.commit()
    # conn.close()
    
    f_name_edit=Entry(editor,width=30)
    f_name_edit.grid(row=0,column=1,padx=20,pady=10)

    l_name_edit=Entry(editor,width=30)
    l_name_edit.grid(row=1,column=1,padx=20,pady=10)

    address_edit=Entry(editor,width=30)
    address_edit.grid(row=2,column=1,padx=20,pady=10)

    city_edit=Entry(editor,width=30)
    city_edit.grid(row=3,column=1,padx=20,pady=10)

    state_edit=Entry(editor,width=30)
    state_edit.grid(row=4,column=1,padx=20,pady=10)

    zipcode_edit=Entry(editor,width=30)
    zipcode_edit.grid(row=5,column=1,padx=20,pady=10)

    # entry labels
    f_name_label_edit=Label(editor,text="Enter first name")
    f_name_label_edit.grid(row=0,column=0,padx=20,pady=10)

    l_name_label_edit=Label(editor,text="Enter last name")
    l_name_label_edit.grid(row=1,column=0,padx=20,pady=10)

    addres_label_edit=Label(editor,text="Enter address")
    addres_label_edit.grid(row=2,column=0,padx=20,pady=10)

    city_label_edit=Label(editor,text="Enter City name")
    city_label_edit.grid(row=3,column=0,padx=20,pady=10)

    state_label_edit=Label(editor,text="Enter state name")
    state_label_edit.grid(row=4,column=0,padx=20,pady=10)

    zipcode_label_edit=Label(editor,text="Enter zipcode")
    zipcode_label_edit.grid(row=5,column=0,padx=20,pady=10)
    
    for record in recordes:
        f_name_edit.insert(0,record[0])
        l_name_edit.insert(0,record[1])
        address_edit.insert(0,record[2])
        city_edit.insert(0,record[3])
        state_edit.insert(0,record[4])
        zipcode_edit.insert(0,record[5])
    
    # update button
    update_btn=Button(editor,text="Update", command=update)
    update_btn.grid(row=6,column=0,columnspan=2,pady=10, padx=10, ipadx=130)
    
    

# the end of editor

# deleting
def delete():
    conn = sqlite3.connect(connection.database_file)
    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid = " + select_box.get())

    select_box.delete(0, END)

    conn.commit()
    conn.close()

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
    records = c.fetchall()
    print(records)
    
    print_records = ""
    for record in records:
        print(record)
        print_records += f"{record[0]} {record[1]} {record[2]} {record[3]} {record[4]} {record[5]} {record[6]}\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2, padx=20,pady=20,ipadx=10,ipady=10)

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

# delete 
select_box=Entry(root, width=30)
select_box.grid(row=9,column=1,pady=10)
select_box_label=Label(root,text="Select Record")
select_box_label.grid(row=9,column=0,pady=10)

# creating submit button
submit_btn=Button(root, text="Add data to database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

# query button
#query_btn=Button(root, text="Show data", command=lambda: connection.query())
query_btn=Button(root, text="Show data", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Delete buttom
delete_btn=Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

edit_btn=Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

root.mainloop()