import pandas

"""
    Pandas es un paquete que permite trabajar, manipular y analisar los datos
    de manera óptima. En el caso de trabajar con archivos csv, este lo hace
    muchísimo mejor que el paquete csv.
    Este requiere que la primera fila del archivo sean los títulos que representarán
    cada columna
"""

data = pandas.read_csv("weather_data.csv")
# print(type(data)) -> DataFrame
# print(type(data["temp"])) -> Series

print(data.to_dict())

series_temp = data["temp"]
print(series_temp)

temp_list = series_temp.tolist()
print(temp_list)

# Average

average = series_temp.mean()
print(round(average, 2))

# Max

maximum_temperature = series_temp.max()
print(maximum_temperature)

# Get data in row

print(data[data.day == "Wednesday"])

print(data[data.temp == maximum_temperature])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a Dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
