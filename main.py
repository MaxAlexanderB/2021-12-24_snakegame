#---------imports-------#

from turtle import Screen
from snakebuild import Snake
from food import Food
from scoreboard import ScoreBoard


#---------Display---------#
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
score=0

#----------Initiate snake-------#
snake = Snake()
food = Food()
scoreboard = ScoreBoard()


#---------key settings with snake movement methods--------#
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.update()


#-----------start game---------#
game_is_on = True
while game_is_on == True:
    screen.update()
    snake.snake_move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.score += 1
        food.refresh()
        snake.extend()
        scoreboard.refresh()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.game_over()
        game_is_on=False


    #detection with tail: with slices
    for squares in snake.squares[2:]:
        if snake.head.distance(squares) < 10:
            snake.reset()
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
