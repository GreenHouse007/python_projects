from turtle import Turtle, Screen
import random
import colorgram

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(11)
tim.hideturtle()
tim.penup()
t_y = -200
t_x = -250

my_colors=[ (218, 148, 104), (35, 101, 168), (158, 57, 87), (142, 82, 55), (115, 173, 213), (240, 225, 96),
            (218, 128, 157), (166, 23, 42), (216, 67, 100), (224, 83, 57), (119, 183, 137), (78, 38, 25),
            (22, 169, 201), (159, 151, 34), (45, 125, 81), (16, 58, 141), (121, 40, 30), (50, 185, 155), (18, 39, 87),
            (134, 234, 190), (240, 164, 154), (234, 163, 181), (98, 103, 185), (134, 214, 234), (75, 33, 45),
            (23, 91, 55)]

def random_color():
    selected_color = random.choice(my_colors)
    tim.color(selected_color)

def draw():
    for _ in range(10):
        tim.dot(25, random.choice(my_colors))
        tim.forward(50)

for _ in range(10):
    tim.goto(t_x, t_y)
    draw()
    t_y += 50
    tim.goto(t_x, t_y)

screen.exitonclick()


# EXTRACT COLORS ----
# colors = colorgram.extract('Hirst.jpg', 30)
#
# rgb_colors =[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

