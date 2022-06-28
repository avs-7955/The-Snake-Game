# TODO03: Create snake food
# TODO04: Detect collision with food
# TODO05: Create a scoreboard
# TODO06: Detect collision with wall
# TODO07: Detect collision with tail

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# SETTING UP THE SCREEN
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
# used to turn turtle animation on or off and set a delay for update drawings
my_screen.tracer(0)

snake = Snake()  # CREATING THE SNAKE
food = Food()
scoreboard = ScoreBoard()

my_screen.listen()  # Listening to key strokes for moving the snake.
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

my_screen.update()

# MOVING THE SNAKE BODY
game_condition = True
while game_condition:
    # All three segments move forward before the screen is updated.
    my_screen.update()
    time.sleep(0.5)  # For controlling the speed of the snake.
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        scoreboard.increment_score()
        snake.extend_snake()
        food.refresh()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_condition = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.all_snake_parts[1:]:
        if segment.distance(snake.head) < 10:
            game_condition = False
            scoreboard.game_over()

my_screen.exitonclick()
