#!/usr/bin/env python
# coding: utf-8

# In[14]:


import requests

def get_weather(city, api_key):
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'description': data['current']['condition']['text'],
            'temperature': data['current']['temp_c'],
            'humidity': data['current']['humidity'],
            'wind_speed': data['current']['wind_kph']
        }
        return weather
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def main():
    city = input("Enter city name: ")
    api_key = 'd8b8a0491a684fb196375855242004'  # Replace 'YOUR_API_KEY' with your actual API key
    weather = get_weather(city, api_key)
    if weather:
        print(f"Weather in {city}:")
        print(f"Description: {weather['description']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    main()


# In[11]:





# In[ ]:




