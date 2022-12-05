def app():
    from turtle import Screen
    from snake import Snake
    from food import Food
    from scoreboard import Scoreboard
    import time

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Xenzia")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    game_is_on = True
    screen.listen()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")

    while game_is_on:
        screen.update()
        time.sleep(0.15)
        snake.move()
        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()
        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.reset_score()
            snake.reset_snake()
        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 15:
                scoreboard.reset_score()
                snake.reset_snake()

    screen.exitonclick()


try:
    app()
except Exception:
    pass
