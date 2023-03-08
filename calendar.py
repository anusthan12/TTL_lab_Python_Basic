
import calendar

print("/*********/")
print("Calendar")


year = int(input("\nEnter the year : "))

print("Calendar for year including all months is:- ")  #this is for getting calendar for the whole year
print(calendar.calendar(year))

month = int(input("\nEnter the month: "))  #this is for getting calendar for an individual month
print("Calendar for month is:- ")
print(calendar.month(year, month))
