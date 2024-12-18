import tkinter
from tkinter import *

class PrintAllStudent:
    def __init__(self, student):
        self.student_data = student

    def show_all_ui(self, print_frame):

        self.text_area = Text(print_frame, font=('Courier', 12), wrap=WORD, bg="white", fg="black", state=DISABLED)
        self.text_area.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        scrollbar = Scrollbar(print_frame, command=self.text_area.yview)
        scrollbar.grid(row=0, column=4, sticky='ns')
        self.text_area.configure(yscrollcommand=scrollbar.set)

        print_btn = Button(print_frame, text="Print All Students", font=('Courier', 14), bg="#008080", fg="white", command=self.print_all_students)
        print_btn.grid(row=1, columnspan=4, padx=20, pady=10)

        print_frame.grid_rowconfigure(0, weight=1)
        print_frame.grid_columnconfigure(0, weight=1)

    def print_all_students(self):
        
        all_students_info = '=' * 30 + " All Students' Information " + '=' * 30 + '\n\n'
        
      
        if self.student_data.allstudents:
            for student in self.student_data.allstudents:
                name, age, idnum, email, phone = student
                all_students_info += f'Name: {name}\nAge: {age}\nID Number: {idnum}\nEmail Address: {email}\nPhone Number: {phone}\n\n'
        
        
            all_students_info += '=' * 37 + " End " + '=' * 38
        else:
            all_students_info = "No students to display."

        self.text_area.config(state=NORMAL) 
        self.text_area.delete(1.0, END)  
        self.text_area.insert(INSERT, all_students_info)  
        self.text_area.config(state=DISABLED)  
