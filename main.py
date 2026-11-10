import json
import os

DATA_FILE = "students.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading file: {e}")
        return []

def save_data(data):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
        print("Record saved successfully!")
    except IOError as e:
        print(f"Error saving data: {e}")

def add_student():
    students = load_data()
    try:
        roll_no = input("Enter Roll Number: ").strip()
        if any(s['roll_no'] == roll_no for s in students):
            print("Roll number already exists!")
            return
        name = input("Enter Name: ").strip()
        course = input("Enter Course: ").strip()
        marks = float(input("Enter Marks: "))

        student = {
            "roll_no": roll_no,
            "name": name,
            "course": course,
            "marks": marks
        }
        students.append(student)
        save_data(students)
    except ValueError:
        print("Invalid input! Marks should be a numeric value.")

def view_students():
    students = load_data()
    if not students:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for s in students:
        print(f"Roll No: {s['roll_no']} | Name: {s['name']} | Course: {s['course']} | Marks: {s['marks']}")
    print("------------------------")

def update_student():
    students = load_data()
    roll_no = input("Enter Roll Number to update: ").strip()
    for s in students:
        if s['roll_no'] == roll_no:
            try:
                s['name'] = input(f"New Name ({s['name']}): ") or s['name']
                s['course'] = input(f"New Course ({s['course']}): ") or s['course']
                new_marks = input(f"New Marks ({s['marks']}): ")
                if new_marks:
                    s['marks'] = float(new_marks)
                save_data(students)
                print("Record updated successfully.")
                return
            except ValueError:
                print("Invalid input for marks!")
                return
    print("Student not found.")

def delete_student():
    students = load_data()
    roll_no = input("Enter Roll Number to delete: ").strip()
    updated_students = [s for s in students if s['roll_no'] != roll_no]
    if len(updated_students) == len(students):
        print("Student not found.")
    else:
        save_data(updated_students)
        print("Record deleted successfully.")

def main():
    while True:
        print("\n=== Student Record Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please select between 1 and 5.")

if __name__ == "__main__":
    main()
  
