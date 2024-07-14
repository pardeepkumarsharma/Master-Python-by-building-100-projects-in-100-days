from turtle import Turtle, Screen , colormode
import random

colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.pensize(10)
tim.speed(0)
#colors = ["CornflowerBlue","DarkOrchid","Green","Red","Blue","SeaGreen","wheat"]
directions=[0,90,180,270]
for i in range(100):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

screen=Screen()
screen.exitonclick()