import turtle, math

def main():
    n = 10
    size = 100
    
    t = turtle.Turtle()
    t.speed(0)
    #t.hideturtle()
    t.setheading(180)
    t.penup()
    t.backward(450)
    t.pendown()
    angle = 90
    
    getString = sierpLSys("A")
    for i in xrange(n):
        sizeToDraw = size/(math.pow(3, i-1))
        drawFrom(getString, t, sizeToDraw)
        
        getString = sierpLSys(getString)
        
        #print i, sizeToDraw
        t.penup()
        t.setheading(t.heading() + angle)
        t.forward(10)
        t.setheading(t.heading() + angle)
        t.pendown()

        angle = -1*angle

    t.getscreen()._root.mainloop()

def sierpLSys(begin):
    newString = []
    for char in begin:
        if char == "A":
            newString.append("ABA")
        elif char == "B":
            newString.append("BBB")
    return "".join(newString)

def drawFrom(drawS, t, size):
    for char in drawS:
        if char == "A":
            t.forward(size)
        elif char == "B":
            t.penup()
            t.forward(size)
            t.pendown()

main()