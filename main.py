from weather_api import get_weather_data
from storage import file_name
from storage import save_weather_data
from analysis import city_statistics, overall_statistics

import csv

def display_weather(data):
    city = data["name"]
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    wind_speed = data["wind"]["speed"]

    print("\n--- Weather Report ---")
    print(f"City: {city}")
    print(f"Condition: {weather}")
    print(f"Temperature: {temperature} °C")
    print(f"Wind Speed: {wind_speed} m/s")
    print("----------------------")
def view_weather_histroy():
    with open(file_name,'r') as file:
        content = csv.reader(file)
        next(content)  # skip header
        print("Date         City            Weather             Temperature(°C)         Wind Speed(m/s)")
        print("---------------------------------------------------------------------------------------------")
        for row in content:
            print(f"{row[0]}     {row[1]}     {row[2]}              {row[3]}                 {row[4]}")

if __name__ == "__main__":
    while True:
        print("Select an option:")
        print("1. Display Weather")
        print("2. View Weather History")
        print("3. Show statistics")
        print("4. Overall Search Statistics")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            city = input("Enter city name: ")
            data = get_weather_data(city)
            display_weather(data)
            save_weather_data(data)
        elif choice == '2':
            view_weather_histroy()
        elif choice == '3':
            city = input("Enter city name for statistics: ")
            city_statistics(city)
        elif choice == '4':
            print("Overall Search Statistics:")
            overall_statistics()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
