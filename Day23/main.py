import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create a turtle and animate it by pressing "UP"
player = Player()
screen.listen()
screen.onkey(player.move, "Up")

scoreboard = Scoreboard()

cars = []
for _ in range(20):
    cars.append(CarManager())

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate moving cars at random points of Y axel
    for i in range(len(cars)):
        cars[i].move_car()
        # Make cars reset if they reach the left wall
        if cars[i].xcor() < -320:
            cars[i].reset()
        # Detect turtle collision with cars
        if cars[i].distance(player) < 20:
            # Game Over
            scoreboard.game_over()
            game_is_on = False

    # Detect turtle reaching the finish line
    if player.ycor() == player.finish_line:
        # Reset turtles position
        player.reset()
        # Upgrade level
        scoreboard.level_up()
        # Increase cars' speed
        for i in range(len(cars)):
            cars[i].increase_speed()



screen.exitonclick()