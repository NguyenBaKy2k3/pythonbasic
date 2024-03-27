a = float(input("Nhập A: "))
b = float(input("Nhập B: "))

if(a != 0):
    print("Giá trị của X: ", -b/a)
else:
    if(b == 0):
        print("Phương trình vô số nghiệm!")
    else:
        print("Phương trình vô nghiệm!")
