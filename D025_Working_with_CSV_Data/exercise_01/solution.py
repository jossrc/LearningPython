import pandas

data = pandas.read_csv("data.csv").groupby(["Primary Fur Color"])

data.size().to_csv("squirrel_counts.csv", header=["Count"])
