# The datetime module supplies classes for manipulating dates and times in both simple and complex ways.


#  Date and datetime are an object in Python, so when you manipulate them, you are actually manipulating objects and not string or timestamps.


# date in python is not a data type we can use datetime module to work with date objects.

# if you want to work with date we have to import the datetime module from python library... kachithamga import cheyyalsinde ledante output raadu....

# To print current date

'''
import datetime

x=datetime.datetime.now()
print(x)
print(datetime.datetime.now())   # date and time both
print(datetime.datetime.now().today()) # above and this commands are same
print(datetime.datetime.now().date()) # only date will print
print(datetime.datetime.now().year) # only year will print
print(datetime.datetime.now().weekday()) # week day in numbers(0-6)
print(datetime.date()) # is used to create date.
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


# To get current date :- from datetime import date  >>>> date.today() >>> it will retuen today's date


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

# %w = weekday as number(week day index) (0-6) monday(start's at 0) to (sunday at 6)
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


# print(date_object.date) = it will print's the  date_object date (1 to 31).
# print(date_object.month) = it will print the date_object month (1 to 12).
# print(date_object.year) = it will print the date_object year.


# timedelta() : calculating differences in dates and also can be used for date manipulations in Python.   Returns : Date

# we have to import it from the datetime module >>>> from datetime import timedelta

# It is one of the easiest ways to perform date manipulations.


# datetime.timedelta( weeks=0, days=0, hours=0, minutes=0, seconds=0, microseconds=0, milliseconds=0 )

# ________ replace() function___________:


# Datetime.replace() function is used to replace the contents of the DateTime object with the given parameters.

# Syntax: Datetime_object.replace(year,month,day,hour,minute,second,microsecond,tzinfo)

# Returns: It returns the modified datetime object


# time.mktime() method of Time module is used to convert a time.struct_time object or a tuple containing 9 elements corresponding to time.struct_time object------
# to time in seconds passed since epoch in local time.

# ichina time epoch time difference seconds lo chupistundi.

# syntax:  time.mktime(t)
# Return type: This method returns a float value which represents the time expressed in seconds since the epoch.(1st jan 1970)


# Time stamp = It is the number of seconds that have elapsed since the Unix epoch, minus leap seconds.
# The Unix epoch is 00:00:00 UTC on 1 January 1970 (an arbitrary date); leap seconds are

# The timetuple() method does not take any parameters.

# Return value :-
# timetuple() returns the time.struct_time() object as a tuple that contains the date and time information, i.e., timestamps.


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
'''
# Model: selecting all sundays in a given year.

# 15. Write a Python program to select all the Sundays of a specified year.

import datetime

print(datetime.datetime.strptime('2015 1 0', '%Y %U %w').strftime('%'))

'''

'''
# 15. Write a Python program to select all the Sundays of a specified year.
import datetime


def getting_all_sundays(year):
    dt = datetime.date(year, 1, 1)       # initializing date
    dt += datetime.timedelta(6 - dt.weekday())    # to get first sunday .....print(dt.weekday()) returns the week day (0-6)of that date.
    while dt.year == year:  # manam initialize chesina year and nenu kanukkovalsina year rendu equal ienantha varaku loop run chey.
        yield dt
        dt += datetime.timedelta(days=7)

    return dt


for i in getting_all_sundays(int(input("Enter the year :"))):
    print(i)
'''

'''
# 16. Write a Python program to add year(s) with a given date and display the new date.
#
# Sample Data : (addYears is the user defined function name)
# print(addYears(datetime.date(2015,1,1), -1))
# print(addYears(datetime.date(2015,1,1), 0))
# print(addYears(datetime.date(2015,1,1), 2))
# print(addYears(datetime.date(2000,2,29),1))

# Expected Output :
# 2014-01-01
# 2015-01-01
# 2017-01-01
# 2001-03-01


# Exp: ichina date ki years add chesi new date ni print cheyyali....

import datetime

# print(datetime.date(2015, 1, 1))

# Datetime_object.replace(year,month,day,hour,minute,second,microsecond,tzinfo)

# replace method is used to change the contents of the datetime module.



def add_date(d, years):
    try:
        return d.replace(year=d.year + years)         # d.year is nothing but dateobject.year
    except ValueError:
        return d + (datetime.date(d.year + years, 1, 1) - datetime.date(d.year, 1, 1))


