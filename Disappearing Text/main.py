from tkinter import *
import random
import time
from tkinter import messagebox

class QuickTyper(Frame):
    def __init__(self, master):
        self.master = master
        Frame.__init__(self)
        self.pack()
        self.headline = Label(window, text="Write your hearts content, but beware - after 5 seconds of not typing it's all gone!", font=("Helvetica", 20))
        self.headline.pack(pady=60)
        self.typing_field = Text(window, font=("Helvetica", 20))
        self.typing_field.pack(pady=100, padx=200)
        self.typing_field.bind('<Key>', self.timer)

        self.is_typing = None


    def timer(self, event):
        if self.is_typing is not None:
            window.after_cancel(self.is_typing)

        self.is_typing = self.after(5000, self.delete_text)

    def delete_text(self):
        self.typing_field.delete(1.0, END)
        messagebox.showinfo("showinfo", "Oops! You didn't type for 5 seconds, and so your text has been deleted.")


window = Tk()
app = QuickTyper(window)
app.mainloop()

