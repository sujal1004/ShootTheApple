# This imports the function randint() from Python’s Random module.
import pgzrun
from random import randint
apple = Actor("apple")  # This creates a new Actor called apple
# An Actor can be drawn on the screen, moved around, and even interact with other Actors in the game.
# Each Actor is given a “script” (the Python code) to tell it how to behave in the game.
HEIGHT = 500
WIDTH = 500
count = 0


def draw():
    screen.clear()
    apple.draw()


def place_apple():
    # apple.x = 300
    # apple.y = 300
    apple.x = randint(10, 400)
    apple.y = randint(10, 400)
# pos is the position of the cursor when you click the mouse.


def on_mouse_down(pos):
    # This function checks if the cursor is in the same position as the apple.
    global count
    if apple.collidepoint(pos):
        print("good shot baby")
        place_apple()
        count += 1
    else:
        print("you missed dumb")
        print("the total number of correct shoots were : ", count)
        quit()

        # place_apple()


place_apple()
pgzrun.go()
