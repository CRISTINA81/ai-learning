import requests
api_key = "d3f29edfe637ca3b05e51b4b600af4f0"

city = input("Enter a city: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()
if data["cod"] == 200:
    print("City found!")
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description =data["weather"][0]["description"]
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")
else:
    print("City not found!")

    

