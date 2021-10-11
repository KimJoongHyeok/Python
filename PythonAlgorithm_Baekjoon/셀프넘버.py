allNum = set(range(1,10001))
notSelfNum = set()

for i in allNum:
    for j in str(i):
        i += int(j)
    notSelfNum.add(i)

selfNum = sorted(allNum - notSelfNum)
for k in selfNum:
    print(k)    
