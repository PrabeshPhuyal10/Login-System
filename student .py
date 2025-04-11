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

# Current username
current_user = None

# Function to hide all widgets on the main window
def clear_window():
    for widget in project.winfo_children():
        widget.destroy()

# Login Logic
def trigger():
    global current_user
    username = entry_username.get()
    password = entry_password.get()

    # Load users data from JSON
    with open("student_data/users.json", "r") as json_file:
        users_data = json.load(json_file)

    if username in users_data:
        if password == users_data[username]["password"]:
            messagebox.showinfo("Success", "Your Data is Correct")
            current_user = username
            show_dashboard()
        else:
            messagebox.showerror("Error", "Incorrect Password")
    else:
        messagebox.showerror("Error", "Username not found")

# Show Dashboard
def show_dashboard():
    clear_window()
    frame = Frame(project, bg="#1e1e2f")
    frame.pack(expand=True)

    # Dashboard content
    Label(frame, text="Dashboard", fg="#ffffff", bg="#1e1e2f", font=title_font).pack(pady=40)

    Button(frame, width=15, height=2, text="ECA Activities", font=button_font,
           fg="#ffffff", bg="#4caf50", command=show_eca).pack(pady=20)

    Button(frame, width=15, height=2, text="Grades", font=button_font,
           fg="#ffffff", bg="#2196f3", command=show_grades).pack(pady=10)
    
    Button(frame, width=15, height=2, text="Logout", font=button_font,
           fg="#ffffff", bg="#f39c12", command=logout).pack(pady=20)  # Logout action

# ECA Page
def show_eca():
    clear_window()

    frame = Frame(project, bg="#16a085")
    frame.pack(expand=True)

    Label(frame, text="ECA Details", fg="#ffffff", bg="#16a085", font=title_font).pack(pady=10)

    # Load ECA details
    eca_content = users_data[current_user]["eca"]

    eca_text = Text(frame, wrap=WORD, font=label_font, bg="#1abc9c", fg="#ffffff", bd=0, padx=10, pady=10, height=10)
    eca_text.insert(END, eca_content)
    eca_text.configure(state=DISABLED)
    eca_text.pack(expand=True, fill=BOTH, padx=20, pady=10)

    Button(frame, width=15, height=2, text="Back to Dashboard", font=button_font,
           fg="#ffffff", bg="#f39c12", command=show_dashboard).pack(pady=20)

# Grades Page
def show_grades():
    clear_window()

    frame = Frame(project, bg="#2980b9")
    frame.pack(expand=True)

    Label(frame, text="Grades Details", fg="#ffffff", bg="#2980b9", font=title_font).pack(pady=10)

    # Load Grades details
    grades_content = users_data[current_user]["grades"]

    grades_text = Text(frame, wrap=WORD, font=label_font, bg="#3498db", fg="#ffffff", bd=0, padx=10, pady=10, height=10)
    grades_text.insert(END, grades_content)
    grades_text.configure(state=DISABLED)
    grades_text.pack(expand=True, fill=BOTH, padx=20, pady=10)

    Button(frame, width=15, height=2, text="Back to Dashboard", font=button_font,
           fg="#ffffff", bg="#f39c12", command=show_dashboard).pack(pady=20)

# Logout Function
def logout():
    global current_user
    current_user = None
    clear_window()
    show_login()

# Login Screen
def show_login():
    clear_window()

    frame = Frame(project, bg="#1e1e2f")
    frame.pack(expand=True)

    Label(frame, text="Student Login System", fg="#ffffff", bg="#1e1e2f", font=title_font).pack(pady=40)

    Label(frame, text="Enter Username", fg="#ffffff", bg="#1e1e2f", font=label_font).pack(pady=5)
    global entry_username
    entry_username = Entry(frame, width=30, font=label_font)
    entry_username.pack(pady=10)

    Label(frame, text="Enter Password", fg="#ffffff", bg="#1e1e2f", font=label_font).pack(pady=5)
    global entry_password
    entry_password = Entry(frame, width=30, font=label_font, show="*")
    entry_password.pack(pady=10)

    Button(frame, width=10, height=2, text="Submit", font=button_font,
           fg="#ffffff", bg="#f39c12", command=trigger).pack(pady=30)

# Show login screen initially
show_login()

# Main loop
project.mainloop()
