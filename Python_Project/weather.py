import requests

CITY = "Lagos"
URL = f"http://wttr.in/{CITY}?format=j1"

try:
    response = requests.get(URL)
    data = response.json()

    # Extract relevant info
    area = data["nearest_area"][0]["areaName"][0]["value"]
    country = data["nearest_area"][0]["country"][0]["value"]
    temp_c = data["current_condition"][0]["temp_C"]
    condition = data["current_condition"][0]["weatherDesc"][0]["value"]

    print(f"📍 Location: {area}, {country}")
    print(f"🌡 Temperature: {temp_c}°C")
    print(f"⛅ Condition: {condition}")

except Exception as e:
    print("Error fetching weather data:", e)
