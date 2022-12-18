numbers=[1,1,2,3,5,8,13,21,34,55]
squared_numbers=[ pow(number,2) for number in numbers]
import numpy
import  pandas
#result=[number for number in numbers if number%2==0]
with open("file1.txt") as file:
    content_1=file.readlines()
    content_1=[int(num.strip('\n')) for num in content_1]
    print(content_1)
with open("file2.txt") as file:
    content_2=file.readlines()
    content_2=[int(num.strip('\n')) for num in content_2]
    print(content_2)
result=[ num2 for num in content_1 for num2 in content_2 if num2==num ]
print(squared_numbers)
print(pandas.unique(result))