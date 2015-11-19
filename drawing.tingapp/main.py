import tingbot
from tingbot import *

screen.fill(color='blue')

@touch()
def on_touch(xy):
    screen.rectangle(xy=xy, size=(5,5), color='white')

# run the app
tingbot.run()
