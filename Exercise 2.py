#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 11:01:34 2024

@author: aliyya
"""

"""
Exercise 2: Alexa tell me a joke
Your solution must be no more than 100 lines of code.

The randomJokes.txt file in the resources folder contains a dataset of random jokes. Each joke is on a new line and consists of a setup and punchline separated by a question mark. For example:

- Why did the chicken cross the road?To get to the other side.
- What happens if you boil a clown?You get a laughing stock.
  Write a program that when prompted with the phrase "Alexa tell me a Joke" responds with a random joke from the dataset. The program should first present the setup then allow the user to enter a key to display the punchline.

  The user should be able to continue requesting new jokes until they decide to quit the program.
"""
from tkinter import * #import tkinter into spyder
import tkinter as tk 
import random
root = tk.Tk() #create a main window
root.title("Alexa, Tell Me a Joke") #Title of your tkinter window
root.geometry("500x500") # Sets the window size 
root.configure(bg="#FFE3DC") #sets the background color 

# def Function for the jokes from the file
def load_jokes(filename):
    jokes = []
    with open("/Users/aliyya/Desktop/Assessments/randomJokes.txt") as file:
        for line in file:
            if "?" in line:  # Ensures it has both setup and punchline
                setup, punchline = line.strip().split("?", 1)
                jokes.append((setup + "?", punchline))
    return jokes

#  def Function to display a new joke setup 
def display_joke():
    global current_joke
    current_joke = random.choice(jokes)  # This function will choose a joke randomly
    setup_label.config(text=current_joke[0])
    punchline_label.config(text="")  # This is to clear the previous punchline 
    punchline_button.config(state="normal") # The punchline button is set to normal which means the button is enable and can be clicked.

# def Function to display the punchline of the joke
def show_punchline():
    punchline_label.config(text=current_joke[1])
    punchline_button.config(state="disabled") # The punchline button is diabled preventing the user from clicking to the next punchline joke.

# This is to load your jokes from the file 'Tellmeajoke.txt'
jokes = load_jokes("/Users/aliyya/Desktop/Tellmeajoke.txt") # This state will allow you to attach your text file 
current_joke = None # No jokes has been assigned yet

# This checks or ensures the jokes are working in the loaded_jokes 
if not jokes:
    raise ValueError("No jokes found in the file. Please check the file format.")


# This is for the Instructions label
instructions = tk.Label(root, text="Click 'Tell me a Joke' to hear a joke!", font=("Baskerville", 20), bg="#FFE3DC", fg="#334139")
instructions.pack(pady=10)

# This is for the Setup label
setup_label = tk.Label(root, text="", font=("Baskerville", 20, "bold"), wraplength=450, bg="#FFE3DC", fg="#334139")
setup_label.pack(pady=20)

# This is for the Punchline label
punchline_label = tk.Label(root, text="", font=("Baskerville", 18), wraplength=450, bg="#FFE3DC", fg="#334139")
punchline_label.pack(pady=10)

# This is for the Tell me a Joke button
joke_button = tk.Button(root, text="Tell me a Joke", command=display_joke, font=("Bodoni Moda", 12), bg="#FFE3DC")
joke_button.pack(pady=10)

# This is for the Show Punchline button
punchline_button = tk.Button(root, text="Show Punchline", command=show_punchline, font=("Bodoni Moda", 12), bg="#FFE3DC", state="disabled")
punchline_button.pack(pady=10)


root.mainloop() #this is to loop the main window of tkinter 
