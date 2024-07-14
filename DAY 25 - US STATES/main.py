import csv
import pandas

# with open("weather_data.csv","r") as file:
#     weather_info = file.readlines()
#
# print(weather_info)

# with open("weather_data.csv","r") as file:
#     weather_info = csv.reader(file)
#     temperatures = []
#     for row in weather_info:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

data = pandas.read_csv("weather_data.csv")
print(data["temp"])