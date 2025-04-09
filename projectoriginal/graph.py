import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox

def plot_student_trend(student_name):

    subjects = ['Math','Science','English']

    try:
        # Read txt file without headers
        df = pd.read_csv('data/grades.txt', header=None)
        
        # Assign column names (Student + Subject1, Subject2, etc.)
        columns = ['Student'] + subjects
        df.columns = columns
        
        # Check if student exists
        if student_name not in df['Student'].values:
            messagebox.showwarning("Not Found", f"Student '{student_name}' not found in records!")
            return

        # Get row of that student
        student_data = df[df['Student'] == student_name]

        # Subjects & their marks (skip 'Student' column)
        subjects = df.columns[1:]  # Gets ['Subject1', 'Subject2', ...]
        marks = student_data.iloc[0, 1:].tolist()  # Gets marks for all subjects

        # Plotting
        plt.figure(figsize=(10, 6))
        
        # Bar plot for better visualization of subject-wise marks
        bars = plt.bar(subjects, marks, color='skyblue')
        
        # Add value labels on top of each bar
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom')
        
        plt.title(f'Subject-wise Marks: {student_name}')
        plt.xlabel('Subjects')
        plt.ylabel('Marks')
        plt.ylim(0, 100)  # Assuming marks are out of 100
        plt.xticks(rotation=45)  # Rotate subject names for better readability
        plt.grid(True, axis='y')  # Only horizontal grid lines
        plt.tight_layout()
        plt.show()
        
    except FileNotFoundError:
        messagebox.showerror("Error", "Grades file not found at 'data/grades.txt'!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


    



# def plot_student_sem(student_name):
    # try:
    #     # Read txt file without headers and assign column names
    #     column_names = ['Student', 'Semester1', 'Semester2', 'Semester3']
    #     df = pd.read_csv('data/persem.txt', header=None, names=column_names)
        
    #     # Check if student exists
    #     if student_name not in df['Student'].values:
    #         messagebox.showwarning("Not Found", f"Student '{student_name}' not found in records!")
    #         return

    #     # Get row of that student
    #     student_data = df[df['Student'] == student_name]

    #     # Semesters & their marks (skip 'Student' column)
    #     semesters = df.columns[1:]  # Gets ['Semester1', 'Semester2', 'Semester3']
    #     marks = student_data.iloc[0, 1:].tolist()  # Gets marks for all semesters

    #     # Plotting
    #     plt.figure(figsize=(8, 5))
    #     plt.plot(semesters, marks, marker='o', color='blue', linestyle='-', linewidth=2)
    #     plt.title(f'Grade Trend: {student_name}')
    #     plt.xlabel('Semester')
    #     plt.ylabel('Marks')
    #     plt.ylim(0, 100)  # Assuming marks are out of 100
    #     plt.grid(True)
    #     plt.tight_layout()
    #     plt.show()
        
    # except FileNotFoundError:
    #     messagebox.showerror("Error", "Grades file not found at 'data/grades.txt'!")
    # except Exception as e:
    #     messagebox.showerror("Error", f"An error occurred: {str(e)}")