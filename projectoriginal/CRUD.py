import tkinter as tk
from tkinter import messagebox, ttk


def user_exists(username):
    try:
        with open("projectoriginal/data/users.txt", 'r') as f:
            for line in f:
                if line.split(",")[0] == username:
                    return True
        return False
    except FileNotFoundError:
        return False


def add_user(username, fullname, role, password, math_mark=0, science_mark=0, english_mark=0):
    if user_exists(username):
        return False
    
    try:
        # Add to users.txt
        with open("projectoriginal/data/users.txt", 'a') as f:
            f.write(f"{username},{fullname},{role}\n")

        # Add to passwords.txt
        with open("projectoriginal/data/passwords.txt", 'a') as f:
            f.write(f"{username},{password},{role}\n")

        # Only save marks for students
        if role == "student":
            with open("projectoriginal/data/grades.txt", 'a') as f:
                f.write(f"{username},{math_mark},{science_mark},{english_mark}\n")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save user: {str(e)}")
        return False
    
def delete_user(username):
    found = False
    try:
        # Remove from users.txt
        with open("projectoriginal/data/users.txt", 'r') as f:
            lines = f.readlines()
        with open("projectoriginal/data/users.txt", 'w') as f:
            for line in lines:
                if line.split(",")[0] != username:
                    f.write(line)
                else:
                    found = True
        
        # Remove from passwords.txt
        with open("projectoriginal/data/passwords.txt", 'r') as f:
            lines = f.readlines()
        with open("projectoriginal/data/passwords.txt", 'w') as f:
            for line in lines:
                if line.split(",")[0] != username:
                    f.write(line)

        with open("projectoriginal/data/grades.txt", 'r') as f:
            lines = f.readlines()
        with open("projectoriginal/data/grades.txt", 'w') as f:
            for line in lines:
                if line.split(",")[0] != username:
                    f.write(line)

        return found
    except FileNotFoundError:
        return False



