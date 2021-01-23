import pandas

data = pandas.read_csv("data.csv")
grey_squirrels = data[data["Primary Fur Color"] == "Grey"]
print(grey_squirrels)

