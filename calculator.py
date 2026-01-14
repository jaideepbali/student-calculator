import datetime
import os

def calculate_grade(average):
    if average >= 90: return "A+"
    elif average >= 80: return "A"
    elif average >= 70: return "B"
    elif average >= 60: return "C"
    elif average >= 50: return "D"
    else: return "F"

def save_to_file(name, total, average, grade):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("student_results.txt", "a") as file:
        file.write(f"{timestamp} | Name: {name} | Avg: {average:.1f}% | Grade: {grade}\n")
    print("\n✅ Record saved successfully!")

def view_results():
    print("\n--- 📝 Saved Student Records ---")
    if not os.path.exists("student_results.txt"):
        print("No records found yet.")
        return
    
    with open("student_results.txt", "r") as file:
        records = file.readlines()
        if not records:
            print("The file is empty.")
        for line in records:
            print(line.strip())

def add_student():
    name = input("\nEnter student name: ")
    subjects = ["Math", "Science", "English", "History", "CS"]
    marks = []

    for sub in subjects:
        while True:
            try:
                score = float(input(f"   Enter {sub} score (0-100): "))
                if 0 <= score <= 100:
                    marks.append(score)
                    break
                print("   Error: Score must be 0-100.")
            except ValueError:
                print("   Error: Please enter a valid number.")

    total = sum(marks)
    avg = total / len(subjects)
    grade = calculate_grade(avg)
    
    print(f"\nResult: {grade} ({avg:.1f}%)")
    save_to_file(name, total, avg, grade)

def main():
    while True:
        print("\n=== 🎓 STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add New Student Record")
        print("2. View All Saved Results")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_results()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()