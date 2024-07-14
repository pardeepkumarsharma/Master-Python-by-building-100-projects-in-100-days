from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
colors = ["CornflowerBlue","DarkOrchid","Green","Red","Blue"]
for i in range(3,10):
    for j in range(i):
        tim.forward(100)
        tim.right(360//i)
    tim.color(random.choice(colors))



screen=Screen()
screen.exitonclick()