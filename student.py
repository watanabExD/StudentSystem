class StudentInfo:
    def __init__(self):
     
        self.allstudents = []
        self.load_students_from_file()

    def load_students_from_file(self):
       
        try:
            with open("student_data.txt", "r") as file:
                for line in file:
                    data = line.strip().split(', ')
                    if len(data) == 5:
                        name, age, idnum, email, phone = data
                        self.add_student_to_memory(name, age, idnum, email, phone)
                    else:
                        print(f"Skipping invalid line in file: {line.strip()}")
        except FileNotFoundError:
            print("No previous student data found.")

    def add_student_to_memory(self, name, age, idnum, email, phone):
        student = [name, age, idnum, email, phone]
        self.allstudents.append(student)

    def add_student(self, name, age, idnum, email, phone):
        self.add_student_to_memory(name, age, idnum, email, phone)
        self.write_to_file(name, age, idnum, email, phone)

    def write_to_file(self, name, age, idnum, email, phone):
        with open("student_data.txt", "a") as file:
            file.write(f"{name},{age},{idnum},{email},{phone}\n")
        print("Data saved successfully.")

    def get_all_students(self):
        return self.allstudents

    def get_student_by_id(self, student_id):
       
        for student in self.allstudents:
            if student[2] == student_id:  
                return student
        return None

    def __str__(self):
        student_info = ""
        for student in self.allstudents:
            student_info += f"Name: {student[0]}, Age: {student[1]}, ID: {student[2]}, Email: {student[3]}, Phone: {student[4]}\n"
        return student_info if student_info else "No students available."

