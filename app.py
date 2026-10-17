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


# CSS section

# CSS section
st.markdown(f"""
<style>

/* Full-screen background image */
.stApp {{
    background:
        linear-gradient(
            rgba(20, 35, 70, 0.15),
            rgba(20, 35, 70, 0.15)
        ),
        url("data:image/png;base64,{bg_image}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    min-height: 100vh;
}}

/* Responsive glass container */
[data-testid="stMainBlockContainer"] {{
    background: rgba(255, 255, 255, 0.16);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);

    border: 1px solid rgba(255, 255, 255, 0.35);
    border-radius: 18px;
    box-shadow: 0 8px 32px rgba(20, 30, 60, 0.12);

    padding: clamp(1rem, 4vw, 2rem);
    margin: 1rem auto;
    width: 100%;
    max-width: 850px;
    box-sizing: border-box;
}}

/* Transparent header */
[data-testid="stHeader"] {{
    background: rgba(255, 255, 255, 0.08);
}}

/* Responsive city input */
.stTextInput input {{
    background: rgba(255, 255, 255, 0.30);
    border: 1px solid rgba(255, 255, 255, 0.55);
    border-radius: 9px;
    width: 100%;
    box-sizing: border-box;
}}

/* Button */
.stButton button {{
    border-radius: 10px;
    max-width: 100%;
    transition: all 0.2s ease;
}}

.stButton button:hover {{
    border-color: #3b82f6;
    color: #3b82f6;
}}

/* Weather metrics */
[data-testid="stMetric"] {{
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.20);
    border-radius: 12px;
    padding: 12px;
    overflow-wrap: anywhere;
}}

/* Phones and tablets */
@media (max-width: 768px) {{
    [data-testid="stMainBlockContainer"] {{
        padding: 1rem;
        margin: 0 auto;
        max-width: 100%;
        border-radius: 14px;
    }}

    [data-testid="stImage"] img {{
        max-width: 110px;
        width: 100%;
        height: auto;
    }}

    h1 {{
        font-size: clamp(1.5rem, 6vw, 2rem) !important;
        overflow-wrap: anywhere;
    }}

    [data-testid="stMetricValue"] {{
        font-size: 1.35rem;
    }}
}}

/* Small phones */
@media (max-width: 480px) {{
    [data-testid="stMainBlockContainer"] {{
        padding: 0.85rem;
    }}

    [data-testid="stMetric"] {{
        padding: 8px;
    }}

    [data-testid="stMetricValue"] {{
        font-size: 1.1rem;
    }}
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





