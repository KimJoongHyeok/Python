list = [0,0,0,0,0,0,0,0,0]
max = 0
maxNum = 0
for i in range(9):
   list[i] = int(input())
   if(max<list[i]):
       max = list[i]
       maxNum = i
print(max)
print(maxNum+1)
