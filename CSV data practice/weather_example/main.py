# with open("weather_data.csv") as data_file:
#     data=data_file.readlines()
#     print(data)
"""
it will take a lot of work to extract each pice of data from this file 
so instead, we use a inbluid librerary of python that helps us to work
with csv.

"""
# import csv

# with open("weather_data.csv") as data_file:
#     # it akes the file and read it and output the data 
#     data=csv.reader(data_file)
#     temperatures=[]
#     #it create an csv.reader object that can be iterable to loop throught
#     for row in data :
#         if row[1]!= "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data=pandas.read_csv("weather_data.csv")
print(data)