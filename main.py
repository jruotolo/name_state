import turtle
import pandas



screen = turtle.Screen()
image = 'blank_states_img.gif'
screen.title(f'Named the States')
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guesses = []

while len(guesses) < 50:

    guess = screen.textinput(title=f'Named States {len(guesses)}/50',
                             prompt='Type the name of a State below').title()
    if guess == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if guess in all_states:
        guesses.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())











