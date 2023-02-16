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

    createTaskrec=Rectangle(Point(10, 450), Point(100, 490))
    createTaskrec.setFill(color_rgb(0,255,0))
    createTaskrec.draw(win)

    createTasktext=Text(Point(55, 470), "Create Task")
    createTasktext.setTextColor(color_rgb(255,255,255))
    createTasktext.draw(win)

    #shows date at the top
    dateText = Text(Point(250, 15), date)
    dateText.setSize(14)
    dateText.setFace('courier')
    dateText.draw(win)

    while True:
        click_point=win.getMouse()
        if click_point.getX()>=450 and click_point.getX()<=490 and click_point.getY()>=450 and click_point.getY()<=490:
            win.close()
            break
        elif click_point.getX()>=10 and click_point.getX()<=100 and click_point.getY()>=450 and click_point.getY()<=490:
            createTask(win, date)

    click_point=win.getMouse()
    if click_point.getX()>=450 and click_point.getX()<=490 and click_point.getY()>=450 and click_point.getY()<=490:
        win.close()

def createTask(win, date):
    #this will be where the user can create a task
    return 0