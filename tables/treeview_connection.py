import sqlite3

conn =sqlite3.connect("tree_crm.db")

# create an instance
c=conn.cursor()
# create table
#   id integer,
c.execute("""CREATE TABLE if not exists customers (
    first_name text,
    last_name text,
   
    address text,
    city text,
    state text,
    zipcode text   
)         
          """)

# commit
conn.commit()
conn.close()
