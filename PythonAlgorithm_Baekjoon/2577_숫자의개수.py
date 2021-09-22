a = int(input())
b = int(input())
c = int(input())

x = a * b * c
list = []
while x > 0:
    list.append(x%10)
    x = x//10
num = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(list)):
    for j in range(10):
        if(list[i] == j):
            num[j] += 1
for k in range(10):
    print(num[k])

"""
a = int(input())
b = int(input())
c = int(input())
result = list(str(a * b * c))
for i in range(10):
print(result.count(str(i)))
"""
    
