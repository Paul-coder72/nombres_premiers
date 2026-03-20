import turtle
from main import *
from liste_premiers import liste

res = int(input("resolution: "))

turtle.tracer(0)
t = turtle.Turtle()
t.penup()
t.hideturtle()
t.speed(0)

distance_a_avancer = 1
index = 0

set_premiers = set(liste)

boucle = 1000 
while boucle:
    for i in range(2):
        for j in range(distance_a_avancer):
            if index in set_premiers:
                t.dot(res + 1, "black")
            t.forward(res)
            index += 1
        t.left(90)
    
    if boucle % 100 == 0:
        turtle.update()
        
    distance_a_avancer += 1
    boucle -= 1

turtle.update()
turtle.done()