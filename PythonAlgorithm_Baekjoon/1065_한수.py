a = int(input())

cnt = 0
for i in range(1,a+1):
    if(i<100):
        cnt += 1
    else:   
        #if((i//100)-((i//10)%10) == ((i//10)%10) - (i % 10)):
        #    cnt += 1
        num = list(map(int,str(i)))
        if(num[0] - num[1] == num[1] - num[2]):
            cnt +=1

print(cnt)            

        
