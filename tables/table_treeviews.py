from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import Scrollbar, ttk
from tkinter import messagebox
import treeview_connection

#from tkinter import Scrollbar


root=Tk()
root.title("Weather app tree views")
# adding logo
root.iconbitmap("img/logo.ico")
root.geometry("600x600")

# Add some style
style=ttk.Style()


# Pick a theme
style.theme_use("default")


# configure the treeview colors
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25, #our height of the row
                fieldbackground="#D3D3D3"
                )


# Change selected color
style.map("Treeview",
          background=[('selected','#347083')])

# creating menu
my_menu=Menu(root)
root.config(menu=my_menu)


def lookup_record():
    searchframe=Frame(root)
    searchframe.pack(pady=20)
    # entry labels
    search_label=Label(searchframe, text="Enter ID", font=("Helvetica",18))
    search_label.grid(row=0,column=0)
    search_entry=Entry(searchframe)
    search_entry.grid(row=0, column=1)
    # search btn
    search_btn=Button(searchframe, text="Search", font=("Helvential",20))
    search_btn.grid(row=0, column=2,padx=10,pady=10)

# search menu
search_menu=Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Search", menu=search_menu)
search_menu.add_command(label="Search Record", command=lookup_record)

user_menu=Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Users", menu=user_menu)



# create a treeview frame
tree_frame=Frame(root)
tree_frame.pack(pady=20)

# create a scrollbar
#tree_scroll=Scrollbar(tree_frame)

# create a treeview scrollbar
tree_scroll=Scrollbar(tree_frame,orient="vertical")
tree_scroll.pack(side=RIGHT, fill=Y)

# create a treeview
my_tree=ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# configure the scrollbar
tree_scroll.config(command=my_tree.yview)


# defines our colunns
#my_tree['columns']=("First Name", "Last Name", "ID", "Address", "City","State", "Zipcode")
my_tree['columns']=("User ID","First Name", "Last Name", "Address", "City","State", "Zipcode")
#my_tree['columns']=("ID", "Address", "City", "State", "Zipcode")



# format our colunns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("User ID", anchor=CENTER, width=100)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column("Last Name", anchor=W, width=140)
my_tree.column("Address", anchor=CENTER, width=100)
my_tree.column("City", anchor=CENTER, width=140)
my_tree.column("State", anchor=CENTER, width=140)
my_tree.column("Zipcode", anchor=CENTER, width=140)



# create headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("User ID", text="ID", anchor=CENTER)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("Address", text="Address", anchor=CENTER)
my_tree.heading("City", text="City", anchor=CENTER)
my_tree.heading("State", text="State", anchor=CENTER)
my_tree.heading("Zipcode", text="Zipcode", anchor=CENTER)

''' 
data = [
    ["chika", "nwazup", "accra ghana", "greater accra", "Ghana", "122"],
    ["john", "doe", "new york", "new york city", "NY", "10001"],
    ["jane", "smith", "los angeles", "los angeles", "CA", "90001"],
    ["alex", "brown", "london", "greater london", "UK", "SW1A 1AA"],
    ["maria", "lopez", "madrid", "community of madrid", "Spain", "28001"],
    ["sara", "miller", "sydney", "new south wales", "Australia", "2000"],
    ["lucas", "wang", "beijing", "beijing", "China", "100000"],
    ["mario", "rossi", "rome", "lazio", "Italy", "00118"],
    ["yuki", "tanaka", "tokyo", "tokyo", "Japan", "100-0001"],
    ["carla", "santos", "rio de janeiro", "rio de janeiro", "Brazil", "20040-902"],
    ["chika", "nwazup", "accra ghana", "greater accra", "Ghana", "122"],
    ["john", "doe", "new york", "new york city", "NY", "10001"],
    ["jane", "smith", "los angeles", "los angeles", "CA", "90001"],
    ["alex", "brown", "london", "greater london", "UK", "SW1A 1AA"],
    ["maria", "lopez", "madrid", "community of madrid", "Spain", "28001"],
    ["sara", "miller", "sydney", "new south wales", "Australia", "2000"],
    ["lucas", "wang", "beijing", "beijing", "China", "100000"],
    ["mario", "rossi", "rome", "lazio", "Italy", "00118"],
    ["yuki", "tanaka", "tokyo", "tokyo", "Japan", "100-0001"],
    ["carla", "santos", "rio de janeiro", "rio de janeiro", "Brazil", "20040-902"]
]
 '''

# add data 
def add_data():
    conn = sqlite3.connect("tree_crm.db")
    c = conn.cursor()
   
    conn.commit()
    conn.close()    



# fetch data

