import schedule
import time

from WeatherSum import check_alerts
from db import insert_weather_data
from weather import parse_weather_data, get_weather


def job():
    print("Job started...")
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    for city in cities:
        print(f"Fetching weather data for {city}...")
        data = get_weather(city)
        weather_info = parse_weather_data(data)
        insert_weather_data(weather_info)
        print(f"Inserted data for {city}: {weather_info}")
    check_alerts()
    print("Job completed.\n")
     

schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
