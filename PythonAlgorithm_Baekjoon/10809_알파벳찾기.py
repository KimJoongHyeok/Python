word = input()
alpha = list(range(97,123))

for i in alpha:
    print(word.find(chr(i)),end=" ")