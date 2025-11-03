import csv
import pandas


"""
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)

    temperatures = []
    for row in data:
        if row[1].isalpha():
            pass
        else:
            temperatures.append(int(row[1]))

    print(temperatures)
"""

"""
data =pandas.read_csv("weather_data.csv")
temp_data = data["temp"].to_list()

combined = 0
for temp in temp_data:
    combined += temp

print(round(combined / len(temp_data), 2))

print(data["temp"].max())
"""

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250924.csv")
furColor = squirrel_data["Primary Fur Color"].to_list()

gray = 0
cinnamon = 0
black = 0

for color in furColor:
    if color == "Black":
        black += 1
    elif color == "Cinnamon":
        cinnamon += 1
    elif color == "Gray":
        gray += 1

furColorData = {
    "Gray": [gray],
    "Cinnamon": [cinnamon],
    "Black": [black]
}

results = pandas.DataFrame(furColorData)

print(results)


#or the same with pandas:

pandasResults = squirrel_data["Primary Fur Color"].value_counts()
print(pandasResults)