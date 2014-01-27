import turtle

angle = 30
divF = 0.7
startSize = 175
startDepth = 13
height = 275

def main():
    prompt = raw_input()
    t = turtle.Turtle()
    turtle.setup(width=1280, height=1280)
    t.hideturtle()
    turtle.colormode(255)
    ##turtle.bgcolor(0, 0, 0)
    ##t.fillcolor(0, 255, 0)
    ##t.pencolor(0, 0, 0)
    t.speed(0)
    t.penup()
    t.left(90)
    t.backward(height)
    t.pendown()

    t.forward(startSize)
    drawTree(t, startSize, startDepth)

    t.getscreen()._root.mainloop()

def drawTree(t, size, depth):
    if depth == 0:
        return
    
    ## Tree
    ##t.begin_fill()
    #t.forward(size)
    t.right(angle)
    t.forward(size)
    ## Right
    drawTree(t, size*divF, depth-1)
    t.backward(size)
    t.left(angle*2)
    t.forward(size)
    ## Left
    drawTree(t, size*divF, depth-1)
    t.backward(size)
    t.right(angle)
    #t.backward(size)
    ##t.end_fill()

    ## Right branch

    ## Left branch

if __name__ == "__main__": main()
