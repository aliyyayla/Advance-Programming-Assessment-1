#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:19:11 2024

@author: aliyya
"""

"""
Exercise 3: Student Manager
Your solution must be no more than 250 lines of code.
A list of student marks are held in the studentMarks.txt file available in the resources folder. These need to be loaded into a program to analyse the data. The first line is a single integer that gives the number of students in the class. Each subsequent line of the file comprises a student code (between 1000 and 9999), three course marks (each out of 20) and an examination mark (out of 100).

There is one line of data for each student in the class, with each piece of data separated by a comma (see example below).

8439,Jake Hobbs,10,11,10,43

Your task is to create a program that enables the user to manage this data. As a minimum expectation your program should include the following menu and use appropriate programming techniques to handle the functionality required by each menu item.

1. View all student records
2. View individual student record
3. Show student with highest total score
4. Show student with lowest total score
Below are the expectations for each menu item:

1. View all student records:
The program should output the following information for each student:

Students Name
Students Number
Total coursework mark
Exam Mark
Overall percentage (coursework and examination marks contributing in direct proportion to the marks available i.e. the percentage is based on the potential total of 160 marks).
Student grade ( ‘A’ for 70%+, ‘B’ for 60%-69%, ‘C’ for 50%-59%, ‘D’ for 40%-49%, ‘F’ for under 40% )
 Once all students have been output you should also output a summary stating the number of students in the class and the average percentage mark obtained.

2. View individual student record
Allow the user to select a student then output their results as per menu item 1. How you enable the user to select the individual student is up to you, this could be done via a menu code:

1. Jake Hobbs
2. Fred Smith
3. Jo Huckleberry
etc...
 Or by allowing the user to enter a students name and/or student number.

3. Show student with highest overall mark
Identify the student with the highest mark and output their results in same format as menu item 1.

4. Show student with lowest overall mark
Identify the student with the lowest mark and output their results in same format as menu item 1.

  Expected output - https://www.loom.com/share/0d255bf19b5f4a35b6d50e63b1a48627?sid=35bb32b8-37c6-409b-87d1-94971282147e

 Note : You are free to enhance the aesthetics of the app devloped.  
"""

import tkinter as tk
from tkinter import messagebox, ttk

#using class function for the students records
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

     #using def function to get the output of the grades of students depending in their percentage
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

#using class function for the students records
class StudentApp:
    def __init__(self, root, students):
        self.root = root
        self.students = students
        self.root.title("Student Manager")
        self.root.geometry("820x500")
        self.root.configure(bg="#D3C4E3")

        tk.Label(self.root, text="Student Manager", font=("Baskerville", 35, "bold"), bg="#D3C4E3", fg="#4C191B").pack(pady=10)

        # these are for the frames of the view all, show highest and show lowest score buttons
        button_frame = tk.Frame(self.root, bg="#D3C4E3")
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="View All Student Records", command=self.view_all_records, width=20, height=2).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Show Highest Score", command=self.show_highest_score, width=20, height=2).grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="Show Lowest Score", command=self.show_lowest_score, width=20, height=2).grid(row=0, column=2, padx=10)

        # a Dropdown or choice for choosing a students record individually
        record_frame = tk.Frame(self.root, bg="#D3C4E3")
        record_frame.pack(pady=10)
        
        tk.Label(record_frame, text="View Individual Student Record:", font=("Baskerville", 12), bg="#D3C4E3", fg="#4C191B").grid(row=0, column=0, padx=0)
        
        self.selected_student = tk.StringVar()
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
        # how the format of the student information should be displayed
        msg = (
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
        
        for student in self.students: #using for loop
            output += self.display_student(student) + "\n"
            total_percentage += student.percentage
        
        avg_percentage = total_percentage / len(self.students)
        output += f"\nTotal Students: {len(self.students)}\nAverage Percentage: {avg_percentage:.2f}%"
        
        self.show_output(output)

    #a def function to VIEW the record of the students INDIVIDUALLY
    def view_individual_record(self):
        selected_name = self.selected_student.get()
        if selected_name: # using if statement
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

    # def function to show the output
    def show_output(self, content):
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", content)
        self.output_text.config(state="disabled")

# this is to check if the code is running
if __name__ == "__main__":
    students = load_data("/Users/aliyya/Desktop/Assessments/studentMarks.txt")  
    root = tk.Tk() # to create a main window
    app = StudentApp(root, students) #for the main window to run 
    root.mainloop() # Start the Tkinter main loop
