import streamlit as st
import requests


st.set_page_config(layout="wide")

def get_weather_data(api_key, city):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

    if weather_data.status_code == 404:
        return None
    else:
        return weather_data.json()




def main():
    st.title("Weather App")

    api_key = '30d4741c779ba94c470ca1f63045390a'

    user_input = st.text_input("Enter city:")
    
    if st.button("Get Weather"):
        weather_json = get_weather_data(api_key, user_input)
        
        if weather_json:
            weather = weather_json['weather'][0]['main']
            temp_fahrenheit = weather_json['main']['temp']
            temp_celsius = (temp_fahrenheit - 32) * 5/9
            press = weather_json['main']['pressure']
            humidity_value = weather_json['main']['humidity']
            country_name = weather_json['sys']['country']

            st.markdown(f"<h1 style='text-align: center; font-size: 2.5em;'>{user_input.title()}, {country_name}</h1>", unsafe_allow_html=True)

            st.markdown(
                f"<div style='text-align: center;'>"
                f"<p>Weather: {weather}</p>"
                f"<p>Temperature: {temp_celsius:.2f}°C</p>"
                f"<p>Pressure: {press} hPa</p>"
                f"<p>Humidity: {humidity_value}%</p>"
                f"</div>",
                unsafe_allow_html=True
            )
        else:
            st.warning("No City Found")

if __name__ == "__main__":
    main()
    

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://raw.githubusercontent.com/vipulmalyan/Weather-App/main/pexels-pixabay-209831.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)


    
hide_st_style = '''
<style> footer {visibility: hidden;} 
</style>
'''
st.markdown(hide_st_style, unsafe_allow_html=True)


footer_html = """
<style>
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    color: white; /* Text color */
    padding: 10px;
    text-align: center; /* Center the text */
    font-size: 18px; /* Adjust the font size */
}
</style>
<div class="footer">Made by Vipul Malyan</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)



