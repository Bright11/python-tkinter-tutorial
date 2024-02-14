import tkinter as tk
from tkinter import ttk
from reportlab.pdfgen import canvas

def save_to_pdf():
    # Create a PDF canvas
    c = canvas.Canvas("output.pdf")
    
    # Get the data from the Treeview
    tree_data = []
    for item in treeview.get_children():
        values = treeview.item(item, "values")
        tree_data.append(values)
    
    # Write the data to the PDF
    y_position = 700
    for data in tree_data:
        text = ", ".join(data)
        c.drawString(100, y_position, text)
        y_position -= 20
    
    # Save the PDF
    c.save()

# Create a tkinter window
root = tk.Tk()
root.title("PDF Generator")

# Create a Treeview widget
treeview = ttk.Treeview(root, columns=("Name", "Age", "Location"), show="headings")
treeview.heading("Name", text="Name")
treeview.heading("Age", text="Age")
treeview.heading("Location", text="Location")
treeview.pack()

# Insert some sample data into the Treeview
treeview.insert("", "end", values=("John Doe", "30", "New York"))
treeview.insert("", "end", values=("Jane Smith", "25", "Los Angeles"))
treeview.insert("", "end", values=("Tom Brown", "40", "Chicago"))

# Create a button to save to PDF
save_button = ttk.Button(root, text="Save to PDF", command=save_to_pdf)
save_button.pack()

# Run the tkinter event loop
root.mainloop()
