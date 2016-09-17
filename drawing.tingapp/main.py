import tingbot
from tingbot import *
from itertools import cycle

state = {
    'previous_xy': None,
    'color': 'black'
}
colors = cycle(['black', 'blue', 'green', 'orange'])

screen.fill(color='white')

@left_button.hold
def clear():
    screen.fill(color='white')

@right_button.press
def next_color():
    state['color'] = colors.next()
    screen.rectangle(
        size=(25,15),
        color=state['color'],
        align='topright')
        
next_color()

@touch()
def on_touch(xy, action):
    if state['previous_xy']:
        screen.line(
            state['previous_xy'],
            xy,
            width=5,
            color=state['color'])

    if action == 'up':
        state['previous_xy'] = None
    else:
        state['previous_xy'] = xy

tingbot.run()