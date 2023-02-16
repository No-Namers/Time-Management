import calendar
import datetime

def main():
    print("Welcome to our calendar")
    date=input("Enter the date in the format of mm/dd/yyyy: ")
    cal(date)

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
