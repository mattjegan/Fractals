import turtle

def main():
    n = 13
    size = 1
    
    getString = sierpLSys("AB")
    for i in xrange(n):
        getString = sierpLSys(getString)
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.setheading(180)
    t.penup()
    t.backward(200)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.pendown()
    drawFrom(getString, t, size)
    
    t.getscreen()._root.mainloop()

def sierpLSys(begin):
    newString = []
    for char in begin:
        if char == "A":
            newString.append("B-A-B")
        elif char == "B":
            newString.append("A+B+A")
        else:
            newString.append(char)
    return "".join(newString)

def drawFrom(drawS, t, size):
    half = len(drawS)/2
    count = 0
    angle = 60
    for char in drawS:
        if count == half:
            break
        if char == "A" or char == "B":
            t.forward(size)
        elif char == "+":
            t.setheading(t.heading() - angle)
        elif char == "-":
            t.setheading(t.heading() + angle)
        count += 1

main()