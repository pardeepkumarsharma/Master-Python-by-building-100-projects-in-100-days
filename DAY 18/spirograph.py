from turtle import Turtle, Screen , colormode
import random

tim = Turtle()
tim.shape("turtle")
colormode(255)
tim.speed(0)
#colors = ["CornflowerBlue","DarkOrchid","Green","Red","Blue"]

def draw_spirograph(size_of_gap):


    for i in range(int(360/size_of_gap)):
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)
        tim.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


draw_spirograph(5)
screen=Screen()
screen.exitonclick()