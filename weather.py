# weather_app.py (main branch)

def get_temperature(celsius=True):
    temp_c = 24
    if celsius:
        return f"Temperature: {temp_c}°C"
    else:
        temp_f = (temp_c * 9/5) + 32
        return f"Temperature: {temp_f}°F"

def get_forecast():
    return "Forecast: Clear skies"

def send_weather_alert():
    return "Weather Alert: No severe conditions."

if __name__ == "__main__":
    print(get_temperature())
    print(get_forecast())
    print(send_weather_alert())
