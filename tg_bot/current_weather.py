import requests


def get_current_weather(city, api_key):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
        response = requests.get(url).json()

        temp = response["main"]["temp"]
        feels_like = response["main"]["feels_like"]
        description = response["weather"][0]["description"].capitalize()
        humidity = response["main"]["humidity"]
    except Exception as e:
        return f"Ошибка при получении погоды: {str(e)}"
    else:
        return (
            f" Погода в {city}:\n"
            f"{description}\n"
            f"Температура: {temp} °C (ощущается как {feels_like} °C )\n"
            f"Влажность: {humidity}%"
        )
