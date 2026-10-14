import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')

st.set_page_config(page_title='Weather App', page_icon='weather.png')

st.title('Weather App ⛅')
st.image("weather.png", width=150)

st.write('Enter the city name and click the button to fetch the weather data')

city=st.text_input('Enter city name')

if(st.button('Fetch Weather')):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
    
    if(response.status_code == 200):
        st.success('Weather Data Fetched successfully')


        data=response.json()

        #Extract weather information
        temparature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_condition = data['weather'][0]['description']
        name = data['name']
        country = data['sys']['country']

        st.subheader(f'{name}, {country}')

        #Create 2 rows and 2 columns
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)


        col1.metric('Temparature', f'🌡️{temparature}°C')
        col2.metric('Humidity', f'💦{humidity}%')
        col3.metric('Wind Speed', f'🍃{wind_speed}m/s')
        col4.metric('Weather Condition', f'⛅{weather_condition}')

    else:
        st.error('City Not Found')    





