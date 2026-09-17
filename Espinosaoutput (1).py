import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title(" Student Management System")
root.geometry("700x500")
root.configure(bg="#F2D9D3")

BG_COLOR="#EAF2F8"
TITLE_COLOR="#2E4057"
LABEL_COLOR="#34495E"
ENTRY_BG="#FFFFFF"
ADD_COLOR="#5DADE2"
UPDATE_COLOR="#58D68D"
DELETE_COLOR="#EC7063"
CLEAR_COLOR="#AF7AC5"

BUTTON_TEXT="FFFFFF"


#Title

title_label=tk.Label(
     root,
     text="Student Mangement System",
     font=("Arial", 18, "bold")
     
)

title_label.pack(pady=10)
#Input Frame

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

#Name
tk.Label(
    input_frame,
    text="Name:"
    ).grid(row=0, column=0,padx=5,pady=5)

name_entry = tk.Entry(input_frame,width=30)
name_entry.grid(row=0,column=1,padx=5,pady=5)


    
#Age
tk.Label(
    input_frame,
    text="Age:"
    ).grid(row=1,column=0,padx=5,pady=5)

age_entry = tk.Entry(input_frame,width=30)
age_entry.grid(row=1,column=1,padx=5,pady=5)



#Course
tk.Label(
    input_frame,
    text="Course:"
    ).grid(row=2,column=0,padx=5,pady=5)

course_entry = tk.Entry(input_frame,width=30)
course_entry.grid(row=2,column=1,padx=5,pady=5)

#Buttons
button_frame=tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Add",
    width=10,
    bg= "#AF7AC5",
    fg="white",
    command="add_student"
    ).grid(row=0,column=0,padx=5)


tk.Button(
    button_frame,
    text="Update",
    width=10,
    bg="#EC7063",
    fg="white",
    command="update_student"
    ).grid(row=0,column=1,padx=5)

tk.Button(
    button_frame,
    text="Delete",
    width=10,
    bg="#5DADE2",
    fg="white",
    command="delete_student"
    ).grid(row=0,column=2,padx=5)


tk.Button(
    button_frame,
    text="Clear",
    width=10,
    bg="#558B2F",
    fg="white",
    command="clear_student"
    ).grid(row=0,column=3,padx=5)


#Table
tree=ttk.Treeview(
    root,
    columns=("ID","Name","Age","Course"),
    show="headings"

    )

tree.heading("ID",text="ID")
tree.heading("Name",text="Name")
tree.heading("Age",text="Age")
tree.heading("Course",text="Course")


tree.column("ID",width=50)
tree.column("Name",width=200)
tree.column("Age",width=80)
tree.column("Course",width=200)


tree.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10

    )
tk.tk
tk.tk
