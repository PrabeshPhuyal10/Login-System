import tkinter as tk
import graph
from tkinter import messagebox, ttk, simpledialog
from PIL import ImageTk, Image
from authy import authenticate, get_user_details, get_student_count, get_eca_count, get_admin_count, get_student_eca, get_student_grades
from CRUD import add_user, delete_user, get_average_percentage_all_students, get_student_names, get_admin_names


class Login_System:

    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        # Load Images
        self.phone_image = ImageTk.PhotoImage(file="projectoriginal/images/login.png")
        self.lbl_Phone_image = tk.Label(self.root, image=self.phone_image, bg="#fafafa")
        self.lbl_Phone_image.place(x=150, y=150)

        # Login Frame
        login_frame = tk.Frame(self.root, bd=2, relief="ridge", bg="white")
        login_frame.place(x=750, y=90, width=350, height=460)

        # Title
        title = tk.Label(
            login_frame, text="Login System", font=("Arial", 20, "bold"), 
            bg="white", fg="#333333"
        )
        title.place(x=0, y=30, relwidth=1)

        # Username
        lbl_user = tk.Label(
            login_frame, text="Username", font=("Arial", 14), 
            bg="white", fg="#767171"
        )
        lbl_user.place(x=50, y=100)
        self.txt_username = tk.Entry(
            login_frame, font=("Arial", 14), bg="#F5F5F5", 
            relief="flat", highlightthickness=1, highlightcolor="#00b0f0"
        )
        self.txt_username.place(x=50, y=140, width=250, height=40)

        # Password
        lbl_pass = tk.Label(
            login_frame, text="Password", font=("Arial", 14), 
            bg="white", fg="#767171"
        )
        lbl_pass.place(x=50, y=200)
        self.txt_pass = tk.Entry(
            login_frame, font=("Arial", 14), bg="#F5F5F5", 
            show="*", relief="flat", highlightthickness=1, highlightcolor="#00b0f0"
        )
        self.txt_pass.place(x=50, y=240, width=250, height=40)

        # Login Button
        btn_login = tk.Button(
            login_frame, text="Login", font=("Arial", 14, "bold"),
            bg="#00b0f0", activebackground="#00a2e8",
            fg="white", activeforeground="white", cursor="hand2",
            relief="flat", command=self.login, bd=0
        )
        btn_login.place(x=50, y=300, width=250, height=45)

        # Add shadow effect to the button
        btn_login.bind("<Enter>", lambda e: btn_login.config(bg="#00a2e8"))
        btn_login.bind("<Leave>", lambda e: btn_login.config(bg="#00b0f0"))


        # Additional Styling
        # Separator Line
        separator = tk.Frame(login_frame, bg="#E0E0E0", height=1)
        separator.place(x=50, y=350, width=250)

        # Footer Text
        footer_text = tk.Label(
            login_frame, text="© 2025 Login System", font=("Arial", 10), 
            bg="white", fg="#767171"
        )
        footer_text.place(x=0, y=420, relwidth=1)
    
    
    def login(self):
        username = self.txt_username.get()
        password = self.txt_pass.get()

        role = authenticate(username, password)
        if role:
            user = get_user_details(username)
            if user:
                messagebox.showinfo("Login Successful", f"Welcome, {user.full_name} ({user.role})!")
                if role == "admin":
                    self.admin_dashboard(user)
                elif role == "student":
                    self.student_dashboard(user)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def admin_dashboard(self, user):
        self.dashboard_fm = tk.Frame(self.root, bg="#1e1e2f", highlightbackground="#ffffff", highlightthickness=2)
        self.dashboard_fm.pack(pady=5, fill=tk.BOTH, expand=True)

        options_fm = tk.Frame(self.dashboard_fm, bg="#1e1e2f", highlightbackground="#ffffff", highlightthickness=2)
        options_fm.place(x=0, y=0, width=120, height=575)

        # Home Button
        home_btn = tk.Button(options_fm, text='Home', font=('Arial', 12, "bold"), fg="#ffffff", bg="#4caf50",
                             bd=0, width=10, height=2, relief="flat",
                             command=lambda: self.switch(self.home_btn_indicator, self.home_page))
        home_btn.place(x=10, y=50)
        self.home_btn_indicator = tk.Label(options_fm, text='', bg="#4caf50")
        self.home_btn_indicator.place(x=9, y=53, width=3, height=40)

        # Find Student Button
        find_student_btn = tk.Button(options_fm, text='Find\nStudent', font=('Arial', 12, "bold"), fg="#ffffff",
                                     bg="#2196f3", bd=0, justify=tk.LEFT, width=10, height=2, relief="flat",
                                     command=lambda: self.switch(self.find_student_btn_indicator, self.find_page))
        find_student_btn.place(x=10, y=100)
        self.find_student_btn_indicator = tk.Label(options_fm, text='', bg="#2196f3")
        self.find_student_btn_indicator.place(x=9, y=103, width=3, height=40)

        # Logout Button
        logout_btn = tk.Button(options_fm, text='Logout', font=('Arial', 12, "bold"), fg="#ffffff", bg="#f44336",
                               bd=0, width=10, height=2, relief="flat", command=self.logout)
        logout_btn.place(x=10, y=240)

        # Pages Frame
        self.pages_fm = tk.Frame(self.dashboard_fm, bg="#1e1e2f")
        self.pages_fm.place(x=122, y=5, width=850, height=550)

        # Initial page load
        self.switch(self.home_btn_indicator, self.home_page)

    def switch(self, indicator, page):
        self.home_btn_indicator.config(bg="#4caf50")
        self.find_student_btn_indicator.config(bg="#2196f3")
        indicator.config(bg="#f39c12")
        for widget in self.pages_fm.winfo_children():
            widget.destroy()
        page()

    def home_page(self):
        # Create the home page frame
        home_page_fm = tk.Frame(self.pages_fm, bg="#1e1e2f", width=880)
        home_page_fm.pack(fill=tk.BOTH, expand=True)

        # Admin image
        admin_image = ImageTk.PhotoImage(file="projectoriginal/images/admin_img.png")
        lbl_admin_image = tk.Label(home_page_fm, image=admin_image, bg="#1e1e2f")
        lbl_admin_image.image = admin_image
        lbl_admin_image.place(x=20, y=20)

        # Welcome message
        hi_lb = tk.Label(home_page_fm, text='Hi Admin!', font=('Arial', 18, 'bold'), fg="#ffffff", bg="#1e1e2f")
        hi_lb.place(x=150, y=30)

        # Define helper functions for showing lists
        def show_student_names():
            admin_window = tk.Toplevel()
            admin_window.title("Student Names")
            admin_window.geometry("300x400")
            admin_window.config(bg="#1e1e2f")

            title_label = tk.Label(admin_window, text="Student List", font=('Arial', 14, 'bold'), bg="#1e1e2f", fg="#ffffff")
            title_label.pack(pady=10)

            frame = tk.Frame(admin_window, bg="#1e1e2f")
            frame.pack(fill=tk.BOTH, expand=True)

            scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, bg="#1e1e2f", troughcolor="#2c2c2c")
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            names_listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, font=('Arial', 12),
                                    bg="#1e1e2f", fg="#ffffff", selectbackground="#4caf50", selectforeground="#ffffff")
            names_listbox.pack(fill=tk.BOTH, expand=True)

            scrollbar.config(command=names_listbox.yview)

            student_names = get_student_names()
            if student_names:
                for name in student_names:
                    names_listbox.insert(tk.END, name)
            else:
                names_listbox.insert(tk.END, "No students found")

        def show_admin_names():
            admin_window = tk.Toplevel()
            admin_window.title("Admin Names")
            admin_window.geometry("300x400")
            admin_window.config(bg="#1e1e2f")

            title_label = tk.Label(admin_window, text="Admin List", font=('Arial', 14, 'bold'), bg="#1e1e2f", fg="#ffffff")
            title_label.pack(pady=10)

            frame = tk.Frame(admin_window, bg="#1e1e2f")
            frame.pack(fill=tk.BOTH, expand=True)

            scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, bg="#1e1e2f", troughcolor="#2c2c2c")
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            names_listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, font=('Arial', 12),
                                    bg="#1e1e2f", fg="#ffffff", selectbackground="#4caf50", selectforeground="#ffffff")
            names_listbox.pack(fill=tk.BOTH, expand=True)

            scrollbar.config(command=names_listbox.yview)

            admin_names = get_admin_names()
            if admin_names:
                for name in admin_names:
                    names_listbox.insert(tk.END, name)
            else:
                names_listbox.insert(tk.END, "No admins found")

        def show_eca_names():
            try:
                from CRUD import get_eca_names
                eca_names = get_eca_names()
            except ImportError:
                messagebox.showerror("Error", "Could not import get_eca_names. Check your CRUD module.")
                return []
            except Exception as e:
                messagebox.showerror("Error", f"Unexpected error while fetching ECA names: {e}")
                return []

            admin_window = tk.Toplevel()
            admin_window.title("ECA List")
            admin_window.geometry("300x400")
            admin_window.config(bg="#1e1e2f")

            title_label = tk.Label(admin_window, text="ECA List", font=('Arial', 14, 'bold'), bg="#1e1e2f", fg="#ffffff")
            title_label.pack(pady=10)

            frame = tk.Frame(admin_window, bg="#1e1e2f")
            frame.pack(fill=tk.BOTH, expand=True)

            scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, bg="#1e1e2f", troughcolor="#2c2c2c")
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            names_listbox = tk.Listbox(
                frame,
                yscrollcommand=scrollbar.set,
                font=('Arial', 12),
                bg="#1e1e2f",
                fg="#ffffff",
                selectbackground="#4caf50",
                selectforeground="#ffffff"
            )
            names_listbox.pack(fill=tk.BOTH, expand=True)

            scrollbar.config(command=names_listbox.yview)

            if eca_names:
                for name in eca_names:
                    names_listbox.insert(tk.END, name)
            else:
                names_listbox.insert(tk.END, "No ECAs found")

        # Student count display
        def studentcount():
            student_count = get_student_count()
            lbl_student_count = tk.Label(home_page_fm, text=f"Students: {student_count}",
                                        font=('Arial', 12), bg="#2196f3", fg='#ffffff', padx=15, pady=10, relief="flat")
            lbl_student_count.place(x=40, y=120)

        studentcount()

        # Admin count display
        def admincount():
            admin_count = get_admin_count()
            lbl_admin_count = tk.Label(home_page_fm, text=f"Admins: {admin_count}",
                                    font=('Arial', 12), bg="#ff9800", fg='#ffffff', padx=15, pady=10, relief="flat")
            lbl_admin_count.place(x=40, y=170)

        admincount()

        # ECA count display
        def totalECA():
            eca_count = get_eca_count()
            lbl_eca_count = tk.Label(home_page_fm, text=f"ECA: {eca_count}",
                                    font=('Arial', 12), bg="#00bcd4", fg='#ffffff', padx=15, pady=10, relief="flat")
            lbl_eca_count.place(x=40, y=220)

        totalECA()

        # Average percentage display
        def avgpercentage():
            avg_per = get_average_percentage_all_students()
            lbl_avg_percentage = tk.Label(home_page_fm, text=f"Avg Percentage: {avg_per:.2f}%",
                                        font=('Arial', 12), bg="#673ab7", fg='#ffffff', padx=15, pady=10, relief="flat")
            lbl_avg_percentage.place(x=40, y=270)

        avgpercentage()

        # Show Students button
        show_students_btn = tk.Button(home_page_fm, text="Show Students", font=('Arial', 12, "bold"),
                                    command=show_student_names, bg="#1976d2", fg="white", relief="flat",
                                    activebackground="#1565c0", activeforeground="white")
        show_students_btn.place(x=300, y=120)

        # Show Admins button
        show_admins_btn = tk.Button(home_page_fm, text="Show Admins", font=('Arial', 12, "bold"),
                                    command=show_admin_names, bg="#1976d2", fg="white", relief="flat",
                                    activebackground="#1565c0", activeforeground="white")
        show_admins_btn.place(x=300, y=170)

        # Show ECAs button
        show_ecas_btn = tk.Button(home_page_fm, text="Show ECAs", font=('Arial', 12, "bold"),
                                command=show_eca_names, bg="#1976d2", fg="white", relief="flat",
                                activebackground="#1565c0", activeforeground="white")
        show_ecas_btn.place(x=300, y=220)

        # Add User button
        add_user_btn = tk.Button(home_page_fm, text="Add User", font=('Arial', 14, "bold"),
                                fg="white", bg="#4caf50", relief="flat", activebackground="#388e3c",
                                activeforeground="white", command=self.add_user_ui)
        add_user_btn.place(x=200, y=400, width=150)

        # Delete User button
        delete_user_btn = tk.Button(home_page_fm, text="Delete User", font=('Arial', 14, "bold"),
                                    fg="white", bg="#f44336", relief="flat", activebackground="#d32f2f",
                                    activeforeground="white", command=self.delete_user_ui)
        delete_user_btn.place(x=450, y=400, width=150)
        
    def find_page(self):
        # Create the find page frame
        find_page_fm = tk.Frame(self.pages_fm, bg="#1e1e2f")
        find_page_fm.pack(fill=tk.BOTH, expand=True)

        # Title label
        title_label = tk.Label(find_page_fm, text="Find", font=('Arial', 20, 'bold'), fg="#ffffff", bg="#1e1e2f")
        title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Button to show grade trend
        def show_graph():
            student_name = simpledialog.askstring("Student Name", "Enter Student Name:")
            if student_name:
                graph.plot_student_trend(student_name)

        grade_trend_btn = tk.Button(
            find_page_fm,
            text="Show Grade Trend",
            font=('Arial', 14, "bold"),
            fg="white",
            bg="#f39c12",
            relief="flat",
            activebackground="#e67e22",
            activeforeground="white",
            command=show_graph
        )
        grade_trend_btn.place(relx=0.5, rely=0.3, anchor=tk.CENTER, width=250, height=50)

        # Button to show grade distribution pie chart
        def show_piegraph():
            graph.plot_grade_distribution_pie()

        grade_distribution_btn = tk.Button(
            find_page_fm,
            text="Grade Distribution",
            font=('Arial', 14, "bold"),
            fg="white",
            bg="#2ecc71",
            relief="flat",
            activebackground="#27ae60",
            activeforeground="white",
            command=show_piegraph
        )
        grade_distribution_btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=250, height=50)

        # Button to compare two students
        def compare_students():
            # Create the popup window
            popup = tk.Toplevel()
            popup.title("Compare Students")
            popup.geometry("350x200")
            popup.config(bg="#1e1e2f")

            # First student entry
            tk.Label(popup, text="First Student Name:", font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack(pady=(10, 0))
            entry1 = tk.Entry(popup, width=25, font=('Arial', 12))
            entry1.pack()
            entry1.focus_set()  # Auto-focus first field

            # Second student entry
            tk.Label(popup, text="Second Student Name:", font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack(pady=(10, 0))
            entry2 = tk.Entry(popup, width=25, font=('Arial', 12))
            entry2.pack()

            # Compare button
            def run_comparison():
                student1 = entry1.get().strip()
                student2 = entry2.get().strip()

                if student1 and student2:  # Only proceed if both fields are filled
                    graph.compare_two_students(student1, student2)
                    popup.destroy()
                else:
                    messagebox.showwarning("Missing Info", "Please enter both student names")

            compare_btn = tk.Button(
                popup,
                text="Compare",
                font=('Arial', 12, "bold"),
                fg="white",
                bg="#3498db",
                relief="flat",
                activebackground="#2980b9",
                activeforeground="white",
                command=run_comparison
            )
            compare_btn.pack(pady=15)

        compare_students_btn = tk.Button(
            find_page_fm,
            text="Compare Students",
            font=('Arial', 14, "bold"),
            fg="white",
            bg="#e74c3c",
            relief="flat",
            activebackground="#c0392b",
            activeforeground="white",
            command=compare_students
        )
        compare_students_btn.place(relx=0.5, rely=0.7, anchor=tk.CENTER, width=250, height=50)

    def add_user_ui(self):

        def submit():
            username = username_entry.get().strip()
            fullname = fullname_entry.get().strip()
            role = role_combobox.get().strip()
            password = password_entry.get().strip()
            eca= eca_entry.get().strip()

            math_mark = math_entry.get() if role == "student" else "0"
            science_mark = science_entry.get() if role == "student" else "0"
            english_mark = english_entry.get() if role == "student" else "0"

            if not username or not fullname or not role or not password:
                messagebox.showerror("Error", "All fields are required!")
                return

            if role == "student":
                try:
                    math_mark = int(math_mark) if math_mark else 0
                    science_mark = int(science_mark) if science_mark else 0
                    english_mark = int(english_mark) if english_mark else 0
                    if not all(0 <= mark <= 100 for mark in [math_mark, science_mark, english_mark]):
                        messagebox.showerror("Error", "Marks must be between 0 and 100!")
                        return
                except ValueError:
                    messagebox.showerror("Error", "Marks must be numbers!")
                    return

            if add_user(username, fullname, role, password, math_mark, science_mark, english_mark):
                messagebox.showinfo("Success", "User added successfully!")
                add_window.destroy()
            else:
                messagebox.showerror("Error", "Username already exists!")

        add_window = tk.Toplevel()
        add_window.title("Add User")
        add_window.geometry("550x550")
        add_window.configure(bg="#1e1e2f")

        tk.Label(add_window, text="Username:", font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack(pady=5)
        username_entry = tk.Entry(add_window, font=('Arial', 12))
        username_entry.pack(pady=5)

        tk.Label(add_window, text="Full Name:", font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack(pady=5)
        fullname_entry = tk.Entry(add_window, font=('Arial', 12))
        fullname_entry.pack(pady=5)

        tk.Label(add_window, text="Password:", font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack(pady=5)
        password_entry = tk.Entry(add_window, show="*", font=('Arial', 12))
        password_entry.pack(pady=5)



        tk.Label(add_window, text="Role:", font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack(pady=5)
        role_combobox = ttk.Combobox(add_window, values=["admin", "student"], state="readonly", font=('Arial', 12))
        role_combobox.pack(pady=5)

        marks_frame = tk.Frame(add_window, bg="#1e1e2f")
        tk.Label(marks_frame, text="Subject Marks:", font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack()

        tk.Label(marks_frame, text="Math:", font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack(pady=2)
        math_entry = tk.Entry(marks_frame, font=('Arial', 12))
        math_entry.pack(pady=2)

        tk.Label(marks_frame, text="ECA:", font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack(pady=5)
        eca_entry = tk.Entry(marks_frame, font=('Arial', 12))
        eca_entry.pack(pady=5)

        tk.Label(marks_frame, text="Science:", font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack(pady=2)
        science_entry = tk.Entry(marks_frame, font=('Arial', 12))
        science_entry.pack(pady=2)

        tk.Label(marks_frame, text="English:", font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack(pady=2)
        english_entry = tk.Entry(marks_frame, font=('Arial', 12))
        english_entry.pack(pady=2)

        def toggle_marks(event):
            if role_combobox.get() == "student":
                marks_frame.pack()
            else:
                marks_frame.pack_forget()

        role_combobox.bind("<<ComboboxSelected>>", toggle_marks)
        marks_frame.pack_forget()

        tk.Button(add_window, text="Submit", font=('Arial', 12, "bold"), fg="#ffffff", bg="#f39c12",
                  command=submit).pack(pady=10)

    def delete_user_ui(self):
        def submit():
            username = username_entry.get().strip()
            if not username:
                messagebox.showerror("Error", "Username is required!")
                return
            if delete_user(username):
                messagebox.showinfo("Success", "User deleted successfully!")
                delete_window.destroy()
            else:
                messagebox.showerror("Error", "User not found!")

        delete_window = tk.Toplevel()
        delete_window.title("Delete User")
        delete_window.geometry("300x150")
        delete_window.configure(bg="#1e1e2f")

        tk.Label(delete_window, text="Username:", font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack(pady=5)
        username_entry = tk.Entry(delete_window, font=('Arial', 12))
        username_entry.pack(pady=5)

        tk.Button(delete_window, text="Delete", font=('Arial', 12, "bold"), fg="#ffffff", bg="#f44336",
                  command=submit).pack(pady=10)

    def student_dashboard(self, user):
        # Create a new Toplevel window for the student dashboard
        student_win = tk.Toplevel(self.root)
        student_win.title(f"Student Dashboard - {user.full_name}")
        student_win.geometry("600x400")  # Increased size for better layout
        student_win.configure(bg="#1e1e2f")

        # Welcome message
        tk.Label(student_win, text=f"Welcome, {user.full_name}", font=('Arial', 18, 'bold'),
                fg="#ffffff", bg="#1e1e2f").pack(pady=20)

        # Function to display ECA information
        def trigger_eca(username):
            eca_win = tk.Toplevel(student_win)
            eca_win.title("ECA Information")
            eca_win.geometry("300x200")
            eca_win.configure(bg="#1e1e2f")

            activities = get_student_eca(username)
            if activities:
                std_eca = "\n".join(activities)
            else:
                std_eca = "No ECA data available for this student."

            tk.Label(eca_win, text=std_eca, font=('Arial', 12), fg="#ffffff", bg="#1e1e2f",
                    wraplength=280).pack(pady=20)

        # Function to display grades
        def trigger_grades(username):
            grades_win = tk.Toplevel(student_win)
            grades_win.title("Grades")
            grades_win.geometry("300x200")
            grades_win.configure(bg="#1e1e2f")

            subjects = ["Math", "Science", "English"]
            grades = get_student_grades(username)

            if grades:
                formatted_grades = [f"{subjects[i]}: {grades[i]}" for i in range(len(grades))]
                std_grades = "\n".join(formatted_grades)
                remarks = "Remarks: Pass"
                for grade in grades:
                    if grade < 30:
                        remarks = "Remarks: Fail"
                        break
                average_percentage = sum(grades) / len(grades)
            else:
                std_grades = "No grades data available for this student."
                remarks = ""
                average_percentage = 0

            tk.Label(grades_win, text=std_grades, font=('Arial', 12), fg="#ffffff", bg="#1e1e2f",
                    wraplength=280).pack(pady=10)
            tk.Label(grades_win, text=f"Average Percentage: {average_percentage:.2f}%",
                    font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack(pady=5)
            tk.Label(grades_win, text=remarks, font=('Arial', 12),
                    fg="#ff4444" if remarks == "Remarks: Fail" else "#44ff44", bg="#1e1e2f").pack(pady=5)

        # Edit Profile Functionality
        def edit_profile(username):
            edit_win = tk.Toplevel(student_win)
            edit_win.title("Edit Profile")
            edit_win.geometry("400x400")
            edit_win.configure(bg="#1e1e2f")

            tk.Label(edit_win, text="Edit Profile", font=('Arial', 16, 'bold'),
                    fg="#ffffff", bg="#1e1e2f").pack(pady=10)

            tk.Label(edit_win, text="New Full Name:", font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack(pady=5)
            new_fullname_entry = tk.Entry(edit_win, font=('Arial', 12))
            new_fullname_entry.pack(pady=5)

            tk.Label(edit_win, text="New Username:", font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack(pady=5)
            new_username_entry = tk.Entry(edit_win, font=('Arial', 12))
            new_username_entry.pack(pady=5)

            tk.Label(edit_win, text="New Password:", font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack(pady=5)
            new_password_entry = tk.Entry(edit_win, font=('Arial', 12), show="*")
            new_password_entry.pack(pady=5)

            tk.Label(edit_win, text="Confirm Password:", font=('Arial', 12), fg="#ffffff", bg="#1e1e2f").pack(pady=5)
            confirm_password_entry = tk.Entry(edit_win, font=('Arial', 12), show="*")
            confirm_password_entry.pack(pady=5)

            def save_changes():
                new_fullname = new_fullname_entry.get().strip()
                new_username = new_username_entry.get().strip()
                new_password = new_password_entry.get().strip()
                confirm_password = confirm_password_entry.get().strip()

                # Validate inputs
                if not all([new_fullname, new_username, new_password, confirm_password]):
                    messagebox.showerror("Error", "All fields are required!")
                    return
                if new_password != confirm_password:
                    messagebox.showerror("Error", "Passwords do not match!")
                    return

                try:
                    # Update users.txt
                    with open("projectoriginal/data/users.txt", "r") as f:
                        users = [line.strip().split(",") for line in f.readlines()]

                    updated = False
                    for user_data in users:
                        if user_data[0] == username:
                            user_data[0] = new_username
                            user_data[1] = new_fullname
                            updated = True
                            break

                    if not updated:
                        messagebox.showerror("Error", "User not found!")
                        return

                    with open("projectoriginal/data/users.txt", "w") as f:
                        for user_data in users:
                            f.write(",".join(user_data) + "\n")

                    # Update passwords.txt
                    with open("projectoriginal/data/passwords.txt", "r") as f:
                        passwords = [line.strip().split(",") for line in f.readlines()]

                    updated = False
                    for pwd_data in passwords:
                        if pwd_data[0] == username:
                            pwd_data[0] = new_username
                            pwd_data[1] = new_password
                            updated = True
                            break

                    if not updated:
                        messagebox.showerror("Error", "Password entry not found!")
                        return

                    with open("projectoriginal/data/passwords.txt", "w") as f:
                        for pwd_data in passwords:
                            f.write(",".join(pwd_data) + "\n")

                    messagebox.showinfo("Success", "Profile updated successfully!")
                    edit_win.destroy()
                    student_win.destroy()  # Close dashboard to force re-login

                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save changes: {str(e)}")

            tk.Button(edit_win, text="Save Changes", font=('Arial', 12, "bold"), fg="#ffffff", bg="#4caf50",
                    command=save_changes).pack(pady=20)

        # New Functionality: View Profile
        def view_profile():
            profile_win = tk.Toplevel(student_win)
            profile_win.title("View Profile")
            profile_win.geometry("300x200")
            profile_win.configure(bg="#1e1e2f")

            profile_info = (
                f"Full Name: {user.full_name}\n"
                f"Username: {user.username}\n"
            )

            tk.Label(profile_win, text=profile_info, font=('Arial', 12), fg="#ffffff", bg="#1e1e2f",
                    wraplength=280).pack(pady=20)

        # Frame for Buttons
        button_frame = tk.Frame(student_win, bg="#1e1e2f")
        button_frame.pack(pady=20)

        # Grid Layout for Buttons
        tk.Button(button_frame, text="View Profile", font=('Arial', 12, "bold"), fg="#ffffff", bg="#673ab7",
                command=view_profile).grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=10)

        tk.Button(button_frame, text="Edit Profile", font=('Arial', 12, "bold"), fg="#ffffff", bg="#ff9800",
                command=lambda: edit_profile(user.username)).grid(row=0, column=1, padx=10, pady=10, ipadx=20, ipady=10)

        tk.Button(button_frame, text="View ECA", font=('Arial', 12, "bold"), fg="#ffffff", bg="#4caf50",
                command=lambda: trigger_eca(user.username)).grid(row=1, column=0, padx=10, pady=10, ipadx=20, ipady=10)

        tk.Button(button_frame, text="View Grades", font=('Arial', 12, "bold"), fg="#ffffff", bg="#2196f3",
                command=lambda: trigger_grades(user.username)).grid(row=1, column=1, padx=10, pady=10, ipadx=20, ipady=10)

        tk.Button(button_frame, text="Logout", font=('Arial', 12, "bold"), fg="#ffffff", bg="#f44336",
                command=lambda: self.logout(student_win)).grid(row=2, column=0, columnspan=2, pady=20, ipadx=20, ipady=10)
    def logout(self, student_win=None):
        """
        Logs out the user and closes the dashboard window.
        """
        # Destroy the admin dashboard frame if it exists
        if hasattr(self, 'dashboard_fm') and self.dashboard_fm:
            self.dashboard_fm.destroy()

        # Destroy the student dashboard window if it exists
        if student_win:
            student_win.destroy()

        # Clear the login fields
        self.txt_username.delete(0, tk.END)
        self.txt_pass.delete(0, tk.END)

        # Show a success message
        messagebox.showinfo("Logged Out", "You have been successfully logged out.")

# Run Application
root = tk.Tk()
obj = Login_System(root)
root.mainloop()