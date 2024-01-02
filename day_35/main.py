import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""

account_id = ""
auth_token = ""

MY_LAT = 49.778290
MY_LON = -126.049393

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()["list"][:12]

for hour in weather_data:
    if int(hour["weather"][0]["id"]) < 700:
        client = Client(account_id, auth_token)
        message = client.messages \
                    .create(
                        body="It's going to rain today. Bring an umbrella",
                        from="",
                        to=""
                    )
        print(message.status)
        break;
