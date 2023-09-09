# WeatherSMSNotifier

# Nairobi Weather SMS Notifier

## Overview

The Nairobi Weather SMS Notifier is a Python script that provides daily weather updates for Nairobi, Kenya, delivered to your phone via SMS. This project utilizes the OpenWeatherMap API to fetch the latest weather information for Nairobi and sends it to your mobile phone number using Twilio's SMS service.

## Features

- Daily weather updates for Nairobi, including temperature and weather description.
- Automated scheduling to send weather updates at a specific time (e.g., 23:00) daily.
- Error handling to gracefully handle issues with API responses and notifications.

## How It Works

1. The script makes an API request to OpenWeatherMap to retrieve the current weather data for Nairobi.
2. It extracts relevant weather information, including temperature and weather description.
3. The weather data is formatted into an SMS message.
4. The message is sent to your specified phone number using Twilio's SMS service.
5. The script runs daily at the scheduled time to provide updated weather information.

## Prerequisites

Before using this project, you need the following:

- Python 3.x installed on your machine.
- A free or paid OpenWeatherMap API key. Sign up at [OpenWeatherMap](https://openweathermap.org/api) to obtain your API key.
- A free or paid Twilio account. Create one at [Twilio](https://www.twilio.com/try-twilio).

## Configuration

1. Clone or download this repository to your local machine.

2. Install the required Python packages using pip:

   ```bash
   pip install requests twilio schedule