# def querydata():
#     conn = sqlite3.connect("tree_crm.db")
#     c = conn.cursor()

#     c.execute("SELECT * FROM customers")
#     records = c.fetchall()
    
#     if not records:
#         print("no recode")
        
#     else:
#         print("we have recored")

#     conn.close()
    
def querydata():
    try:
        print("Attempting to connect to the database...")
        conn = sqlite3.connect("tree_crm.db")
        print("Connected to database")
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM customers")
        records = c.fetchall()
        global count
        count=0

        if not records:
            print("No records found.")
        else:
            #print("Records found:", records)
            for i, row in enumerate(records, start=1):
                if i % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=i, text='', values=row, tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=i, text='', values=row, tags=('oddrow', ))
            
    except sqlite3.Error as e:
        print("SQLite error:", e)

    finally:
        conn.close()


# create striped row tags

my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# add our data to the screen
# global count
# count=0

# for record in data:
#     if count % 2 ==0:
#         my_tree.insert(parent='',index='end',iid=count, text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('evenrow',))
        
#     else:
#         my_tree.insert(parent='',index='end',iid=count, text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('oddrow',))
#         # increament counter
#     count +=1
        

# creating our inputs
data_frame=LabelFrame(root,text="Record")
data_frame.pack(fill="x",expand="yes",padx=20)

fn_label=Label(data_frame, text="First Name")
fn_label.grid(row=0,column=0,padx=10,pady=10)
fn_entry=Entry(data_frame)
fn_entry.grid(row=0,column=1,padx=10,pady=10)

ln_label=Label(data_frame, text="Last Name")
ln_label.grid(row=0,column=2,padx=10,pady=10)
ln_entry=Entry(data_frame)
ln_entry.grid(row=0,column=3,padx=10,pady=10)



address_label=Label(data_frame, text="Address")
address_label.grid(row=0,column=4,padx=10,pady=10)
address_entry=Entry(data_frame)
address_entry.grid(row=0,column=5,padx=10,pady=10)

city_label=Label(data_frame, text="City")
city_label.grid(row=1,column=0,padx=10,pady=10)
city_entry=Entry(data_frame)
city_entry.grid(row=1,column=1,padx=10,pady=10)

state_label=Label(data_frame, text="State")
state_label.grid(row=1,column=2,padx=10,pady=10)
state_entry=Entry(data_frame)
state_entry.grid(row=1,column=3,padx=10,pady=10)

zipcode_label=Label(data_frame, text="Zipcode")
zipcode_label.grid(row=1,column=4,padx=10,pady=10)
zipcode_entry=Entry(data_frame)
zipcode_entry.grid(row=1,column=5,padx=10,pady=10)

# getting selected data in the treeview into entry box
def select_record(e):
    global id_label
    global id_entry
    id_label=Label(data_frame, text="ID")
    id_label.grid(row=2,column=0,padx=10,pady=10)
    id_entry=Entry(data_frame)
    id_entry.grid(row=2,column=1,padx=10,pady=10)
    
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)
    
    # grab the selected number
    selected=my_tree.focus()
    # grab the focus value
    values=my_tree.item(selected, "values")
    
    fn_entry.insert(0, values[1])
    ln_entry.insert(0, values[2])
    id_entry.insert(0, values[0])
    address_entry.insert(0, values[3])
    city_entry.insert(0, values[4])
    state_entry.insert(0, values[5])
    zipcode_entry.insert(0, values[6])


# clearentries
def clearentries():
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)
    id_entry.grid_remove()
    id_label.grid_remove()
    

# move row up 
def move_up():
    rows=my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)


# move row down
def move_down():
    rows=my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

# remove one
def remove_one():
    x=my_tree.selection()[0]
    my_tree.delete(x)
    conn =sqlite3.connect("tree_crm.db")
    c=conn.cursor()
    # delete from database
    c.execute("DELETE FROM customers WHERE oid="+id_entry.get())
    
    conn.commit()
    conn.close()
    # message box
    messagebox.showinfo("Deleted", "Record has been deleted")
    # clear the entry box
    clearentries()
    id_entry.grid_remove()
    id_label.grid_remove()
    # clear the treeview table
    my_tree.delete(*my_tree.get_children())
    
    # query the database
    querydata()
    
# remove_many
def remove_many():
   res=messagebox.askyesno("Delete many record", "Are you sure you want to delete many records \n on the table?")
   if res == 1:
        x=my_tree.selection()
        ids_to_delete=[]
        for record in x:
            ids_to_delete.append(my_tree.item(record, "values")[0])
            print(ids_to_delete)
        for record in x:
            my_tree.delete(record)
            conn =sqlite3.connect("tree_crm.db")
            c=conn.cursor()
            
            c.executemany("DELETE FROM customers WHERE oid=?", [(id,) for id in ids_to_delete])
            
            conn.commit()
            conn.close()
            my_tree.delete(*my_tree.get_children())
            # query the database
            querydata()
 
           

             
        
