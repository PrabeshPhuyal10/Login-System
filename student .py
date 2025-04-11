from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import os
import json

# Ensure data folder exists
os.makedirs("student_data", exist_ok=True)

# Save credentials for three users in a JSON file
users_data = {
    "Prabesh": {
        "password": "leomessi",
        "eca": "Prabesh Phuyal:\n- Football\n- Debate Club",
        "grades": "Prabesh Phuyal:\n- Math: A\n- Science: B+\n- English: A-\n- History: B\n- Biology: B+\n- Chemistry: A"
    },
    "Samrat": {
        "password": "sam",
        "eca": "Samrat:\n- Basketball\n- Drama Club",
        "grades": "Samrat:\n- Math: B\n- Science: A-\n- English: B+\n- History: A\n- Biology: B\n- Chemistry: A-"
    },
    "Supritam": {
        "password": "sup",
        "eca": "Supritam:\n- Chess\n- Music Club",
        "grades": "Supritam:\n- Math: A-\n- Science: B+\n- English: B\n- History: A-\n- Biology: A\n- Chemistry: A+"
    }
}

# Save users data to a JSON file
with open("student_data/users.json", "w") as json_file:
    json.dump(users_data, json_file)

# Main window setup
project = Tk()
project.title("Student Login System")
project.geometry("800x600")
project.configure(background="#1e1e2f")

# Fonts
title_font = Font(family="Poppins", size=30)
label_font = Font(family="Roboto", size=15)
button_font = Font(family="Poppins", size=12)

# Globals
current_user = None
error_label = None

# Hover effect functions
def on_enter(e):
    hover_colors = {
        "Submit": "#e74c3c",
        "ECA Activities": "#2ecc71",
        "Grades": "#00bfff",  # brighter blue!
        "Logout": "#e74c3c",
        "Back to Dashboard": "#e74c3c"
    }
    e.widget["background"] = hover_colors.get(e.widget.cget("text"), "#e74c3c")

def on_leave(e):
    original_colors = {
        "Submit": "#f39c12",
        "ECA Activities": "#4caf50",
        "Grades": "#2196f3",  # original blue
        "Logout": "#f39c12",
        "Back to Dashboard": "#f39c12"
    }
    e.widget["background"] = original_colors.get(e.widget.cget("text"), "#f39c12")

# Function to hide all widgets
def clear_window():
    for widget in project.winfo_children():
        widget.destroy()

# Login Logic
def trigger():
    global current_user, error_label
    username = entry_username.get()
    password = entry_password.get()

    # Load users data from JSON
    with open("student_data/users.json", "r") as json_file:
        users_data = json.load(json_file)

    if error_label:
        error_label.destroy()

    if username in users_data and password == users_data[username]["password"]:
        current_user = username
        show_dashboard()
    else:
        error_label = Label(frame, text="Invalid username or password", fg="red", bg="#1e1e2f", font=label_font)
        error_label.pack(pady=5)

# Show Dashboard
def show_dashboard():
    clear_window()
    frame = Frame(project, bg="#1e1e2f")
    frame.pack(expand=True)

    Label(frame, text="Dashboard", fg="#ffffff", bg="#1e1e2f", font=title_font).pack(pady=40)

    add_hover_button(frame, "ECA Activities", "#4caf50", show_eca).pack(pady=20)
    add_hover_button(frame, "Grades", "#2196f3", show_grades).pack(pady=10)
    add_hover_button(frame, "Logout", "#f39c12", logout).pack(pady=20)

# ECA Page
def show_eca():
    clear_window()
    frame = Frame(project, bg="#16a085")
    frame.pack(expand=True)

    Label(frame, text="ECA Details", fg="#ffffff", bg="#16a085", font=title_font).pack(pady=10)

    with open("student_data/users.json", "r") as json_file:
        data = json.load(json_file)
        eca_content = data[current_user]["eca"]

    eca_text = Text(frame, wrap=WORD, font=label_font, bg="#1abc9c", fg="#ffffff", bd=0, padx=10, pady=10, height=10)
    eca_text.insert(END, eca_content)
    eca_text.configure(state=DISABLED)
    eca_text.pack(expand=True, fill=BOTH, padx=20, pady=10)

    add_hover_button(frame, "Back to Dashboard", "#f39c12", show_dashboard).pack(pady=20)

# Grades Page
def show_grades():
    clear_window()
    frame = Frame(project, bg="#2980b9")
    frame.pack(expand=True)

    Label(frame, text="Grades Details", fg="#ffffff", bg="#2980b9", font=title_font).pack(pady=10)

    with open("student_data/users.json", "r") as json_file:
        data = json.load(json_file)
        grades_content = data[current_user]["grades"]

    grades_text = Text(frame, wrap=WORD, font=label_font, bg="#3498db", fg="#ffffff", bd=0, padx=10, pady=10, height=10)
    grades_text.insert(END, grades_content)
    grades_text.configure(state=DISABLED)
    grades_text.pack(expand=True, fill=BOTH, padx=20, pady=10)

    add_hover_button(frame, "Back to Dashboard", "#f39c12", show_dashboard).pack(pady=20)

# Logout
def logout():
    global current_user
    current_user = None
    clear_window()
    show_login()

# Login screen
def show_login():
    global frame, entry_username, entry_password, error_label
    clear_window()

    frame = Frame(project, bg="#1e1e2f")
    frame.pack(expand=True)

    error_label = None

    Label(frame, text="Student Login System", fg="#ffffff", bg="#1e1e2f", font=title_font).pack(pady=40)

    Label(frame, text="Enter Username", fg="#ffffff", bg="#1e1e2f", font=label_font).pack(pady=5)
    entry_username = Entry(frame, width=30, font=label_font)
    entry_username.pack(pady=10)

    Label(frame, text="Enter Password", fg="#ffffff", bg="#1e1e2f", font=label_font).pack(pady=5)
    entry_password = Entry(frame, width=30, font=label_font, show="*")
    entry_password.pack(pady=10)

    add_hover_button(frame, "Submit", "#f39c12", trigger).pack(pady=30)

# Reusable button with hover effect
def add_hover_button(parent, text, bg, command):
    btn = Button(parent, text=text, font=button_font, fg="#ffffff", bg=bg,
                 activebackground=bg, width=15, height=2, command=command, border=0)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

# Start with login
show_login()
project.mainloop()
