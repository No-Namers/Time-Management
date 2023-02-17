import calendar
from graphics import *
import datetime as dt

def showtodoListPane(date):

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

    readTasks(win, date)

    click_point=win.getMouse()
    if click_point.getX()>=450 and click_point.getX()<=490 and click_point.getY()>=450 and click_point.getY()<=490:
        win.close()
    elif click_point.getX()>=10 and click_point.getX()<=100 and click_point.getY()>=450 and click_point.getY()<=490:
        createTask(win, date)

def createTask(win, date):
    #create a Text object to hold the calendar output
    taskText = Text(Point(250, 250), "")
    taskText.setSize(14)
    taskText.setFace('courier')
    taskText.draw(win)

    txt = Text(Point(250, 15), "Enter the task:")
    txt.setTextColor(color_rgb(0,0,0))
    txt.setSize(14)
    txt.setFace('courier')
    txt.draw(win)

    input_box = Entry(Point(250, 50), 20)
    input_box.draw(win)

    txt=Text(Point(250, 100), "")
    txt.draw(win)

    while True:
        click_point=win.getMouse()
        if click_point.getX()>=450 and click_point.getX()<=490 and click_point.getY()>=450 and click_point.getY()<=490:
            win.close()
            break
        elif click_point.getX()>=10 and click_point.getX()<=100 and click_point.getY()>=450 and click_point.getY()<=490:
            taskText.setText(input_box.getText())
            #save task to file
            file = open("todoList.txt", "a")
            file.write(date + " " + input_box.getText()+"\n")
            file.close()
            break

def readTasks(win, date):
    #create a Text object to hold the calendar output
    taskText = Text(Point(250, 250), "")
    taskText.setSize(14)
    taskText.setFace('courier')
    taskText.draw(win)

    file = open("todoList.txt", "r")
    tasks = file.read()
    file.close()

    tasks = tasks.split("\n")

    