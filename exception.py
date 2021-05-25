import time


class UserException(Exception):
    def __init__(self, text):
        self.text = text
        with open("log.txt", "a") as file:
            file.write(f"{self.text} --> {time.time()}\n")


class UserAlreadyExist(UserException):
    pass


class PasswordTooShort(UserException):
    pass

class UserAndPassNotMatch(UserException):
    pass