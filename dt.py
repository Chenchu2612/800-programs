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

# import datetime

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
# %d = day of the month (1-31)
# %x%X%c%C = local version of the date| local version of the time | local version of the date and time | Century

# Hours... HIMS

# %H = hour in 24 hours format
# %I = hours in 12 hours format
# %M = minutes (0-59)
# %S = seconds (0-59)
# %p = am/pm
# %f = fraction of seconds

# %Z = time zone
# %z = utc offset


# timedelta() : calculating differences in dates and also can be used for date manipulations in Python.   Returns : Date

# we have to import it from the datetime module >>>> from datetime import timedelta

# It is one of the easiest ways to perform date manipulations.


# datetime.timedelta( weeks=0, days=0, hours=0, minutes=0, seconds=0, microseconds=0, milliseconds=0 )


# problems:

'''

# Model:1 Fetching various information from the dateobject.

# 1. Write a Python script to display the various Date Time formats
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week

# date problem chese mundu manam date time moduke ni import cheyyali.

import datetime

date_obj = datetime.datetime.now()

print("The current date :", date_obj.strftime('%x'), "The current time :", date_obj.strftime('%X'))
print("Current year :", date_obj.strftime('%Y'))
print("The month of the year:", date_obj.strftime("%B"))
print("The Week number of the year:", date_obj.strftime('%W'))
print("The week day of the week:", date_obj.strftime('%w'))
print("The day of the month :", date_obj.strftime('%d'))
print("The day of the year :", date_obj.strftime('%j'))
print("The day of the week :", date_obj.strftime('%A'))

# Note: i confused points....week day of the week ante : (0-6) .... day of the week ante : sunday to saturday.
'''
'''

# Model: Leaf year or not

2. Write a Python program to determine whether a given year is a leap year.

# Explanation : leef year kanukkovadaniki 400 tho or 4 tho  %(modular division or reminder division) chestam == 0 >>> True
# tharuvatha 100tho chestam == 0 iethe False ... tharuvatha else block lo return False rastam.    


def leaf_or_not(year_obj):
    if (year_obj % 400 == 0) or (year_obj % 4 == 0):
        return True
    elif year_obj % 100 == 0:
        return False
    else:
        return False

    
print(leaf_or_not(int(input("Enter the year to compute :"))))

'''

'''
# Model: conversion of string to date time.

# 3. Write a Python program to convert a string to datetime.
# Sample String : Jan 1 2014 2:43PM
# Expected Output : 2014-07-01 14:43:00


# EXplanation : output vachi manaki normal time stamp formate lo vundi so manam eami change cheyyalsina pani ledu....daaniki just ededi eami ani
# chepthe chalu adi automatic ga convert chesukuntundi

# datetime.strptime() ===>>> ee function manaki string nunchi dates ga marchadaniki vaadatharu.... strftime() use avvadu

import datetime


def conv_string_date(string_obj):
     return datetime.datetime.strptime(string_obj, '%b %d %Y %I:%M%p')


print(conv_string_date(input("Enter the string_obj :")))
'''

'''


# Model : To get current time

# 4. Write a Python program to get the current time in Python.

# Sample Format :  13:19:49.078205

# Explanation: manam current time ni icchina for mate lo kanukkovadaniki format methods vaadathamu.

import datetime


def current_time():
    return datetime.datetime.now().strftime('%H:%M:%S.%f')


print(current_time())
'''
'''
# *** Model: Substraction of days from date...  n day's before days. (very important)

# 5. Write a Python program to subtract five days from current date.
# Sample Date :
# Current Date : 2015-06-22
# 5 days before Current Date : 2015-06-17


# Explanation: manam time lo calculations cheyyadaniki timedelta ni import cheyyali... aa tharuvatha strptime() function vaduthamu....
# strptime() function tho matrame calculations cheyyagalam strftime() tho cheyyalemu... aa tharuvatha timedelta(days=) lo days raasi tesiveyyali....


from datetime import timedelta


def new_day(enter_days):
     day_varible = datetime.datetime.strptime('2015-06-22', '%Y-%m-%d')-timedelta(days=enter_days)
     return day_varible.strftime('%Y-%m-%d')

print(new_day(int(input("Enter number of days to reduce :"))))

'''