student = [[5,4,8,4,5],[7,8,4,3,2],[9,9,8,3,3],[9,3,4,7,8],[3,3,6,9,6],[4,3,8,6,8],[9,3,5,9,2]]

Sum = [sum(student[0]),sum(student[1]),sum(student[2]),sum(student[3]),sum(student[4]),sum(student[5]),sum(student[6])]
studentnum = [2,3,5,6,4,0,1]
k = [] + Sum
k.sort()


for i in range(7):
    print("학생 "  + str(studentnum[i]) + "의 총점은",k[6-i])




