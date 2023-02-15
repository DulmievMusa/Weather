from dotenv import load_dotenv
from requests import request
import os
path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(path):
    load_dotenv(path)
    API_KEY = os.environ.get('API_KEY')


def get_weather(query):
    if not query:
        query = 'fetch:ip'
    response = request(
        method='GET',
        url='http://api.weatherstack.com/current',
        params={
            'access_key': API_KEY,
            'query': query
        }
    )
    if response.status_code == 200:
        return {
            'icon': request(
                method='GET',
                url=response.json()['current']['weather_icons'][0]
            ).content,
            'temperature': response.json()['current']['temperature'],
            'wind_speed': response.json()['current']['wind_speed']
        }