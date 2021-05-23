import hashlib


class Authentication:
    def __init__(self, username, password, type=None, signup=False):
        self.username = username
        self.__password = Authentication.make_hex(password)
        self.signup = signup
        self.type = type
        # try:
        with open("users/database.txt", "r") as file:
            self.database = file.readlines()
        # except:
        # print("opening databse")  # todo: make an approptiate error
        self.user_info = self.find_user_info()
        if self.user_info:
            self.__database_password = self.user_info.split(",")[1].strip()
            if self.authentication():
                self.type = self.user_info.split(",")[2].strip()
                self.logged_in = True
                self.found = True
            else:
                self.logged_in = False
                self.found = True
            self.signed_up = False

    def find_user_info(self):
        user_line = None
        for line in self.database:
            if user_line is not None:
                break
            if self.username in line:
                index = line.index(self.username)
                if line[index + len(self.username)] == ",":
                    user_line = line

        return False if user_line is None else user_line

    @staticmethod
    def make_hex(text):
        return hashlib.sha256(str.encode(text)).hexdigest()

    def authentication(self):
        return True if self.__password == self.__database_password else False

    def register(self, user_type):
        try:
            with open("users/database.txt", "a") as file:
                file.write(f"{self.username},{self.__password},{user_type}\n")
                return True
        except:
            return False

# sina = Auth("sina", "haha")
# print(sina.logged_in)
