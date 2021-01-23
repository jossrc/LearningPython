import pandas

"""
    Pandas es un paquete que permite trabajar, manipular y analisar los datos
    de manera óptima. En el caso de trabajar con archivos csv, este lo hace
    muchísimo mejor que el paquete csv.
    Este requiere que la primera fila del archivo sean los títulos que representarán
    cada columna
"""

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
