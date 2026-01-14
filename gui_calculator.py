import tkinter as tk
from tkinter import messagebox, ttk
import datetime
import os

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Marks Management System")
        self.root.geometry("500x600")

        # --- Input Section ---
        tk.Label(root, text="Student Name:", font=('Arial', 10, 'bold')).pack(pady=5)
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.pack()

        self.subjects = ["Math", "Science", "English", "History", "CS"]
        self.entries = {}

        for sub in self.subjects:
            tk.Label(root, text=f"{sub} Marks:").pack(pady=2)
            ent = tk.Entry(root, width=10)
            ent.pack()
            self.entries[sub] = ent

        # --- Buttons ---
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Calculate & Save", command=self.process_data, bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="View Records", command=self.show_records, bg="#2196F3", fg="white").pack(side=tk.LEFT, padx=10)

        # --- Output Display ---
        self.display_area = tk.Text(root, height=10, width=55)
        self.display_area.pack(pady=10)

    def calculate_grade(self, avg):
        if avg >= 90: return "A+"
        elif avg >= 80: return "A"
        elif avg >= 70: return "B"
        elif avg >= 60: return "C"
        elif avg >= 50: return "D"
        else: return "F"

    def process_data(self):
        try:
            name = self.name_entry.get()
            if not name:
                messagebox.showerror("Error", "Please enter a name")
                return

            marks = []
            for sub in self.subjects:
                val = float(self.entries[sub].get())
                if 0 <= val <= 100:
                    marks.append(val)
                else:
                    raise ValueError
            
            avg = sum(marks) / len(marks)
            grade = self.calculate_grade(avg)
            
            result_str = f"Name: {name} | Avg: {avg:.1f}% | Grade: {grade}"
            
            # Save to file
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            with open("student_results.txt", "a") as file:
                file.write(f"{timestamp} | {result_str}\n")
            
            messagebox.showinfo("Success", f"Saved!\nGrade: {grade}")
            self.clear_inputs()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers (0-100) for all subjects.")

    def show_records(self):
        self.display_area.delete('1.0', tk.END)
        if not os.path.exists("student_results.txt"):
            self.display_area.insert(tk.END, "No records found.")
            return
            
        with open("student_results.txt", "r") as file:
            data = file.read()
            self.display_area.insert(tk.END, data)

    def clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        for ent in self.entries.values():
            ent.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()