def forecast(*args):
    weather = {}
    for city, current_weather in args:
        if city not in weather:
            weather[city] = current_weather
    sorted_dict = dict(sorted(weather.items(), key=lambda x: (x[1], x[0])))
    sunny = ''
    rainy = ''
    cloudy = ''
    for k, v in sorted_dict.items():
        if v == "Sunny":
            sunny += f"{k} - {v}\n"
        elif v == "Rainy":
            rainy += f"{k} - {v}\n"
        elif v == "Cloudy":
            cloudy += f"{k} - {v}\n"
    return sunny + cloudy + rainy


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
