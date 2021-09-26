a = int(input())

b = list(map(int,input().split()))
max_num = max(b)    

answer = 0
for i in range(a):
    answer += b[i]/max_num * 100
print(answer/a)

