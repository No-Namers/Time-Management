import calendar
from graphics import *
import datetime as dt
import todoListPane as tlp

def main():
    win = GraphWin("Calendar", 500, 500)
    #win.setBackground(color_rgb(0,0,0))

    pt=Point(0, 0)

    exitrec=Rectangle(Point(450, 450), Point(490, 490))
    exitrec.setFill(color_rgb(255,0,0))
    exitrec.draw(win)

    exittext=Text(Point(470, 470), "Exit")
    exittext.setTextColor(color_rgb(255,255,255))
    exittext.draw(win)

    searchrec=Rectangle(Point(10, 450), Point(70, 490))
    searchrec.setFill(color_rgb(0,255,0))
    searchrec.draw(win)

    searchtext=Text(Point(40, 470), "Search")
    searchtext.setTextColor(color_rgb(255,255,255))
    searchtext.draw(win)

    todorec=Rectangle(Point(100, 450), Point(170, 490))
    todorec.setFill(color_rgb(0,0,255))
    todorec.draw(win)

    todotext=Text(Point(135, 470), "ToDoList")
    todotext.setTextColor(color_rgb(255,255,255))
    todotext.draw(win)

    #create a Text object to hold the calendar output
    calText = Text(Point(250, 250), "")
    calText.setSize(14)
    calText.setFace('courier')
    calText.draw(win)

    today = dt.date.today()
    cal(today.strftime("%m/%d/%Y"), win, calText)

    txt = Text(Point(250, 15), "Enter the date in the format of mm/dd/yyyy:")
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
        txt.setText("")
        date=input_box.getText()
        if click_point.getX()>=10 and click_point.getX()<=70 and click_point.getY()>=450 and click_point.getY()<=490:
            try:
                month,day,year=date.split("/")
                month=int(month)
                day=int(day)
                year=int(year)
                if month>12 or month<1 or day>31 or day<1 or year>9999 or year<1:
                    raise ValueError
                else:
                    calText.setText("")
                    cal(date, win,calText)
            except ValueError:
                txt.setText("Invalid date. Please try again.")
                input_box.setText("")
        elif click_point.getX()>=100 and click_point.getX()<=170 and click_point.getY()>=450 and click_point.getY()<=490:
            tlp.showtodoListPane(date)
    

    click_point=win.getMouse()
    if click_point.getX()>=450 and click_point.getX()<=490 and click_point.getY()>=450 and click_point.getY()<=490:
        win.close()
    


#Need to make days clickable for user to add events and tasks
#i think we will have to print out parts of the calendar individually so that we can make the days clickable
#not sure how to do this yet

#or we could search if the user types in the full date (mm/dd/yyyy) and then print out the calendar for 
#that month as well as the todo list for that day
#this is probably the easiest way to do it
#and if the user types in a month and year, we just can print out the calendar for that month
def cal(date, win,calText):
    #define the calendar
    textCal = calendar.TextCalendar(firstweekday=0)
    
    month,day,year=date.split("/")
    month=int(month)
    day=int(day)
    year=int(year)

    #set the text to the calendar output
    calOutput = textCal.formatmonth(year, month, w=0, l=0)

    first_day, num_days = calendar.monthrange(year, month)
    # get the day of the week for the last day of the month
    last_day = (first_day + num_days - 1) % 7
    # calculate the number of days left in the last week
    days_left = 6 - last_day
    
    #remove the last \n from calOutput
    calOutput = calOutput[:-1]

    #add spaces to the end of the calendar
    calOutput += " " * (days_left * 3)
    calText.setText(calOutput)

    for i in range(1, num_days+1):
        xPos = (i + first_day - 1) % 7
        yPos = (i + first_day - 1) // 7
        
        Pos1 = Point(150 + xPos * 30, 210 + yPos * 30)
        size = Point(Pos1.getX() + 20, Pos1.getY() + 20)

        calButtons = Rectangle(Pos1,size)
        calButtons.draw(win)


if __name__ == "__main__":
    main()
