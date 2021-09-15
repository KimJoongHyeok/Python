#행과 열별로 입력받고 넣기
matrix = [] # Create an empty list
numberOfRows = eval(input("Enter the number of rows: "))
numberOfColumns = eval(input("Enter the number of columns: "))

for row in range(0, numberOfRows): 
    matrix.append([]) # Add an empty new row 
    for column in range(0, numberOfColumns): 
        value = eval(input("Enter an element and press Enter: "))
        matrix[row].append(value) 

print(matrix)


#set
set2 = set([2,5,6,4,3,5,6,5,10,15,34]) # Create a set from a list
print(set2)
