import tkinter
from tkinter import *
from tkinter import messagebox

class SearchStudent:
    def __init__(self, student):
        self.student_data = student
    
    def verify_login(self, idnum):
        for student in self.student_data.allstudents:
            if student[2] == idnum:
                return [student[0], student[2]]  
        return False

    def show_search_ui(self, search_frame):
        self.search_lbl = Label(search_frame, text="", font=('Courier', 12), bg="white", fg="red")
        self.search_lbl.grid(row=4, column=0, columnspan=4, pady=(10, 0)) 

        self.search_entry = Entry(search_frame, width=30, font=('Courier', 14), bg="white")
        self.search_entry.grid(row=2, column=1, columnspan=3, pady=(10, 5))
        Label(search_frame, text="Enter ID Number", font=('Courier', 14), width=15, bg="#ecf0f1").grid(row=2, column=0, pady=(10, 5))

        search_btn = Button(search_frame, width=15, text="Search Student", font=('Courier', 14), bg="#008080", fg="white", command=self.check_search)
        search_btn.grid(row=3, column=0, columnspan=4, pady=(5, 10))

    def check_search(self):
        student_id = self.search_entry.get()
        result = self.search_student(student_id)
        if result:
            self.search_lbl.config(text=result, fg="green")
        else:
            self.search_lbl.config(text="Student not found", fg="red")

    def search_student(self, keyword):
        for student in self.student_data.allstudents:
            if student[2] == keyword:
                name, age, idnum, email, phone = student
                return f'Name: {name}\nAge: {age}\nID Number: {idnum}\nEmail: {email}\nPhone: {phone}'
        return None
