import threading
import time
import os
from tkinter import ttk
import tkinter as tk

from PIL import ImageTk, Image
from PIL.ImageTk import PhotoImage

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
        self.root.title("Login")
        self.root.geometry("1100x800")
        # background image
        bg = PhotoImage(file="image/background.jpg")
        self.spacer1_label = tk.Label(self.root, text="", font=("calabri", 18), height=900, width=1200, image=bg)
        self.spacer1_label.grid(column=1, row=1, columnspan=2)
        # center page
        self.spacer2_label = tk.Label(self.root, text="", font=("calabri", 18), height=15, width=40, bg="alice blue")
        self.spacer2_label.place(x=250, y=150)

        self.welcome_label = tk.Label(self.root, text="User athentication", font=("calabri", 18), height=2, width=40,
                                      bg='tan1')
        self.welcome_label.place(x=250, y=150)

        self.spacer_label = tk.Label(self.root, text="", font=("calabri", 18), height=1, bg="white")
        self.spacer_label.place(x=400, y=535)

        # user and pass
        self.username_label = tk.Label(self.root, text="Username:", font=("calabri", 18), bg="alice blue")
        self.username_label.place(x=300, y=250)
        self.username_entry = tk.Entry(self.root, textvariable=self.username, width=15, font=("calabri", 20),
                                       bg="gray91")
        self.username_entry.place(x=500, y=250)

        self.password_label = tk.Label(self.root, text="Password:", font=("calabri", 18), bg="alice blue")
        self.password_label.place(x=300, y=325)

        self.password_entry = tk.Entry(self.root, textvariable=self.password, width=15, font=("calabri", 20),
                                       bg="gray91")
        self.password_entry.place(x=500, y=325)

        self.log_in_button = tk.Button(text="Log in!", height=2, width=25, command=lambda: self.login(), bg="cyan")
        self.log_in_button.place(x=300, y=475)
        self.register_button = tk.Button(text="Sign up!", height=2, width=25, command=lambda: self.signup(), bg="cyan")
        self.register_button.place(x=550, y=475)
        self.teacher_radio = tk.Radiobutton(self.root, var=self.option, text="Teacher", value="teacher",
                                            font=("calabri", 18), bg="white", activebackground="white")
        self.teacher_radio.place(x=550, y=400)
        self.student_radio = tk.Radiobutton(self.root, var=self.option, text="Student", value="student",
                                            font=("calabri", 18), bg="white", activebackground="white")
        self.student_radio.place(x=350, y=400)
        self.root.wm_attributes("-fullscreen")
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
            self.spacer_label.config(text="User of password wrong")
            self.timer = threading.Timer(1.0, self.change)
            self.timer.start()

    def signup(self):
        user = User(self.username_entry.get(), self.password_entry.get(), self.option.get())
        # autatiocation = Auth(self.username_entry.get(), self.password_entry.get(), self.option.get(), True)
        user.register()
        if user.is_registered:
            self.spacer_label.config(text="you have signed up successfully")
            self.timer = threading.Timer(1.0, self.change)
            self.timer.start()
            user_info = UserInfo(user)

    def change(self):
        self.spacer_label.config(text="")
        self.timer.cancel()
        del self.timer


