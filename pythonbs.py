"""
# 1
print("Hello, World!")

# 2
print("Welcome to Codelearn.io!")

# 3
print(3273+2282)

# 4
print("2468 + 1234 = ", 2468 + 1234)
print("2468 - 1234 = ", 2468 - 1234)
print("2468 * 1234 = ", 2468 * 1234)
print("2468 / 1234 = ", 2468 / 1234)

# 5
print("Area = ", 7.8 * 6.4)
print("Perimeter = ", (7.8 + 6.4)*2)

# 8
i = 5000
f = 1.2345
t = 'Codelearn.io'
b = False
print(i, f, t, b)

# 9
name = "Codelearn"
print("Hello " + name)

# 10 
name = "Codelearn"
date_of_birth = 2019
print("Name: " + name)
print("Date of birth: " + str(date_of_birth))

# 11
a = 438
b = 636
print("a + b = " + str(a+b))
print("a - b = " + str(a-b))
print("a * b = " + str(a*b))
print("a / b = " + str(a/b))

# 12
length = 7.8
width = 3.5
print("Area = " + str(length*width))
print("Perimeter = ", str((length+width)*2))

# 13
name = str(input())
print("Hello " + name)

# 14
name = str(input())
age = int(input())
print("In 15 years, age of " + name + " will be " + str(age))

# 15
print("Nhap a: ")
a = int(input())
print("Nhap b: ")
b = int(input())
print("a%b = " + str(a%b))

# 16
print("Nhap a: ")
a = int(input())
print("Nhap b: ")
b = int(input())
print("a + b = " + str(a + b))
print("a - b = " + str(a - b))
print("a * b = " + str(a * b))
print("a / b = " + str(a / b))
print("a % b = " + str(a % b))

# 17
print("Nhap a: ")
a = int(input())
print("Nhap b: ")
b = int(input())
c = a
a = b 
b = c
print(a, b)

# 18
print("Nhap ban binh r cua duong tron: ")
r = float(input())
print("Circumference = " + str(2 * 3.14 * r))

# 19
a = int(input())
h = int(input())
s = 1/2 * a * h
print("Dien tich tam giac: ", s)

# 21
x = int(input())
y = int(input())
print("x > y: ", x > y)

# 22
a = int(input())
Total = int(input())
Total += a
print("Total + a:", Total)
Total -= a 
print("Total - a:", Total)
Total *= a 
print("Total * a:", Total)
Total //= a
print("Total // a:", Total)
Total **= a 
print("Total ** a:", Total)
Total /= a 
print("Total / a:", Total)
Total %= a
print("Total % a:", Total)

# 23
x = str(input())
print('H' in x)

# 24
a = int(input())
b = int(input())
print(a == b)

# 25
x = int(input())
y = int(input())
z = int(input())
t = int(input())
print("Result evaluation is", x>y and z<t)

# 26
age = int(input())
if(age < 5):
    print("Your cat is young")
else:
    print("Your cat is old")

# 27
temperature = int(input())
if(temperature >= 100):
    print("Stay at home and enjoy a good movie")
elif(temperature >= 92):
    print("Stay at home")
elif(temperature == 75):
    print("Go outside and enjoy the weather")
elif(temperature < 0):
    print("It's cool outside")
else:
    print("Let's go to school")

# 28
x = int(input())
y = int(input())
z = int(input())
if(x % 2 == 0):
    if(y >= 20):
        print("y is greater than or equal to 20")
    else:
        print("y is less than 20")
if(x % 2 != 0):
    if(z >= 30):
        print("y is greater than or equal to 30")
    else:
        print("y is less than 30")

# 29
a = int(input())
b = int(input())
c = int(input())
avg = (a+b+c)/3
if(avg > a and avg > b):
    print("The average value is greater than both a and b")
elif(avg > a and avg > c):
    print("The average value is greater than both a and c")
elif(avg > b and avg > c):
    print("The average value is greater than both b and c")
elif(avg > a):
    print("The average value is greater than a")
elif(avg > b):
    print("The average value is greater than b")
elif(avg > c):
    print("The average value is greater than c")

# 30
age = int(input())
if(age <= 0):
    print("This can hardly be true")
elif(age == 1):
    print("About 1 human year")
elif(age == 2):
    print("About 2 human years")
elif(age > 2):
    print("Over 5 human years")

# 31
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

# 32
a = int(input())
b = int(input())
sum = 0
for i in range(a, b+1):
    if(i % 2 != 0):
        sum += i
print(sum)

# 33
s = input()
for c in s:
    if c == 'y':
        continue
    print("Current character:", c)

# 34
a = int(input())
for i in range(1, 6):   
    print(a, "*", i, "=", a*i)

# 35
print("Nhap a: ")
a = int(input())
print("Nhap b: ")
b = int(input())
couteven = 0
coutodd = 0
for i in range(a, b):
    if(i % 2 == 0):
        couteven += 1
    else:
        coutodd += 1
print("Even: " + str(couteven))
print("Odd: " + str(coutodd))

# 36
n = int(input())
sum = 0 
for i in range(1, n+1):
    sum += i/(i+1)
print(round(sum, 2))

# String
s = str(input("Nhập chuỗi: "))
# Chữ hoa
print(s.upper())
# Chữ thường
print(s.lower())
# Kiểm tra string có kí tự chữ và số hay k. Có trả True >< False
print(s.isalnum())
# Kiểm tra string có chứa toàn các ký tự chữ không
print(s.isalpha())
# Kiểm tra string có chứa toàn các ký tự số không
print(s.isnumeric())
# Nối 
print("?".join(s))
# Loại bỏ các khoảng trắng thừa trong chuỗi
print(" ".join(s.split()))
# Thay thế các chuỗi tìm thấy thành chuỗi mới
print(s.replace("Kỳ", "Phước"))

# 43
s = input("Nhập chuỗi: ")
if (len(s)<2):
    print("")
else:
    print(s[0:2]+s[-2:])

# 44
s1 = input("Nhập chuỗi S1: ")
s2 = input("Nhập chuỗi S2: ")
x = s1[0:2] + s2[2:]
s1 = s2[0:2] + s1[2:]
s2 = x
print(s1 + " " + s2)

# 45
s = input("Nhập chuỗi: ").split()
print(" ".join(reversed(s)))

# 37, 38 , 39, 40
lst = []
sum = 0
n = int(input("Số phần tử: "))
for i in range(n):
    lst.append(int(input("lst["+str(i)+"]= ")))
    sum += lst[i]
print(min(lst))
print("Tổng các phần tử trong list:", sum)
lst.sort()
print(lst)
le = []
for i in lst:
    if (i % 2 != 0):
        le.append(i)
print(le)
l = []
for i in lst:
    if (i % 5 == 0):
        l.append(i)
if(len(l) == 0):
    l = [0]
print(l)


# 46
n = int(input("Số phần tử trong mảng: "))
l = []
def sum(l):
    s = 0 
    for i in l:
        s += i
    return s 

for i in range(n):
    l.append(int(input("l[" + str(i) + "]= ")))
print(sum(l))


# 47 
a, b, c = map(int, input("Nhập: ").split())
def maxx(a,b,c):
    if a>b and a>c:
        return a
    if b>c:
        return b
    else:
        return c
    
print(maxx(a,b,c))


# 48
s = str(input("Chuỗi s: ")) 
def c(s):
    countupper = 0
    countlower = 0
    for i in s:
        if i.isupper():
            countupper += 1
        if i.islower():
            countlower += 1
    print("Chuỗi S: ", s)
    print("Số chữ cái in hoa: ", countupper)
    print("Số chữ cái in thường", countlower)
print(c(s))

# 49
n = int(input("Số phần tử trong mảng: "))
l = []
def c(l):
    a = []
    for i in l:
        if i not in a:
            a.append(i)
    print(a)
for i in range(n):
    l.append(int(input("l[" + str(i) + "]= ")))

print(c(l))


# 50 
n = int(input("Nhập số: "))
def ktr(n):
    count = 0
    for i in range(1, n+1):
        if(n % i == 0 ):
            count += 1
    if count == 2:
        print("n là số nguyên tố.")
    else:
        print("n không là số nguyên tố.")
print(ktr(n))
"""