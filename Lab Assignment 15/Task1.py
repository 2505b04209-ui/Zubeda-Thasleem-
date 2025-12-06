# ===============================================
# TASK 1: Simple Weather API - No Error Handling
# Goal: Get weather data and print pretty JSON
# ===============================================

import requests  # This library helps us talk to websites/APIs
import json      # This helps us make JSON look beautiful

# TODO: Replace this with YOUR real API key
API_KEY = "31a14e40f729658b839c1524989dbfd6"   # ← CHANGE THIS!

# This is the website (URL) we will visit to get weather
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    # Step 1: Prepare the full address with city and API key
    params = {
        'q': city_name,      # the city user typed
        'appid': API_KEY,    # your secret key
        'units': 'metric'    # so temperature comes in Celsius (not Kelvin)
    }
    
    # Step 2: Send the request to OpenWeatherMap
    response = requests.get(BASE_URL, params=params)
    
    # Step 3: Convert the response to Python dictionary (like a JSON object)
    data = response.json()
    
    # Step 4: Print it beautifully (pretty JSON)
    print("\n=== Weather Data from API ===")
    print(json.dumps(data, indent=4))  # indent=4 makes it readable!

# ===============================================
# Main Program Starts Here
# ===============================================

print("Welcome to Weather Checker - Task 1")
print("You are about to see raw JSON data (pretty printed)\n")

# Ask user for city name
city = input("Enter city name (e.g., London, Paris, Tokyo): ").strip()

# Call our function
get_weather(city)

print("\nTask 1 Completed Successfully!")