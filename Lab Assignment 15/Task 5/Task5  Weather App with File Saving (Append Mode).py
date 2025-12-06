# ===============================================
# TASK 5: Weather App with File Saving (Append Mode)
# Features:
# - Clean output on screen
# - Saves every successful result to results.json
# - Appends new data (never deletes old)
# - Creates file automatically if not exists
# ===============================================

import requests
import json
import os

# Replace with your real API key
API_KEY = "31a14e40f729658b839c1524989dbfd6"   # ← Put your actual key here!

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FILE_NAME = "results.json"   # This file will be created in the same folder

def save_to_file(city_data):
    """
    Saves or appends weather data to results.json
    """
    # Step 1: Check if file already exists
    if os.path.exists(FILE_NAME):
        # File exists → read old data
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            data_list = json.load(file)
    else:
        # File doesn't exist → start fresh
        data_list = []

    # Step 2: Add new city data
    data_list.append(city_data)

    # Step 3: Save back to file (pretty format)
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(data_list, file, indent=4)

    print(f"Data saved to {FILE_NAME} successfully!\n")


def show_weather(city_name):
    """
    Main function: Gets weather + shows clean output + saves to file
    """
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        # Special check for city not found (404)
        if response.status_code == 404:
            print("Error: City not found. Please enter a valid city.")
            return

        # Any other error (like wrong API key)
        response.raise_for_status()

        data = response.json()

        # Extract required info
        city = data['name']
        temp = round(data['main']['temp'])           # Round to whole number
        humidity = data['main']['humidity']
        description = data['weather'][0]['description'].capitalize()

        # Clean screen output (same as Task 4)
        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")

        # Prepare data to save
        weather_record = {
            "city": city,
            "temp": temp,
            "humidity": humidity,
            "weather": description
        }

        # Save to file (this is the NEW part!)
        save_to_file(weather_record)

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.")
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
    except requests.exceptions.HTTPError:
        print("Error: Could not connect to API. Check your API key.")
    except Exception as e:
        print("Error: Something went wrong. Try again.")


# ===============================================
# Main Program
# ===============================================

print("Welcome to Weather Checker - Task 5 (With File Saving!)")
print("All successful results will be saved to results.json\n")

city = input("Enter city name: ").strip()
show_weather(city)

print("Task 5 Completed!")