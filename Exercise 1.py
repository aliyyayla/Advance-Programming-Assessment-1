#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 01:45:09 2024

@author: aliyya
"""

"""
Exercise 1: Math Quiz 
Your solution must be no more than 250 lines of code.
Develop a program that presents the user with quiz of arithmetic problems. Each "play" of the quiz should be 10 questions. The user should initially be presented with a short menu of options to select a difficulty level. It could look something like this:

DIFFICULTY LEVEL
 1. Easy
 2. Moderate
 3. Advanced
The difficulty levels determine the number of digits in the numbers to be added or subtracted. Easy means only single digit numbers; moderate means double digit numbers; and advanced means 4-digit numbers. After the user picks the level they desire, your program presents problems that look like this:

45 + 9 =
34 - 88 =
etc
For each problem presented, the user is given a chance to answer. If the answer is correct, another problem is presented. If the answer is wrong, the user is to be given one more chance at that problem. The program should keep a tally of the users score, awarding 10 points for a correct answer on first attempt and 5 points on the second attempt. You should implement a random number generator (see the resources folder) to determine:

The values to be added or subtracted
Whether the problem is addition or subtraction
  The program should include the functions listed below. These functions should make use of parameters and return values as appropriate. You may include others or extend the functionality of the program if you see fit.

displayMenu: A function that displays the difficulty level menu at the beginning of the quiz.
randomInt: A function that determines the values used in each question. The min and max values of the numbers should be based on the difficulty level chosen as described above.
decideOperation: A function that randomly decides whether the problem is an addition or subtraction problem and returns a char.
displayProblem: A function that displays the question to the user and accepts their answer.
isCorrect: A function that checks whether the users answer was correct and outputs an appropriate message
displayResults: function that outputs the users final score out of a possible 100 and ranks the user based on their score (e.g. A+ for a score over 90)
  Once the user has finished the quiz, prompt them to see if they'd like to play it again.
"""

from tkinter import * #import tkinter into spyder
import tkinter as tk
import random
root = tk.Tk() #create a main window
root.title("Arithmetic Math Quiz") #Title of your tkinter window
root.geometry("500x500") #Sets the window size 
root.configure(bg="#FFD166")#sets the background color 

# This is for all the global variables for def function 
score = 0
question_count = 0
current_answer = None
attempts = 0
difficulty_level = 1

# def funtion for display menu for difficulty selection
def displayMenu():
    global score, question_count, difficulty_level
    score = 0
    question_count = 0
    difficulty_label.config(text="Hi ! Welcome to Math quiz, \n please select your difficulty level.")
    problem_label.config(text="")
    answer_entry.delete(0, tk.END)
    result_label.config(text="")
    start_button.pack_forget()
    play_again_button.pack_forget()
    easy_lvl.pack(side=tk.LEFT, padx= +10)
    moderate_lvl.pack(side=tk.LEFT, padx= +10)
    advance_lvl.pack(side=tk.LEFT, padx= +10) 
    difficulty_label.pack(pady=10) # This is to show the frame for the buttons
   

# def funtcion to set the difficulty level and to start the quiz
def set_difficulty(level):
    global difficulty_level
    difficulty_level = level
    easy_lvl.pack_forget()
    moderate_lvl.pack_forget()
    advance_lvl.pack_forget()
    start_button.pack(pady=10)
    displayProblem()

# def function to generate a random integer based on the difficulty
def randomInt():
    if difficulty_level == 1:
        return random.randint(1, 9)
    elif difficulty_level == 2:
        return random.randint(10, 99)
    elif difficulty_level == 3:
        return random.randint(1000, 9999)

# This def function decideOperation is to decide if the problem is addition or subtraction
def decideOperation():
    return '+' if random.choice([True, False]) else '-'

# The def displayProblem is to display the current problem of the equation 
def displayProblem():
    global current_answer, attempts, question_count
    attempts = 0
    if question_count < 10:
        question_count += 1
        num1 = randomInt()
        num2 = randomInt()
        operation = decideOperation()
        current_answer = num1 + num2 if operation == '+' else num1 - num2
        problem_label.config(text=f"{num1} {operation} {num2} = ?")
    else:
        displayResults()

# this def function isCorrect to check if your answer is correct
def isCorrect():
    global score, attempts
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number.", bg="#FFD166",fg="#6A2E35")
        return

    if user_answer == current_answer: # here using the if else statement if the answer you got is correct, you will obtain a +10 points.
        if attempts == 0:
            score += 10
            result_label.config(text="Outstanding ! You got +10 points.", fg="#334139")
        else: # else, you get +5 if you got the second answer correct
            score += 5 
            result_label.config(text="Good Job ! You got +5 points.", fg="#334139")
        answer_entry.delete(0, tk.END)
        displayProblem()
    else: # else, if your both of your answer got wrong, then repeat.
        attempts += 1
        if attempts < 2:
            result_label.config(text="Uh-oh. Keep going !", fg="#334139")
        else: #else, you got the wrong answer three times.
            result_label.config(text=f"Unfortunately the answer was {current_answer}. \n Try again :)", fg="#502419")
            answer_entry.delete(0, tk.END)
            displayProblem()

# this def function is to display your final score and grade using the nested if statement
def displayResults():
    grade = ""
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    problem_label.config(text="")
    result_label.config(text=f"YAY ! You Made it ! Your Score is: {score}/100. Grade: {grade}")
    play_again_button.pack(pady=10)

# Displaying the Widgets
difficulty_label = tk.Label(root, text="DIFFICULTY LEVEL", font=("PT Serif", 16), bg="#FFD166")
difficulty_label.pack(pady=10)

# this is for the Difficulty Level Buttons
easy_lvl = tk.Button(root, text="Easy", command=lambda: set_difficulty(1), font=("PT Serif", 12), padx= 30)
moderate_lvl = tk.Button(root, text="Moderate", command=lambda: set_difficulty(2), font=("PT Serif", 12), padx= 30)
advance_lvl = tk.Button(root, text="Advanced", command=lambda: set_difficulty(3), font=("PT Serif", 12), padx=30)

# this is for the Problem Label
problem_label = tk.Label(root, text="", font=("PT Serif", 16, "bold"), bg="#FFD166")
problem_label.pack(pady=20)

# this is for the Answer Entry
answer_entry = tk.Entry(root, font=("PT Serif", 14))
answer_entry.pack()

# this is for the Result Label
result_label = tk.Label(root, text="", font=("PT Serif", 12), bg="#F0F8FF")
result_label.pack(pady=10)

# this one is for Buttons of the start and submit 
start_button = tk.Button(root, text="Start the Quiz", command=displayProblem, font=("PT Serif", 12),bg="#FFD166" ,fg="#3C0000")
submit_button = tk.Button(root, text="Submit your Answer", command=isCorrect, font=("PT Serif", 12), bg="#FFD166",fg="#3C0000")
submit_button.pack(pady=10)

play_again_button = tk.Button(root, text="Play Again", command=displayMenu, font=("PT Serif", 12), bg="#FFD166",fg="#3C0000")

# This call to function will initialize the menu with the use of the def function
displayMenu()

# Start the Tkinter main loop
root.mainloop()
