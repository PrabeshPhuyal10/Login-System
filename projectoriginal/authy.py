import os
import pandas as pd

class User:
    def __init__(self, username, full_name, role):
        self.username = username
        self.full_name = full_name
        self.role = role


def authenticate(username, password):
    """
    Authenticate the user by checking the credentials in passwords.txt.
    Returns the role (admin or student) if valid, otherwise None.
    """
    try:
        with open("projectoriginal/data/passwords.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 3:  # Ensure exactly 3 values
                    print(f"Skipping malformed line in passwords.txt: {line.strip()}")
                    continue
                stored_username, stored_password, role = parts
                if username == stored_username and password == stored_password:
                    return role  # Return the role (admin or student)
    except FileNotFoundError:
        print("Error: passwords.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None

def get_user_details(username):
    """
    Fetch user details from users.txt based on the username.
    Returns a User object if found, otherwise None.
    """
    try:
        with open("projectoriginal/data/users.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 3:  # Ensure exactly 3 values
                    print(f"Skipping malformed line in users.txt: {line.strip()}")
                    continue
                stored_username, full_name, role = parts
                if username == stored_username:
                    return User(username, full_name, role)
    except FileNotFoundError:
        print("Error: users.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None

def get_student_count():
    """
    Count the total number of students from users.txt.
    Returns the student count.
    """
    count = 0  # Initialize the count

    try:
        with open("projectoriginal/data/users.txt", "r") as file:  # Open the file
            for line in file:
                parts = line.strip().split(",")  # Split by comma
                if len(parts) == 3 and parts[2] == "student":  # Check if role is 'student'
                    count += 1  # Increment count
    except FileNotFoundError:
        print("Error: users.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")

    return count  # Return the final count
def get_admin_count():
    """
    Count the total number of students from users.txt.
    Returns the student count.
    """
    count = 0  # Initialize the count

    try:
        with open("projectoriginal/data/users.txt", "r") as file:  # Open the file
            for line in file:
                parts = line.strip().split(",")  # Split by comma
                if len(parts) == 3 and parts[2] == "admin":  # Check if role is 'student'
                    count += 1  # Increment count
    except FileNotFoundError:
        print("Error: users.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")

    return count  # Return the final count
def get_eca_count():
    """
    Count the total number of students from users.txt.
    Returns the student count.
    """
    unique_ecas = set()

    try:
        with open("projectoriginal/data/eca.txt", "r") as file:  # Open the file
            for line in file:
                parts = line.strip().split(",") 
                ecas = parts[1:]
                unique_ecas.update(ecas)
                
    except FileNotFoundError:
        print("Error: users.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")

    return len(unique_ecas) # Return the final count





def add_user(username, full_name, password, role):
    """
    Add a new user to users.txt and passwords.txt.
    """
    try:
        # Check if the username already exists
        with open("projectoriginal/data/users.txt", "r") as file:
            for line in file:
                stored_username = line.strip().split(",")
                if username == stored_username:
                    return False  # Username already exists

        # Add the user to users.txt
        with open("projectoriginal/data/users.txt", "a") as file:
            file.write(f"{username},{full_name},{role}\n")

        # Add the user to passwords.txt
        with open("projectoriginal/data/passwords.txt", "a") as file:
            file.write(f"{username},{password},{role}\n")

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def delete_user(username):
    """
    Delete a user from users.txt and passwords.txt.
    """
    try:
        # Remove the user from users.txt
        with open("projectoriginal/data/users.txt", "r") as file:
            lines = file.readlines()
        with open("projectoriginal/data/users.txt", "w") as file:
            for line in lines:
                if not line.startswith(username + ","):
                    file.write(line)

        # Remove the user from passwords.txt
        with open("projectoriginal/data/passwords.txt", "r") as file:
            lines = file.readlines()
        with open("projectoriginal/data/passwords.txt", "w") as file:
            for line in lines:
                if not line.startswith(username + ","):
                    file.write(line)

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False




def get_student_eca(username):
    """
    Fetch extracurricular activities for a student from eca.txt.
    Returns a list of activities if found, otherwise None.
    """
    try:
        with open("projectoriginal/data/eca.txt", "r") as file:  # Adjust path as needed
            for line in file:
                parts = line.strip().split(",")  # Split the line by commas
                stored_username = parts[0]       # First part is the username
                ecas = parts[1:]                 # Everything after is activities
                if stored_username == username:  # Match the username
                    return ecas                  # Return the list of activities
            print(f"No match found for username: {username}")  # Debug
    except FileNotFoundError:
        print("Error: eca.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None

def get_student_grades(username):
    """
    Fetch grades for a student from grades.txt using pandas.
    Returns a list of grades if found, otherwise None.
    """
    subjects = ['Math', 'Science', 'English']  # Define subjects

    try:
        # Read txt file without headers
        df = pd.read_csv("projectoriginal/data/grades.txt", header=None)
        
        # Assign column names: 'Student' for username, then subjects
        columns = ['Student'] + subjects
        df.columns = columns
        
        # Check if student exists
        if username not in df['Student'].values:
            print(f"No match found for username: {username}")
            return None

        # Get row of that student
        student_data = df[df['Student'] == username]

        # Extract grades (skip 'Student' column)
        grades = student_data.iloc[0, 1:].tolist()  # Gets grades as a list
        
        return grades

    except FileNotFoundError:
        print("Error: grades.txt file not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def update_student_profile(username, full_name):
    """
    Update the student's profile information in users.txt.
    """
    try:
        updated = False
        with open("data/users.txt", "r") as file:
            lines = file.readlines()
        with open("data/users.txt", "w") as file:
            for line in lines:
                stored_username, role = line.strip().split(",")
                if username == stored_username:
                    file.write(f"{username},{full_name},{role}\n")
                    updated = True
                else:
                    file.write(line)
        return updated
    except Exception as e:
        print(f"Error: {e}")
        return False



