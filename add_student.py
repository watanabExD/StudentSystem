import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox

class AddStudent:
    def __init__(self, student_info):
        self.student_data = student_info
        
    def input_add_student(self):
        print("="*10, "Add a New Student", "="*10)
      
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        idnum = input("Enter ID Number: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone Number: ")

        self.add_student(name, age, idnum, email, phone)
        print("="*10, "Student added successfully", "="*10)

    def add_student(self, name, age, idnum, email, phone):
        print(f"\nAdded student {name} to the list.\n")

        self.student_data.add_student_to_memory(name, age, idnum, email, phone)

        self.write_to_file(f"{name}, {age}, {idnum}, {email}, {phone}\n")
        for entry in self.reg_entry:
            entry.delete(0, END)

    def write_to_file(self, data_to_write):
        with open("student_data.txt", "a") as file:
            file.write(data_to_write)
        print("Data saved successfully.")
        
    def show_reg_ui(self, reg_frame):
        self.lblErrors = Label(reg_frame, text="", font=('Courier', 12), bg="white", fg="red")
        self.lblErrors.grid(row=1, column=1, columnspan=4, pady=10)  
        
        self.reg_txt = ["Name", "Age", "ID Number", "Email", "Phone"]
        self.reg_entry = []
        
        for i in range(len(self.reg_txt)):
         
            Label(reg_frame, text=self.reg_txt[i], font=('Courier', 14), width=15, bg="#ecf0f1").grid(row=i+2, column=0, pady=10)  
     
            entry = Entry(reg_frame, width=30, font=('Courier', 14), bg="white")
            entry.grid(row=i+2, column=1, columnspan=3, pady=5)  
            self.reg_entry.append(entry)
        
   
        reg_btn = Button(reg_frame, width=15, text="Register Student", font=('Courier', 14), bg="#008080", fg="white", command=self.check_entries)
        reg_btn.grid(row=len(self.reg_txt)+2, columnspan=4, pady=20)  
        
    def check_entries(self):
        errors = []
        for i in range(len(self.reg_entry)):
            if self.reg_entry[i].get() == "":
                errors.append(f"{self.reg_txt[i]} is required.")
        if not errors:
            self.add_student(self.reg_entry[0].get(), self.reg_entry[1].get(), self.reg_entry[2].get(), self.reg_entry[3].get(), self.reg_entry[4].get())
            messagebox.showinfo("Nice!", "Na Add na ang Student!")
        else:
            self.lblErrors.config(text="\n".join(errors))
