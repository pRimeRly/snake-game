# Snake Xenzia Game
This is a clone of the popular classic game Snake, created using the Turtle module in Python. The game involves controlling a snake to eat food and grow longer, while avoiding collision with the walls and the snake's own tail. The score increases as the snake eats food, and the game ends when the snake collides with the walls or its own tail.

## Files
The game consists of four Python files:
```
main.py: This file contains the main game loop and controls the interaction between the different game components. It imports the Snake, Food, and Scoreboard classes from their respective modules, and sets up the game window using the turtle.Screen() function from the Turtle module.

snake.py: This file contains the Snake class, which represents the snake in the game. The class includes methods for moving the snake, extending its length, and changing its direction.

food.py: This file contains the Food class, which represents the food that the snake can eat to increase its score. The class includes a refresh() method that randomly places the food on the screen and changes its shape and color.

scoreboard.py: This file contains the Scoreboard class, which displays the player's score and high score on the screen. The class includes methods for updating the score, resetting the score after a collision, and writing the high score to a file.
```

## How to Play
```
To start the game, run the main.py file in a Python environment. The game window will appear, and the snake will start moving automatically. Use the arrow keys or the W, A, S, and D keys to control the direction of the snake.

The objective of the game is to eat as much food as possible to increase the score. The snake will grow longer each time it eats food. If the snake collides with the walls or its own tail, the game ends and the score is reset.

The high score is saved to a file (data.txt), and will be displayed at the top of the screen along with the current score.
```

## Dependencies
1. Python 3.x
2. Turtle module (built-in with Python)
