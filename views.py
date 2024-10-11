import os
import requests
from flask import request, jsonify
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv('api_weather_key')


def weather_view():
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)

    if lat is None or lon is None:
        return jsonify({"error": "Missing latitude or longitude"}), 400

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        return jsonify(weather_data)
    except requests.RequestException:
        return jsonify({"error": "Error fetching weather data"}), 500
