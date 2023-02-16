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
    cal(date, win)

        
    win.getMouse()
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
