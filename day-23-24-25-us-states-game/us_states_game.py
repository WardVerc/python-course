import turtle
import pandas
import state_label


screen = turtle.Screen()
screen.setup(740, 500)
screen.title("US States Quiz")
screen.bgpic('./blank_states_img.gif')
data = pandas.read_csv("50_states.csv")


# data["state"] = data.state
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(f"{len(guessed_states)}/50", "Guess a name of a state:").lower()

    if answer == "exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer.title() in all_states:
        row = data[data.state == answer.title()]
        guessed_states.append(row.state.item())
        label = state_label.Label(row.state.item(), (int(row.x), int(row.y)))
