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
"""

# 36
n = int(input())
sum = 0 
for i in range(1, n+1):
    sum += i/(i+1)
print(round(sum, 2))