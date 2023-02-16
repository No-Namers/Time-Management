from graphics import *

def main():
    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(0,0,0))

    c = Circle(Point(100, 100), 50)
    c.setFill(color_rgb(255,0,0))
    c.draw(win)

    pt1=Point(100,150)
    pt2=Point(150,200)
    li=Line(pt1,pt2)
    li.setOutline(color_rgb(0,255,255))
    li.draw(win)

    win.getMouse() 
    win.close()    # Close window when done

main()