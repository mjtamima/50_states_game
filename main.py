import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state?").title()
    if answer_state == "Exit":
        not_guessed = [state for state in state_list if state not in guessed_states]
        df = pandas.DataFrame(not_guessed)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)
        st_name = turtle.Turtle()
        st_name.hideturtle()
        st_name.penup()
        st_row = data[data.state == answer_state]
        st_name.goto(int(st_row.x), int(st_row.y))
        st_name.write(answer_state)
