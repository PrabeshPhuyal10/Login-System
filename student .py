from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import os

# Ensure data folder exists
os.makedirs("projectoriginal/data", exist_ok=True)

# Save credentials
with open("student_data/id.txt", "w") as f:
    f.write("Prabesh")

with open("student_data/password.txt", "w") as r:
    r.write("leomessi")

# Main window setup
project = Tk()
project.title("Student Login System")
project.geometry("800x600")
project.configure(background="#1e1e2f")

# Fonts
title_font = Font(family="Poppins", size=30)
label_font = Font(family="Roboto", size=15)
button_font = Font(family="Poppins", size=12)

# Login Logic
def trigger():
    f1 = form.get()
    f2 = form_ii.get()

    with open("projectoriginal/data/users.txt", "r") as z1:
        save_id = z1.read().strip()

    with open("projectoriginal/data/passwords.txt", "r") as z2:
        save_pass = z2.read().strip()

    if f1 == save_id and f2 == save_pass:
        messagebox.showinfo("Success", "Your Data is Correct")
        new_window()
    else:
        messagebox.showerror("Error", "Your Data is Incorrect")

# Dashboard Window
def new_window():
    win = Toplevel()
    win.geometry("300x200")
    win.configure(background="#1e1e2f")

    Button(win, width=10, height=2, text="ECA", font=button_font,
           fg="#ffffff", bg="#4caf50", command=trigger_eca).pack(pady=10)

    Button(win, width=10, height=2, text="Grades", font=button_font,
           fg="#ffffff", bg="#2196f3", command=trigger_grades).pack(pady=10)

# ECA Page
def trigger_eca():
    eca = Toplevel()
    eca.geometry("300x200")
    eca.configure(background="#1e1e2f")

    try:
        with open("projectoriginal/data/eca.txt", "r") as eca_data:
            std_eca = eca_data.read()
    except:
        std_eca = "No ECA data available."

    Label(eca, text=std_eca, fg="#ffffff", bg="#1e1e2f", font=label_font, wraplength=280).pack(pady=10)

# Grades Page
def trigger_grades():
    grades = Toplevel()
    grades.geometry("300x200")
    grades.configure(background="#1e1e2f")

    try:
        with open("projectoriginal/data/grades.txt", "r") as grades_data:
            grades_eca = grades_data.read()
    except:
        grades_eca = "No grades data available."

    Label(grades, text=grades_eca, fg="#ffffff", bg="#1e1e2f", font=label_font, wraplength=280).pack(pady=10)

# UI Components
Label(project, text="Student Login System", fg="#ffffff", bg="#1e1e2f", font=title_font).pack(pady=40)

Label(project, text="Enter Username", fg="#ffffff", bg="#1e1e2f", font=label_font).pack(pady=5)
form = Entry(project, width=30, font=label_font)
form.pack(pady=10)

Label(project, text="Enter Password", fg="#ffffff", bg="#1e1e2f", font=label_font).pack(pady=5)
form_ii = Entry(project, width=30, font=label_font, show="*")
form_ii.pack(pady=10)

Button(project, width=10, height=2, text="Submit", font=button_font,
       fg="#ffffff", bg="#f39c12", command=trigger).pack(pady=30)

project.mainloop()
