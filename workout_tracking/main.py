#Importar Librerias

import requests
from datetime import datetime
import os

#### step 2 of the project######
# link with the example about the using of the API
#https://gist.github.com/mattsilv/d99cd145cc2d44d71fa5d15dd4829e03https://gist.github.com/mattsilv/d99cd145cc2d44d71fa5d15dd4829e03
#https://trackapi.nutritionix.com/docs/#/default/post_v2_natural_exercise
GENDER = "MALE"
WEIGHT_KG = 80
HEIGHT_CM= 170
AGE = 22

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell which exercise you did today?: ")

header = {
"x-app-id": APP_ID,
"x-app-key": API_KEY,
}

parameters = {
"query":exercise_input,
"gender": GENDER,
"weight_kg": WEIGHT_KG,
"height_cm": HEIGHT_CM,
"age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()
print(result)

###Step 3 - Setup Your Google Sheet with Sheety##################


google_sheets_endpoint="https://api.sheety.co/99590fd56f514951e3e0791088f7aa9f/myWorkouts/workouts"
auth_google_sheet=os.environ["BEARER_AUTH"]
bearer_headers = {
    "Authorization": f"Bearer {auth_google_sheet} "
}
exercise_name=str(result["exercises"][0]["name"])
exercise_duration=str(result["exercises"][0]["duration_min"])
exercise_calories=str(result["exercises"][0]["nf_calories"])

today=datetime.now()
today_time=today.time().strftime("%H:%M:%S")
today_date=today.date().strftime("%Y/%m/%d")# to interprete it as a format
print(exercise_calories)
params_google_sheet_api={
    #even if the name of the columns are capitalized you must write it in lowercase  ex: Date ->date
    "workout":{
        "date":str(today_date),
        "time":str(today_time),
        "exercise":exercise_name,
        "duration":exercise_duration,
        "calories":exercise_calories
    }
}
response_google_sheet_api=requests.post(url=google_sheets_endpoint,json=params_google_sheet_api,headers=bearer_headers)
result_google_api=response_google_sheet_api.json()
# result_google_api=response_google_sheet_api.text#it shows the process
print(result_google_api)





