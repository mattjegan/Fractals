import turtle

angle = 135
divF = 0.5
startSize = 100
startDepth = 5
height = 275

def main():
    #prompt = raw_input()
    t = turtle.Turtle()
    turtle.setup(width=1280, height=1280)
    t.hideturtle()
    turtle.colormode(255)
    t.speed(0)
    t.penup()
    t.left(90)
    t.backward(height)
    t.right(90)
    t.backward(startSize/2)
    t.pendown()
    drawOct(t, startSize, startDepth)

    t.getscreen()._root.mainloop()

def drawOct(t, size, depth):
    if depth == 0:
        return

    for i in xrange(8):
        t.forward(size/2)
        drawOct(t, size*divF, depth-1)
        t.forward(size/2)
        t.left(180-angle)

if __name__ == "__main__": main()
