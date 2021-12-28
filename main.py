from turtle import Screen, Turtle
import pandas

us_states = pandas.read_csv('50_states.csv')
states = us_states.state
guessed_states = []

# Main Setup
screen = Screen()
root = Screen()._root
root.iconbitmap('UnitedStates.ico')
screen.setup(width=725, height=496)
screen.bgpic('blank_states_img.gif')
screen.title('Fill-in The U.S.')

pen = Turtle()
pen.pu()
pen.hideturtle()

while True:
    guess = screen.textinput('Finished? Type "quit"', "Name a state").title()
    if guess == 'Quit':
        break
    for state in states:
        if guess == state:
            guessed_states.append(guess)
            x = int(us_states[states == guess].x)
            y = int(us_states[states == guess].y)
            pen.goto(x, y)
            pen.write(guess)


for state in states:
    if state not in guessed_states:
        x = int(us_states[states == state].x)
        y = int(us_states[states == state].y)
        pen.color("red")
        pen.goto(x, y)
        pen.write(state)
screen.exitonclick()