# Author: Christopher LeMoss
# Date: 1-30-2021
# Description: 
#   Homework 3 for CS362 Software Engineering II at Oregon State University.
#   Determines whether or not the given year is a leap year.
#   Lacks error handling. 

year = int(input("Enter year: "))
is_leap_year = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
    else:
        is_leap_year = True

if is_leap_year:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