class UserInfo:
    def __init__(self, user):
        self.root = tk.Tk()
        self.root.geometry("1100x900")
        self.first_name = str()
        self.last_name = str()
        self.email = str()
        self.user = user
        self.root.title("more information")
        self.root.config(background="white")
        # bg=ImageTk.PhotoImage(Image.open("image/background.jpg"))
        # bg = PhotoImage(file="image/background.jpg")
        bg = Image.open("image/avatar5.png")
        bg = bg.resize((250, 250), Image.ANTIALIAS)
        bg = ImageTk.PhotoImage(bg)
        # self.spacer1_label = tk.Label(self.root, text="", font=("calabri", 18), height=900, width=1200, image=bg)
        # self.spacer1_label.grid(column=1, row=1, columnspan=2)
        # self.image_canvas=tk.Canvas(self.root,image=bg)
        self.image_label = tk.Label(self.root, text="", height=300, width=300, image=bg, bg="white").place(x=10, y=10)
        self.first_name_label = tk.Label(self.root, text="First_name: ", font=("calabri", 18), height=4,
                                         bg="white").place(x=350,
                                                           y=10)
        self.first_name_entry = tk.Entry(self.root, textvariable=self.first_name, width=25, font=("calabri", 18))
        self.first_name_entry.place(x=550, y=50)
        self.last_name_label = tk.Label(self.root, text="Last_name: ", font=("calabri", 18), height=4,
                                        bg="white").place(x=350,
                                                          y=100)
        self.last_name_entry = tk.Entry(self.root, bg="white", textvariable=self.last_name, width=25,
                                        font=("calabri", 18))
        self.last_name_entry.place(x=550, y=140)
        self.email_label = tk.Label(self.root, text="Email: ", font=("calabri", 18), height=4, bg="white").place(x=350,
                                                                                                                 y=200)
        self.email_entry = tk.Entry(self.root, textvariable=self.email, width=25, font=("calabri", 18))
        self.email_entry.place(x=550, y=240)
        self.save = tk.Button(self.root, text="Save", command=lambda: self.save_user(), bg="cyan", width=25,
                              height=3).place(x=1000, y=50)
        self.picture = tk.Button(self.root, text="Avatar", command=lambda: self.save_user(), bg="cyan", width=25,
                                 height=3).place(x=1000, y=150)
        self.spacer = tk.Label(self.root, text="", font=("calabri", 18), height=1, width=900, bg="light gray").place(
            x=0,
            y=300)

        self.spacer = tk.Label(self.root, text="Available classes", font=("calabri", 18), height=1, width=40, bg="white").place(
            x=0,
            y=350)
        self.spacer = tk.Label(self.root, text="Your classes", font=("calabri", 18), height=1, width=40,
                               bg="white").place(
            x=675,
            y=350)
        # left tree view
        self.class_tree = ttk.Treeview(self.root)
        self.class_tree["columns"] = ("ID", "name", "level", "capacity")

        self.class_tree.column('#0', width=0, stretch=tk.NO)
        self.class_tree.column('ID', width=50, anchor=tk.CENTER)
        self.class_tree.column('name', width=170, anchor=tk.CENTER)
        self.class_tree.column('level', width=220, anchor=tk.CENTER)
        self.class_tree.column('capacity', width=90, anchor=tk.CENTER)
        # self.teachers_tree.column('classes', width=240, anchor=tk.CENTER)

        self.class_tree.heading('#0', text="", anchor=tk.W)
        self.class_tree.heading('ID', text="ID", anchor=tk.CENTER)
        self.class_tree.heading('name', text="Name", anchor=tk.CENTER)
        self.class_tree.heading('level', text="Level", anchor=tk.CENTER)
        self.class_tree.heading('capacity', text="Capacuty", anchor=tk.CENTER)
        self.class_tree.insert(parent='', index=1, iid=1, text='',
                               values=(1, 406, "lower intermediate", 8))
        self.class_tree.insert(parent='', index=2, iid=2, text='',
                               values=(2, 601, "higher intermediate", 5))
        self.class_tree.insert(parent='', index=3, iid=3, text='',
                               values=(3, "CPE", "Advance (C2)", 7))
        self.class_tree.place(x=30, y=400)
        # self.teachers_tree.heading('classes', text="Classes", anchor=tk.CENTER)

        # right
        self.profile_tree = ttk.Treeview(self.root)
        self.profile_tree["columns"] = ("ID", "name", "level", "capacity")

        self.profile_tree.column('#0', width=0, stretch=tk.NO)
        self.profile_tree.column('ID', width=50, anchor=tk.CENTER)
        self.profile_tree.column('name', width=170, anchor=tk.CENTER)
        self.profile_tree.column('level', width=220, anchor=tk.CENTER)
        self.profile_tree.column('capacity', width=90, anchor=tk.CENTER)
        # self.teachers_tree.column('classes', width=240, anchor=tk.CENTER)

        self.profile_tree.heading('#0', text="", anchor=tk.W)
        self.profile_tree.heading('ID', text="ID", anchor=tk.CENTER)
        self.profile_tree.heading('name', text="Name", anchor=tk.CENTER)
        self.profile_tree.heading('level', text="Level", anchor=tk.CENTER)
        self.profile_tree.heading('capacity', text="Capacuty", anchor=tk.CENTER)
        # self.profile_tree.insert(parent='', index=1, iid=1, text='',
        #                          values=(1, 406, "lower intermediate", 8))
        self.profile_tree.place(x=700, y=400)

        self.add_button = tk.Button(self.root, text="-->", width=12, command=lambda: self.add()).place(x=570, y=400)
        self.remove_button = tk.Button(self.root, text="Delete", width=12,command= lambda :self.remove()).place(x=570, y=440)
        self.info_button = tk.Button(self.root, text="Info", width=12).place(x=570, y=480)
        self.counter = 4
        self.root.mainloop()


    def remove(self):
        # print(self.class_tree.selection())
        get_tree_value = self.profile_tree.selection()
        class_tree_items = self.profile_tree.get_children()
        class_tree_items = self.class_tree.get_children()
        # print(profile_tree_items)
        # print(get_tree_value)
        if len(get_tree_value) >= 2:
            for item in get_tree_value:
                selected = self.profile_tree.item(item)['values']
                # print(selected)
                # print(self.profile_tree.item(item)['values'][0])
                # print(selected[0])
                # if self.profile_tree.exists()
                found = False
                for other_items in class_tree_items:
                    if self.class_tree.item(other_items)['values'][0] == selected[0]:
                        found = True
                if not found:
                    self.class_tree.insert(parent='', index=self.counter, iid=self.counter, text='',
                                             values=selected)
                    self.profile_tree.delete(item)
                    self.counter += 1
                    found = False
        elif len(get_tree_value) == 1:
            selected = self.profile_tree.item(get_tree_value)['values']
            # print(selected)
            found = False
            for other_items in class_tree_items:
                if self.class_tree.item(other_items)['values'][0] == selected[0]:
                    found = True
            if not found:
                self.class_tree.insert(parent='', index=self.counter, iid=self.counter, text='',
                                         values=selected)
                self.profile_tree.delete(get_tree_value)
                self.counter += 1
                found = False
            self.counter += 1
        # self.class_tree.delete(self.class_tree.selection())

    def add(self):
        # print(self.class_tree.selection())
        get_tree_value = self.class_tree.selection()
        class_tree_items = self.class_tree.get_children()
        profile_tree_items = self.profile_tree.get_children()
        #print(profile_tree_items)
        # print(get_tree_value)
        if len(get_tree_value) >= 2:
            for item in get_tree_value:
                selected = self.class_tree.item(item)['values']
                # print(selected)
                # print(self.profile_tree.item(item)['values'][0])
                # print(selected[0])
                # if self.profile_tree.exists()
                found = False
                for other_items in profile_tree_items:
                    if self.profile_tree.item(other_items)['values'][0] == selected[0]:
                        found = True
                if not found:
                    self.profile_tree.insert(parent='', index=self.counter, iid=self.counter, text='',
                                             values=selected)
                    self.class_tree.delete(item)
                    self.counter += 1
                    found = False
        elif len(get_tree_value) == 1:
            selected = self.class_tree.item(get_tree_value)['values']
            # print(selected)
            found = False
            for other_items in profile_tree_items:
                if self.profile_tree.item(other_items)['values'][0] == selected[0]:
                    found = True
            if not found:
                self.profile_tree.insert(parent='', index=self.counter, iid=self.counter, text='',
                                         values=selected)
                self.class_tree.delete(get_tree_value)
                self.counter += 1
                found = False
            self.counter += 1
        # self.class_tree.delete(self.class_tree.selection())

    def save_user(self):
        # todo: check input and raise appropriate errors
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
        self.teachers_tree = ttk.Treeview(self.root)
        self.teachers_tree["columns"] = ("name", "family", "email", "classes")

        self.teachers_tree.column('#0', width=0, stretch=tk.NO)
        self.teachers_tree.column('name', width=240, anchor=tk.CENTER)
        self.teachers_tree.column('family', width=240, anchor=tk.CENTER)
        self.teachers_tree.column('email', width=240, anchor=tk.CENTER)
        self.teachers_tree.column('classes', width=240, anchor=tk.CENTER)

        self.teachers_tree.heading('#0', text="", anchor=tk.CENTER)
        self.teachers_tree.heading('name', text="Name", anchor=tk.CENTER)
        self.teachers_tree.heading('family', text="Family", anchor=tk.CENTER)
        self.teachers_tree.heading('email', text="Email", anchor=tk.CENTER)
        self.teachers_tree.heading('classes', text="Classes", anchor=tk.CENTER)
        teacher_tree = self.teacher_tree()
        counter = 0
        for col_info in teacher_tree:
            self.teachers_tree.insert(parent='', index=counter, iid=counter, text='',
                                      values=(col_info[0], col_info[1], col_info[2], col_info[3]))
            counter += 1
        self.teachers_tree.grid(column=1, row=1, rowspan=4)
        self.add = tk.Button(self.root, text="add").grid(column=2, row=1)
        self.remove = tk.Button(self.root, text="remove").grid(column=2, row=2)
        self.modify = tk.Button(self.root, text="modify").grid(column=2, row=3)
        self.name = tk.Label(self.root, text=self.user.username).grid(column=2, row=4)
        self.root.mainloop()

    def teacher_tree(self):
        data_provider = list()
        with open("users/database.txt", "r") as file:
            data = file.readlines()
            teachers = [teacher.split(",")[0].strip() for teacher in data if teacher.split(",")[2].strip() == "teacher"]
            for teacher in teachers:
                dataloader = User(teacher, "nothing")
                dataloader.load_data()
                data_provider.append([dataloader.firt_name, dataloader.last_name, dataloader.email, dataloader.classes])
        return data_provider


user1asd = UserInfo(None)
# user1asd.root.mainloop()
# scr = Log()
# user=User_interface()
