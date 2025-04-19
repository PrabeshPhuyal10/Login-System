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
        self.current_user = None
        
        # This will track if we're showing login or dashboard
        self.show_login_screen()

    def show_login_screen(self):
        """Display the login screen"""
        # Clear any existing frames
        for widget in self.root.winfo_children():
            widget.destroy()
            
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
                self.current_user = user
                messagebox.showinfo("Login Successful", f"Welcome, {user.full_name} ({user.role})!")
                self.root.title(f"{user.role.capitalize()} Dashboard - {user.full_name}")
                if role == "admin":
                    self.show_admin_dashboard(user)
                elif role == "student":
                    self.show_student_dashboard(user)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show_admin_dashboard(self, user):
        """Display the admin dashboard"""
        # Clear login screen
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Main container
        main_container = tk.Frame(self.root, bg="#1e1e2f")
        main_container.pack(fill=tk.BOTH, expand=True)

        # Sidebar
        sidebar = tk.Frame(main_container, bg="#1e1e2f", width=150)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        # Main content area
        content = tk.Frame(main_container, bg="#2c2c3a")
        content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Sidebar buttons
        btn_home = tk.Button(sidebar, text="Home", font=('Arial', 12), bg="#4caf50", fg="white",
                            command=lambda: self.show_admin_home(content))
        btn_home.pack(fill=tk.X, pady=5)

        btn_find = tk.Button(sidebar, text="Find Student", font=('Arial', 12), bg="#2196f3", fg="white",
                            command=lambda: self.show_admin_find(content))
        btn_find.pack(fill=tk.X, pady=5)

        btn_add = tk.Button(sidebar, text="Add User", font=('Arial', 12), bg="#673ab7", fg="white",
                           command=self.add_user_ui)
        btn_add.pack(fill=tk.X, pady=5)

        btn_delete = tk.Button(sidebar, text="Delete User", font=('Arial', 12), bg="#f44336", fg="white",
                              command=self.delete_user_ui)
        btn_delete.pack(fill=tk.X, pady=5)

        btn_logout = tk.Button(sidebar, text="Logout", font=('Arial', 12), bg="#ff9800", fg="white",
                              command=self.logout)
        btn_logout.pack(fill=tk.X, pady=5, side=tk.BOTTOM)

        # Show home content by default
        self.show_admin_home(content)

    def show_admin_home(self, content_frame):
        """Show admin home content"""
        # Clear existing content
        for widget in content_frame.winfo_children():
            widget.destroy()

        # Welcome message
        welcome_label = tk.Label(content_frame, text="Admin Dashboard", font=('Arial', 20, 'bold'),
                               bg="#2c2c3a", fg="white")
        welcome_label.pack(pady=20)

        # Stats frame
        stats_frame = tk.Frame(content_frame, bg="#2c2c3a")
        stats_frame.pack(pady=20)

        # Student count
        student_count = get_student_count()
        tk.Label(stats_frame, text=f"Students: {student_count}", font=('Arial', 14),
                bg="#2196f3", fg="white", padx=20, pady=10).grid(row=0, column=0, padx=10, pady=10)

        # Admin count
        admin_count = get_admin_count()
        tk.Label(stats_frame, text=f"Admins: {admin_count}", font=('Arial', 14),
                bg="#ff9800", fg="white", padx=20, pady=10).grid(row=0, column=1, padx=10, pady=10)

        # ECA count
        eca_count = get_eca_count()
        tk.Label(stats_frame, text=f"ECAs: {eca_count}", font=('Arial', 14),
                bg="#4caf50", fg="white", padx=20, pady=10).grid(row=0, column=2, padx=10, pady=10)

        # Average percentage
        avg_per = get_average_percentage_all_students()
        tk.Label(stats_frame, text=f"Avg Percentage: {avg_per:.2f}%", font=('Arial', 14),
                bg="#673ab7", fg="white", padx=20, pady=10).grid(row=1, column=0, columnspan=3, pady=10)

        # Quick actions frame
        actions_frame = tk.Frame(content_frame, bg="#2c2c3a")
        actions_frame.pack(pady=20)

        # View lists buttons
        tk.Button(actions_frame, text="View Students", font=('Arial', 12),
                 command=self.show_student_list).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(actions_frame, text="View Admins", font=('Arial', 12),
                 command=self.show_admin_list).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(actions_frame, text="View ECAs", font=('Arial', 12),
                 command=self.show_eca_list).grid(row=0, column=2, padx=10, pady=10)

    def show_admin_find(self, content_frame):
        """Show find student content"""
        # Clear existing content
        for widget in content_frame.winfo_children():
            widget.destroy()

        # Title
        tk.Label(content_frame, text="Student Analytics", font=('Arial', 20, 'bold'),
                bg="#2c2c3a", fg="white").pack(pady=20)

        # Graph options frame
        graph_frame = tk.Frame(content_frame, bg="#2c2c3a")
        graph_frame.pack(pady=20)

        # Buttons for different graph options
        tk.Button(graph_frame, text="Grade Trend", font=('Arial', 12),
                 command=self.show_grade_trend).pack(pady=10, fill=tk.X)
        tk.Button(graph_frame, text="Grade Distribution", font=('Arial', 12),
                 command=self.show_grade_distribution).pack(pady=10, fill=tk.X)
        tk.Button(graph_frame, text="Compare Students", font=('Arial', 12),
                 command=self.show_compare_students).pack(pady=10, fill=tk.X)

    def show_student_list(self):
        """Show student names in a new window"""
        student_names = get_student_names()
        self.show_list_window("Student List", student_names)

    def show_admin_list(self):
        """Show admin names in a new window"""
        admin_names = get_admin_names()
        self.show_list_window("Admin List", admin_names)

    def show_eca_list(self):
        """Show ECA names in a new window"""
        try:
            from CRUD import get_eca_names
            eca_names = get_eca_names()
            self.show_list_window("ECA List", eca_names)
        except ImportError:
            messagebox.showerror("Error", "Could not import get_eca_names. Check your CRUD module.")

    def show_list_window(self, title, items):
        """Generic function to show a list in a new window"""
        list_window = tk.Toplevel(self.root)
        list_window.title(title)
        list_window.geometry("300x400")
        list_window.config(bg="#2c2c3a")

        tk.Label(list_window, text=title, font=('Arial', 14, 'bold'),
                bg="#2c2c3a", fg="white").pack(pady=10)

        frame = tk.Frame(list_window, bg="#2c2c3a")
        frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, bg="#2c2c3a")
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, font=('Arial', 12),
                           bg="#2c2c3a", fg="white", selectbackground="#4caf50")
        listbox.pack(fill=tk.BOTH, expand=True)

        scrollbar.config(command=listbox.yview)

        if items:
            for item in items:
                listbox.insert(tk.END, item)
        else:
            listbox.insert(tk.END, f"No {title.lower()} found")

    def show_grade_trend(self):
        """Show grade trend input dialog"""
        popup = tk.Toplevel(self.root)
        popup.title("Student Grade Trend")
        popup.geometry("350x150")
        popup.config(bg="#2c2c3a")
        popup.resizable(False, False)

        # Label
        label = tk.Label(popup, text="Enter Student Name:", bg="#2c2c3a", fg="white", font=("Arial", 12))
        label.pack(pady=(20, 5))

        # Entry field
        name_entry = tk.Entry(popup, font=("Arial", 12))
        name_entry.pack(pady=5)

        # Submit button
        def submit():
            student_name = name_entry.get().strip()
            if student_name:
                popup.destroy()
                graph.plot_student_trend(student_name)

        submit_btn = tk.Button(popup, text="Show Trend", command=submit, bg="#4CAF50", fg="white", font=("Arial", 11), width=15)
        submit_btn.pack(pady=15)


    def show_grade_distribution(self):
        """Show grade distribution pie chart"""
        graph.plot_grade_distribution_pie()

    def show_compare_students(self):
        """Show student comparison dialog"""
        popup = tk.Toplevel(self.root)
        popup.title("Compare Students")
        popup.geometry("350x200")
        popup.config(bg="#2c2c3a")
        popup.resizable(False, False)

        tk.Label(popup, text="First Student Name:", font=('Arial', 12),
                fg="white", bg="#2c2c3a").pack(pady=(10, 0))
        entry1 = tk.Entry(popup, width=25, font=('Arial', 12))
        entry1.pack()
        entry1.focus_set()

        tk.Label(popup, text="Second Student Name:", font=('Arial', 12),
                fg="white", bg="#2c2c3a").pack(pady=(10, 0))
        entry2 = tk.Entry(popup, width=25, font=('Arial', 12))
        entry2.pack()

        def run_comparison():
            student1 = entry1.get().strip()
            student2 = entry2.get().strip()

            if student1 and student2:
                graph.compare_two_students(student1, student2)
                popup.destroy()
            else:
                messagebox.showwarning("Missing Info", "Please enter both student names", parent=popup)

        tk.Button(popup, text="Compare", font=('Arial', 12),
                 command=run_comparison).pack(pady=15)

    def add_user_ui(self):
        """Show add user dialog"""
        def submit():
            username = username_entry.get().strip()
            fullname = fullname_entry.get().strip()
            role = role_combobox.get().strip()
            password = password_entry.get().strip()
            eca = eca_entry.get().strip()

            math_mark = 0
            science_mark = 0
            english_mark = 0

            if not (username and fullname and role and password):
                messagebox.showerror("Error", "Username, Full Name, Role, and Password are required!")
                return

            if role == "student":
                try:
                    math_mark = int(math_entry.get().strip()) if math_entry.get().strip() else 0
                    science_mark = int(science_entry.get().strip()) if science_entry.get().strip() else 0
                    english_mark = int(english_entry.get().strip()) if english_entry.get().strip() else 0

                    if not all(0 <= mark <= 100 for mark in [math_mark, science_mark, english_mark]):
                        messagebox.showerror("Error", "Marks must be between 0 and 100!")
                        return
                except ValueError:
                    messagebox.showerror("Error", "Marks must be valid numbers!")
                    return

            if add_user(username, fullname, role, password, eca, math_mark, science_mark, english_mark):
                messagebox.showinfo("Success", "User added successfully!")
                add_window.destroy()
            else:
                messagebox.showerror("Error", "Username already exists!")

        add_window = tk.Toplevel(self.root)
        add_window.title("Add User")
        add_window.geometry("400x500")
        add_window.configure(bg="#2c2c3a")

        tk.Label(add_window, text="Add New User", font=('Arial', 16, 'bold'),
                fg="white", bg="#2c2c3a").pack(pady=10)

        form_frame = tk.Frame(add_window, bg="#2c2c3a")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Username:", font=('Arial', 12), fg="white", bg="#2c2c3a").grid(row=0, column=0, pady=5, sticky="e")
        username_entry = tk.Entry(form_frame, font=('Arial', 12))
        username_entry.grid(row=0, column=1, pady=5)

        tk.Label(form_frame, text="Full Name:", font=('Arial', 12), fg="white", bg="#2c2c3a").grid(row=1, column=0, pady=5, sticky="e")
        fullname_entry = tk.Entry(form_frame, font=('Arial', 12))
        fullname_entry.grid(row=1, column=1, pady=5)

        tk.Label(form_frame, text="Password:", font=('Arial', 12), fg="white", bg="#2c2c3a").grid(row=2, column=0, pady=5, sticky="e")
        password_entry = tk.Entry(form_frame, show="*", font=('Arial', 12))
        password_entry.grid(row=2, column=1, pady=5)

        tk.Label(form_frame, text="Role:", font=('Arial', 12), fg="white", bg="#2c2c3a").grid(row=3, column=0, pady=5, sticky="e")
        role_combobox = ttk.Combobox(form_frame, values=["admin", "student"], state="readonly", font=('Arial', 12))
        role_combobox.grid(row=3, column=1, pady=5)

        # Marks frame (initially hidden)
        marks_frame = tk.Frame(form_frame, bg="#2c2c3a")
        
        tk.Label(marks_frame, text="ECA:", font=('Arial', 12), fg="white", bg="#2c2c3a").grid(row=0, column=0, pady=5, sticky="e")
        eca_entry = tk.Entry(marks_frame, font=('Arial', 12))
        eca_entry.grid(row=0, column=1, pady=5)

        tk.Label(marks_frame, text="Math:", font=('Arial', 12), fg="white", bg="#2c2c3a").grid(row=1, column=0, pady=5, sticky="e")
        math_entry = tk.Entry(marks_frame, font=('Arial', 12))
        math_entry.grid(row=1, column=1, pady=5)

        tk.Label(marks_frame, text="Science:", font=('Arial', 12), fg="white", bg="#2c2c3a").grid(row=2, column=0, pady=5, sticky="e")
        science_entry = tk.Entry(marks_frame, font=('Arial', 12))
        science_entry.grid(row=2, column=1, pady=5)

        tk.Label(marks_frame, text="English:", font=('Arial', 12), fg="white", bg="#2c2c3a").grid(row=3, column=0, pady=5, sticky="e")
        english_entry = tk.Entry(marks_frame, font=('Arial', 12))
        english_entry.grid(row=3, column=1, pady=5)

        def toggle_marks(event):
            if role_combobox.get() == "student":
                marks_frame.grid(row=4, column=0, columnspan=2)
            else:
                marks_frame.grid_forget()

        role_combobox.bind("<<ComboboxSelected>>", toggle_marks)
        marks_frame.grid_forget()

        # Submit button
        tk.Button(add_window, text="Submit", font=('Arial', 12), command=submit).pack(pady=20)

    def delete_user_ui(self):
        """Show delete user dialog"""
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

        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete User")
        delete_window.geometry("300x150")
        delete_window.configure(bg="#2c2c3a")

        tk.Label(delete_window, text="Username:", font=('Arial', 12),
                fg="white", bg="#2c2c3a").pack(pady=5)
        username_entry = tk.Entry(delete_window, font=('Arial', 12))
        username_entry.pack(pady=5)

        tk.Button(delete_window, text="Delete", font=('Arial', 12),
                 command=submit).pack(pady=10)

    def show_student_dashboard(self, user):
        """Display the student dashboard"""
        # Clear login screen
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Main container
        main_frame = tk.Frame(self.root, bg="#1e1e2f")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Welcome message
        tk.Label(main_frame, text=f"Welcome, {user.full_name}", font=('Arial', 20, 'bold'),
                fg="white", bg="#1e1e2f").pack(pady=30)

        # Button frame
        button_frame = tk.Frame(main_frame, bg="#1e1e2f")
        button_frame.pack(pady=20)

        # View Profile button
        tk.Button(button_frame, text="View Profile", font=('Arial', 12),
                 command=lambda: self.show_student_profile(user)).grid(row=0, column=0, padx=10, pady=10)

        # View ECA button
        tk.Button(button_frame, text="View ECA", font=('Arial', 12),
                 command=lambda: self.show_student_eca(user)).grid(row=0, column=1, padx=10, pady=10)

        # View Grades button
        tk.Button(button_frame, text="View Grades", font=('Arial', 12),
                 command=lambda: self.show_student_grades(user)).grid(row=1, column=0, padx=10, pady=10)

        # Edit Profile button
        tk.Button(button_frame, text="Edit Profile", font=('Arial', 12),
                 command=lambda: self.edit_student_profile(user)).grid(row=1, column=1, padx=10, pady=10)

        # Logout button
        tk.Button(main_frame, text="Logout", font=('Arial', 12),
                 command=self.logout).pack(pady=20)

    def show_student_profile(self, user):
        """Show student profile"""
        profile_window = tk.Toplevel(self.root)
        profile_window.title("Profile")
        profile_window.geometry("300x150")
        profile_window.configure(bg="#2c2c3a")

        profile_info = f"Name: {user.full_name}\nUsername: {user.username}\nRole: {user.role}"
        tk.Label(profile_window, text=profile_info, font=('Arial', 12),
                fg="white", bg="#2c2c3a").pack(pady=20)

    def show_student_eca(self, user):
        """Show student ECA"""
        eca_window = tk.Toplevel(self.root)
        eca_window.title("ECA Activities")
        eca_window.geometry("300x200")
        eca_window.configure(bg="#2c2c3a")

        activities = get_student_eca(user.username)
        if activities:
            eca_text = "\n".join(activities)
        else:
            eca_text = "No ECA activities found"

        tk.Label(eca_window, text=eca_text, font=('Arial', 12),
                fg="white", bg="#2c2c3a").pack(pady=20)

    def show_student_grades(self, user):
        """Show student grades"""
        grades_window = tk.Toplevel(self.root)
        grades_window.title("Grades")
        grades_window.geometry("300x250")
        grades_window.configure(bg="#2c2c3a")

        subjects = ["Math", "Science", "English"]
        grades = get_student_grades(user.username)

        if grades:
            formatted_grades = [f"{subjects[i]}: {grades[i]}" for i in range(len(grades))]
            grades_text = "\n".join(formatted_grades)
            remarks = "Remarks: Pass"
            for grade in grades:
                if grade < 30:
                    remarks = "Remarks: Fail"
                    break
            average_percentage = sum(grades) / len(grades)
        else:
            grades_text = "No grades data available"
            remarks = ""
            average_percentage = 0

        tk.Label(grades_window, text=grades_text, font=('Arial', 12),
                fg="white", bg="#2c2c3a").pack(pady=10)
        tk.Label(grades_window, text=f"Average: {average_percentage:.2f}%", 
                font=('Arial', 12), fg="white", bg="#2c2c3a").pack()
        tk.Label(grades_window, text=remarks, font=('Arial', 12),
                fg="#ff4444" if remarks == "Remarks: Fail" else "#44ff44", 
                bg="#2c2c3a").pack(pady=10)

    def edit_student_profile(self, user):
        """Edit student profile"""
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Profile")
        edit_window.geometry("350x300")
        edit_window.configure(bg="#2c2c3a")

        tk.Label(edit_window, text="Edit Profile", font=('Arial', 16, 'bold'),
                fg="white", bg="#2c2c3a").pack(pady=10)

        form_frame = tk.Frame(edit_window, bg="#2c2c3a")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="New Full Name:", font=('Arial', 12),
                fg="white", bg="#2c2c3a").grid(row=0, column=0, pady=5, sticky="e")
        name_entry = tk.Entry(form_frame, font=('Arial', 12))
        name_entry.insert(0, user.full_name)
        name_entry.grid(row=0, column=1, pady=5)

        tk.Label(form_frame, text="New Username:", font=('Arial', 12),
                fg="white", bg="#2c2c3a").grid(row=1, column=0, pady=5, sticky="e")
        user_entry = tk.Entry(form_frame, font=('Arial', 12))
        user_entry.insert(0, user.username)
        user_entry.grid(row=1, column=1, pady=5)

        tk.Label(form_frame, text="New Password:", font=('Arial', 12),
                fg="white", bg="#2c2c3a").grid(row=2, column=0, pady=5, sticky="e")
        pass_entry = tk.Entry(form_frame, show="*", font=('Arial', 12))
        pass_entry.grid(row=2, column=1, pady=5)

        tk.Label(form_frame, text="Confirm Password:", font=('Arial', 12),
                fg="white", bg="#2c2c3a").grid(row=3, column=0, pady=5, sticky="e")
        confirm_entry = tk.Entry(form_frame, show="*", font=('Arial', 12))
        confirm_entry.grid(row=3, column=1, pady=5)

        def save_changes():
            new_name = name_entry.get().strip()
            new_user = user_entry.get().strip()
            new_pass = pass_entry.get().strip()
            confirm_pass = confirm_entry.get().strip()

            if not all([new_name, new_user, new_pass, confirm_pass]):
                messagebox.showerror("Error", "All fields are required!")
                return
            if new_pass != confirm_pass:
                messagebox.showerror("Error", "Passwords do not match!")
                return

            try:
                # Update users.txt
                with open("projectoriginal/data/users.txt", "r") as f:
                    users = [line.strip().split(",") for line in f.readlines()]

                for user_data in users:
                    if user_data[0] == user.username:
                        user_data[0] = new_user
                        user_data[1] = new_name
                        break

                with open("projectoriginal/data/users.txt", "w") as f:
                    for user_data in users:
                        f.write(",".join(user_data) + "\n")

                # Update passwords.txt
                with open("projectoriginal/data/passwords.txt", "r") as f:
                    passwords = [line.strip().split(",") for line in f.readlines()]

                for pwd_data in passwords:
                    if pwd_data[0] == user.username:
                        pwd_data[0] = new_user
                        pwd_data[1] = new_pass
                        break

                with open("projectoriginal/data/passwords.txt", "w") as f:
                    for pwd_data in passwords:
                        f.write(",".join(pwd_data) + "\n")

                messagebox.showinfo("Success", "Profile updated successfully!")
                edit_window.destroy()
                self.logout()  # Force re-login with new credentials
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save changes: {str(e)}")

        tk.Button(edit_window, text="Save Changes", font=('Arial', 12),
                 command=save_changes).pack(pady=20)

    def logout(self):
        """Logout and return to login screen"""
        self.current_user = None
        self.show_login_screen()

# Run Application
root = tk.Tk()
obj = Login_System(root)
root.mainloop()