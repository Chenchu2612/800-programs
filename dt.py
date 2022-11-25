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
import time

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
'''
# Model: Unix time stamp to readable date.


# 6. Write a Python program to convert unix timestamp string to readable date.
# Sample Unix timestamp string : 1284105682
# Expected Output : 2010-09-10 13:31:22


# Explanation: time stamp nunchi manaki nachina vidham ga output techukovali ....daaniki manam fromtimestamp() ane function vaadathamu..

# new_func: fromtimestamp()

# The fromtimestamp() function is used to return the date corresponding to a specified timestamp.

# Note: Here the timestamp is ranging from the year 1970 to the year 2038, and this function does not consider leap seconds if any present in the----
# timestamp.

# manam ikkada fromtimestamp() function lo string ni int() loki marchi pampali .... leda manam input() function lone marchavachu.int(input())........

import datetime

def unix_to_time(unix):
     return datetime.datetime.fromtimestamp(int(unix)).strftime('%Y-%m-%d %H:%M:%S')


print(unix_to_time(input("Enter the unix time: ")))

'''

'''
# Model :  yesterday, Today, Tomorrow,

# 7. Write a Python program to print yesterday, today, tomorrow.

# Exp : based on timedelta we can add and remove dates from today dates....

import datetime

def yes_tod_tom():
     today = datetime.date.today()
     yesterday = today-datetime.timedelta(days=1)
     tomorrow = today+datetime.timedelta(days=1)
     return 'Yesterday is : {}, \nToday is : {}\nTomorrow is : {}'.format(yesterday, today, tomorrow)


print(yes_tod_tom())


# important : datetime.date.today() >>> it returns  only today date.....

'''
'''
# Model : conversion of date to datetime.

# 8. Write a Python program to convert the date to datetime (midnight of the date) in Python.
# Sample Output : 2015-06-22 00:00:00

# Exp: oka date ni datetime ga matchali...adi kuda mid night of the date ani ichadu...00.00.00

# combine() ane function ni use chesi manam combie chestam.
# combine(date, time) 
# midnight vadda time 00.00.00 vuntundi kaabatti....manam min.time() use chesi get cheyyochu.

import datetime

date = datetime.datetime.today()
print(datetime.datetime.combine(date, datetime.datetime.min.time()))

'''

'''
# Model: printing next fivedays.

# 9. Write a Python program to print next 5 days starting from today.

# Exp: 1.currentdate kanukkoni 2. danni loop dwara timedelta function dwara add chesi print cheyyali. 

# important : starting from today annadu kabatti today date tesukunnamu.  


import datetime


def printing_next_five_days(num_of_days):
    base = datetime.datetime.today()
    for i in range(0, num_of_days):
         print(base+datetime.timedelta(days=i))


printing_next_five_days(int(input("Enter the number of days :")))

'''
'''
# Model: adding seconds to the model.


# 10. Write a Python program to add 5 seconds with the current time.
# Sample Data :
# 13:28:32.953088
# 13:28:37.953088

# Exp:we can add by using the timedelta function...datetime.timedelta( weeks=0, days=0, hours=0, minutes=0, seconds=0, microseconds=0, milliseconds=0)

import datetime


def add_sec(num_of_sec):
    base = datetime.datetime.now()
    print(base)  # for understanding purpose. to see the difference.
    return base+datetime.timedelta(seconds=num_of_sec)


print(add_sec(int(input("Enter the number of seconda to add: "))))
'''
'''
# *** imp
# Model : Year/Month/Day to day of year.


# 11. Write a Python program to convert Year/Month/Day to Day of Year in Python.


# Exp: ichina date 366 days day's lo  enno day ani kanukkovali.....

# 1. first  time ni cal calculate cheyyali strptime() dwara ...daani nunchi manaki ea formate lo kavalo strftime() ni vaadukovali....

# Note : strftime() string input ki workout avvadu....manam strptime() ni vaadukovali....

import datetime


def day_of_year_(date_obj):
    return datetime.datetime.strptime(date_obj, '%Y/%m/%d').strftime('%j')


print(day_of_year_(input("Enter the date: ")))


'''
'''
# Model: current time in milli seconds

# 12. Write a Python program to get current time in milliseconds in Python

# Exp: present time ni milliseconds lo kanukkovali...

# 1. manam time.time() >>> from time module from time() function  we have to get current time ....the after multiply to 1000 to convert milli seconds.

import datetime

# print(int(round(time.time()*1000)))


# Model: to get week number.

# 13. Write a Python program to get week number.
# Sample Date : 2015, 6, 16
# Expected Output : 25


# Exp: strptime() function dwara manam stringlonumchi time kanukkoni daani numchi strftime() function dwara manam week day ni kanukkuntaam.

import datetime

print(datetime.datetime.strptime('2015, 6, 16', '%Y, %m, %d').strftime('%W'))

'''
'''
# Model: date of first monday of given week

# 14. Write a Python program to find the date of the first Monday of a given week.
# Sample Year and week : 2015, 50
# Expected Output : Mon Dec 14 00:00:00 2015

# Exp: year and week number istadu manam aa week number lo first monday date kanukkovali...

# Imp: week ichadu...week lo monday kavali annadu kabatti 1 pettali as per weekday index '%w' (0-6)  prakaram....okati petti daaniki malli weekday---
# index_number ivvali...


import datetime

print(datetime.datetime.strptime('2022 50 1', '%Y %U %w').strftime('%a %b  %d %H:%M:%S %Y'))

'''

# Model: selecting all sundays in a given year.

# 15. Write a Python program to select all the Sundays of a specified year.

import datetime

print(datetime.datetime.strptime('2015 1 0', '%Y %U %w').strftime('%'))



















