import turtle
import pandas
from scoreboard import Scoreboard

states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].to_list()
lower_states_list = []
for state in states_list:
    l_state = state.lower()
    lower_states_list.append(l_state)

game_is_on = True

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
sc = Scoreboard()

guessed_states = []

def get_cor(answer):
    state_name = answer.title()
    state_row = states_data[states_data["state"] == state_name]

    x_coord = state_row["x"].iloc[0]
    y_coord = state_row["y"].iloc[0]

    return x_coord, y_coord

while game_is_on:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").lower().strip()
    if answer_state in guessed_states:
        continue
    elif answer_state not in lower_states_list:
        continue
    else:
        sc.update_scoreboard()
        
        x_coord, y_coord = get_cor(answer_state)
        sc.create_state_label(answer_state, x_coord, y_coord)
        
        guessed_states.append(answer_state)
        
        if len(guessed_states) == 50:
            print("You guessed all the states!")
            game_is_on = False

screen.exitonclick()