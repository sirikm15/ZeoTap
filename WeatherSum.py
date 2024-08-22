import datetime
import sqlite3

def daily_summary():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT city, date(dt, 'unixepoch'), 
               AVG(temp), MAX(temp), MIN(temp),
               (SELECT main FROM weather WHERE city=w.city ORDER BY COUNT(main) DESC LIMIT 1)
        FROM weather w
        GROUP BY city, date(dt, 'unixepoch')
    ''')

    summaries = cursor.fetchall()
    conn.close()
    return summaries

def check_alerts():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    threshold_temp = 35  # Example threshold
    cursor.execute('''
        SELECT city, COUNT(*)
        FROM weather
        WHERE temp > ? AND dt > strftime('%s', 'now', '-10 minutes')
        GROUP BY city
    ''', (threshold_temp,))

    alerts = cursor.fetchall()
    conn.close()

    if alerts:
        print("Alert! Temperature threshold exceeded in the following cities:")
        for alert in alerts:
            print(f"City: {alert[0]}, Instances: {alert[1]}")

