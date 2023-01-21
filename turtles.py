from turtle import  Turtle, Screen
import random
race_on=False
screen= Screen()
screen.setup(500,400)
choix=screen.textinput("color choice","choose ur turtule color:")
couleur = ["red","orange","yellow","blue","green","purple","black"]
positions =[80,40,0,-40,-80,-120,-160]
turtles=[]
array=[]
array = [0 for i in range(7)]
for idex in range(0,7):
    tim =Turtle(shape="turtle")
    tim.color(couleur[idex])
    tim.penup()
    tim.goto(x=-230,y=positions[idex])
    turtles.append(tim)
if choix:
    race_on=True
while race_on:
    for i in range(0,7):
        rand_dist=random.randint(0,10)
        turtles[i].forward(rand_dist)
        array[i]+=rand_dist
        if array[i]>=450:
            race_on=False
            if couleur[i]==choix:
                print("Your turtle won")
            else:
                print("the "+couleur[i]+" turtle won and you lost")
screen.exitonclick()