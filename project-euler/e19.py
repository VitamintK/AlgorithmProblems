"""
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

day_of_week = 1
months = [31,28,31,30,31,30,31,31,30,31,30,31]
ans = 0
for yr in range(1900, 2001):
    for mo in range(12):
        if yr > 1900 and day_of_week == 0:
            ans += 1
        days = months[mo]
        if mo == 2 and yr%4 == 0 and yr%400 != 0:
            days += 1
        day_of_week = (day_of_week + days)%7
print(ans)
        