# weather_app.py (feature/new_ui branch)

def get_temperature():
    return "Temperature: 24°C"

def get_forecast():
    return "Forecast: Clear skies"

def display_ui():
    print("📡 Weather Dashboard")
    print("====================")
    print(get_temperature())
    print(get_forecast())

def apply_theme(theme="light"):
    return f"Theme applied: {theme}"

if __name__ == "__main__":
    display_ui()
    print(apply_theme("dark"))
