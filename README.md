## Nairobi Weather SMS Notifier

### Overview
The Nairobi Weather SMS Notifier is a Python script that provides daily weather updates for Nairobi, Kenya, delivered to your phone via SMS. This project utilizes the OpenWeatherMap API to fetch the latest weather information for Nairobi and sends it to your mobile phone number using Twilio's SMS service.

### Features
- Daily weather updates for Nairobi, including temperature and weather description.
- Automated scheduling to send weather updates at a specific time daily.
- Error handling to gracefully handle issues with API responses and notifications.
- Logging for tracking script execution and troubleshooting.

### Prerequisites
- Python 3.x installed on your machine.
- A free or paid OpenWeatherMap API key. Sign up at OpenWeatherMap to obtain your API key.
- A free or paid Twilio account. Create one at Twilio.

### Setup
1. Clone or download this repository to your local machine.
2. Create a `.env` file and add the following environment variables:
    ```
    TWILIO_ACCOUNT_SID=your_twilio_account_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    TWILIO_PHONE_NUMBER=your_twilio_phone_number
    YOUR_PHONE_NUMBER=your_phone_number
    OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
    ```
3. Install the required Python packages using pip:
    ```
    pip install -r requirements.txt
    ```
4. Run the script:
    ```
    python weather_forecast.py
    ```

### How It Works
- The script makes an API request to OpenWeatherMap to retrieve the current weather data for Nairobi.
- It extracts relevant weather information, including temperature and weather description.
- The weather data is formatted into an SMS message.
- The message is sent to your specified phone number using Twilio's SMS service.
- The script runs daily at the scheduled time to provide updated weather information.
