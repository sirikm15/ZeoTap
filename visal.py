import matplotlib.pyplot as plt
import sqlite3

def plot_temperature_trends(city):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT date(dt, 'unixepoch'), AVG(temp)
        FROM weather
        WHERE city=?
        GROUP BY date(dt, 'unixepoch')
    ''', (city,))

    data = cursor.fetchall()
    dates = [row[0] for row in data]
    temps = [row[1] for row in data]

    plt.plot(dates, temps, marker='o')
    plt.title(f"Temperature Trends in {city}")
    plt.xlabel('Date')
    plt.ylabel('Average Temperature (Celsius)')
    plt.grid(True)
    plt.show()

    conn.close()


