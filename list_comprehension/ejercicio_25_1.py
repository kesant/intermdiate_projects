numbers=[1,1,2,3,5,8,13,21,34,55]
squared_numbers=[ pow(number,2) for number in numbers]
result=[number for number in numbers if number%2==0]
with open("file1.txt") as file:
    content_1=file.readlines()
    print(content_1)
print(squared_numbers)
print(result)