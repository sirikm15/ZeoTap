import requests

API_KEY = "f0b288e143b65f447ac9bfdd4bcb669b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # To get temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def parse_weather_data(data):
    weather_info = {
        'city': data['name'],
        'main': data['weather'][0]['main'],
        'temp': data['main']['temp'],
        'feels_like': data['main']['feels_like'],
        'dt': data['dt']
    }
    return weather_info

#london_weather_data = get_weather("London")

#parsed_london_weather = parse_weather_data(london_weather_data)

# Print the parsed data
#print(parsed_london_weather)
