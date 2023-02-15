import sys

locations = sys.path
print(locations)
for i in locations:
    print(i)


import calendar # press command key to go to calender file

leapdays = calendar.leapdays(2000, 2050)
print(leapdays) # 13

is_leap = calendar.isleap(2036)
print(is_leap) # True

