#libraries of course
import os
import requests
from twilio.rest import Client
import schedule
import time
import logging
from datetime import datetime
import pytz

#logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#loading sensitive data from environment variables (chris' credentials)
twilio_account_sid = os.getenv("AC3f11b6f0b01a0a5ffe1b04f99f8dc91f")
twilio_auth_token = os.getenv("329da0ba047ab35aeeab8fcc501b409b")
twilio_phone_number = os.getenv("+17634965742")
your_phone_number = os.getenv("+254701519313") #subject to user(chris) & github data privacy policy
openweathermap_api_key = os.getenv("842db1d135cec527e489a97ad7c8b8f9")
city = "Nairobi"

def send_sms(message):
    try:
        client = Client(twilio_account_sid, twilio_auth_token)
        client.messages.create(to=your_phone_number, from_=twilio_phone_number, body=message)
        logging.info("SMS sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send SMS: {e}")

def get_weather():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweathermap_api_key}"
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()

        temperature_kelvin = weather_data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15
        weather_description = weather_data["weather"][0]["description"]

        message = f"Weather in {city}:\nTemperature: {temperature_celsius:.2f}°C\nDescription: {weather_description}"
        send_sms(message)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching weather data: {e}")
    except KeyError as e:
        logging.error(f"Unexpected response format: {e}")

#setting Nairobi timezone
nairobi_tz = pytz.timezone('Africa/Nairobi')

#schedule weather update to be at scheduled time - Nairobi's timezone
def schedule_weather_updates():
    schedule_time = datetime.now(nairobi_tz).strftime('%H:%M')
    schedule.every().day.at(schedule_time).do(get_weather)
    logging.info(f"Scheduled weather updates at {schedule_time} Nairobi time.")
schedule_weather_updates()

#main loop keeping script running
while True:
    schedule.run_pending()
    time.sleep(1)
