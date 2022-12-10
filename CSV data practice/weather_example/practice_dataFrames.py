import pandas
data= pandas.read_csv("weather_data.csv")
# # print(type(data))#it is a dataframe->represent a whole table
# # print(type(data["temp"]))#it is a series->represent a column
#
# #Pandas can also convert oour dataframes to other types as dictionaries
# data_dic=data.to_dict()#transforma nuestro dataframes into a dictionary
# print(data_dic)
#
# # we can also make use of pandas to convert series
# #for instance we can convert from a series data type into a list
# temp_list=data["temp"].tolist()
# temp_list_mean=data["temp"].mean()#the average of temperatures from our dataframe
# data["temp"].max()# we get the max value from tempeture series
#
# print(temp_list_mean)
# print(temp_list)
#
# #Get data in columns
# print(data["condition"])
# print(data.condition)#another way of calling columns is :

#Gest data in row

print(data[data.day=="Monday"])
temp_max=data[data.temp==data.temp.max()]
print(temp_max)
#getting a the value of a column from a row
monday =data[data.day=="Monday"]
print(monday.condition)
monday_temp=int(monday.temp)
monday_temp_f=monday_temp * 9/5 + 32
print(monday_temp_f)


#create a datafram from scratch


data_dict={
    "students":["amy","james","angela"],
    "scores":[76,56,65]
}
data2=pandas.DataFrame(data_dict)
data.to_csv("neew_data.csv")#create a csv from the data frame given a path