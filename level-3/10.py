'''
Build a countdown calculator. Write some code that can
 take two dates as input, and
then calculate the amount of time between them
'''
from datetime import date

# Taking dates from user
start = input("Enter start date formatted as (YYYY/MM/DD): ").split("/")
end = input("Enter end date formatted as (YYYY/MM/DD): ").split("/")
 
def countdown_days(f_date, s_date):
    # Convert start date to date
    y1, m1, d1 = [int(date_1) for date_1 in f_date]
    f_date = date(y1, m1,d1)

    # Convert end date to date
    y2, m2, d3 = [int(date_2) for date_2 in s_date]
    s_date = date(y2, m2,d3)

    # Get days diffrence between start and end dates
    days_between = s_date - f_date

    if days_between.days == 1:
        return f"{days_between.days} Day."
    return f"{days_between.days} Days."


print(countdown_days(start, end))













