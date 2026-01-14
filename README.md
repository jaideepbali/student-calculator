🎓 Student Management & Grade System 
A robust Python-based CLI (Command Line Interface) application designed to automate student performance tracking. This tool allows users to input grades, calculate academic standing, and maintain a persistent history of results using file handling.

## 🖥️ Graphical User Interface (GUI)
This project now includes a desktop application version built with **Tkinter**.
* **Visual Inputs:** No more typing in a black terminal.
* **Instant Pop-ups:** Get immediate feedback via dialog boxes.
* **Scrollable History:** View all saved records directly within the app window.


## 🚀 Key Features

**Interactive Menu System:** A user-friendly console menu for seamless navigation.Data Persistence: Automatically creates and updates a student_results.txt file to store records.Input Sanitization: Robust error handling for non-numeric inputs and out-of-range scores.Historical View: A built-in viewer to read and display all past student records from the database file.Automated Grading: Instant calculation of Total, Average, and Letter Grade (A+ through F).

🛠️ 
**Technical Workflow**
The application follows a structured data flow to ensure accuracy and reliability:Input: User enters student name and marks for 5 core subjects.Validation: The system checks if scores are between 0 and 100.
Processing: Python logic calculates the sum and mean of the scores.Storage: Results are appended to a local text file with a unique timestamp.
Retrieval: The program reads the .txt file to display historical data to the user.

📂 
**Installation & Usage.**
Prerequisites
1. Python 3.x installed on your machine.
2. SetupClone the repository to your local machine:

git clone https://github.com/jaideepbali/student-calculator.git cd student-calculator

3. Run the App
Execute the script using the terminal:

python calculator.py


🛡️ 
## LicenseDistributed under the MIT License. See LICENSE for more information.

🤝 
## Contact- Jaideep Singh Bali


## Project Link: https://github.com/jaideepbali/student-calculator
