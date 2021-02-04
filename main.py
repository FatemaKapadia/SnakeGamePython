from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

s = Snake()
food = Food()
scoreb = Scoreboard()
# file=open("high_score.txt")
# print(file)

isOn = True

while isOn:
    s.move()
    screen.update()
    time.sleep(0.1)

    screen.onkeypress(key="Up", fun=s.turnUp)
    screen.onkeypress(key="Down", fun=s.turnDown)
    screen.onkeypress(key="Left", fun=s.turnLeft)
    screen.onkeypress(key="Right", fun=s.turnRight)

    if s.isOverlap():
        isOn = False

    if s.head.distance(food) <= 15:
        food.newLocation()
        scoreb.increaseScore()
        s.addSegment()

    if s.head.xcor() > 280 or s.head.xcor() < -280 or s.head.ycor() > 230 or s.head.ycor() < -280:
        isOn = False

scoreb.endGame()

screen.exitonclick()
