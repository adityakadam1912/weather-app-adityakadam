import streamlit as st
import requests
from dotenv import load_dotenv
import os
import base64

load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')

with open("image.png", "rb") as image_file:
    bg_image = base64.b64encode(image_file.read()).decode()

st.set_page_config(page_title='Weather App', page_icon='weather.png')

#css section

st.markdown(f"""
<style>
/* Full-screen blurred weather background */
.stApp {{
    background:
        linear-gradient(
            rgba(20, 35, 70, 0.18),
            rgba(20, 35, 70, 0.18)
        ),
        url("data:image/jpeg;base64,{bg_image}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Centered translucent glass card */
[data-testid="stMainBlockContainer"] {{
    background: rgba(255, 255, 255, 0.24);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);

    border: 1px solid rgba(255, 255, 255, 0.42);
    border-radius: 18px;
    box-shadow: 0 8px 32px rgba(20, 30, 60, 0.12);

    padding: 2rem;
    margin-top: 2rem;
}}

/* Transparent Streamlit header */
[data-testid="stHeader"] {{
    background: rgba(255, 255, 255, 0.08);
}}

/* Translucent city input */
.stTextInput input {{
    background: rgba(255, 255, 255, 0.30);
    border: 1px solid rgba(255, 255, 255, 0.55);
    border-radius: 9px;
}}

/* Glass-style button */
.stButton button {{
    background: rgba(75, 125, 255, 0.88);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.55);
    border-radius: 10px;
    transition: all 0.2s ease;
}}

.stButton button:hover {{
    background: rgba(55, 105, 235, 0.98);
    color: white;
    border-color: white;
}}
</style>
""", unsafe_allow_html=True)

#css section


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





