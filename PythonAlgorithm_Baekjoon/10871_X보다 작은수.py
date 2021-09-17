N,X = map(int,input().split())
A = list(map(int, input().split()))

for j in range(N):
   if(A[j] < X):
       print(A[j],end=" ")
