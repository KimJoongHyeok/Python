N = int(input())

cnt = 0

while True:
    X = ((N % 10) * 10) + ((((N % 10) + (N // 10)) % 10))
    cnt += 1
    if X == N:
        break
print(cnt)
