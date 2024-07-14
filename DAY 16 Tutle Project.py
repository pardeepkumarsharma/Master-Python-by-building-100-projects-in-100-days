# from turtle import *
#
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("orange")
# timmy.forward(200)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"],
    ]
)
table.align = 'r'
print(table)
