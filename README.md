# Weather App using OpenWeatherMap API

This project retrieves weather information using OpenWeatherMap's API based on user-inputted city names. It includes both a Python script for fetching weather data and a Streamlit-based web application to display weather details.

## Table of Contents
- [Introduction](#introduction)
- [Python Weather Retrieval Script](#python-weather-retrieval-script)
- [Streamlit Web App](#streamlit-web-app)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)

## Introduction

This project aims to provide users with real-time weather data for specified cities using the OpenWeatherMap API. It involves a Python script to fetch weather information and a Streamlit-based web app for a user-friendly interface.

## Python Weather Retrieval Script

- **Weather Retrieval**: The Python script utilizes the OpenWeatherMap API to obtain weather data for a specified city.
- **Displaying Information**: The script displays the weather, temperature (in Celsius), pressure, humidity, and country for the requested city.

## Streamlit Web App

- **User Interface**: The Streamlit web app allows users to input a city name and fetch weather details by clicking the "Get Weather" button.
- **Display Weather Information**: Upon successful retrieval, the app presents weather information such as type, temperature, pressure, and humidity for the entered city.

## Usage

To run the project:

1. Clone this repository.
2. Install the necessary Python dependencies (`requests`, `streamlit`).
3. Execute the Python script (`weather_retrieval.py`) to fetch weather data.
4. Run the Streamlit app (`streamlit run app.py`) for a user-friendly weather display interface.

## Technologies Used

- Python
- Requests library for API requests
- Streamlit for building the web application

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or encounter any issues, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
