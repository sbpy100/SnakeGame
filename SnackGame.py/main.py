from turtle import Screen,Turtle
from food import Food
from scorebord import Scorebord
from snake import snake
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("red")
screen.title("welcome to the game")
screen.tracer(0)

snake = snake()
food=Food()
scorebord=Scorebord()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.2)


    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scorebord.increse_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280 :
        game_is_on=False
        scorebord.game_over()

    for segment in snake.segment[1:]:   # slicing of list
        
        if snake.head.distance(segment)<10:
            game_is_on=False
            scorebord.game_over()



screen.exitonclick()
