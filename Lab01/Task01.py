def gather_weather_forecast(location, hours_from_now, temperatures, rain_probabilities, pressures):
    forecast = []
    for index in range(len(hours_from_now)):
        forecast.append({"hour":hours_from_now[index], 
                                    "temperature":temperatures[index],
                                    "rain probability": rain_probabilities[index],
                                    "pressure": pressures[index]})

    dictionary = {"location": location, "forecast": forecast}
    return dictionary

assert gather_weather_forecast("Test Island", [1], [22], [12], [1000]) == {
    "location": "Test Island",
    "forecast": [
        {"hour": 1, "temperature": 22, "rain probability": 12, "pressure": 1000},
    ]
}

assert gather_weather_forecast("Studentski Grad", [24, 48, 72], [20, 18, 15], [0, 50, 88], [1000, 990, 980]) == {
    "location": "Studentski Grad",
    "forecast": [
        {"hour": 24, "temperature": 20, "rain probability": 0, "pressure": 1000},
        {"hour": 48, "temperature": 18, "rain probability": 50, "pressure": 990},
        {"hour": 72, "temperature": 15, "rain probability": 88, "pressure": 980},
    ]
}

"✅ All OK! +0.75 points"
