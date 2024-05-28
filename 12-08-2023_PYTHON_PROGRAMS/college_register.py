class Student:
    def __init__(self, name, age, gender, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

class CollegeRegister:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, student):
        self.students[student_id] = student

    def find_student_by_id(self, student_id):
        return self.students.get(student_id, None)

    def display_all_students(self):
        for student_id, student in self.students.items():
            print(f"ID: {student_id}, Name: {student.name}, Age: {student.age}, Gender: {student.gender}, Email: {student.email}")

def main():
    college_register = CollegeRegister()

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Find Student by ID")
        print("3. Display All Students")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            gender = input("Enter Gender: ")
            email = input("Enter Email: ")
            student = Student(name, age, gender, email)
            college_register.add_student(student_id, student)
            print("Student added successfully!")

        elif choice == "2":
            student_id = input("Enter Student ID: ")
            student = college_register.find_student_by_id(student_id)
            if student:
                print(f"Student found - Name: {student.name}, Age: {student.age}, Gender: {student.gender}, Email: {student.email}")
            else:
                print("Student not found.")

        elif choice == "3":
            college_register.display_all_students()

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
