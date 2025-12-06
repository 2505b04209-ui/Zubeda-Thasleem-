# ===============================================
# TASK 3: Extract and Display Specific Weather Data
# Goal: Show only important info in a beautiful way!
# ===============================================

import requests
import json

# Replace with your real API key
API_KEY = "31a14e40f729658b839c1524989dbfd6"   # ← Put your 32-character key here!

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'      # For Celsius
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()        # Checks for 404, 401, etc.
        data = response.json()

        # Extract only the fields we need
        city = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description'].capitalize()  # Makes first letter big

        # Beautiful user-friendly output
        print("\n" + "="*40)
        print(f"     City        : {city}")
        print(f"     Temperature : {temp}°C")
        print(f"     Humidity    : {humidity}%")
        print(f"     Weather     : {description}")
        print("="*40 + "\n")

    except requests.exceptions.HTTPError:
        print("Error: City not found or invalid API key. Please try again.")
    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.")
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Check your internet.")
    except Exception:
        print("Error: Could not connect to API. Check your API key or network connection.")

# ===============================================
# Main Program
# ===============================================

print("Welcome to Weather Checker - Task 3")
print("You will now see clean and beautiful output!\n")

city = input("Enter city name (e.g. London, Delhi, Tokyo): ").strip()
get_weather(city)

print("Task 3 Completed Successfully!")