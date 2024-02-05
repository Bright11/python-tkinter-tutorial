import sqlite3
import os

database_file = 'address_book.db'

# Check if the database file already exists
if not os.path.exists(database_file):
    # If not, create the database and tables
    conn = sqlite3.connect(database_file)
    c = conn.cursor()

    # Creating database tables
    c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
    )""")

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()
else:
    print(f"The database '{database_file}' already exists.")
