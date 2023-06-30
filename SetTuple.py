# Set
"""
# 8.1
n = map(float, input().split())
a = set(n)
sum = 0
for i in a:
    sum += i
print(round(sum/len(a), 2))

# 8.2
a = set()
n = input().split()
for i in n:
    if i not in a:
        a.add(i)
print(len(a))

# 8.3
n = map(int, input().split())
a = set(n)
x = map(int, input("Số cần xóa: ").split())
for i in x:
    if i in a:
        a.remove(i)
print(sum(a))
"""



