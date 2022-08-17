import turtle
import random

tortuga = turtle.Turtle()
window = turtle.Screen()

for _ in range(random.randint(0, 3)):
    tortuga.forward(random.randint(0, 200))
    tortuga.right(random.randint(0, 50))


window.mainloop()