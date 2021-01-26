# Author: Christopher LeMoss
# Date: 1-30-2021
# Description: 
#   Homework 3 for CS362 Software Engineering II at Oregon State University.
#   Determines whether or not the given year is a leap year.
#   Contains error handling. 

year = 0;

while year < 1582:
    try:
        year = int(input("Enter year: "))
        if year < 1582:
            print("Error: Please enter an integer >= 1582.")
    except ValueError:
        print("Error: Please enter an integer.")

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
