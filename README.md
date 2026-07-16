<h1>pyGDE (Python Game Development Engine) Documentation</h1>
Overview
pyGDE is a lightweight Python game development engine built on top of Pygame. It provides an intuitive interface for creating 2D games and graphical applications with simplified object management, event handling, and rendering.

Version: 1.0.0
License: MIT
Creator: MACsepehri
GitHub: https://github.com/MACsepehri/pyGameDevelopmentEngine

Table of Contents
Installation

Quick Start

Core Classes

Window

Object

Button

Font

Text

Key Constants

Debugging and Logging

Exception Handling

Examples

API Reference

Installation
Prerequisites
Python 3.x

Pygame library

Install Pygame
bash
pip install pygame
# or
pip3 install pygame
Import pyGDE
python
import pygde  # Your engine file name
Quick Start
Here's a minimal example to get you started:

python
import pygde

# Create a window
window = pygde.Window(size=(800, 600), title="My Game")

# Create a rectangle object
rect = pygde.Object(x=100, y=100, win_object=window, outer=True)
rect.draw_rect(width=100, height=50, color=(255, 0, 0))

# Run the game
window.run()
Core Classes
Window
The main window class that manages the game display and event loop.

Constructor
python
Window(size=None, title="GDE", fullscreen=False, icon=None)
Parameters:

size (tuple): Window dimensions (width, height). Defaults to full screen.

title (str): Window title. Default: "GDE".

fullscreen (bool): Enable fullscreen mode. Default: False.

icon (str): Path to window icon image file.

Methods
fill_color(color)
Fills the window background with a color.

python
window.fill_color((0, 0, 255))  # RGB tuple
window.fill_color("black")      # Named color
add_event_listener(event_type=None, func=None)
Adds custom event handlers.

python
def on_quit():
    print("Game exiting...")

window.add_event_listener("quit", on_quit)
quit_game()
Exits the game and triggers any quit event listeners.

update_window(func)
Sets a function to be called every frame for custom updates.

python
def update():
    # Custom update logic
    pass

window.update_window(update)
press_key(key, callback_func)
Checks if a specific key is pressed and executes the callback.

python
def jump():
    print("Jump!")

window.press_key(pygde.keyboard['space'], jump)
delay(seconds)
Pauses execution for the specified number of seconds.

python
window.delay(2.0)  # Wait 2 seconds
run()
Starts the main game loop. This must be called last.

Object
Base class for all game objects (images, rectangles, circles).

Constructor
python
Object(x=0, y=0, win_object=None, outer=True)
Parameters:

x, y (int): Initial position.

win_object (Window): Parent window object.

outer (bool): If True, object can move outside window bounds. If False, object stays within window.

Methods
render_image(img_path)
Loads and renders an image.

python
obj.render_image("assets/player.png")
draw_rect(width, height, color)
Draws a rectangle.

python
obj.draw_rect(100, 50, (255, 0, 0))
draw_circle(color, radius, thickness=0)
Draws a circle.

python
obj.draw_circle((0, 255, 0), 30, 2)
collision(obj: Object)
Checks collision with another object.

python
if player.collision(enemy):
    print("Hit!")
get_pos()
Returns current position as tuple (x, y).

python
pos = obj.get_pos()
add_move_condition(key, direction, speed, callback_action=None)
Adds keyboard movement controls.

python
# Move right with 'd' key
obj.add_move_condition(pygde.keyboard['d'], "right", 5)

# Move up with 'w' and trigger callback
def on_move():
    print("Moving up!")

obj.add_move_condition(pygde.keyboard['w'], "up", 3, on_move)
callback_keyboard_action()
Processes all keyboard movement conditions. Called automatically in the game loop.

Button
A specialized Object class for interactive buttons.

Constructor
python
Button(x, y, width, height, font=None, text="", middle=False, 
       text_color="white", button_color="black", hover_color=(21,21,21), 
       image=None, r=5, win_object=None)
Parameters:

x, y (int): Position.

width, height (int): Button dimensions.

font (tuple): (font_path, size) or ("system", size).

text (str): Button label.

middle (bool): Center button horizontally.

text_color (str or tuple): Text color.

button_color (str or tuple): Background color.

hover_color (str or tuple): Color when hovered.

image (Surface): Optional image instead of text.

r (int): Border radius.

win_object (Window): Parent window.

Methods
draw()
Renders the button.

is_clicked()
Returns True if the button was clicked.

