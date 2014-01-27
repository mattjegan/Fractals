import turtle
import random

divF = 0.8
angle = 60
startSize = 1
startDepth = 10
turtles = []
maxTurtles = 50
minSize = 0

def main():
    t = turtle.Turtle()
    turtle.setup(width=1280, height=600)
    turtle.colormode(255)
    t.hideturtle()
    t.speed(0)
    brownianFractal(t, startSize, startDepth)
    t.getscreen()._root.mainloop()

def brownianFractal(t, size, depth):
    if depth == 0 or size < minSize:
        return

    #print len(turtles)

    if len(turtles) < maxTurtles:
        turtles.append(t.clone())

    t.forward(size)
    t.right(random.randint(-angle, angle))
    for turt in turtles:
        brownianFractal(turt, size, depth-1)

if __name__ == "__main__": main()