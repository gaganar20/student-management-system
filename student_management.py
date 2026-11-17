"""Student Management System - a simple console app.

Features: add, update, search, display (and delete) students.
Concepts practiced: functions, loops, conditions, dictionaries, input validation.
Data is saved to students.json so it is still there next time you run it.
"""

import json
import os

DATA_FILE = "students.json"


# ---------- Saving and loading ----------
def load_students():
    """Load students from the file. Return an empty dict if there is none."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)


# ---------- Input validation helpers ----------
def get_text(prompt):
    """Keep asking until the user types something that isn't empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Input cannot be empty. Try again.")


def get_number(prompt, low, high):
    """Keep asking until the user types a whole number within a range."""
    while True:
        value = input(prompt).strip()
        if value.isdigit() and low <= int(value) <= high:
            return int(value)
        print(f"  Enter a whole number between {low} and {high}.")


# ---------- Core features ----------
def add_student(students):
    roll = get_text("Roll number: ")
    if roll in students:
        print("  A student with this roll number already exists.")
        return
    students[roll] = {
        "name": get_text("Name: "),
        "age": get_number("Age (5-100): ", 5, 100),
        "course": get_text("Course: "),
        "marks": get_number("Marks (0-100): ", 0, 100),
        "    }
    save_students(students)
    print("  Student added.")


def update_student(students):
    roll = get_text("Roll number to update: ")
    if roll not in students:
        print("  Student not found.")
        return
    print("  Press Enter to keep the current value.")
    student = students[roll]

    name = input(f"Name [{student['name']}]: ").strip()
    if name:
        student["name"] = name

    course = input(f"Course [{student['course']}]: ").strip()
    if course:
        student["course"] = course

    marks = input(f"Marks [{student['marks']}]: ").strip()
    if marks:
        if marks.isdigit() and 0 <= int(marks) <= 100:
            student["marks"] = int(marks)
        else:
            print("  Invalid marks, keeping the old value.")

    save_students(students)
    print("  Student updated.")


def search_student(students):
    term = get_text("Search by roll number or name: ").lower()
    found = False
    for roll, s in students.items():
        if term == roll.lower() or term in s["name"].lower():
            print_student(roll, s)
            found = True
    if not found:
        print("  No matching student found.")


def delete_student(students):
    roll = get_text("Roll number to delete: ")
    if roll in students:
        del students[roll]
        save_students(students)
        print("  Student deleted.")
    else:
        print("  Student not found.")


def print_student(roll, s):
    print(f"  Roll: {roll} | Name: {s['name']} | Age: {s['age']} "
          f"| Course: {s['course']} | Marks: {s['marks']}")


def display_students(students):
    if not students:
        print("  No students yet.")
        return
    for roll, s in students.items():
        print_student(roll, s)


# ---------- Main menu ----------
def main():
    students = load_students()
    while True:
        print("\n=== Student Management System ===")
        print("1. Add student")
        print("2. Update student")
        print("3. Search student")
        print("4. Display all students")
        print("5. Delete student")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            update_student(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("  Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
