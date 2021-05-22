import threading
import time
import tkinter as tk
from users.auth import *


class Log:
    def __init__(self):
        self.username = str()
        self.password = str()

        self.root = tk.Tk()
        self.option = tk.StringVar()
        self.option.set("student")
        # self.option = self.root.StringVar()
        self.root.title("Authentication")
        self.root.geometry("400x500")
        self.spacer1_label = tk.Label(self.root, text="", font=("calabri", 18), height=4)
        self.spacer1_label.grid(column=1, row=1, columnspan=2)
        self.welcome_label = tk.Label(self.root, text="Welcome to SinaMedia", font=("calabri", 18))
        self.welcome_label.grid(column=1, row=2, columnspan=2)
        self.spacer_label = tk.Label(self.root, text="", font=("calabri", 18), height=2)
        self.spacer_label.grid(column=1, row=3, columnspan=2)
        self.username_label = tk.Label(self.root, text="Username:", font=("calabri", 18))
        self.username_label.grid(column=1, row=4)
        self.username_entry = tk.Entry(self.root, textvariable=self.username, width=15, font=("calabri", 18))
        self.username_entry.grid(column=2, row=4)
        ###########
        self.spacer2_label = tk.Label(self.root, text="", font=("calabri", 18), height=1)
        self.spacer2_label.grid(column=1, row=5, columnspan=2)
        self.password_label = tk.Label(self.root, text="Password:", font=("calabri", 18))
        self.password_label.grid(column=1, row=6)

        self.password_entry = tk.Entry(self.root, textvariable=self.password, width=15, font=("calabri", 18))
        self.password_entry.grid(column=2, row=6)

        self.spacer3_label = tk.Label(self.root, text="", font=("calabri", 18), height=1)
        self.spacer3_label.grid(column=1, row=7, columnspan=2)
        self.log_in_button = tk.Button(text="log in!", height=2, command=lambda: self.login())
        self.log_in_button.grid(column=1, row=8, sticky="we")
        self.register_button = tk.Button(text="sign up!", height=2, command=lambda: self.signup())
        self.register_button.grid(column=2, row=8, sticky="we")
        self.teacher_radio = tk.Radiobutton(self.root, var=self.option, text="teacher",value="teacher",
                                            font=("calabri", 18))
        self.teacher_radio.grid(column=1, row=9)
        self.student_radio = tk.Radiobutton(self.root, var=self.option,text="student", value="student",
                                            font=("calabri", 18))
        self.student_radio.grid(column=2, row=9)
        self.root.mainloop()

    def login(self):
        autatiocation = Auth(self.username_entry.get(), self.password_entry.get())
        if autatiocation.logged_in:
            self.root.quit()

    def signup(self):
        print()
        autatiocation = Auth(self.username_entry.get(), self.password_entry.get(),self.option.get(), True)
        if autatiocation.signed_up:
            self.spacer1_label.config(text="you have signed up successfully")
            self.timer = threading.Timer(1.0, self.change)
            self.timer.start()
            # self.spacer1_label.config(text="")
        del autatiocation

    def change(self):
        self.spacer1_label.config(text="")
        self.timer.cancel()


class Home:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Home")


class User_interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("User interface")
        self.root.geometry("1200x900")
        self.root.mainloop()


scr = Log()
# user=User_interface()
