# ===============================================
# TASK 2 DEBUG VERSION: Weather API with Error Handling + Debug Prints
# Run this to see EXACTLY where it stops (remove debug prints later for final version)
# ===============================================

import requests  # Library to make HTTP requests to APIs
import json      # Library to handle and pretty-print JSON

# TODO: Replace with YOUR real API key (32 characters, no spaces!)
API_KEY = "d5f8e9a1234567890abcdef1234567890"   # ← CHANGE THIS! Test with your exact key

# Base URL for OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """
    Fetches weather data for a city and prints pretty JSON.
    Now with error handling + DEBUG prints to find issues!
    """
    print(f"DEBUG: Starting get_weather for city '{city_name}'")  # ← NEW: See if function starts
    
    # Prepare the request parameters (like query string)
    params = {
        'q': city_name,      # City name from user (e.g., "London,UK")
        'appid': API_KEY,    # Your secret API key
        'units': 'metric'    # Celsius instead of weird Kelvin
    }
    
    print(f"DEBUG: API Key starts with: {API_KEY[:10]}...")  # ← NEW: Check if key is loaded (hides full key for safety)
    print(f"DEBUG: Full URL would be: {BASE_URL}?q={city_name}&appid=...")  # ← NEW: See the URL
    
    # ===============================================
    # ERROR HANDLING STARTS HERE
    # ===============================================
    try:
        print("DEBUG: Sending request to API...")  # ← NEW: See if request starts
        # Step 1: Send GET request to API (with 10-second timeout to avoid hanging)
        response = requests.get(BASE_URL, params=params, timeout=10)
        
        print(f"DEBUG: Got response! Status code: {response.status_code}")  # ← NEW: See status (200 = good)
        
        # Step 2: Check if response is successful (status code 200 = OK)
        response.raise_for_status()  # Raises error if not 200 (e.g., 401 for bad key, 404 for bad city)
        
        # Step 3: Convert raw response to Python dict and pretty-print as JSON
        data = response.json()
        print("\n=== Weather Data from API (Success!) ===")
        print(json.dumps(data, indent=4))  # indent=4 makes it look beautiful and readable
        
    except requests.exceptions.Timeout:
        print("DEBUG: Caught Timeout error")
        print("Error: Could not connect to API. Check your network connection.")
    except requests.exceptions.ConnectionError:
        print("DEBUG: Caught ConnectionError")
        print("Error: Could not connect to API. Check your network connection.")
    except requests.exceptions.HTTPError:
        print(f"DEBUG: Caught HTTPError - Status: {response.status_code if 'response' in locals() else 'Unknown'}")
        print("Error: Could not connect to API. Check your API key or try a different city.")
    except requests.exceptions.RequestException as e:
        print(f"DEBUG: Caught RequestException: {type(e).__name__}")
        print("Error: Could not connect to API. Check your API key or network connection.")
    except json.JSONDecodeError:
        print("DEBUG: Caught JSON decode error")
        print("Error: Could not connect to API. Check your API key or network connection.")
    except Exception as e:
        print(f"DEBUG: Caught Unexpected Error: {type(e).__name__}: {str(e)}")  # ← NEW: Show exact error
        print("Error: Could not connect to API. Check your API key or network connection.")
    # ===============================================
    # ERROR HANDLING ENDS HERE
    # ===============================================
    
    print("DEBUG: get_weather function ended")  # ← NEW: See if function finishes

# ===============================================
# Main Program (With extra debugs)
# ===============================================

print("DEBUG: Program starting...")  # ← NEW
print("Welcome to Weather Checker - Task 2 (With Error Handling + DEBUG)")
print("Enter a city name. If wrong, you'll get a friendly error!\n")

# Get city from user and clean it (remove extra spaces)
city = input("Enter city name (e.g., London,UK or Paris,FR): ").strip()
print(f"DEBUG: You entered: '{city}'")  # ← NEW

# Call the function
get_weather(city)

print("DEBUG: Main program ended")  # ← NEW
print("\nTask 2 Debug Completed!")