import calendar
from graphics import *
import datetime

def main():
    win = GraphWin("My Window", 500, 500)
    #win.setBackground(color_rgb(0,0,0))

    pt=Point(0, 0)

    exitrec=Rectangle(Point(450, 450), Point(490, 490))
    exitrec.setFill(color_rgb(255,0,0))
    exitrec.draw(win)

    exittext=Text(Point(470, 470), "Exit")
    exittext.setTextColor(color_rgb(255,255,255))
    exittext.draw(win)

    searchrec=Rectangle(Point(10, 450), Point(50, 490))
    searchrec.setFill(color_rgb(0,255,0))
    searchrec.draw(win)

    searchtext=Text(Point(30, 470), "Search")
    searchtext.setTextColor(color_rgb(255,255,255))
    searchtext.draw(win)

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
        if click_point.getX()>=10 and click_point.getX()<=50 and click_point.getY()>=450 and click_point.getY()<=490:
            try:
                month,day,year=date.split("/")
                month=int(month)
                day=int(day)
                year=int(year)
                if month>12 or month<1 or day>31 or day<1 or year>9999 or year<1:
                    raise ValueError
                else:
                    cal(date, win)
            except ValueError:
                txt.setText("Invalid date. Please try again.")
                input_box.setText("")
    

    click_point=win.getMouse()
    if click_point.getX()>=450 and click_point.getX()<=490 and click_point.getY()>=450 and click_point.getY()<=490:
        win.close()

    #print("Welcome to our calendar")
    #date=input("Enter the date in the format of mm/dd/yyyy: ")
    #cal(date)

#Function
def cal(date, win):
    #define the calendar
    textCal = calendar.TextCalendar(firstweekday=0)
    
    month,day,year=date.split("/")
    month=int(month)
    day=int(day)
    year=int(year)

    #create a Text object to hold the calendar output
    calText = Text(Point(250, 250), "")
    calText.setSize(14)
    calText.setFace('courier')
    calText.draw(win)

    #set the text to the calendar output
    calOutput = textCal.formatmonth(year, month, w=0, l=0)
    calText.setText(calOutput)


if __name__ == "__main__":
    main()
