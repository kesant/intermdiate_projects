import requests

GENDER = "MALE"
WEIGHT_KG = 80
HEIGHT_CM= 170
AGE = 22

APP_ID = MY_ID
API_KEY = MY_KEY

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell which exercise you did today?: ")

header = {
"x-app-id": "",
"x-remote-user-id": "",
}

parameters = {
"gender": GENDER,
"weight_kg": WEIGHT_KG,
"height_cm": HEIGHT_CM,
"age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()
print(result)













