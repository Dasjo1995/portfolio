from tkinter import *
import random
import time
from tkinter import messagebox


with open('1-1000.txt') as file:
    word_list = [word for word in file]
    word_list_clean = [word.strip("\n") for word in word_list]          # Removes the characters before or after each word
    random.shuffle(word_list_clean)                                     # Shuffles the words randomly


max_time = time.time() + 60         # Timer for 60 seconds
score = 0

def score_keeping():
    global score
    score += 1
    print(score)
    return score

def check_word():
    written_word = typing_field.get()
    if written_word == chosen_word + " ":
        correct = True
        print("correct")
        score_keeping()
        typing_field.delete(0, END)
        incorrect_label.config(text="")
        word_displayer()
    else:
        incorrect_label.config(text="Incorrect spelling, try again.")
        typing_field.delete(0, END)
        correct = False

def word_displayer():
    global chosen_word
    chosen_word = word_list_clean[random.randint(0, 999)]
    sentences.config(text=chosen_word)
    if time.time() > max_time:
        print("game over")
        messagebox.showinfo("showinfo", f"Your score is: {score} words per minute!")
        incorrect_label.config(text=f"Score: {score} words/minute")







window = Tk()
window.title("Typester")
window.geometry("800x600")
window.config(bg="light grey")


headline_label = Label(window, text="Welcome to Typester!", font=("Helvetica", 20))
headline_label.pack(pady=30)

headline_label = Label(window, text="Press start and write the words as quickly as you can!\nPress space to submit your word.", font=("Helvetica", 15))
headline_label.pack(pady=30)

incorrect_label = Label(window, text="")
incorrect_label.pack(pady=20)

typing_field = Entry(window, font=("Helvetica", 20))
typing_field.pack()

sentences = Label(window, text="", font=("Helvetica", 20))
sentences.pack(pady=30)

start_button = Button(window, text="Start", command=word_displayer)
start_button.pack()

check_answer_btn = Button(window, text="Submit", command=check_word)
check_answer_btn.pack(pady=20)
window.bind("<space>", lambda event:check_word())



window.mainloop()