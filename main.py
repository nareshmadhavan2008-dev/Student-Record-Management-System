import csv
import os

FILE_NAME = "students.csv"


# Create CSV file if it does not exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Department", "Year"])


# Add student
def add_student():
    try:
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        department = input("Enter Department: ")
        year = input("Enter Year: ")

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([student_id, name, department, year])

        print("Student added successfully!")

    except Exception as e:
        print("Error:", e)


# View students
def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:
                print("No student records found.")
                return

            for row in rows:
                print(" | ".join(row))

    except FileNotFoundError:
        print("File not found!")


# Update student
def update_student():
    student_id = input("Enter Student ID to update: ")
    updated = False

    try:
        with open(FILE_NAME, "r") as file:
            rows = list(csv.reader(file))

        for row in rows[1:]:
            if row[0] == student_id:
                row[1] = input("Enter new Name: ")
                row[2] = input("Enter new Department: ")
                row[3] = input("Enter new Year: ")
                updated = True
                break

        if updated:
            with open(FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            print("Student updated successfully!")
        else:
            print("Student ID not found.")

    except FileNotFoundError:
        print("File not found!")


# Delete student
def delete_student():
    student_id = input("Enter Student ID to delete: ")

    try:
        with open(FILE_NAME, "r") as file:
            rows = list(csv.reader(file))

        new_rows = [rows[0]]

        for row in rows[1:]:
            if row[0] != student_id:
                new_rows.append(row)

        if len(new_rows) == len(rows):
            print("Student ID not found.")
            return

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)

        print("Student deleted successfully!")

    except FileNotFoundError:
        print("File not found!")


# Main menu
def main():
    initialize_file()

    while True:
        print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()

            elif choice == 2:
                view_students()

            elif choice == 3:
                update_student()

            elif choice == 4:
                delete_student()

            elif choice == 5:
                print("Thank you!")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number!")

        finally:
            print("Operation completed.")


if __name__ == "__main__":
    main()