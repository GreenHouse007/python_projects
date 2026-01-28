import pandas as pd
import turtle

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    if answer_state in data.state.values:
        guessed_states.append(answer_state)
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.up()
        state_data = data[data.state == answer_state]
        pen.goto(state_data.x.item(), state_data.y.item())
        pen.write(answer_state)


screen.exitonclick()


