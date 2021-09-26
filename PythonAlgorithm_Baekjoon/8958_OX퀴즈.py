a = int(input())

for i in range(a):
    answer = 0
    cnt = 0
    b = list(input())
    for j in range(len(b)):
        if(b[j]=='O'):
            cnt += 1
            answer += cnt
        else:
            cnt = 0    
    print(answer)
         