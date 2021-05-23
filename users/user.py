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

    def log_in(self):
        if self.authentication.logged_in:
            self.type = self.authentication.type
            self.is_login = True

    def register(self):
        self.is_registered = self.authentication.register(self.type)
