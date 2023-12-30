# Weather App using OpenWeatherMap API

This project retrieves weather information using OpenWeatherMap's API based on user-inputted city names. It includes both a Python script for fetching weather data and a Streamlit-based web application to display weather details.

![Weather App Screenshot](snapshot.png)

## Table of Contents
- [Introduction](#introduction)
- [Python Weather Retrieval Script](#python-weather-retrieval-script)
- [Streamlit Web App](#streamlit-web-app)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Updates](#updates)
- [License](#license)

## Introduction

This project provides real-time weather data for specified cities using the OpenWeatherMap API. It consists of a Python script for fetching weather information and a Streamlit-based web app for a user-friendly interface.

## Python Weather Retrieval Script

- **Weather Retrieval**: The Python script utilizes the OpenWeatherMap API to obtain weather data for a specified city.
- **Displaying Information**: The script presents weather details such as type, temperature (in Celsius), pressure, humidity, and country for the requested city.

## Streamlit Web App

- **User Interface**: The Streamlit web app enables users to input a city name and fetch weather details by clicking the "Get Weather" button.
- **Display Weather Information**: Upon successful retrieval, the app displays weather information including type, temperature, pressure, humidity, and wind details for the entered city.

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

## Updates

### Version 2.0.0 (January 1, 2024)

#### Changelog

- Implemented a more responsive UI for improved user experience.
- Enhanced error handling to gracefully manage API request failures.
- Added support for displaying wind speed and direction.
- Updated dependencies to the latest versions (`requests`, `streamlit`).

## License

This project is licensed under the [MIT License](LICENSE).
