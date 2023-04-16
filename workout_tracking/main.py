
#importar librerias
import requests


#### step 2 of the project######
# link with the example about the using of the API
#https://gist.github.com/mattsilv/d99cd145cc2d44d71fa5d15dd4829e03https://gist.github.com/mattsilv/d99cd145cc2d44d71fa5d15dd4829e03
#https://trackapi.nutritionix.com/docs/#/default/post_v2_natural_exercise
GENDER = "MALE"
WEIGHT_KG = 80
HEIGHT_CM= 170
AGE = 22

APP_ID = ""
API_KEY = ""

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













