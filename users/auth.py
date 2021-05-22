import hashlib


class Auth:
    def __init__(self, username, password,type=None, signup=False):
        self.username = username
        self.__password = Auth.make_hex(password)
        self.signup = signup
        self.type=type
        # try:
        with open("users/database.txt", "r") as file:
            self.database = file.readlines()
        # except:
        # print("opening databse")  # todo: make an approptiate error
        self.user_info = self.find_user_info()
        if self.user_info:
            self.__database_password = self.user_info.split(",")[1].strip()
            if self.authentication():
                self.logged_in = True
                print(True)
            else:
                self.logged_in = False
            self.signed_up = False
        elif not self.user_info and self.signup:
            try:
                with open("users/database.txt", "a") as file:
                    file.write(f"{self.username},{self.__password},{self.type}\n")
                    self.signed_up = True
            except:
                self.signed_up = False
        else:
            self.logged_in = False
            print(False)

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

# sina = Auth("sina", "haha")
# print(sina.logged_in)
