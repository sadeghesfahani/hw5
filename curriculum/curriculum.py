import os


class Curriculum:
    def __init__(self, name=None, level=None, ID=None, teachers=None, students=None, capacity=None, time=None):
        self.ID = ID
        self.teachers = teachers
        self.students = students
        self.name = name
        self.capacity = capacity
        self.time = time
        self.level = level

    def load_all_classes(self):
        list_of_classes=list()
        all_files=os.listdir("curriculum/")
        all_txt_files=[file for file in all_files if ".txt" in file]
        print(all_txt_files)
        for file in all_txt_files:
            print(file[:len(file)-4])
            self.ID=file[:len(file)-4]
            self.load(self.ID)
            list_of_classes.append([self.ID,self.name,self.level,self.capacity])
        return list_of_classes
    def load(self,ID):
        with open(f"curriculum/{ID}.txt", "r") as file:
            class_data = file.readlines()

            self.level = class_data[1].split("=")[1].strip()
            self.name = class_data[2].split("=")[1].strip()
            self.capacity = class_data[3].split("=")[1].strip()
            try:
                self.students = class_data[4].split("=")[1].strip().split(",")
            except:
                self.students = None
            try:
                self.teachers = class_data[5].split("=")[1].strip().split(",")
            except:
                self.teachers = None
            # (wed,10:30-12:00)(friday,12:00,13:30)
            times = class_data[6].split("=")[1].strip().split(")")
            time = [t[1:] for t in times]
            self.time = {t.split(",")[0]: t.split(",")[1:] for t in time if t!=""}


#cl = Curriculum(ID=1)
#cl.load_all_classes()
# cl.load()
# print(cl.ID)
# print(cl.name)
# print(cl.level)
# print(cl.students)
# print(cl.teachers)
# print(cl.time)

