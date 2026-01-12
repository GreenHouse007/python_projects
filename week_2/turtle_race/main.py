from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
all_turtles = []

colors = ["red", "blue", "green", "yellow", "orange", "purple"]
starting_location = 130
for color in colors:
    my_turtle = Turtle(shape="turtle")
    my_turtle.color(color)
    my_turtle.penup()
    my_turtle.goto (-240, starting_location)
    starting_location -= 50
    all_turtles.append(my_turtle)

user_bet = (screen.textinput(title="Make your bet", prompt="Which turtle will win the race? \n(red, blue, green, yellow, orange, purple)\nEnter a color: ").strip().lower())

if user_bet:
    is_race_on = True

while is_race_on:
    random_distance = random.randint(0,10)

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You Lost. The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
