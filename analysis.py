from storage import file_name
import csv


def city_statistics(city_name):

    list_of_rows = []
    max_temp = float('-inf')
    min_temp = float('inf')
    Avg_Temp = 0
    Avg_wind = 0
    i = 0

    with open(file_name, 'r') as file:
        content = csv.reader(file)
        next(content)  # skip header

        for row in content:
            if city_name.lower() == row[1].lower():
                list_of_rows.append(row)

    if len(list_of_rows) == 0:
        print(f"No data found for city: {city_name}")
        return

    for row in list_of_rows:

        temp = float(row[3])
        wind = float(row[4])

        if temp > max_temp:
            max_temp = temp

        if temp < min_temp:
            min_temp = temp

        i += 1
        Avg_Temp += temp
        Avg_wind += wind

    Avg_Temp = Avg_Temp / i
    Avg_wind = Avg_wind / i

    print(f"Maximum temperature recorded for {city_name} is: {max_temp:.2f} °C")
    print(f"Minimum temperature recorded for {city_name} is: {min_temp:.2f} °C")
    print(f"Average temperature recorded for {city_name} is: {Avg_Temp:.2f} °C")
    print(f"Average wind speed recorded for {city_name} is: {Avg_wind:.2f} m/s")
    print(f"Total number of records for {city_name} is: {i}")


def overall_statistics():

    max_temp = float('-inf')
    min_temp = float('inf')
    Avg_Temp = 0
    i = 0

    hottest_city = ""
    coldest_city = ""

    with open(file_name, 'r') as file:

        content = csv.reader(file)
        next(content)  # skip header

        for row in content:

            city = row[1]
            temp = float(row[3])

            # hottest city
            if temp > max_temp:
                max_temp = temp
                hottest_city = city

            # coldest city
            if temp < min_temp:
                min_temp = temp
                coldest_city = city

            Avg_Temp += temp
            i += 1

    if i == 0:
        print("No weather data available.")
        return

    Avg_Temp = Avg_Temp / i

    print(f"The hottest city recorded is: {hottest_city} with a temperature of {max_temp:.2f} °C")
    print(f"The coldest city recorded is: {coldest_city} with a temperature of {min_temp:.2f} °C")
    print(f"The average temperature recorded across all cities is: {Avg_Temp:.2f} °C")
