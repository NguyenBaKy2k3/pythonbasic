# 1
import math
print("Tọa độ của A: ")
a1 = int(input())
a2 = int(input())
print("Tọa độ của B: ")
b1 = int(input())
b2 = int(input())
print("Tọa độ của C: ")
c1 = int(input())
c2 = int(input())

def cau1():
    if((b1 - a1)/(c1 - a1) != (b2 - a2)/(c2 - a2)):
        print("Tọa độ của 3 đỉnh tạo thành 1 tam giác")
    if((b1 - a1)/(c1 - a1) == (b2 - a2)/(c2 - a2)):
        print("Tọa độ của 3 đỉnh không tạo thành 1 tam giác")

def _():
    if((b1 - a1)/(c1 - a1) != (b2 - a2)/(c2 - a2)):
        # Câu 2
        AB = math.sqrt(math.pow((b1 - a1), 2) + math.pow((b2 - a2), 2))
        BC = math.sqrt(math.pow((c1 - b2), 2) + math.pow((c2 - b2), 2))
        AC = math.sqrt(math.pow((c1 - a1), 2) + math.pow((c2 - a2), 2))
        print("Độ dài AB:", AB)
        print("Độ dài BC:", BC)
        print("Độ dài AC:", AC)
        ABC = math.degrees(math.acos(((a1 - b1)*(c1 - b1) + (a2 - b2)*(c2 - b2))/(math.sqrt(math.pow((a1 - b1), 2) + math.pow((a2 - b2), 2)) * math.sqrt(math.pow((c1 - b1), 2) + math.pow((c2 - b2), 2)))))
        ACB = math.degrees(math.acos(((a1 - c1)*(b1 - c1) + (a2 - c2)*(b2 - c2))/(math.sqrt(math.pow((a1 - c1), 2) + math.pow((a2 - c2), 2)) * math.sqrt(math.pow((b1 - c1), 2) + math.pow((b2 - c2), 2)))))
        BAC = math.degrees(math.acos(((b1 - a1)*(c1 - a1) + (b2 - a2)*(c2 - a2))/(math.sqrt(math.pow((b1 - a1), 2) + math.pow((b2 - a2), 2)) * math.sqrt(math.pow((c1 - a1), 2) + math.pow((c2 - a2), 2)))))
        print("Góc ABC: ", ABC)
        print("Góc ACB: ", ACB)
        print("Góc BAC: ", BAC)

        # Câu 3
        if(AB == BC):
            print("Tam giác cân tại B")
            if(ABC == 90 or ACB == 45 or BAC == 45):
                print("và vuông tại B")
        elif(AB == AC):
            print("Tam giác cân tại A")
            if(BAC == 90 or ACB == 45 or ABC == 45):
                print("và vuông tại A")
        elif(AC == BC):
            print("Tam giác cân tại C")
            if(ACB == 90 or ABC == 45 or BAC == 45):
                print("và vuông tại C")
        elif(AC == AB and AC == BC):
            print("Tam giác đều")
        elif(ABC == 90 or ACB == 90 or BAC == 90):
            print("Tam giác vuông")
        else:
            print("Tam giác thường")

        # Câu 4
        x = (AC + AC + BC)/2
        s = math.sqrt(x * (x - AC) * (x - AC) * (x - BC))
        print("Diện tích tam giác:", s)

        # Câu 5
        Ha = 2*s/BC
        Hb = 2*s/AC
        Hc = 2*s/AB
        print("Đường cao hạ từ A", Ha)
        print("Đường cao hạ từ B", Hb)
        print("Đường cao hạ từ C", Hc)

        # Câu 6
        TTab = math.sqrt(((math.pow(AC, 2) + math.pow(BC, 2))/2) - (math.pow(AB, 2)/4))
        TTac = math.sqrt(((math.pow(AB, 2) + math.pow(BC, 2))/2) - (math.pow(AC, 2)/4))
        TTbc = math.sqrt(((math.pow(AC, 2) + math.pow(AB, 2))/2) - (math.pow(BC, 2)/4))
        print("Trung tuyến của AB: ", TTab)
        print("Trung tuyến của AC: ", TTac)
        print("Trung tuyến của BC: ", TTbc)

        # Câu 7 
            # Trọng tâm 
        xg = (a1 + b1 + c1)/3
        yg = (a2 + b2 + c2)/3
        print("Trọng tâm G của tam giác có tọa độ: G(" + str(xg) + "," + str(yg))
            # Trực tâm 

print(cau1())
print(_())