import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox

def plot_student_trend(student_name):

    subjects = ['Math','Science','English']

    try:
        # Read txt file without headers
        df = pd.read_csv('projectoriginal/data/grades.txt', header=None)
        
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


    

def plot_grade_distribution_pie():
    # Define grade categories (simpler version)
    grade_ranges = [
        ('A+', 90, 100),
        ('A', 80, 89),
        ('B', 70, 79),
        ('C', 60, 69),
        ('D', 50, 59),
        ('F', 0, 49)
    ]
    
    try:
        # Read the grades file (assuming columns: Student, Math, Science, English)
        df = pd.read_csv('projectoriginal/data/grades.txt', header=None)
        df.columns = ['Student', 'Math', 'Science', 'English']
        
        # Combine all subject grades into a single list
        all_grades = []
        for subject in ['Math', 'Science', 'English']:
            all_grades.extend(df[subject].tolist())
        
        # Count how many grades fall into each category
        grade_counts = {}
        for (grade, low, high) in grade_ranges:
            if grade == 'F':
                count = sum(1 for mark in all_grades if mark <= high)
            else:
                count = sum(1 for mark in all_grades if low <= mark <= high)
            grade_counts[grade] = count
        
        # Plot the pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(grade_counts.values(), labels=grade_counts.keys(), autopct='%1.1f%%')
        plt.title('Overall Grade Distribution (All Students)')
        plt.show()
        
    except FileNotFoundError:
        messagebox.showerror("Error", "Could not find grades.txt file")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
  

import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox

def compare_two_students(student1, student2):
    """Compare two students using a horizontal bar chart."""
    try:
        # Read data
        df = pd.read_csv('projectoriginal/data/grades.txt', header=None)
        df.columns = ['Student', 'Math', 'Science', 'English']
        
        # Get student data
        if student1 not in df['Student'].values or student2 not in df['Student'].values:
            messagebox.showwarning("Not Found", "One or both students not found in records!")
            return
        
        student1_data = df[df['Student'] == student1].iloc[0]
        student2_data = df[df['Student'] == student2].iloc[0]
        
        # Prepare data
        subjects = ['Math', 'Science', 'English']
        grades1 = student1_data[subjects].values
        grades2 = student2_data[subjects].values
        
        # Create figure
        plt.figure(figsize=(8, 5))
        
        # Plot horizontal bars
        plt.barh(subjects, grades1, color='lightblue', label=student1, alpha=0.8)
        plt.barh(subjects, grades2, color='orange', label=student2, alpha=0.8)
        
        # Add value labels
        for i, (g1, g2) in enumerate(zip(grades1, grades2)):
            plt.text(g1, i, f' {g1}', va='center', color='black')
            plt.text(g2, i, f' {g2}', va='center', color='black')
        
        # Formatting
        plt.title(f'Grade Comparison: {student1} vs {student2}')
        plt.xlabel('Grades')
        plt.ylabel('Subjects')
        plt.xlim(0, 100)  # Assuming grades are out of 100
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.legend()
        plt.tight_layout()
        plt.show()
        
    except FileNotFoundError:
        messagebox.showerror("Error", "Grades file not found at 'data/grades.txt'!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")