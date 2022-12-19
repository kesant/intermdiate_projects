sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below
#EXERCISE 1
# list_words=sentence.split(" ")
#
# new_dict={word:len(word) for word in list_words }
# print(new_dict)
#EXERCISE 2
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# new_dict={day:((temperture * 9/5) + 32) for (day, temperture) in weather_c.items()}
# print( new_dict)
#EXERCISE 3
import pandas
student_dict={

"student":["Angela","James","Lily"],
"score":[56,76,98]
}
student_data_frame=pandas.DataFrame(student_dict)
print(student_data_frame)
for (index,row) in student_data_frame.iterrows():
	print(row)