print(add_date(datetime.date(2015,1,1),-1))
print(add_date(datetime.date(2015,1,1),2))
print(add_date(datetime.date(2000, 2,29),1))
 
'''

'''
# Model : eliminate microseconds.

# 17. Write a Python program to drop microseconds from datetime.

# Exp:

# 1.manam replace() method dwara cheyya vachhu....date_obj.replace(parameter)...oka date time object lo eamemi iethe vunnayo avanni change cheyyochu

import datetime

def drop_microsecond():
    return datetime.datetime.now().replace(microsecond=0)

print(drop_microsecond())

'''

'''
# Model: Getting days between two days.

# 18. Write a Python program to get days between two dates.
# Sample Dates : 2000,2,28, 2001,2,28
# Expected Output : 366 days, 0:00:00

import datetime


def getting_days_btwn_two_days():
    return datetime.date(2001, 2, 28)-datetime.date(2000, 2, 28)       # Note: pedda date mundu vundali chinna date tharuvatha vundali ledante result

                                                                                                                        # negative lo vastundi...
print(getting_days_btwn_two_days())

'''

'''
# Model: date of last tuesday

# 19. Write a Python program to get the date of the last Tuesday.


# Exp: 1. mundu manam today date kanukkoni danini time delta dwara tesiveyyali.
# 2. off_set kanukkovali ::: today weekday kanukkoni, problem lo adigina day ki  daani mundu weekday ni tesivesi mothanni %7 tho modulardivision-----  
# cheyyali.



from datetime import date
from datetime import timedelta


def date_of_last_tuesday():
    today = datetime.date.today()
    off_set = (today.weekday()-1) % 7    # 1 is before weekday of tuesday i.e monday  % 7 means modular division of total number of days.
    print(off_set)                                   # off_set is a formula....
    last_tuesday = today - timedelta(days=off_set)
    return last_tuesday


print(date_of_last_tuesday())

'''
'''
# Model: third tuesday of the month.

# 20. Write a Python program to test the third Tuesday of a month

# Exp : ichina date ni strp dwara convert chesukovali.... chesukunna danniki wee day kanukkovali....aa week day 1 anna vundali and 14 nunchi 22----
# madhyalo iena vundali.


# week day and day.

import datetime


def third_tuesday(dat):
    d= datetime.datetime.strptime(dat, '%b %d, %Y')
    print(d.weekday())   # (0 to 6)
    print(d.day)  # month lo date vastundi.
    print(d.month) # understanding purpose
    print(d.year)  # understanding purpose
    return d.weekday() == 1 and 14 < d.day < 22   #(deeni ardham 15 nunchi 21 varaku)(above 14 bellow 21) 


print(third_tuesday('Jun 23, 2015'))
'''

'''
# Model : fetching last day of specified year and sprcified month.

#21. Write a Python program to get the last day of a specified year and month.


# Exp : year and nela istadu aa nelalo manam last date kaunukkovali.


# calender ni import chesi.... month range kanukkovali.

import calendar

def last_day(year, month):
    return calendar.monthrange(year, month)[1]

# print(calendar.monthrange(2015,5))   # for understanding purpose.....>>>> it will prints the range in tuple format (starts, end)


print(last_day(int(input("Enter the year :")), int(input("Enter the month :"))))

'''
'''
# Model : number of days in a month for a specified year.

# 22. Write a Python program to get the number of days of a given month and year.

from calendar import monthrange


def num_days_in_a_month(year, month):
    return 'The total number of days in a month : {}'.format(monthrange(year=year, month=month)[1])


print(num_days_in_a_month(int(input('Enter the year :')), int(input('Enter the month: '))))

'''
'''
# Model : specified date ki month add cheyyali.

Error came

# 23. Write a Python program to add a month with a specified date.



from datetime import date
import calendar
from datetime import timedelta


def add_month_to_date():
    start_date = date(2014, 12, 25)
    number_of_days_in_a_month = calendar.monthrange(start_date.year, start_date.month)[1]
    return datetime.date(start_date+timedelta(number_of_days_in_a_month))


print(add_month_to_date())
'''
'''
# Model: number of mondays as 1st day of month.

# 24. Write a Python program to count the number of Monday of the 1st day of the month from 2015 to 2016.

# Exp: 2015-16 lo enni months starting monday tho start avutundi.


from datetime import date
import calendar
from datetime import timedelta


