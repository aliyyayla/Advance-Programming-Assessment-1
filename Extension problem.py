#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:51:29 2024

@author: aliyya
"""

"""
Extension Problem
"""

import tkinter as tk
from tkinter import messagebox, ttk

# using class function to define and to manage students record individually
class Student:
    def __init__(self, code, name, mark1, mark2, mark3, exam_mark):
        self.code = code
        self.name = name
        self.coursework_marks = [mark1, mark2, mark3]
        self.exam_mark = exam_mark
        self.total_coursework = sum(self.coursework_marks)
        self.total_score = self.total_coursework + self.exam_mark
        self.percentage = (self.total_score / 160) * 100
        self.grade = self.get_grade()

    # using def function to get the output of the grades of students depending in their percentage
    def get_grade(self):
        if self.percentage >= 70:
            return 'A'
        elif self.percentage >= 60:
            return 'B'
        elif self.percentage >= 50:
            return 'C'
        elif self.percentage >= 40:
            return 'D'
        else:
            return 'F'

# def function to load the data from a file
def load_data(filename):
    students = []
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        for line in file:
            code, name, mark1, mark2, mark3, exam_mark = line.strip().split(',')
            students.append(Student(int(code), name, int(mark1), int(mark2), int(mark3), int(exam_mark)))
    return students

#def function to save the data from the file of the students
def save_data(filename, students):
    """Save the student data back to the file."""
    with open(filename, 'w') as file:
        file.write(f"{len(students)}\n")
        for student in students:
            line = f"{student.code},{student.name},{student.coursework_marks[0]},{student.coursework_marks[1]},{student.coursework_marks[2]},{student.exam_mark}\n"
            file.write(line)

#using class function for the students records
class StudentApp:
    def __init__(self, root, students): #
        self.root = root
        self.students = students
        self.root.title("Student Manager")
        self.root.geometry("900x500")
        self.root.configure(bg="#D3C4E3")
        
        tk.Label(self.root, text="Student Manager", font=("Baskerville", 35, "bold"), bg="#D3C4E3", fg="#4C191B").pack(pady=10)

        # This is for the top menu buttons
        button_frame = tk.Frame(self.root, bg="#D3C4E3")
        button_frame.pack(pady=10)
        
        # creating buttons for the view, show lowest and highest score
        tk.Button(button_frame, text="View All Student Records", command=self.view_all_records, width=20, height=2).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Show Highest Score", command=self.show_highest_score, width=20, height=2).grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="Show Lowest Score", command=self.show_lowest_score, width=20, height=2).grid(row=0, column=2, padx=10)
        
        #an addditional buttons for the sort, add, delete and update
        tk.Button(button_frame, text="Sort Records", command=self.sort_records, width=20, height=2).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(button_frame, text="Add Record", command=self.add_record, width=20, height=2).grid(row=1, column=1, padx=10, pady=5)
        tk.Button(button_frame, text="Delete Record", command=self.delete_record, width=20, height=2).grid(row=1, column=2, padx=10, pady=5)
        tk.Button(button_frame, text="Update Record", command=self.update_record, width=20, height=2).grid(row=1, column=3, padx=10, pady=5)

        # a Dropdown or choice for choosing a students record individually
        record_frame = tk.Frame(self.root, bg="#D3C4E3")
        record_frame.pack(pady=10)
        
        tk.Label(record_frame, text="View Individual Student Record:", font=("Baskerville", 12), bg="#D3C4E3", fg="#4C191B").grid(row=0, column=0, padx=0)
        
        self.selected_student = tk.StringVar() #using this variable to allow the string content to the widget associated with
        student_names = [student.name for student in self.students]
        self.student_dropdown = ttk.Combobox(record_frame, textvariable=self.selected_student, values=student_names, state="readonly", width=20)
        self.student_dropdown.grid(row=0, column=1, padx=5)
        
        tk.Button(record_frame, text="View Record", command=self.view_individual_record).grid(row=0, column=2, padx=5)

        # These are the text area to display the results of each students
        self.output_text = tk.Text(self.root, wrap="word", width=70, height=15, font=("Lato", 10))
        self.output_text.pack(pady=10)
        self.output_text.config(state="disabled", bg="#4C191B")

    #def function to display all the records of the students
    def display_student(self, student):
        msg = ( # this is how the format of student information should look like when displayed
            f"Grade: {student.grade}\n"
            f"Name: {student.name}\n"
            f"Number: {student.code}\n"
            f"Coursework Total: {student.total_coursework}\n"
            f"Exam Mark: {student.exam_mark}\n"
            f"Overall Percentage: {student.percentage:.2f}%\n"
            f"Grade: {student.grade}\n"
        )
        return msg
    
    # def function to view all the records of the students
    def view_all_records(self):
        total_percentage = 0
        output = ""
        
        for student in self.students: #uisng for loop 
            output += self.display_student(student) + "\n"
            total_percentage += student.percentage
        
        avg_percentage = total_percentage / len(self.students)
        output += f"\nTotal Students: {len(self.students)}\nAverage Percentage: {avg_percentage:.2f}%"
        
        self.show_output(output)

    #a def function to VIEW the record of the students INDIVIDUALLY
    def view_individual_record(self):
        selected_name = self.selected_student.get()
        if selected_name:
            student = next((s for s in self.students if s.name == selected_name), None)
            if student:
                output = self.display_student(student)
                self.show_output(output)

    # def function to show the highest score of a students
    def show_highest_score(self):
        student = max(self.students, key=lambda s: s.total_score)
        output = self.display_student(student)
        self.show_output(output)

    # def function to show the lowest score of a students
    def show_lowest_score(self):
        student = min(self.students, key=lambda s: s.total_score)
        output = self.display_student(student)
        self.show_output(output)

    # def function to display the sorted records of the students
    def sort_records(self):
        """Sort student records in ascending or descending order and display them."""
        order = messagebox.askquestion("Sort Order", "Sort in ascending order?")
        self.students.sort(key=lambda s: s.total_score, reverse=(order == 'no'))
        self.view_all_records()  # Display sorted records

    # def function to add the record of the student/s 
    def add_record(self):
        """Add a new student record."""
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Student Record")

        # this is to create an entry fields for the new student data
        fields = ["Student Code", "Name", "Coursework Mark 1", "Coursework Mark 2", "Coursework Mark 3", "Exam Mark"]
        entries = {}
        for i, field in enumerate(fields): #using the for loop for the variable fields
            tk.Label(add_window, text=field).grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(add_window)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries[field] = entry
        
        # def function to save a new record of the student/s
        def save_new_record():
            try:
                code = int(entries["Student Code"].get())
                name = entries["Name"].get()
                marks = [int(entries[f"Coursework Mark {i+1}"].get()) for i in range(3)]
                exam_mark = int(entries["Exam Mark"].get())
                new_student = Student(code, name, *marks, exam_mark)
                self.students.append(new_student)
                self.student_dropdown['values'] = [student.name for student in self.students]  # Update dropdown
                save_data("/Users/aliyya/Desktop/Assessments/studentMarks.txt", self.students)
                add_window.destroy()
                messagebox.showinfo("Success", "Student record added successfully.")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid data.")

        tk.Button(add_window, text="Save", command=save_new_record).grid(row=len(fields), column=0, columnspan=2, pady=10)

    # def function for removing a record of data of the student
    def delete_record(self):
        """Delete a student record by name."""
        selected_name = self.selected_student.get()
        if selected_name:
            student = next((s for s in self.students if s.name == selected_name), None)
            if student:
                self.students.remove(student)
                self.student_dropdown['values'] = [student.name for student in self.students]  # Update dropdown
                save_data("/Users/aliyya/Desktop/Assessments/studentMarks.txt", self.students)
                self.show_output(f"Record for {selected_name} has been deleted.")
            else:
                messagebox.showerror("Error", "Student not found.")

    # def function for updating the record data of the student 
    def update_record(self):
        """Update an existing student's record."""
        selected_name = self.selected_student.get()
        student = next((s for s in self.students if s.name == selected_name), None)
        
        if student: #using the if statement
            update_window = tk.Toplevel(self.root)
            update_window.title("Update Student Record")

            # this is for creating an entry fields for updating student's data
            fields = {
                "Coursework Mark 1": student.coursework_marks[0],
                "Coursework Mark 2": student.coursework_marks[1],
                "Coursework Mark 3": student.coursework_marks[2],
                "Exam Mark": student.exam_mark
            }
            entries = {}
            for i, (label, value) in enumerate(fields.items()): # using for loop 
                tk.Label(update_window, text=label).grid(row=i, column=0, padx=5, pady=5)
                entry = tk.Entry(update_window)
                entry.insert(0, str(value))
                entry.grid(row=i, column=1, padx=5, pady=5)
                entries[label] = entry

            # def function to save the updated record data of the student
            def save_updated_record():
                try:
                    student.coursework_marks = [int(entries[f"Coursework Mark {i+1}"].get()) for i in range(3)]
                    student.exam_mark = int(entries["Exam Mark"].get())
                    student.total_coursework = sum(student.coursework_marks)
                    student.total_score = student.total_coursework + student.exam_mark
                    student.percentage = (student.total_score / 160) * 100
                    student.grade = student.get_grade()
                    save_data("/Users/aliyya/Desktop/Assessments/studentMarks.txt", self.students)
                    update_window.destroy()
                    messagebox.showinfo("Success", "Student record updated successfully.")
                except ValueError:
                    messagebox.showerror("Input Error", "Please enter valid data.")

            tk.Button(update_window, text="Save", command=save_updated_record).grid(row=len(fields), column=0, columnspan=2, pady=10)

    # def function to show the output
    def show_output(self, content):
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", content)
        self.output_text.config(state="disabled")

if __name__ == "__main__": # to check if the code is running 
    students = load_data("/Users/aliyya/Desktop/Assessments/studentMarks.txt")
    root = tk.Tk() # to create a main window
    app = StudentApp(root, students) #for the main window to run 
    root.mainloop() # Start the Tkinter main loop
