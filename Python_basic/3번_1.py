d={1:"one",2:"two",3:"three",4:"four",5:"five"}


while True:
    
    choice = input("'a' to add word, 'l' to lookup table, 'q' to qutit: ")
    
    if(choice=='a'):
        result = input("'Type the word: ")
        if(result=='1'):
            print("one")
        elif(result=='2'):
            print("two")
        elif(result=='3'):
            print("three")
        elif(result=='4'):
            print("four")
        elif(result=='5'):
            print("five")
    elif (choice=='l'):
       print("사전에 없음")
    else:
       break;
       print("종료")
    
