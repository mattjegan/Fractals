import turtle

angle = 60
divF = 0.5
startSize = 300
startDepth = 4
height = 100
points = []

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

    #t.penup()
    drawTri(t, startSize, startDepth)
    #t.pendown()
    
    #for p in points:
    #    t.goto(p[0], p[1])

    t.getscreen()._root.mainloop()

def drawTri(t, size, depth):
    if depth == 0:
        return

    #base
    t.forward(size/3)
    t.right(angle)
    points.append(t.pos())
    drawTri(t, size*divF, depth-1)
    t.left(angle)
    t.forward(size/3)
    t.forward(size/3)
    t.left(180-angle)
    points.append(t.pos())

    # right side
    t.forward(size/3)
    t.right(angle)
    points.append(t.pos())
    drawTri(t, size*divF, depth-1)
    t.left(angle)
    t.forward(size/3)
    t.forward(size/3)
    t.left(180-angle)
    points.append(t.pos())

    # left side
    t.forward(size/3)
    t.right(angle)
    points.append(t.pos())
    drawTri(t, size*divF, depth-1)
    t.left(angle)
    t.forward(size/3)
    t.forward(size/3)
    t.left(180-angle)
    points.append(t.pos())

if __name__ == "__main__": main()
