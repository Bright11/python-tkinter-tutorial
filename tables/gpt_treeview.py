from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import Scrollbar, ttk
import treeview_connection

# import treeview_connection

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
my_tree['columns']=("First Name", "Last Name", "ID", "Address", "City","State", "Zipcode")


# format our colunns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column("Last Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Address", anchor=CENTER, width=100)
my_tree.column("City", anchor=CENTER, width=140)
my_tree.column("State", anchor=CENTER, width=140)
my_tree.column("Zipcode", anchor=CENTER, width=140)



# create headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Address", text="Address", anchor=CENTER)
my_tree.heading("City", text="City", anchor=CENTER)
my_tree.heading("State", text="State", anchor=CENTER)
my_tree.heading("Zipcode", text="Zipcode", anchor=CENTER)


data = [
    ["chika", "nwazup", "1", "accra ghana", "greater accra", "Ghana", "122"],
    ["john", "doe", "2", "new york", "new york city", "NY", "10001"],
    ["jane", "smith", "3", "los angeles", "los angeles", "CA", "90001"],
    ["alex", "brown", "4", "london", "greater london", "UK", "SW1A 1AA"],
    ["maria", "lopez", "5", "madrid", "community of madrid", "Spain", "28001"],
    ["sara", "miller", "6", "sydney", "new south wales", "Australia", "2000"],
    ["lucas", "wang", "7", "beijing", "beijing", "China", "100000"],
    ["mario", "rossi", "8", "rome", "lazio", "Italy", "00118"],
    ["yuki", "tanaka", "9", "tokyo", "tokyo", "Japan", "100-0001"],
    ["carla", "santos", "10", "rio de janeiro", "rio de janeiro", "Brazil", "20040-902"],
    ["chika", "nwazup", "11", "accra ghana", "greater accra", "Ghana", "122"],
    ["john", "doe", "12", "new york", "new york city", "NY", "10001"],
    ["jane", "smith", "13", "los angeles", "los angeles", "CA", "90001"],
    ["alex", "brown", "14", "london", "greater london", "UK", "SW1A 1AA"],
    ["maria", "lopez", "15", "madrid", "community of madrid", "Spain", "28001"],
    ["sara", "miller", "16", "sydney", "new south wales", "Australia", "2000"],
    ["lucas", "wang", "17", "beijing", "beijing", "China", "100000"],
    ["mario", "rossi", "18", "rome", "lazio", "Italy", "00118"],
    ["yuki", "tanaka", "19", "tokyo", "tokyo", "Japan", "100-0001"],
    ["carla", "santos", "20", "rio de janeiro", "rio de janeiro", "Brazil", "20040-902"]
]



# create striped row tags

my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# add our data to the screen
global count
count=0

for record in data:
    if count % 2 ==0:
        my_tree.insert(parent='',index='end',iid=count, text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('evenrow',))
        
    else:
        my_tree.insert(parent='',index='end',iid=count, text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('oddrow',))
        # increament counter
    count +=1
        

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

id_label=Label(data_frame, text="ID")
id_label.grid(row=0,column=4,padx=10,pady=10)
id_entry=Entry(data_frame)
id_entry.grid(row=0,column=5,padx=10,pady=10)

address_label=Label(data_frame, text="Address")
address_label.grid(row=1,column=0,padx=10,pady=10)
address_entry=Entry(data_frame)
address_entry.grid(row=1,column=1,padx=10,pady=10)

city_label=Label(data_frame, text="City")
city_label.grid(row=1,column=2,padx=10,pady=10)
city_entry=Entry(data_frame)
city_entry.grid(row=1,column=3,padx=10,pady=10)

state_label=Label(data_frame, text="State")
state_label.grid(row=1,column=4,padx=10,pady=10)
state_entry=Entry(data_frame)
state_entry.grid(row=1,column=5,padx=10,pady=10)

zipcode_label=Label(data_frame, text="Zipcode")
zipcode_label.grid(row=1,column=6,padx=10,pady=10)
zipcode_entry=Entry(data_frame)
zipcode_entry.grid(row=1,column=7,padx=10,pady=10)

# getting selected data in the treeview into entry box
def select_record(e):
    
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
    
    fn_entry.insert(0, values[0])
    ln_entry.insert(0, values[1])
    id_entry.insert(0, values[2])
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
    
# remove_many
def remove_many():
    x=my_tree.selection()
    for record in x:
        my_tree.delete(record)
        
# remove all record
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)


# update record
def update_record():
    # grab selected values
    selected=my_tree.focus()
    my_tree.item(selected, text="", values=(fn_entry.get(), ln_entry.get(), id_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(),zipcode_entry.get(),))
    
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)

# add dummy data

def dummdata():
    conn =sqlite3.connect("tree_crm.db")
    c=conn.cursor()
    for record in data:
       c.execute(
            "INSERT INTO customers VALUES (:first_name, :last_name, :id, :address, :city, :state, :zipcode )",
            {
                'first_name': record[0],
                'last_name':record[1],
                'id':record[2],
                'address':record[3],
                'city':record[4],
                'state':record[5],
                'zipcode':record[6]
            }
        )
    conn.commit()
    conn.close()

# query database sellect all
def querydata():
     conn =sqlite3.connect("tree_crm.db")
     c=conn.cursor()
     
     c.execute("SELECT * FROM customers")
     record=c.fetchall()
     print(record)
     
     
     conn.commit()
     conn.close()


# command fram
cm_frame=LabelFrame(root, text="Command", )
cm_frame.pack(fill="x", expand="yes", padx=20, pady=20)
# Center the contents horizontally
cm_frame.pack_propagate(False)
# fill="both"
update_btn=Button(cm_frame, text="Update Record", padx=10,pady=10, command=update_record)
update_btn.grid(row=0,column=0,padx=5,pady=5)

add_btn=Button(cm_frame, text="Add Record", padx=10,pady=10)
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

adddummydata_btn=Button(cm_frame, text="Add dummy data", padx=10,pady=10, command=dummdata)
adddummydata_btn.grid(row=1,column=0,padx=5,pady=5)

querydata_btn=Button(cm_frame, text="Query data", padx=10,pady=10, command=querydata)
querydata_btn.grid(row=1,column=1,padx=5,pady=5)
# binding our treeview
my_tree.bind("<ButtonRelease-1>", select_record)
root.mainloop()




# for i, row in enumerate(data, start=1):
#     if i % 2 == 0:
#         my_tree.insert(parent='', index='end', iid=i, values=row, tags=('evenrow',))
#     else:
#         my_tree.insert(parent='', index='end', iid=i, values=row, tags=('oddrow',))
