from tkinter import messagebox
import bcrypt
import os
def user_exists(username):
    try:
        with open("projectoriginal/data/users.txt", 'r') as f:
            for line in f:
                if line.split(",")[0] == username:
                    return True
        return False
    except FileNotFoundError:
        return False


def add_user(username, fullname, role,password,eca=None,math_mark=0, science_mark=0, english_mark=0):
    if user_exists(username):
        return False
    
    try:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        # Add to users.txt
        with open("projectoriginal/data/users.txt", 'a+') as f:
            f.write(f"{username},{fullname},{role}\n")

        with open("projectoriginal/data/passwords_hashed.txt", 'a+') as f:
            f.write(f"{username},{hashed_password},{role}\n")

        # Add to passwords.txt
        with open("projectoriginal/data/passwords.txt", 'a+') as f:
            f.write(f"{username},{password},{role}\n")

        # Only save marks for students
        if role == "student":
            with open("projectoriginal/data/grades.txt", 'a+') as f:
                f.write(f"{username},{math_mark},{science_mark},{english_mark}\n")

            with open("projectoriginal/data/eca.txt", 'a+') as f:
                f.write(f"{username},{eca}\n")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save user: {str(e)}")
        return False
    
def delete_user(username):
    found = False
    try:
        # hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

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

        with open("projectoriginal/data/passwords_hashed.txt", 'r') as f:
            lines = f.readlines()
        with open("projectoriginal/data/passwords_hashed.txt", 'w') as f:
            for line in lines:
                if line.split(",")[0] != username:
                    f.write(line)

        with open("projectoriginal/data/grades.txt", 'r') as f:
            lines = f.readlines()
        with open("projectoriginal/data/grades.txt", 'w') as f:
            for line in lines:
                if line.split(",")[0] != username:
                    f.write(line)

        try:
            eca_path = "projectoriginal/data/eca.txt"
            if os.path.exists(eca_path):
                with open(eca_path, 'r') as f:
                    lines = f.readlines()
                with open(eca_path, 'w') as f:
                    for line in lines:
                        if line.split(",")[0] != username:
                            f.write(line)
            # If file doesn't exist, just do nothing
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete ECA data: {str(e)}")

        return found

        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save user: {str(e)}")
        return False
    except FileNotFoundError:
        return False
    
    

def get_average_percentage_all_students():
    total_percentage = 0
    student_count = 0

    try:
        with open("projectoriginal/data/grades.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")

                # Convert grades to integer list
                grades = list(map(int, parts[1:]))

                # Calculate percentage of current student
                percentage = sum(grades) / 3  

                total_percentage += percentage
                student_count += 1

        if student_count == 0:
            return 0  # Avoid divide by zero error

        # Final average percentage of all students
        avg= total_percentage / student_count  
        return avg

    except FileNotFoundError:
        print("Error: grades.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")

    return 0

def get_student_names():
    student_names = []
    try:
        with open("projectoriginal/data/users.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3 and parts[2] == "student":
                    student_names.append(parts[0])
    except FileNotFoundError:
        print("Error: users.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return student_names

def get_admin_names():
    admin_names = []
    try:
        with open("projectoriginal/data/users.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3 and parts[2] == "admin":
                    admin_names.append(parts[0])
    except FileNotFoundError:
        print("Error: users.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return admin_names


def get_eca_names():
    eca_names = set()
    try:
        with open("projectoriginal/data/eca.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                activities = parts[1:]  # Skip the username
                eca_names.update(activities)
    except FileNotFoundError:
        print("Error: eca.txt file not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return list(eca_names)

