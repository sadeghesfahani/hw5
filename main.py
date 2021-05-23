import threading
import time
import tkinter as tk
from users.auth import *
from users.user import *


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
        self.welcome_label = tk.Label(self.root, text="Welcome to our institute", font=("calabri", 18))
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
        self.teacher_radio = tk.Radiobutton(self.root, var=self.option, text="teacher", value="teacher",
                                            font=("calabri", 18))
        self.teacher_radio.grid(column=1, row=9)
        self.student_radio = tk.Radiobutton(self.root, var=self.option, text="student", value="student",
                                            font=("calabri", 18))
        self.student_radio.grid(column=2, row=9)
        self.root.mainloop()

    def login(self):
        user = User(self.username_entry.get(), self.password_entry.get())
        user.log_in()
        # autatiocation = Auth()
        if user.is_login:
            self.root.forget(self.root)
            user_interface = UserInterface(user)
            # self.root.quit()
        else:
            self.spacer1_label.config(text="User of password wrong")
            self.timer = threading.Timer(1.0, self.change)
            self.timer.start()

    def signup(self):
        user = User(self.username_entry.get(), self.password_entry.get(), self.option.get())
        # autatiocation = Auth(self.username_entry.get(), self.password_entry.get(), self.option.get(), True)
        user.register()
        if user.is_registered:
            self.spacer1_label.config(text="you have signed up successfully")
            self.timer = threading.Timer(1.0, self.change)
            self.timer.start()
            user_info = UserInfo(user)

    def change(self):
        self.spacer1_label.config(text="")
        self.timer.cancel()
        del self.timer


class UserInfo:
    def __init__(self, user):
        self.root = tk.Tk()
        self.first_name = str()
        self.last_name = str()
        self.email = str()
        self.user = user
        self.root.title("more information")
        self.first_name_label = tk.Label(self.root, text="First_name: ", font=("calabri", 18), height=4).grid(column=1,
                                                                                                              row=1)
        self.first_name_entry = tk.Entry(self.root, textvariable=self.first_name, width=15, font=("calabri", 18))
        self.first_name_entry.grid(column=2, row=1)
        self.last_name_label = tk.Label(self.root, text="Last_name: ", font=("calabri", 18), height=4).grid(column=1,
                                                                                                            row=2)
        self.last_name_entry = tk.Entry(self.root, textvariable=self.last_name, width=15, font=("calabri", 18))
        self.last_name_entry.grid(column=2, row=2)
        self.email_label = tk.Label(self.root, text="Email: ", font=("calabri", 18), height=4).grid(column=1,
                                                                                                    row=3)
        self.email_entry = tk.Entry(self.root, textvariable=self.email, width=15, font=("calabri", 18))
        self.email_entry.grid(column=2, row=3)
        self.save = tk.Button(self.root, text="save", command=lambda: self.save_user()).grid(column=1, row=4,
                                                                                             columnspan=2)

    def save_user(self):
        #todo: check input and raise appropriate errors
        print("hi hi")
        print(self.first_name_entry.get())
        print(self.last_name_entry.get())
        print(self.email_entry.get())
        self.user.save_initial_data(self.first_name_entry.get(), self.last_name_entry.get(), self.email_entry.get())
        self.root.quit()


class UserInterface:
    def __init__(self, user):
        self.user = user
        self.root = tk.Tk()
        self.root.title("User interface")
        self.root.geometry("1100x800")
        self.add = tk.Button(self.root, text="add").pack()
        self.remove = tk.Button(self.root, text="remove").pack()
        self.modify = tk.Button(self.root, text="modify").pack()
        self.name = tk.Label(self.root, text=self.user.username).pack()
        self.root.mainloop()


scr = Log()
# user=User_interface()
