Student Login System 

This is a simple Python GUI application that simulates a multi-user student login system using Tkinter. 
The application features a single-window interface for user login, viewing ECA (Extra Curricular Activities), checking Grades, and logging out — all within one dynamic window.



Features
🔐 Login Authentication with pre-defined usernames and passwords

📋 Dashboard after login with navigation to:

✅ ECA Activities section

📚 Grades section

🚪 Logout button that returns to the login screen

🎨 Clean and colorful UI using Tkinter Frames and Text widgets

💾 User data (username, password, ECA, grades) stored in JSON format




Technologies Used

1)Python
   
2)Tkinter for GUI

3)JSON for data storage



Getting Started

Make sure you have Python installed:



How to Run

Clone or download this repository.


Run the Python script:

python student_login.py


![image](https://github.com/user-attachments/assets/f4a27f7b-9819-483b-8ed2-80e1133c70e0)

🔐 Login Screen
This is the main entry point of the application where users input their username and password to log in.
A successful login leads to the dashboard; errors show a message if credentials are invalid.


![image](https://github.com/user-attachments/assets/33e4f69b-c8dc-4f0d-8f77-09a2a0eb2e87)

🏠 Dashboard
After logging in, users are presented with two main options:

ECA Activities to view their extracurricular involvement

Grades to view academic performance
Also includes a Logout button to return to the login screen.

🚪 Logout Action
When the Logout button is clicked, the dashboard and any open windows are closed and the main login screen is restored — creating a seamless single-window experience.


![image](https://github.com/user-attachments/assets/82234ba0-84a7-402c-b810-30560d06b32a)

✅ ECA Activities Page
Displays the list of extracurricular activities assigned to the logged-in user.
Styled with a dark background and centered layout for clarity.


![image](https://github.com/user-attachments/assets/c6013ab4-140b-4ea0-9281-0d2c455d9cd8)


📚 Grades Page
Displays the student's grades across multiple subjects in a clean and readable format.
Each user's data is personalized and loaded dynamically.






