import requests

API_KEY = "a64f4d9e80c018a4efff97cbb6a4a247"  # paste your key here
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        print("\n==========================================")
        print(f"  📍 City     : {data['name']}, {data['sys']['country']}")
        print(f"  🌡️  Temp     : {data['main']['temp']}°C")
        print(f"  🤔 Feels like: {data['main']['feels_like']}°C")
        print(f"  💧 Humidity  : {data['main']['humidity']}%")
        print(f"  🌤️  Weather  : {data['weather'][0]['description']}")
        print(f"  💨 Wind      : {data['wind']['speed']} m/s")
        print("==========================================\n")

    elif response.status_code == 404:
        print("❌ City not found. Please check the name and try again.")
    else:
        print("❌ Something went wrong. Check your API key.")

def main():
    print("🌍 Welcome to the Weather App!")
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ")
        if city.lower() == "quit":
            print("Goodbye! 👋")
            break
        get_weather(city)

main()