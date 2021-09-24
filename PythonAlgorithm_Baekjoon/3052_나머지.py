"""
list = []
for i in range(10):
    a = int(input()) % 42
    list.append(a)

cnt = 0
for i in range(9):
    if(list[i] != list[i+1]):
        cnt += 1
print(cnt)
"""

a=set()
for i in range(10):
    a.add(int(input())%42)
print(len(a))