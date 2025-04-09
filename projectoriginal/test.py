from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import messagebox, ttk
from tkinter import simpledialog, messagebox
import graph
from PIL import ImageTk
from authy import authenticate, get_user_details, get_student_count, get_eca_count, get_admin_count
from CRUD import add_user, delete_user
class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")  
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='#fafafa')

        # Load Images
        self.phone_image = ImageTk.PhotoImage(file="projectoriginal/images/image.png")
        self.lbl_Phone_image = Label(self.root, image=self.phone_image)
        self.lbl_Phone_image.place(x=100, y=50)

        # Login Frame
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=650, y=90, width=350, height=460)

        title = Label(login_frame, text="Login system", font=("Elephant", 20, "bold"), bg='white')
        title.place(x=0, y=30, relwidth=1)

        # Username
        lbl_user = Label(login_frame, text="Username", font=("Andalus", 15), bg="white", fg="#767171")
        lbl_user.place(x=50, y=100)
        
        self.txt_username = Entry(login_frame, font=("times new roman", 15), bg="#ECECEC")
        self.txt_username.place(x=50, y=140, width=250)

        # Password
        lbl_pass = Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171")
        lbl_pass.place(x=50, y=200)
        
        self.txt_pass = Entry(login_frame, font=("times new roman", 15), bg="#ECECEC", show="*")
        self.txt_pass.place(x=50, y=240, width=250)

        # Login Button
        btn_login = Button(
            login_frame, text="Login", font=("Arial", 15),
            bg="#00b0f0", activebackground="#00b0f0",
            fg='white', activeforeground='white', cursor='hand2',
            command=self.login
        )
        btn_login.place(x=50, y=300, width=250, height=35)

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
        self.dashboard_fm = tk.Frame(self.root, highlightbackground="#00b0f0", highlightthickness=3, bg="white")
        self.dashboard_fm.pack(pady=5)
        self.dashboard_fm.pack_propagate(False)
        self.dashboard_fm.configure(width=880, height=580)

        options_fm = tk.Frame(self.dashboard_fm, highlightbackground="#00b0f0", highlightthickness=3, bg="#c3c3c3")
        options_fm.place(x=0, y=0, width=120, height=575)

        home_btn = tk.Button(options_fm, text='Home', font=('Bold', 15), fg='blue', bg='#c3c3c3', bd=0, 
                             command=lambda: self.switch(self.home_btn_indicator, self.home_page))
        home_btn.place(x=10, y=50)
        self.home_btn_indicator = tk.Label(options_fm, text='', bg='#c3c3c3')
        self.home_btn_indicator.place(x=5, y=48, width=3, height=40)

        find_student_btn = tk.Button(options_fm, text='Find\nStudent', font=('Bold', 15), fg='blue', 
                                     bg='#c3c3c3', bd=0, justify=tk.LEFT, 
                                     command=lambda: self.switch(self.find_student_btn_indicator, self.find_page))
        find_student_btn.place(x=10, y=100)
        self.find_student_btn_indicator = tk.Label(options_fm, text='', bg='#c3c3c3')
        self.find_student_btn_indicator.place(x=5, y=108, width=3, height=40)

        logout_btn = tk.Button(options_fm, text='Logout', font=('Bold', 15), fg='green', bg='#c3c3c3', bd=0)
        logout_btn.place(x=10, y=240)

        self.pages_fm = tk.Frame(self.dashboard_fm, bg='gray')
        self.pages_fm.place(x=122, y=5, width=550, height=550)

        # Initial page load
        self.switch(self.home_btn_indicator, self.home_page)

    def switch(self, indicator, page):
        self.home_btn_indicator.config(bg="#c3c3c3")
        self.find_student_btn_indicator.config(bg='#c3c3c3')
        indicator.config(bg='red')
        # Clear previous content in pages_fm
        for widget in self.pages_fm.winfo_children():
            widget.destroy()
            self.root.update()
        page()  # Call the page function to load the new page

    def home_page(self):
        home_page_fm = tk.Frame(self.pages_fm)
        home_page_fm.pack(fill=tk.BOTH, expand=True)
        
        admin_image = ImageTk.PhotoImage(file="projectoriginal/images/admin_img.png")
        lbl_admin_image = tk.Label(home_page_fm, image=admin_image)
        lbl_admin_image.place(x=10, y=10)
        
        hi_lb = tk.Label(home_page_fm, text='!Hi Admin', font=('Bold', 15))
        hi_lb.place(x=128, y=40)

        def studentcount():
            student_count = get_student_count()
            class_list_lb = tk.Label(home_page_fm, text=f"Number of Students : {student_count}", 
                                    font=('Bold', 13), bg='blue', fg='white')
            class_list_lb.place(x=20, y=130)
        studentcount()

        def admincount():
            admin_count = get_admin_count()
            class_list_lb = tk.Label(home_page_fm, text=f"Number of Admin : {admin_count}", 
                                    font=('Bold', 13), bg='blue', fg='white')
            class_list_lb.place(x=20, y=150)
        admincount()
    
        def totalECA():
            eca_count = get_eca_count()
            class_list_lb = tk.Label(home_page_fm, text=f"Number of ECA : {eca_count}", 
                                    font=('Bold', 13), bg='blue', fg='white')
            class_list_lb.place(x=20, y=170)
        totalECA()

        def quicklink():
            link_lb = tk.Label(home_page_fm, text='--- Quick Actions ---', font=('Bold', 15))
            link_lb.place(x=50, y=50)

        quicklink()
        
        # Add buttons to home_page_fm
        add_btn = tk.Button(home_page_fm, text="Add User", command=self.add_user_ui)
        add_btn.place(x=50, y=200)

        delete_btn = tk.Button(home_page_fm, text="Delete User", command=self.delete_user_ui)
        delete_btn.place(x=150, y=200)

        lbl_admin_image.image = admin_image

    def find_page(self):
        find_page_fm = tk.Frame(self.pages_fm)
        find_label = tk.Label(find_page_fm, text="Find", font=('Bold', 15))
        find_label.pack(fill=tk.BOTH, expand=True)

        def show_graph():
            student_name = simpledialog.askstring("Student Name", "Enter Student Name:")
            if student_name:
                graph.plot_student_trend(student_name)

        button = tk.Button(find_page_fm, text="Show Grade Trend", command=show_graph, height=2, width=30)
        button.pack(pady=20)

        # def graph_sem():
        #     student_name = simpledialog.askstring("Student Name", "Enter Student Name:")
        #     if student_name:
        #         graph.plot_student_sem(student_name)

        # button = tk.Button(find_page_fm, text="Show Grade Trend", command=graph_sem, height=2, width=30)
        # button.pack(pady=10)

        find_page_fm.pack(fill=tk.BOTH, expand=True)

    def add_user_ui(self):
        def submit():
            username = username_entry.get()
            fullname = fullname_entry.get()
            role = role_combobox.get()
            password = password_entry.get()

            # Initialize marks as empty strings
            math_mark = math_entry.get()
            science_mark = science_entry.get()
            english_mark = english_entry.get()

            if not username or not fullname or not role or not password:
                messagebox.showerror("Error", "All fields are required!")
                return

            # Validate marks if student
            if role == "student":
                try:
                    math_mark = int(math_mark) if math_mark else 0
                    science_mark = int(science_mark) if science_mark else 0
                    english_mark = int(english_mark) if english_mark else 0
                    
                    # Validate mark range (0-100)
                    if not all(0 <= mark <= 100 for mark in [math_mark, science_mark, english_mark]):
                        messagebox.showerror("Error", "Marks must be between 0 and 100!")
                        return
                except ValueError:
                    messagebox.showerror("Error", "Marks must be numbers!")
                    return
            else:  # For admin, set marks to 0 or None
                math_mark = science_mark = english_mark = 0

            if add_user(username, fullname, role, password, math_mark, science_mark, english_mark):
                messagebox.showinfo("Success", "User added successfully!")
                add_window.destroy()
            else:
                messagebox.showerror("Error", "Username already exists!")

        add_window = tk.Toplevel()
        add_window.title("Add User")
        add_window.geometry("350x450")  # Increased size for marks

        # User info fields
        tk.Label(add_window, text="Username:").pack(pady=5)
        username_entry = tk.Entry(add_window)
        username_entry.pack(pady=5)

        tk.Label(add_window, text="Full Name:").pack(pady=5)
        fullname_entry = tk.Entry(add_window)
        fullname_entry.pack(pady=5)

        tk.Label(add_window, text="Password:").pack(pady=5)
        password_entry = tk.Entry(add_window, show="*")
        password_entry.pack(pady=5)

        tk.Label(add_window, text="Role:").pack(pady=5)
        role_combobox = ttk.Combobox(add_window, values=["admin", "student"], state="readonly")
        role_combobox.pack(pady=5)

        # Marks section (initially hidden)
        marks_frame = tk.Frame(add_window)
        
        tk.Label(marks_frame, text="\nSubject Marks:").pack()
        
        tk.Label(marks_frame, text="Math:").pack(pady=2)
        math_entry = tk.Entry(marks_frame)
        math_entry.pack(pady=2)
        
        tk.Label(marks_frame, text="Science:").pack(pady=2)
        science_entry = tk.Entry(marks_frame)
        science_entry.pack(pady=2)
        
        tk.Label(marks_frame, text="English:").pack(pady=2)
        english_entry = tk.Entry(marks_frame)
        english_entry.pack(pady=2)

        # Show/hide marks based on role selection
        def toggle_marks(event):
            if role_combobox.get() == "student":
                marks_frame.pack()
            else:
                marks_frame.pack_forget()
        
        role_combobox.bind("<<ComboboxSelected>>", toggle_marks)
        marks_frame.pack_forget()  # Hide initially

        tk.Button(add_window, text="Submit", command=submit).pack(pady=10)

    def delete_user_ui(self):
        def submit():
            username = username_entry.get()
            
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

        tk.Label(delete_window, text="Username:").pack(pady=5)
        username_entry = tk.Entry(delete_window)
        username_entry.pack(pady=5)

        tk.Button(delete_window, text="Delete", command=submit).pack(pady=10)

    def student_dashboard(self, user):
        messagebox.showinfo("Student", f"Redirecting {user.full_name} to student dashboard.")

# Run Application
root = Tk()
obj = Login_System(root)
root.mainloop()