# Import necessary libraries
import requests
from twilio.rest import Client
import schedule
import time

# Twilio credentials (you need to set up a Twilio account and get these from your dashboard)
twilio_account_sid = "AC3f11b6f0b01a0a5ffe1b04f99f8dc91f"
twilio_auth_token = "329da0ba047ab35aeeab8fcc501b409b"
twilio_phone_number = "+17634965742"  # Should be in the format "+1234567890"
your_phone_number = "+254701519313"  # Your phone number in the format "+1234567890"

# OpenWeatherMap API key (sign up at https://openweathermap.org/api and get your API key)
openweathermap_api_key = "842db1d135cec527e489a97ad7c8b8f9"
city = "Nairobi"

# Function to send an SMS using Twilio
def send_sms(message):
    client = Client(twilio_account_sid, twilio_auth_token)
    client.messages.create(to=your_phone_number, from_=twilio_phone_number, body=message)

# Function to get the weather information from OpenWeatherMap
def get_weather():
    # Make an API request to OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweathermap_api_key}"
    response = requests.get(url)
    weather_data = response.json()

    # Extract relevant weather information
    temperature_kelvin = weather_data["main"]["temp"]
    temperature_celsius = temperature_kelvin - 273.15  # Convert Kelvin to Celsius
    weather_description = weather_data["weather"][0]["description"]

    # Compose the weather message
    message = f"Weather in {city}:\nTemperature: {temperature_celsius:.2f}°C\nDescription: {weather_description}"

    # Send the weather information via SMS
    send_sms(message)

# Schedule the weather update to be sent every day at 23:00
schedule.every().day.at("13:56").do(get_weather)

# Main loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
