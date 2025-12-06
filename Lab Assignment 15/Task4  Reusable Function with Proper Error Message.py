# ===============================================
# TASK 4: Reusable Function with Proper Error Message
# Goal: Function takes city as parameter + exact error for invalid city
# ===============================================

import requests

# Replace with your real API key
API_KEY = "31a14e40f729658b839c1524989dbfd6"   # ← Put your actual key here!

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def show_weather(city_name):
    """
    This function takes city name as parameter and displays clean weather info.
    Shows exact error message if city is not found.
    """
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'      # Celsius
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        
        # If city not found → status code 404
        if response.status_code == 404:
            print("Error: City not found. Please enter a valid city.")
            return
        
        # For any other error (like 401 invalid key)
        response.raise_for_status()
        
        data = response.json()

        # Extract data
        city = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description'].capitalize()

        # Beautiful output (exactly as expected)
        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.")
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
    except requests.exceptions.HTTPError:
        # This catches 401 (wrong key) or other server errors
        print("Error: Could not connect to API. Check your API key.")
    except Exception:
        print("Error: Could not connect to API. Check your API key or network connection.")


# ===============================================
# Main Program - Takes user input and calls the function
# ===============================================

print("Welcome to Weather Checker - Task 4")
print("Enter any city name and see clean results!\n")

city = input("Enter city name: ").strip()

# Call the function with the city as parameter
show_weather(city)

print("\nTask 4 Completed!")