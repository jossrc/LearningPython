from prettytable import PrettyTable
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

timmy.shape("turtle")
timmy.color("DeepSkyBlue2")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

print(table)

my_screen.exitonclick()
