from turtle import Turtle, Screen
import random, os
import colorgram

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

t = Turtle()
s = Screen()

t.speed("fastest")
s.colormode(255)
no_of_dots = input("Enter the number of dots: ")
print(s.screensize())
print(no_of_dots)

s.exitonclick()