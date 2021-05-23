class Curriculum:
    def __init__(self, ID=None, teachers=None, students=None, days=None, time=None):
        self.ID = ID
        self.teachers = teachers
        self.students = students
        self.days = days
        self.time = time
        self.data=None

    def load(self):
        with open("curriculum/database.txt","r") as file:
            data=file.readlines()
        for cl in data:
            if cl.split(",")[0]==self.Id:
                self.data=cl
        if self.data is not None:
            pass