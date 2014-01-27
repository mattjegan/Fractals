import turtle

angle = 60
divF = 0.5
startSize = 600
startDepth = 7
height = 275

def main():
    t = turtle.Turtle()
    turtle.setup(width=1280, height=600)
    turtle.colormode(255)
    t.speed(0)
    t.penup()
    t.left(90)
    t.backward(height)
    t.right(90)
    t.backward(startSize/2)
    t.pendown()
    drawTri(t, startSize, startDepth)

    t.getscreen()._root.mainloop()

def drawTri(t, size, depth):
    if depth == 0:
        return

    #base
    t.forward(size/2)
    drawTri(t, size*divF, depth-1)
    t.forward(size/2)
    t.left(180-angle)

    # right side
    t.forward(size)
    t.left(180-angle)

    # left side
    t.forward(size/2)
    t.left(180-angle)
    drawTri(t, size*divF, depth-1)
    t.right(180-angle)
    t.forward(size/2)
    t.left(180-angle)
    drawTri(t, size*divF, depth-1)

if __name__ == "__main__": main()