python
if button.is_clicked():
    print("Button pressed!")
hide()
Hides the button.

show()
Shows the button.

Font
Handles font loading and rendering.

Constructor
python
Font(font=None, size=32)
Parameters:

font (str): Font file path or "system" for default.

size (int): Font size.

Method
font()
Returns the Pygame font object.

python
my_font = Font("arial.ttf", 24).font()
Text
Creates and manages text objects.

Constructor
python
Text(font, text, color, middle=False, x=0, y=0, win_object=None)
Parameters:

font (Font): Font object.

text (str): Text content.

color (str or tuple): Text color.

middle (bool): Center text on screen.

x, y (int): Position.

win_object (Window): Parent window.

Method
draw()
Renders the text.

python
text_obj = Text(my_font, "Hello, World!", "white", middle=True, win_object=window)
text_obj.draw()
Key Constants
The keyboard dictionary provides easy access to Pygame key constants:

python
keyboard = {
    'a', 'b', 'c', ..., 'z',      # Letters
    '0' through '9',               # Numbers
    'up', 'down', 'left', 'right', # Arrow keys
    'space', 'enter', 'escape',    # Special keys
    'lshift', 'rshift',            # Shift keys
    'lctrl', 'rctrl',              # Control keys
    'lalt', 'ralt',                # Alt keys
    'num0' through 'num9',         # Numpad
    'numperiod', 'numdivide',      # Numpad operators
    'nummultiply', 'numminus', 
    'numplus', 'numenter'
}
Usage:

python
if keys[pygde.keyboard['a']]:
    print("A key pressed")
Debugging and Logging
Enable debugging or logging to troubleshoot your game:

python
pygde.DEBUG = True   # Creates debug log file
pygde.LOGGER = True  # Prints events to console
Exception Handling
Custom exceptions for error handling:

Exception	Description
IconNotFoundError	Window icon file not found
ImageNotFound	Image file not found
InvalidObjectType	Invalid object type
InvalidRgbColor	Invalid RGB color tuple
InvalidTextColor	Invalid text color name
InvalidColor	Invalid color format
InvalidCallbackFunction	Invalid callback function
InvalidKey	Invalid key constant
InvalidFont	Invalid font
InvalidFontSize	Invalid font size
FontNotFound	Font file not found
Usage:

python
try:
    window.fill_color("invalid_color")
except pygde.InvalidTextColor:
    print("Invalid color name!")
Examples
Complete Game Example
python
import pygde

# Enable debugging
pygde.DEBUG = True

# Create window
window = pygde.Window(size=(800, 600), title="My Pygame Game")

# Create player
player = pygde.Object(x=400, y=300, win_object=window, outer=False)
player.draw_rect(50, 50, (0, 255, 0))

# Add movement controls
player.add_move_condition(pygde.keyboard['w'], "up", 5)
player.add_move_condition(pygde.keyboard['s'], "down", 5)
player.add_move_condition(pygde.keyboard['a'], "left", 5)
player.add_move_condition(pygde.keyboard['d'], "right", 5)

# Create button
button = pygde.Button(
    x=350, y=400, width=100, height=50,
    text="Quit", font=("system", 24),
    button_color=(50, 50, 50),
    hover_color=(100, 100, 100),
    text_color="white",
    win_object=window
)

# Create text
font = pygde.Font("system", 36)
title = pygde.Text(font, "My Game", "white", middle=True, win_object=window)
title.y = 50

# Game update function
def game_update():
    # Fill background
    window.fill_color("black")
    
    # Draw title
    title.draw()
    
    # Update player position
    player.callback_keyboard_action()
    
    # Draw button
    button.draw()
    
    # Check button click
    if button.is_clicked():
        window.quit_game()

# Set update function
window.update_window(game_update)

# Run the game
window.run()
API Reference
Global Variables
keyboard - Dictionary of key constants

DEBUG - Boolean for debugging mode

LOGGER - Boolean for console logging

Class Hierarchy
text
Object
├── Button
└── Text (uses Font)

Window
Font
Best Practices
Always call run() last - After setting up all objects and events

Use outer=False for objects you want to keep within the window bounds

Enable DEBUG during development for better error tracking

Handle exceptions gracefully using the provided exception classes

Use the middle parameter for easy centering of elements

Organize game logic in the update_window callback function

Contributing
Contributions are welcome! Please visit the GitHub repository for contribution guidelines.

License
This project is licensed under the MIT License - see the GitHub repository for details
