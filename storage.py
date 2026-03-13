import csv
import datetime
import os
file_name = "weather_history.csv"

def intialize_csv():
    if not os.path.exists(file_name):
        # Create the CSV file and write the header if it doesn't exist
        # if file exist and it is empty then also write the header 
        with open(file_name,'w',newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date","City","Weather","Temperature","Wind Speed"])
def save_weather_data(data):
    intialize_csv()
    with open(file_name,"a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.datetime.now().strftime("%d-%m-%Y"),data["name"],data["weather"][0]["description"],data["main"]["temp"],data["wind"]["speed"]])


