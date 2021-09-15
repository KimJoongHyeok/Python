

k = 1
list1 =[]
list2 =[]
while ( k != 0):
    list1.append(input("(입력모드)이름을 입력하시오: "))
    list2.append(input("전화번호를 입력하시오: "))
    if list1.append(""):
        t = input("(검색모드)이름을 입력하시오")
        if t in list1 == 1:
            s = list1.index(t)
            print(str(list1[s]) + " 의 전화번호는" + str(list2[s]) + " 입니다.")
        else:
            print(str(t) + " 의 이름과 전화번호가 등록되어 있지 않습니다.")
        if t == " ":
            k = 0




