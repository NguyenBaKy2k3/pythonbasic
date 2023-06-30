class Student():
    def __init__(x, name, avg):
        x.name = name
        x.avg = avg
    
    def print_diemtk(x):
        print("Điểm tổng kết của {} :".format(x.name)+str(sum(x.avg)/len(avg)))

name = str(input("Student name: "))
avg = list(map(float, input("Điểm trung bình môn: ").split()))
Student(name, avg).print_diemtk()