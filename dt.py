
# The datetime module supplies classes for manipulating dates and times in both simple and complex ways.

# date in python is not a data type we can use datetime module to work with date objects.

# if you want to work with date we have to import the datetime module from python library... kachithamga import cheyyalsinde ledante output raadu....

# To print current date
'''
import datetime

x=datetime.datetime.now()
print(x)
'''

import datetime

# print(datetime.datetime.now())

# Time stamp ::: 2022-11-25 13:13:33.764083 ... denni time stamp antaru... order ::: year-month-day hour.minutes.seconds.microseconds

# datetime module has many methods to return information about date object.

# create dateobject :- To create date objects we use datetime()class

# Ex : create date i.e 2015 dec 24

# print(datetime.datetime(2015, 12, 24))


# datetime() class requires must three parameters for creating date i.e year, month, date ...these three are mandatory... remaining are optional---
# i.e Hours, minutes, seconds, and time zone.  *** The default value for hour minute and seconds is 0, default value for timezone is None.

# Ex : 2 create datetime for 2015 dec 24 13hours 15 min 25.69sec (milli seconds tho create cheyyalemu) so 25sec

# print(datetime.datetime(2015, 12, 24, 13, 15, 25))

# strftime(): we can convert datetime object to the readable strings by using strftime() ::: datetime object nunchi manaki kavalsina rupam lo date---
# ni techukovadaniki manam strftime() method vadathamu.

# strftime() takes one parameter that is format ....format is used To specify the format of returned string.

# We must use strftime() method with dateobject...... >>>> dateobject.strftime(format)....to represent specific formate.
'''
time_stamp = datetime.datetime.now()
print(time_stamp.strftime("%Y"))
print(time_stamp.strftime("%M"))
print(time_stamp.strftime('%c'))
'''

# formates :

# %Y = year full version (2023)
# %y = year short version (23)
# %B = month fullform (january)
# %b = month shortform (jan)
# %A = week fullform (saturday)
# %a = week short form (sat)

# weekday index, week index, month index and day index......

# %w = weekday as number(week day index) (0-6) sunday starts at 0
# %m = month as number (month index) (1-12) jan starts at 1
# %j = day number of the year (day index) (1-366)
# %W = week number (week index) monday as the first day of week (0-52)
# %U = week number (week index) sunday as the first day of week (0-52)

# %x%X%c%C = local version of the date| local version of the time | local version of the date and time | Century

# Hours...

# %H = hour in 24 hours format
# %I = hours in 12 hours format
# %p = am/pm


# %Z = time zone
# %z = utc offset
















