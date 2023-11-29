def leap_year():
    year=int(input("enter a year:"))
    if(year%400==0)or(year%4==0)and (year%100!=0):
        print(year,"it is a leap year:")
    else:
        print(year,"it is not a leap year:")
leap_year()
             