def finding_mondays():
    count =0
    for year in range(2015, 2017):
        for month in range(1, 13):                              # weekday 0 means monday.
            if datetime.datetime(year, month, 1).weekday() == 0:  # datetime.date(year, month, date) is used to initialise the date object...
                count += 1                     
    return count


print(finding_mondays())

'''
'''

# 25. Write a Python program to print a string five times, delay three seconds


# Python time sleep:

# Python time sleep function is used to add delay in the execution of a program

# syntax : time.sleep(seconds)

# exp: oka string ni 5 times print chey okkoka time execute chesetappudu 3 sec delay chey.

import time


def delay_3sec_prog():
    x = 0
    while x < 5:
       print("before sleep")
       print('hi')
       time.sleep(3)     # program execution ni three seconds stop chestundi......
       print("after sleep")
       x = x+1


delay_3sec_prog()

'''
'''
# Model : current date nunchi six months tharuvatha date kanukkovali.  >>> current date ki six month's kalapali.

# 26. Write a Python program calculates the date six months from the current date using the datetime module.

# Exp: current date ki 6months add cheyyali...so months ni days rupamloki marchukoni add cheyyali.

# Important : date ki month add cheyyalante months ni date loki marchukovali.... >>>> months_to_be_added*365/12

# Convert Months to Days (formula) => days = months × 30.436875 (365/12)

import datetime

print((datetime.date.today()+datetime.timedelta(6*365/12)).isoformat())

# isoformate: international organisation for standardisation.
'''
'''
# Model : creating 12 dates from the given date...the days differnce between two dates is 20 days.

# 27. Write a Python program to create 12 fixed dates from a specified date over a given period. The difference between two dates will be 20

# Exp : ichina date nunchi 20 rojulu theda gala 12 dates ni kanukkovali.

# 12 dates kavali kabatti manam range function use chesi 12 iterations chestam.....given date every ki prathi iteration lo timedelta dwara 20days add chestam.

import datetime

def every_20_days(date):
    print('starting date :{}'.format(date))
    print('12 days time differnce')
    for i in range(12):
        date += datetime.timedelta(days=20)
        print('{}'.format(date))


every_20_days(datetime.date(2016,8,1))

'''
'''
# Model : fetch date 30days before date and 30days after date.

# 28. Write a Python program to get the dates 30 days before and after from the current date.

# Exp: ichina date nunchi 30rojulu mundu date ni and 30 rojulu tharuvatha date ni kanukkovali.


# my code:::

import datetime


def before_30_after_30(date):
    print('30 days before date ::: {}'.format(date-datetime.timedelta(days=30)))
    print('30 days after date ::: {}'.format(date+datetime.timedelta(days=30)))


before_30_after_30(datetime.date(2022, 12, 1))


# w3 code:::

from datetime import date, timedelta

current_date = date.today().isoformat()
days_before = (date.today()-timedelta(days=30)).isoformat()
days_after = (date.today()+timedelta(days=30)).isoformat()

print("\nCurrent Date: ",current_date)
print("30 days before current date: ",days_before)
print("30 days after current date : ",days_after)

'''
'''
# Model : fetch green wich mean time and local time

# 29. Write a Python program to get the GMT and local current time.


from datetime import time
from time import gmtime
import time

print(time.strftime('%a, %d %b %Y, %I:%M:%S, %p, %Z', time.gmtime()))
print(time.strftime('%a, %d %b %Y, %I:%M:%S, %p, %Z'))

'''
'''
# Model : conversion date to timestamp.

# 30. Write a Python program to convert a date to the timestamp.


import datetime

# print(datetime.datetime.now())


# time.mktime() method of Time module is used to convert a time.struct_time object or a tuple containing 9 elements corresponding to time.struct_time object------
# to time in seconds passed since epoch in local time.

# ichina time epoch time difference seconds lo chupistundi.

# syntax:  time.mktime(t)
# Return type: This method returns a float value which represents the time expressed in seconds since the epoch.(1st jan 1970)


# Time stamp = It is the number of seconds that have elapsed since the Unix epoch, minus leap seconds.
# The Unix epoch is 00:00:00 UTC on 1 January 1970 (an arbitrary date); leap seconds are

# The timetuple() method does not take any parameters. >>>> timeobject.timetuple()

# Return value :-
# timetuple() returns the time.struct_time() object as a tuple that contains the date and time information, i.e., timestamps.


