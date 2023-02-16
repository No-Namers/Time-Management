import calendar
from graphics import *
import datetime as dt

def showtodoListPane(win, date):

    win = GraphWin("ToDoList", 500, 500)
    #win.setBackground(color_rgb(0,0,0))

    pt=Point(0, 0)

    exitrec=Rectangle(Point(450, 450), Point(490, 490))
    exitrec.setFill(color_rgb(255,0,0))
    exitrec.draw(win)

    exittext=Text(Point(470, 470), "Exit")
    exittext.setTextColor(color_rgb(255,255,255))
    exittext.draw(win)

    click_point=win.getMouse()
    if click_point.getX()>=450 and click_point.getX()<=490 and click_point.getY()>=450 and click_point.getY()<=490:
        win.close()