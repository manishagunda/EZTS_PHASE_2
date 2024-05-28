class StudentRegister:
    def __init__(self):
        self.students = {}

    def add_student(self, name, age, gender, mail):
        self.students[name] = {'age': age, 'gender': gender, 'mail': mail}

    def get_details(self, name, field):
        if name in self.students and field in self.students[name]:
            return self.students[name][field]
        else:
            return "Details not found"

if __name__ == "__main__":
    register = StudentRegister()

    register.add_student("Ram", 21, "Male", "ram@gmail.com")
    register.add_student("Shivani", 19, "Female", "shivani@gmail.com")
    register.add_student("Arjun", 25, "Male", "arjun@gmail.com")

    while True:
        input_str = input("Input: ")
        input_str = input_str.capitalize()
        if input_str == "exit":
            break
        
        input_parts = input_str.split()
        if len(input_parts) != 2:
            print("Invalid input format. Please enter in the format: Name field")
            continue
        
        name, field = input_parts
        result = register.get_details(name, field)
        print(result)