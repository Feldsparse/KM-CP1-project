#charles m: racing tutels
import random
turtles = 0
import turtle as tutel_red
import turtle as tutel_blue
import turtle as tutel_yellow
import turtle as tutel_black
import turtle as tutel_green
import turtle as tutel_zomp #yes that's a real color look it up

tutel_red.shape("turtle") 
tutel_red.pencolor("red")
tutel_red.fillcolor("red")

tutel_blue.shape("turtle") 
tutel_blue.pencolor("blue")
tutel_blue.fillcolor("blue")

tutel_yellow.shape("turtle") 
tutel_yellow.pencolor("yellow")
tutel_yellow.fillcolor("yellow")

tutel_black.shape("turtle")

tutel_green.shape("turtle") 
tutel_green.pencolor("green")
tutel_green.fillcolor("greem")

tutel_yellow.shape("turtle") 
tutel_zomp.pencolor("zomp")
tutel_zomp.fillcolor("zomp")

tutel_red.teleport(-200, 400)
tutel_red.showturtle

tutel_red.teleport(-200, 400)
tutel_blue.showturtle

while True:
    tutel_red.forward(random.randint(1,11))
    tutel_blue.forward(random.randint(1,11))
    tutel_yellow.forward(random.randint(1,11))
    tutel_black.forward(random.randint(1,11))
    tutel_green.forward(random.randint(1,11))
    tutel_zomp.forward(random.randint(1,11))