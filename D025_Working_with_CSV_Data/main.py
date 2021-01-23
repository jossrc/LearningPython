import csv

"""
    El paquete csv permite trabajar de manera sencilla los archivos de ese tipo,
    ya que cuenta con métodos que permiten leerlos. El método `reader()`
    retorna un objeto de tipo reader, el cual al ser trabajado en un ciclo for
    obtendremos la fila como una lista de string
"""

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
