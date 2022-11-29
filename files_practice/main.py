
#read a file
# with open("my_file.txt") as file:
#     content=file.read()
#     print(content)

#write  a file
#when we use the mode w and the name of the funtion doesn't exist python will
#create the funtion by default
# with open("my_file.txt",mode="w") as file:
# #we change the mode to w to be able to write in the text ,
# #otherwise if we dont specify a mode it will be reading as default.
# 		  file.write("new text ")

#add informatio to the file
with open("my_file.txt",mode="a") as file:
#changing the mode to a its that we are going to add new information
#to the file
		  file.write("\n new text ")
