import json

FILE_NAME = "students.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_student(data):
    roll = input("Enter Roll Number: ")
    if roll in data:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    data[roll] = {
        "name": name,
        "marks": marks
    }

    save_data(data)
    print("Student added successfully!")

def view_students(data):
    if not data:
        print("No student records found.")
        return

    for roll, info in data.items():
        print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}")

def search_student(data):
    roll = input("Enter Roll Number to search: ")
    if roll in data:
        info = data[roll]
        print(f"Name: {info['name']}, Marks: {info['marks']}")
    else:
        print("Student not found!")

def delete_student(data):
    roll = input("Enter Roll Number to delete: ")
    if roll in data:
        del data[roll]
        save_data(data)
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

def main():
    data = load_data()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            delete_student(data)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
