# Weather Data Analyzer (CLI)

Weather Analyzer is a Python project that collects weather data using a public weather API and analyzes it to generate useful statistics for different cities.

The project demonstrates working with APIs, file handling, data processing, and basic data analysis using Python. Weather data is stored locally and can be used to calculate statistics such as average temperature and city-based comparisons.

It is a command line application that fetches real-time weather data using the OpenWeather API and analyzes stored weather search history.

## Features

- Fetch real-time weather data for any city
- Display weather information:
  - City
  - Temperature
  - Weather condition
  - Wind speed
- Store weather searches in CSV
- View search history
- City-based weather statistics
- Overall weather statistics:
  - Hottest city recorded
  - Coldest city recorded
  - Average temperature
  - Most searched city

## Technologies Used

- Python
- Requests library
- CSV storage
- REST API (OpenWeather)

## Project Structure
weather-analyzer/
│
├── config.py
├── weather_api.py
├── storage.py
├── analysis.py
├── main.py
├── weather_history.csv


## Installation

Clone the repository:
Install dependencies:


pip install -r requirements.txt


## Run the Application


python main.py


## Learning Objectives

This project demonstrates:

- API integration
- JSON data parsing
- CSV data storage
- Data analysis using Python
- Modular project structure
