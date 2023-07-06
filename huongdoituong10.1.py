class Student:
    def __init__(self, name, avgsubject):
        self.name = name
        self.avgsubject = avgsubject

    def overall(self):
        print("Total average score of {} :".format(self.name)+str(sum(self.avgsubject)/len(self.avgsubject)))

name = str(input("Student name: "))
avgsubject = list(map(float, input("Average of subject: ").split()))
Student(name, avgsubject).overall()