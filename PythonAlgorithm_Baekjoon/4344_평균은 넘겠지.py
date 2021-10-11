C = int(input())

for i in range(C):
    A = list(map(int,input().split()))
    avg = sum(A[1:]) / A[0]
    cnt = 0
    for j in A[1:]:
        if(j > avg):
            cnt += 1
    answer = cnt / A[0] * 100
    print(f'{answer:.3f}%')  