from turtle import Turtle, Screen , colormode
import random

screen=Screen()
screen.listen()

is_race_on = False
all_turtles = []
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def move_left():
#     new_heading = tim.heading()+10
#     tim.setheading(new_heading)
#
#
# def move_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.onkey(key="w",fun=move_forwards)
# screen.onkey(key="s",fun=move_backwards)
# screen.onkey(key="a",fun=move_left)
# screen.onkey(key="d",fun=move_right)
# screen.onkey(key="c",fun=clear)

# colormode(255)
# tim.speed(0)
# tim.penup()
# tim.setheading(225)
# tim.forward(250)
# tim.setheading(0)
# tim.hideturtle()


screen.exitonclick()

