from tkinter import *
from tkinter import messagebox, ttk
import os

# Ensure data folder exists
os.makedirs("student_data", exist_ok=True)

# Save credentials
with open("student_data/id.txt", "w") as f:
    f.write("Prabesh,Samrat,Supritam")  # Three usernames
with open("student_data/password.txt", "w") as r:
    r.write("leomessi,sam,supritam123")  # Three passwords

# Save ECA and Grades for each user
with open("student_data/eca_Prabesh.txt", "w") as eca_file:
    eca_file.write("Football, Debate Club")
with open("student_data/eca_Samrat.txt", "w") as eca_file:
    eca_file.write("Basketball, Drama Club")
with open("student_data/eca_Supritam.txt", "w") as eca_file:
    eca_file.write("Chess, Music Club")

with open("student_data/grades_Prabesh.txt", "w") as grades_file:
    grades_file.write("A in Math, B+ in Science")
with open("student_data/grades_Samrat.txt", "w") as grades_file:
    grades_file.write("A- in English, B in History")
with open("student_data/grades_Supritam.txt", "w") as grades_file:
    grades_file.write("B+ in Biology, A in Chemistry")

# Main window setup
project = Tk()
project.title("Student Login System")
project.geometry("800x600")
project.configure(background="#1e1e2f")

# Fonts
title_font = ("Poppins", 30)
label_font = ("Roboto", 15)
button_font = ("Poppins", 12)

# Login Logic
def trigger():
    f1 = form.get()
    f2 = form_ii.get()

    with open("student_data/id.txt", "r") as z1:
        save_ids = z1.read().strip().split(",")  # Split IDs into a list
    with open("student_data/password.txt", "r") as z2:
        save_passwords = z2.read().strip().split(",")  # Split passwords into a list

    if f1 in save_ids:
        index = save_ids.index(f1)  # Find username index
        if f2 == save_passwords[index]:  # Check matching password
            messagebox.showinfo("Success", "Your Data is Correct")
            new_window()
        else:
            messagebox.showerror("Error", "Your Password is Incorrect")
    else:
        messagebox.showerror("Error", "Your Username is Incorrect")

# Dashboard Window
def new_window():
    win = Toplevel()
    win.geometry("300x200")
    win.configure(background="#2c3e50")
    win.title("Dashboard")

    Button(win, width=10, height=2, text="ECA", font=button_font,
           fg="#ffffff", bg="#4caf50", command=trigger_eca).pack(pady=10)

    Button(win, width=10, height=2, text="Grades", font=button_font,
           fg="#ffffff", bg="#2196f3", command=trigger_grades).pack(pady=10)

# ECA Page
def trigger_eca():
    eca = Toplevel()
    eca.geometry("400x300")
    eca.configure(background="#2c3e50")
    eca.title("ECA Details")

    Label(eca, text="Your ECA Activities", font=("Poppins", 18, "bold"), fg="#ecf0f1", bg="#2c3e50").pack(pady=10)

    frame = Frame(eca, bg="#34495e", bd=2, relief=GROOVE)
    frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

    text_area = Text(frame, wrap=WORD, font=("Roboto", 12), bg="#34495e", fg="#ecf0f1", bd=0, highlightthickness=0)
    text_area.pack(fill=BOTH, expand=True, padx=10, pady=10)

    scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=text_area.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    text_area["yscrollcommand"] = scrollbar.set

    try:
        with open(f"student_data/eca_{form.get()}.txt", "r") as eca_data:
            std_eca = eca_data.read()
    except:
        std_eca = "No ECA data available for this user."

    text_area.insert(END, std_eca)
    text_area.configure(state=DISABLED)

# Grades Page
def trigger_grades():
    grades = Toplevel()
    grades.geometry("400x300")
    grades.configure(background="#2c3e50")
    grades.title("Grades Details")

    Label(grades, text="Your Grades", font=("Poppins", 18, "bold"), fg="#ecf0f1", bg="#2c3e50").pack(pady=10)

    frame = Frame(grades, bg="#34495e", bd=2, relief=GROOVE)
    frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

    text_area = Text(frame, wrap=WORD, font=("Roboto", 12), bg="#34495e", fg="#ecf0f1", bd=0, highlightthickness=0)
    text_area.pack(fill=BOTH, expand=True, padx=10, pady=10)

    scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=text_area.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    text_area["yscrollcommand"] = scrollbar.set

    try:
        with open(f"student_data/grades_{form.get()}.txt", "r") as grades_data:
            grades_content = grades_data.read()
    except:
        grades_content = "No grades data available for this user."

    text_area.insert(END, grades_content)
    text_area.configure(state=DISABLED)

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