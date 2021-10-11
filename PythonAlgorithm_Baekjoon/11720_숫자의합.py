a = int(input())
b = int(input())

num = list(map(int,str(b)))
sum=0
for i in num:
    sum += i
print(sum)    