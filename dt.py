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

# strftime() takes one parameter that is format .... To specify the format of returned string.




























