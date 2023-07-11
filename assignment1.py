# 1
import math
print("Coordinates of A: ")
a1, a2 = map(int,input().split())
print("Coordinates of B: ")
b1, b2 = map(int,input().split())
print("Coordinates of C: ")
c1, c2 = map(int,input().split())

class assignment:
    def __init__(self, a1, a2, b1, b2, c1, c2):
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2
        self.c1 = c1
        self.c2 = c2
    
    # Xét điều kiện
    def question_one(self):
        if((self.b1 - self.a1)/(self.c1 - self.a1) != (self.b2 - self.a2)/(self.c2 - self.a2)):
            print("Coordinates of 3 vertices forming a triangle")
        if((self.b1 -self.a1)/(self.c1 - self.a1) == (self.b2 - self.a2)/(self.c2 - self.a2)):
            print("The coordinates of the 3 vertices do not form a triangle")

    # Độ dài, góc
    def question_two(self):
        if((self.b1 - self.a1)/(self.c1 - self.a1) != (self.b2 - self.a2)/(self.c2 - self.a2)):
            AB = math.sqrt(math.pow((self.b1 - self.a1), 2) + math.pow((self.b2 - self.a2), 2))
            BC = math.sqrt(math.pow((self.c1 - self.b2), 2) + math.pow((self.c2 - self.b2), 2))
            AC = math.sqrt(math.pow((self.c1 - self.a1), 2) + math.pow((self.c2 - self.a2), 2))
            print("Length AB:", AB)
            print("Length BC:", BC)
            print("Length AC:", AC)
            ABC = math.degrees(math.acos(((self.a1 - self.b1)*(self.c1 - self.b1) + (self.a2 - self.b2)*(self.c2 - self.b2))/(math.sqrt(math.pow((self.a1 - self.b1), 2) + math.pow((self.a2 - self.b2), 2)) * math.sqrt(math.pow((self.c1 - self.b1), 2) + math.pow((self.c2 - self.b2), 2)))))
            ACB = math.degrees(math.acos(((self.a1 - self.c1)*(self.b1 - self.c1) + (self.a2 - self.c2)*(self.b2 - self.c2))/(math.sqrt(math.pow((self.a1 - self.c1), 2) + math.pow((self.a2 - self.c2), 2)) * math.sqrt(math.pow((self.b1 - self.c1), 2) + math.pow((self.b2 - self.c2), 2)))))
            BAC = math.degrees(math.acos(((self.b1 - self.a1)*(self.c1 - self.a1) + (self.b2 - self.a2)*(self.c2 - self.a2))/(math.sqrt(math.pow((self.b1 - self.a1), 2) + math.pow((self.b2 - self.a2), 2)) * math.sqrt(math.pow((self.c1 - self.a1), 2) + math.pow((self.c2 - self.a2), 2)))))
            print("Angle ABC: ", ABC)
            print("Angle ACB: ", ACB)
            print("Angle BAC: ", BAC)

    # Xét tam giác
    def question_three(self):
        if((self.b1 - self.a1)/(self.c1 - self.a1) != (self.b2 - self.a2)/(self.c2 - self.a2)):
            AB = math.sqrt(math.pow((self.b1 - self.a1), 2) + math.pow((self.b2 - self.a2), 2))
            BC = math.sqrt(math.pow((self.c1 - self.b2), 2) + math.pow((self.c2 - self.b2), 2))
            AC = math.sqrt(math.pow((self.c1 - self.a1), 2) + math.pow((self.c2 - self.a2), 2))
            ABC = math.degrees(math.acos(((self.a1 - self.b1)*(self.c1 - self.b1) + (self.a2 - self.b2)*(self.c2 - self.b2))/(math.sqrt(math.pow((self.a1 - self.b1), 2) + math.pow((self.a2 - self.b2), 2)) * math.sqrt(math.pow((self.c1 - self.b1), 2) + math.pow((self.c2 - self.b2), 2)))))
            ACB = math.degrees(math.acos(((self.a1 - self.c1)*(self.b1 - self.c1) + (self.a2 - self.c2)*(self.b2 - self.c2))/(math.sqrt(math.pow((self.a1 - self.c1), 2) + math.pow((self.a2 - self.c2), 2)) * math.sqrt(math.pow((self.b1 - self.c1), 2) + math.pow((self.b2 - self.c2), 2)))))
            BAC = math.degrees(math.acos(((self.b1 - self.a1)*(self.c1 - self.a1) + (self.b2 - self.a2)*(self.c2 - self.a2))/(math.sqrt(math.pow((self.b1 - self.a1), 2) + math.pow((self.b2 - self.a2), 2)) * math.sqrt(math.pow((self.c1 - self.a1), 2) + math.pow((self.c2 - self.a2), 2)))))
            if(AB == BC):
                print("Isosceles triangle at B")
                if(ABC == 90 or ACB == 45 or BAC == 45):
                    print("and square at B")
            elif(AB == AC):
                print("Isosceles triangle at A")
                if(BAC == 90 or ACB == 45 or ABC == 45):
                    print("and square at A")
            elif(AC == BC):
                print("Isosceles triangle at C")
                if(ACB == 90 or ABC == 45 or BAC == 45):
                    print("and square at C")
            elif(AC == AB and AC == BC):
                print("Equilateral triangle")
            elif(ABC == 90 or ACB == 90 or BAC == 90):
                print("Right triangle")
            else:
                print("Normal triangle")

    # Diện tích
    def question_four(self):
        if((self.b1 - self.a1)/(self.c1 - self.a1) != (self.b2 - self.a2)/(self.c2 - self.a2)):
            AB = math.sqrt(math.pow((self.b1 - self.a1), 2) + math.pow((self.b2 - self.a2), 2))
            BC = math.sqrt(math.pow((self.c1 - self.b2), 2) + math.pow((self.c2 - self.b2), 2))
            AC = math.sqrt(math.pow((self.c1 - self.a1), 2) + math.pow((self.c2 - self.a2), 2))
            x = (AB + AC + BC)/2
            s = math.sqrt(x * (x - AB) * (x - AC) * (x - BC))
            print("Triangle area:", s)

    # Đường cao
    def question_five(self):
        if((self.b1 - self.a1)/(self.c1 - self.a1) != (self.b2 - self.a2)/(self.c2 - self.a2)):
            AB = math.sqrt(math.pow((self.b1 - self.a1), 2) + math.pow((self.b2 - self.a2), 2))
            BC = math.sqrt(math.pow((self.c1 - self.b2), 2) + math.pow((self.c2 - self.b2), 2))
            AC = math.sqrt(math.pow((self.c1 - self.a1), 2) + math.pow((self.c2 - self.a2), 2))
            x = (AB + AC + BC)/2
            s = math.sqrt(x * (x - AB) * (x - AC) * (x - BC))
            Ha = 2*s/BC
            Hb = 2*s/AC
            Hc = 2*s/AB
            print("Altitude from A", Ha)
            print("Altitude from B", Hb)
            print("Altitude from C", Hc)

    # Trung tuyến
    def question_six(self):
        if((self.b1 - self.a1)/(self.c1 - self.a1) != (self.b2 - self.a2)/(self.c2 - self.a2)):
            AB = math.sqrt(math.pow((self.b1 - self.a1), 2) + math.pow((self.b2 - self.a2), 2))
            BC = math.sqrt(math.pow((self.c1 - self.b2), 2) + math.pow((self.c2 - self.b2), 2))
            AC = math.sqrt(math.pow((self.c1 - self.a1), 2) + math.pow((self.c2 - self.a2), 2))
            TTab = math.sqrt(((math.pow(AC, 2) + math.pow(BC, 2))/2) - (math.pow(AB, 2)/4))
            TTac = math.sqrt(((math.pow(AB, 2) + math.pow(BC, 2))/2) - (math.pow(AC, 2)/4))
            TTbc = math.sqrt(((math.pow(AC, 2) + math.pow(AB, 2))/2) - (math.pow(BC, 2)/4))
            print("Midline of AB: ", TTab)
            print("Midline of AC: ", TTac)
            print("Midline of BC: ", TTbc)

    # Trọng tâm 
    def question_seven(self):
        if((self.b1 - self.a1)/(self.c1 - self.a1) != (self.b2 - self.a2)/(self.c2 - self.a2)):
            xg = (self.a1 + self.b1 + self.c1)/3
            yg = (self.a2 + self.b2 + self.c2)/3
            print("The centroid G of the triangle has coordinates: G(" + str(xg) + "," + str(yg))

    # Trực tâm
    def question_eight(self):
        D = (self.c1 - self.b1) * (self.c2 - self.a2) - (self.c1 - self.a1) * (self.c2 - self.b2)
        Dx = (self.a1 * (self.c1 - self.b1) + self.a2 * (self.c2 - self.b2)) * (self.c2 - self.a2) - (self.b1 * (self.c1 - self.a1) + self.b2 * (self.c2 - self.a2)) * (self.c2 - self.b2)
        Dy = (self.c1 - self.b1) * (self.b1 * (self.c1 - self.a1) + self.b2 * (self.c2 - self.a2)) - (self.c1 - self.a1) * (self.a1 * (self.c1 - self.b1) + self.a2 * (self.c2 - self.b2))
        if (D != 0):
            x = round(Dx/D, 2)
            y = round(Dy/D, 2)
            print("Orthocenter of a triangle with coordinates H(" + str(int(x)) + "," + str(int(y)) + ")")
        else:
            print("Not available")


assignment(a1, a2, b1, b2, c1, c2).question_eight()


