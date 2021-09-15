import random
dice = []
for i in range(5) :
    dice.append(random.randint(1,6))

#랜덤주사위 값
print(dice)

print(dice.count('1'))
print(dice.count('2'))
print(dice.count('3'))
print(dice.count('4'))
print(dice.count('5'))
print(dice.count('6'))

