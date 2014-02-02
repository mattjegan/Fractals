import turtle, math

def main():
    n = 10
    size = 10
    
    t = turtle.Turtle()
    turtle.setup(width=1280, height=900)
    t.speed(0)
    t.hideturtle()
    t.penup()
    #t.goto(620, -430)
    t.pendown()
    t.setheading(180)
    
    getString = sierpLSys("F")
    for i in xrange(n-1):
        getString = sierpLSys(getString)
    
    #print getString
    drawFrom(getString, t, size)

    t.getscreen()._root.mainloop()

def sierpLSys(begin):
    newString = []
    for char in begin:
        if char == "F":
            newString.append("XF-FX")
        else:
            newString.append(char)
    ret = "".join(newString)
    return ret

def drawFrom(drawS, t, size):
    for char in drawS:
        if char == "F":
            t.forward(size)
        elif char == "f":
            t.forward(size/2)
        elif char == "x":
            t.setheading(t.heading() + 45)
        elif char == "X":
            t.setheading(t.heading() - 45)
        elif char == "+":
            t.setheading(t.heading() - 90)
        elif char == "-":
            t.setheading(t.heading() + 90)

main()