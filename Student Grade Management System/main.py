# Initializing an empty dictionary to store student grades
student_grades = {}

# Function to add a new student
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a grade of {grade}")

# Function to update an existing student's grade
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s marks are updated to {grade}")
    else:
        print(f"{name} is not found!")

# Function to delete a student record
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found!")

# Function to view all student records
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found or added yet.")

# Main function to handle the program logic and user interface
def main():
    while True:
        print("\n--- Student Grade Management System ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            add_student(name, grade)
            
        elif choice == '2':
            name = input("Enter student name to update: ")
            grade = int(input("Enter new grade: "))
            update_student(name, grade)
            
        elif choice == '3':
            name = input("Enter student name to delete: ")
            delete_student(name)
            
        elif choice == '4':
            display_all_students()
            
        elif choice == '5':
            print("Closing the program...")
            break
            
        else:
            print("Invalid choice, please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()