print(time.mktime(datetime.datetime.now().timetuple()))    #  very very important.
'''
'''
# Model : string date to time stamp...

# 31.Write a Python program to convert a string date to the timestamp.


# Exp: string formate lo ichina date ni timestamp loki marchali.

import datetime


# timeobject.timetuple() >>>> output is timestamp.

# time.mktime() is used to convert time structure.

print(time.mktime(datetime.datetime.strptime('26/11/2022', '%d/%m/%Y').timetuple()))

'''
'''
# Model: number of days between twodays.

# 32. Write a Python program to calculate a number of days between two dates

# Exp: rendu dates istadu daani madhya enni rojulu vundo kanukkovali


# Note: date object vadetappudu manam direct ga date ni import cheyyadam manchidi... ledante errors vache chance vundi....

import datetime
from datetime import date


def diff_days(date1, date2):
    return (date1 - date2).days


print(diff_days(date(2022, 12, 24), date(2022, 12, 1)))

'''
'''
# Model : number of days between datetimes.


# 33. Write a Python program to calculate no of days between two datetimes.

from datetime import date

def days_between_datetimes(dt1, dt2):
    return (dt1-dt2).days


print(days_between_datetimes(datetime.datetime(2022, 12, 2, 12, 12, 12), datetime.datetime(2022, 12, 1, 11, 50, 11)))

'''
'''
# Model : date to Unix time stamp.

# 35. Write a Python program to convert a date to Unix timestamp

# Exp: date ni unix timestamp ga marchali.....unix anna epoh anna okate...manam timestamp ga marchali anthe....


# time.mktime() function is used to convert datetime object structure and timetuple() is used to convert timestamp... 

from datetime import date
import time

print(time.mktime(datetime.date(2022, 12, 25).timetuple()))

'''

'''
# Model: Difference between two dates in seconds...

# 36. Write a Python program to calculate two date difference in seconds.

# Model :1 this is my approach .... from epoch time.

from datetime import time
import datetime
import time

print(time.mktime(datetime.datetime.now().timetuple())-time.mktime(datetime.datetime(2015, 1, 1).timetuple()), 'seconds')


# Model :2 this is w3 model....  by converting days to seconds (days*hours_per_day * minutes_per_day)


from datetime import datetime, time
def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
#Specified date
date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
#Current date
date2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
print()

'''
'''
# Model :  two date difference in >>>> days, hours, minutes, seconds.

# 37. Write a Python program to convert two date difference in days, hours, minutes, seconds

# Exp: bellow method is super method...

# new func: divmod(arg1, arg2)  ::: in this function argument1 is devided by argument2

# %d instead of formate method. vimp...

# minutes = seconds/60 ...hours=minutes/60...days=hours/24.


from datetime import date
import time
import datetime


def difference(dt1, dt2):
    timedelta = dt2 - dt1
    return timedelta.days * 24 * 3600 + timedelta.seconds


def dhms_from_seconds(seconds):  # This seconds will goes to bellow parameter.
    minutes, seconds = divmod(seconds, 60)     # lesf side of '=' minutes value calculate iena tharuvatha assign avutindi...seconds 60 ani ichamu...function call---
    hours, minutes = divmod(minutes, 60)                                      # daggara ichina seconds divmod seconds ki assign avutundi......
    days, hours = divmod(hours, 24)
    return days, hours, minutes, seconds


dt1 = datetime.datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
dt2 = datetime.datetime.now()

print('%d days, %d hours, %d minutes, %d seconds'% dhms_from_seconds(difference(dt1, dt2)))

'''

'''
# Model: last modified file information.

# 38. Write a Python program to get last modified information of a file.


# not understanding.

'''
'''
# Model : finding age

# 39. Write a Python program to calculate an age in year

# Super method....

# Exp: mundu years ni minus chesi tharuvatha  (today.month , today.day) < (dob.month , dob.day)  0 add avutundi ledante 1 add avutundi----

# adi ela ani daoubt vachindi naku ela ? ... today.month, today.day anedi ichina condition(<,>) prakaram true iethe 1 false 



from datetime import datetime
from datetime import date


def age(dob):
    today = datetime.today()
    return today.year-dob.year-((today.month, today.day) < (dob.month, dob.day))


print(age(date(1993, 12,24)))
'''


'''
# 40. Write a Python program to get the current date time information.


