from circle import *

num1 = eval(input("원의 반지름을 입력하시오:"))
num2,num3 = eval(input("삼각형의 높이와 밑변을 입력하시오:"))
num4 = eval(input("사각형 한변의 길이를 입력하시오:"))


circle = Circle(num1)
triangle = Triangle(num2,num3)
squre = Square(num4)
print("원의 둘레는", format(circle.getLength()," .4f"),  "원의 면적은", format(circle.getArea(), " .4f"))
print("삼각형의 둘레는", format(triangle.getLength()," .4f"),  "삼각형의 면적은", format(triangle.getArea(), " .4f"))
print("사각형의 둘레는", format(squre.getLength()," .4f"),  "사각형의 면적은", format(squre.getArea(), " .4f"))
