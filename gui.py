from tkinter import *
from functools import partial
from add_student import AddStudent
from search_student import SearchStudent
from print_all_student import PrintAllStudent
from student import StudentInfo

student_data = StudentInfo()
add_student = AddStudent(student_data)
search_student = SearchStudent(student_data)
print_all_students = PrintAllStudent(student_data)

logged_in_student_id = ""
login_attempts = 0  

win = Tk()
win.title("AIMS LPU CAVITE")
win.geometry(f"1366x768+{(win.winfo_screenwidth()-1366)//2}+{(win.winfo_screenheight()-768)//2}")
win.configure(bg="#ffffff")

btns = []
container = []
btns_txt = ["MyInfo", "Search", "Register", "View All", "Logout"]

def login_confirmation(student_id):
    global logged_in_student_id, login_attempts
    student_info = student_data.get_student_by_id(student_id)
    
    if student_info:
        logged_in_student_id = student_id
        login_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)
    else:
        login_attempts += 1
        if login_attempts < 4:
            error_label.config(text=f"Invalid student ID. Attempt {login_attempts} of 4.", fg="red")
        else:
            error_label.config(text="Maximum login attempts reached.", fg="red")
            student_id_entry.config(state=DISABLED)  
            login_btn.config(state=DISABLED) 

def logout_confirm():
    global logged_in_student_id, login_attempts
    logged_in_student_id = ""
    login_attempts = 0  
    main_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)
    student_id_entry.delete(0, END) 
    student_id_entry.config(state=NORMAL)  
    login_btn.config(state=NORMAL)  
    error_label.config(text="")  



def open_frame(frame_open, frames_close):
    for frame in frames_close:
        if frame.winfo_ismapped():
            frame.pack_forget()
    frame_open.pack(fill="both", expand=True)

def show_myinfo_ui():
    clear_frame()
    student_info = student_data.get_student_by_id(logged_in_student_id)
    if student_info:
        Label(form_frame, text="Student Info", font=("Courier", 20, "bold"), fg="#2c3e50").pack(pady=10)
        Label(form_frame, text=f"Name: {student_info[0]}", font=("Courier", 14), fg="#2c3e50").pack(pady=5)
        Label(form_frame, text=f"Age: {student_info[1]}", font=("Courier", 14), fg="#2c3e50").pack(pady=5)
        Label(form_frame, text=f"Student ID: {student_info[2]}", font=("Courier", 14), fg="#2c3e50").pack(pady=5)
        Label(form_frame, text=f"Email: {student_info[3]}", font=("Courier", 14), fg="#2c3e50").pack(pady=5)
        Label(form_frame, text=f"Phone: {student_info[4]}", font=("Courier", 14), fg="#2c3e50").pack(pady=5)
    else:
        Label(form_frame, text="Student info not found.", font=("Courier", 14), fg="red").pack(pady=5)

def show_search_student_ui():
    clear_frame()
    search_student.show_search_ui(form_frame)

def show_add_student_ui():
    clear_frame()
    add_student.show_reg_ui(form_frame)

def show_print_all_students_ui():
    clear_frame()
    print_all_students.show_all_ui(form_frame)

def clear_frame():
    for widget in form_frame.winfo_children():
        widget.destroy()

func = [
    show_myinfo_ui,
    show_search_student_ui,
    show_add_student_ui,
    show_print_all_students_ui,
    logout_confirm
]

login_frame = Frame(win, bg="#ffffff")
login_frame.pack(fill="both", expand=True)

login_form = Frame(login_frame, bg="white", padx=20, pady=20, relief=SOLID, bd=2)
login_form.place(relx=0.5, rely=0.5, anchor=CENTER)

Label(login_form, text="Login", font=("Courier", 20, "bold"), bg="white", fg="#2c3e50").pack(pady=10)

student_id_label = Label(login_form, text="Student ID", font=("Courier", 12), bg="white", fg="#2c3e50")
student_id_label.pack(pady=5)
student_id_entry = Entry(login_form, font=("Courier", 12), bg="white", fg="black")
student_id_entry.pack(pady=5)

error_label = Label(login_form, text="", font=("Courier", 12), bg="white")
error_label.pack(pady=5)

login_btn = Button(login_form, text="Login", font=("Courier", 12, "bold"), bg="#27ae60", fg="white", relief=FLAT, height=2, width=15,
                   command=lambda: login_confirmation(student_id_entry.get()))
exit_btn = Button(login_form, text="Exit", font=("Courier", 12), bg="#e74c3c", fg="white", relief=FLAT, height=2, width=15, command=win.quit)

login_btn.pack(side="left", padx=5)
exit_btn.pack(side="left", padx=5)

main_frame = Frame(win, bg="#ffffff")

menu_contain = Frame(main_frame, bg="#27ae60", border=2, relief=SOLID, padx=20)
menu_contain.pack(side="right", fill="y", padx=20, pady=20)

def on_enter(btn):
    btn['background'] = "#1e8449"

def on_leave(btn):
    btn['background'] = "#27ae60"

for i, text in enumerate(btns_txt):
    btn = Button(menu_contain, text=text, font=("Courier", 14), bg="#27ae60", fg="white", relief=FLAT, height=3, width=20, borderwidth=0, command=func[i])
    btn.grid(row=i, column=0, pady=8, padx=8)
    btn.bind("<Enter>", lambda e, btn=btn: on_enter(btn))
    btn.bind("<Leave>", lambda e, btn=btn: on_leave(btn))
    btns.append(btn)

content_frame = Frame(main_frame, bg="#ffffff", border=2, relief=SOLID, padx=20, pady=20)
content_frame.pack(side="left", fill="both", expand=True, padx=30, pady=30)

form_frame = Frame(content_frame, bg="white", padx=40, pady=40)
form_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

win.mainloop()
