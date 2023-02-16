import calendar
from graphics import *
import datetime

def main():
    win = GraphWin("My Window", 500, 500)
    #win.setBackground(color_rgb(0,0,0))

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
        win.getMouse()
        date=input_box.getText()
        try:
            month,day,year=date.split("/")
            month=int(month)
            day=int(day)
            year=int(year)
            if month>12 or month<1 or day>31 or day<1 or year>9999 or year<1:
                raise ValueError
            break
        except ValueError:
            txt.setText("Invalid date. Please try again.")
            input_box.setText("")

        
    win.getMouse()
    win.close()

    #print("Welcome to our calendar")
    #date=input("Enter the date in the format of mm/dd/yyyy: ")
    #cal(date)

#Function
def cal(date):
    #define the calendar
    textCal = calendar.TextCalendar(firstweekday=0)
    
    month,day,year=date.split("/")
    month=int(month)
    day=int(day)
    year=int(year)

    #print the calendar
    textCal.formatmonth(year, month, w=0, l=0)
    textCal.prmonth(year, month, w=0, l=0)

    #print(calendar.calendar(year))

if __name__ == "__main__":
    main()
