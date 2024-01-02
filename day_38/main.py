import requests
import datetime

NUTRITIONIX_APP_ID = ""
NUTRITIONIX_API_KEY = ""
NUTRITIONIX_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


nutritionix_header = {
    "x-app-id":  NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}

nutritionix_body = {
    "query" : input("What exercise today? "),
    "gender": "male",
    "weight_kg": 76.2035,
    "height_cm": 172.72,
    "age": 45
}

nutritionix_response = requests.post(url=NUTRITIONIX_EXERCISE_ENDPOINT, json=nutritionix_body, headers=nutritionix_header)
nutritionix_response.raise_for_status()
datetime_now = datetime.datetime.now()

SHEETY_URL = ''
sheety_header = {
    "Authorization": ""
}

for exercise in nutritionix_response.json()['exercises']:
    sheety_body = {
        "workout": {
            "date": datetime_now.strftime("%d/%m/%Y"),
            "time": datetime_now.strftime("%H:%M:%S"),
            "exercise": exercise['name'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }
  
    sheety_response = requests.post(url=SHEETY_URL, json=sheety_body, headers=sheety_header)
    print(sheety_response.text)