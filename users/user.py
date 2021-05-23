# type=[teacher,manager,student]
from users.authentication import *


class User:
    def __init__(self, username, password, type=None):
        self.username = username
        self.__password = password
        self.type = type
        self.authentication = Authentication(self.username, self.__password)
        self.is_login = False
        self.is_registered = False
        self.classes = list()

    def log_in(self):
        if self.authentication.logged_in:
            self.type = self.authentication.type
            self.is_login = True

    def register(self):
        self.is_registered = self.authentication.register(self.type)

    def load_data(self):
        with open(f"users/user_info/{self.username}.txt", "r") as file:
            data = file.readlines()
        for dt in data:
            # if len(dt) == 2:
            first = dt.split("=")[0].strip()
            last = dt.split("=")[1].strip()
            if first == "first_name":
                self.firt_name = last
            elif first == "last_name":
                self.last_name = last
            elif first == "email":
                self.email = last
            elif first == "class" and last is not "":
                self.classes.append(last)
            # else:
            #     first = dt.split(",")[0].strip()
            #     if first == "class":
            #         for cl in dt.split(",")[1:].strip():
            #             self.classes.append(cl)

    def save_initial_data(self, first_name, last_name, email):
        with open(f"users/user_info/{self.username}.txt", "w") as file:
            file.write(f"first_name={first_name}\n")
            file.write(f"last_name={last_name}\n")
            file.write(f"email={email}\n")
