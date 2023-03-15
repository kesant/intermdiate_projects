import pandas
import pandas as pd
import datetime as dt
import  random
import smtplib

#CONSTANTS
MY_EMAIL="dkasasfaskf"
MY_PASSWORD="asffasfsaas"

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
birthdays=pd.read_csv("./birthdays.csv")
birthdays=birthdays.drop(index=birthdays.iloc[1].name)

dict={"name":["carlos","kevin"],
      "email":["ajdajksda@hotmail.com","kejsadas@hotmail.com"],
      "year":[2000,2000],
      "month":[5,3],
      "day":[21,11]}

birthdays.loc[1]=["carlos","ajdajksda@hotmail.com",2000,5,21]
birthdays.loc[2]=["kevin","kejsadas@hotmail.com",2000,3,14]
print(birthdays)


# 2. Check if today matches a birthday in the birthdays.csv
now=dt.datetime.now()
month=now.month
day=now.day
Cumleanero=birthdays[(birthdays["day"]==day) & (birthdays["month"]==month)]


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
list_letters=["letter_1.txt","letter_2.txt","letter_3.txt"]
random_letter=random.choice(list_letters)
with open(f"./letter_templates/{random_letter}") as file :
      carta=file.readlines()
      name=Cumleanero["name"].to_list()[0]
      carta[0]=carta[0].replace("[NAME]",name)
      with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=[print(i) for i in carta]
                                )

# 4. Send the letter generated in step 3 to that person's email address.


