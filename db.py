import sqlite3

def init_db():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY,
            city TEXT,
            main TEXT,
            temp REAL,
            feels_like REAL,
            dt INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def insert_weather_data(weather_info):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather (city, main, temp, feels_like, dt)
        VALUES (?, ?, ?, ?, ?)
    ''', (weather_info['city'], weather_info['main'], weather_info['temp'],
          weather_info['feels_like'], weather_info['dt']))
    conn.commit()
    conn.close()