# remove all record
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)
    
    # delete from database
    response=messagebox.askyesno("Delete all record", "Are you sure you want to delete all records \n on the table?")
    if response == 1:
        conn =sqlite3.connect("tree_crm.db")
        c=conn.cursor()
        c.execute("DROP TABLE customers")

        conn.commit()
        conn.close()

    # clear the entry box
    clearentries()
    # clear the treeview table
    my_tree.delete(*my_tree.get_children())

    # query the database
    querydata()


       


# add data in to database
def add_record():
    conn =sqlite3.connect("tree_crm.db")
    c=conn.cursor()
    c.execute("INSERT INTO customers VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  "f_name":fn_entry.get(),
                  "l_name":ln_entry.get(),
                  "address":address_entry.get(),
                  "city":city_entry.get(),
                  "state":state_entry.get(),
                  "zipcode":zipcode_entry.get(),
              }

              )
    conn.commit()
    conn.close()

    # clear the entry box
    # fn_entry.delete(0, END)
    # ln_entry.delete(0, END)
    # address_entry.delete(0, END)
    # city_entry.delete(0, END)
    # state_entry.delete(0, END)
    # zipcode_entry.delete(0, END)
    clearentries()
    
    # clear the treeview table
    my_tree.delete(*my_tree.get_children())

    # query the database
    querydata()

# update record
def update_record():
    # grab selected values
    selected=my_tree.focus()
    # get database id
    my_tree.item(selected, text="", values=(id_entry.get(),fn_entry.get(), ln_entry.get(),  address_entry.get(), city_entry.get(), state_entry.get(),zipcode_entry.get(),))
    # update data in database
    conn =sqlite3.connect("tree_crm.db")
    c=conn.cursor()
    c.execute("""UPDATE customers SET 
              first_name=:first,
              last_name=:last,
              address=:address,
              city=:city,
              state=:state,
              zipcode=:zipcode
              
              WHERE oid=:oid""",
              {
                  "first":fn_entry.get(),
                  "last":ln_entry.get(),
                  "address":address_entry.get(),
                  "city":city_entry.get(),
                  "state":state_entry.get(),
                  "zipcode":zipcode_entry.get(),
                  "oid":id_entry.get(),
              }
              
              )
    conn.commit()
    conn.close()
   
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)
    id_label.grid_remove()
    id_entry.grid_remove()


# command fram
cm_frame=LabelFrame(root, text="Command", )
cm_frame.pack(fill="x", expand="yes", padx=20, pady=20)
# Center the contents horizontally
cm_frame.pack_propagate(False)
# fill="both"
update_btn=Button(cm_frame, text="Update Record", padx=10,pady=10, command=update_record)
update_btn.grid(row=0,column=0,padx=5,pady=5)

add_btn=Button(cm_frame, text="Add Record", padx=10,pady=10, command=add_record)
add_btn.grid(row=0,column=1,padx=5,pady=5)

remove_all_btn=Button(cm_frame, text="Remove all Records", padx=10,pady=10, command=remove_all)
remove_all_btn.grid(row=0,column=2,padx=5,pady=5)

remove_one_btn=Button(cm_frame, text="Remove one Record", padx=10,pady=10, command=remove_one)
remove_one_btn.grid(row=0,column=3,padx=5,pady=5)

remove_many_btn=Button(cm_frame, text="Remove many Record", padx=10,pady=10, command=remove_many)
remove_many_btn.grid(row=0,column=4,padx=5,pady=5)

move_up_btn=Button(cm_frame, text="Move up record", padx=10,pady=10, command=move_up)
move_up_btn.grid(row=0,column=5,padx=5,pady=5)

move_down_btn=Button(cm_frame, text="Move down record", padx=10,pady=10, command=move_down)
move_down_btn.grid(row=0,column=6,padx=5,pady=5)


clear_entries_btn=Button(cm_frame, text="Clear  entries", padx=10,pady=10, command=clearentries)
clear_entries_btn.grid(row=0,column=7,padx=5,pady=5)

querydata_btn=Button(cm_frame, text="Add data", padx=10,pady=10, command=add_data)
querydata_btn.grid(row=1,column=0,padx=5,pady=5)

# binding our treeview
my_tree.bind("<ButtonRelease-1>", select_record)

querydata()

root.mainloop()