import datetime

a=datetime.datetime.now() # it wi  return's date and time also.
b=datetime.date.today()   # it will return only today date.
print(a)
print(b)
print(b.strftime('%Y'))
print(b.strftime('%y'))
print(b.strftime('%B'))
print(b.strftime('%b'))
print(b.strftime('%A'))
print(b.strftime('%a'))
print(b.strftime('%j'))
print(b.strftime('%W'))
print(b.strftime('%w'))
print(b.strftime('%d/%m/%Y'))
'''
'''
# Model : date and time as a string.

# 41. Write a python program to generate a date and time as a string.

# Exp : date and time ni string formate lo generate cheyyamannaru....


import datetime

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %p'))
print(type(datetime.datetime.now()))  # obj datetime.datetime
print(type(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %p')))  # string formate

'''
'''
# Model : printing calender

# 42. Write a Python program to display formatted text output of a month and start weeks on Sunday.

# Exp : oka month calender print cheyyali calender sunday nunchi start avvali.

# 1. mundu manam calender ni import chesukovali 2.textCalender kavali ani adagali 3.calender ea day nuchi start avvalo cheppali. 4. ee mudu kalipi---
# object ni return chetunsdi 5.deeni nuncchi manam peryear kavala ? leda per month kavala ani adugutham( year, month) parameter lo pass ccheyyali.



import calendar

print(calendar.TextCalendar(calendar.SUNDAY).prmonth(2022, 12))  # per month
print(calendar.TextCalendar(calendar.SUNDAY).pryear(2023)) # per year


'''
'''
# Model : printing 3 column calender

# 43. Write a Python program to print a 3-column calendar for an entire year.

# Exp : it is same as above problem but er have to use for mate year method.

import calendar

print(calendar.TextCalendar(calendar.SUNDAY).formatyear(2023, 2, 1, 1, 3))
'''
'''
# Model: calender for locale.

# 44. Write a Python program to display a calendar for a locale

# Exp: aa locale= ani rasindi endo naku teliyadu

import calendar

print(calendar.LocaleTextCalendar(locale='en_AU.utf8').pryear(2023, 12))

'''
'''
# Getting current week

# 45. Write a Python program to get the current week.


# Exp : naku telisina method strftime() kaani w3 lo isocalender method ichadu....

# isocalender output vareity ga vuntundi... year vastundi next week numer (0-52) vastundi tharuvatha weekday(0-6)

import datetime

print(datetime.date(2022, 12, 24).isocalendar())  # it's output is >>>> datetime.IsoCalendarDate(year=2022, week=51, weekday=6)

year, week_number, day_of_the_week = datetime.datetime.now().isocalendar()

print('Year = %d, Week_number = %d, Day_of_the_week = %d' %(year, week_number, day_of_the_week ))
'''

'''
# Model : creation of HTML calender with data.

# Write a Python program to create a HTML calendar with data for a specific year and month


# Exp: HTML calender with data for specific year and month.

import calendar

print((calendar.HTMLCalendar(calendar.SUNDAY)).formatmonth(2022,12))

'''

'''
# Model : list of all second saturdaya in a year.


import calendar

# print((calendar.monthcalendar(2022, 2))[0])  *** very important  

# month calender.monthcalender yappudu every seven days nested list's tho vastundi...okavela week lo month start kakpothe 0's vastundi.
# every nested lists manam index dwara access cheyyochu...

# print(calendar.TextCalendar(calendar.SUNDAY).formatmonth(2022,3))  

# TextCalendar manaki calder ni istundi.manam ea day tho start avvalo mention cheyyochu. 
# and formate dwara manam total year calendar or particular month kanukkovachu.


# print(calendar.SATURDAY)



# print(calendar.monthcalendar(2022,12)[2])  # third week


# print(calendar.TextCalendar(calendar.MONDAY).formatmonth(2022, 12))


for month in range(1, 13):
    cal = calendar.monthcalendar(2022, month)
    first_week = cal[0]
    second_week = cal[1]
    third_week = cal[2]
    if first_week[calendar.SATURDAY]:
        holiday = second_week[calendar.SATURDAY]
    else:
        holiday = third_week[calendar.SATURDAY]

    print(calendar.month_abbr[month], holiday)


print(calendar.TextCalendar(calendar.SATURDAY).formatyear(2022, 12))

'''