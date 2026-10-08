import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# DATABASE
conn = sqlite3.connect("student_system.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT UNIQUE NOT NULL,
    full_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    city TEXT NOT NULL,
    occupation TEXT NOT NULL
)
""")
conn.commit()

# WINDOW
window = tk.Tk()
window.title("Student Management System")
window.geometry("1000x600")
window.resizable(False, False)

# VARIABLES
fields = [
    "Student ID", "Full Name", "Age",
    "Email", "Phone", "City", "Occupation"
]

vars = {x: tk.StringVar() for x in fields}


# CLEAR
def clear():
    for v in vars.values():
        v.set("")

    for item in table.selection():
        table.selection_remove(item)


# DISPLAY
def display():
    for item in table.get_children():
        table.delete(item)

    cursor.execute("""
        SELECT student_id, full_name, age, email,
               phone, city, occupation
        FROM students
        ORDER BY id
    """)

    for row in cursor.fetchall():
        table.insert("", tk.END, values=row)


# GET DATA
def get_data():
    data = [vars[x].get().strip() for x in fields]

    if "" in data:
        messagebox.showwarning(
            "Warning",
            "Please fill in all fields."
        )
        return None

    try:
        data[2] = int(data[2])

        if data[2] <= 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Error",
            "Age must be a valid number."
        )
        return None

    return data


# ADD
def add_student():
    data = get_data()

    if data:
        try:
            cursor.execute("""
                INSERT INTO students
                (student_id, full_name, age, email,
                 phone, city, occupation)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, data)

            conn.commit()
            messagebox.showinfo(
                "Success",
                "Student added successfully!"
            )

            clear()
            display()

        except sqlite3.IntegrityError:
            messagebox.showerror(
                "Error",
                "Student ID already exists."
            )


# SELECT
def select_student(event):
    selected = table.selection()

    if selected:
        values = table.item(selected[0])["values"]

        for i, field in enumerate(fields):
            vars[field].set(values[i])


# UPDATE
def update_student():
    selected = table.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a student."
        )
        return

    data = get_data()

    if data:
        old_id = table.item(selected[0])["values"][0]

        try:
            cursor.execute("""
                UPDATE students
                SET student_id=?, full_name=?, age=?,
                    email=?, phone=?, city=?, occupation=?
                WHERE student_id=?
            """, (*data, old_id))

            conn.commit()

            messagebox.showinfo(
                "Success",
                "Student updated successfully!"
            )

            clear()
            display()

        except sqlite3.IntegrityError:
            messagebox.showerror(
                "Error",
                "Student ID already exists."
            )


# DELETE
def delete_student():
    selected = table.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a student."
        )
        return

    student_id = table.item(
        selected[0]
    )["values"][0]

    if messagebox.askyesno(
        "Delete",
        "Are you sure you want to delete this student?"
    ):
        cursor.execute(
            "DELETE FROM students WHERE student_id=?",
            (student_id,)
        )

        conn.commit()

        messagebox.showinfo(
            "Success",
            "Student deleted successfully!"
        )

        clear()
        display()


# EXIT
def exit_program():
    if messagebox.askyesno(
        "Exit",
        "Are you sure you want to exit?"
    ):
        conn.close()
        window.destroy()


# TITLE
tk.Label(
    window,
    text="Student Management System",
    font=("Arial", 20, "bold")
).pack(pady=15)


# INPUTS
input_frame = tk.Frame(window)
input_frame.pack()

for i, field in enumerate(fields):
    row = i // 2
    col = (i % 2) * 2

    tk.Label(
        input_frame,
        text=field + ":"
    ).grid(
        row=row,
        column=col,
        padx=10,
        pady=8
    )

    tk.Entry(
        input_frame,
        textvariable=vars[field],
        width=30
    ).grid(
        row=row,
        column=col + 1,
        padx=10,
        pady=8
    )


# BUTTONS
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

for i, (text, command) in enumerate([
    ("Add", add_student),
    ("Update", update_student),
    ("Delete", delete_student),
    ("Clear", clear),
    ("Exit", exit_program)
]):
    tk.Button(
        button_frame,
        text=text,
        width=10,
        command=command
    ).grid(
        row=0,
        column=i,
        padx=5
    )


# TABLE TITLE
tk.Label(
    window,
    text="Student Information",
    font=("Arial", 14, "bold")
).pack(pady=10)


# TABLE
table = ttk.Treeview(
    window,
    columns=fields,
    show="headings",
    height=10
)

for field in fields:
    table.heading(field, text=field)
    table.column(field, width=130)

table.column("Student ID", width=110)
table.column("Age", width=50)

table.pack()

table.bind(
    "<<TreeviewSelect>>",
    select_student
)


# SHOW DATA
display()

# RUN
window.mainloop()
