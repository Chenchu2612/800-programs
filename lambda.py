# Important_points : lambda function never start's with def keyword it start's with lambda keyword

# lambda functions are most commonly use with filter(), map(), reduce() functions ....
# filter() function returns iteraror, and map() function returns map object which is aloan iterator
# we can extract values from filter(), map(), reduce() functions by using for loop and by using constructor methods(list(),tuple(),set() etc..,)
#

# confusion: nenu filter() ki , map() ki confuse avutunna >>>>> clarity :::: map() function lo  original list lo prathi element new list lo vuntundi
# map() function lo original list ki , new_list ki same length vuntundi but every element ki some modifications vuntundi.

"""
# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and print the result

# adding 15 to a given number passed in as an argument

a = lambda x: x+15 # adding 15
a1= lambda y :y-15 # substracting 15
print(a(5))

b= lambda x, y: x*y
b1 = lambda x, y: x/y
b1 = lambda x, y: x//y
print(b(2, 3))
print(b1(5, 2))

"""

"""

# 2. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

# Explanation : function ni create cheyyali dantlo lambda function rayali.


def multiplication(number):
    return lambda x: x * number  # multiplication function returns the lambda function object and that lambda function will ssign to the varoble
                                                                                        # and passing value to the lambda function arguments


result = multiplication(10)
print(result(5))           # print(multiplication(10)(5)
"""
"""
# 3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
a= [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

a.sort(key=lambda x: x[1], reverse=False) # sort ascending    >>>>> 0 means first item in the tuple ... 1 means numbers in a tuple
a.sort(key=lambda x: x[1], reverse = True) # sort decending  >>> manam mention cheyyochu o or 1 deni adharamga sort cheyyali ani
print(a)
print(sorted(a, key= lambda x: x[1], reverse=False)) # by using sorted function. sorted ascending
print(sorted(a, key= lambda x: x[1], reverse=True))   # sorted decending
"""
"""
# 4. Write a Python program to sort a list of dictionaries using Lambda. Go to the editor
# Original list of dictionaries :
a=[{'make': 'Nokia', 'model': 216, 'color': 'Black'},
 {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
 {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
b=[{'make': 'Nokia', 'model': 216, 'color': 'Black'},
 {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
 {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]


print(sorted(a, key= lambda x: x['color']))  # ikkada a.items() ani ivvalemu a anedi dictionary kaadu list so...value adharamga sort chesamu...
                                                                                                    # value ni key dwara get chesamu.

#By using sort() function.

a.sort(key=lambda x: x['color'])  
print(a)

"""
"""
# Model: filtering using lambda  (even, odd)

# Function = filter(function, iterable)

# 5. Write a Python program to filter a list of integers using Lambda.
# Original list of integers:
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

print("List_of_even_number's :", list(filter(lambda x: x % 2 == 0, a)))
print("List_of_odd_numbers :", list(filter(lambda x:  x % 2 != 0, a))) 

"""
"""
# Model : square and cubic of every element

# applying the some functionality to the every element to the iterable so use map(function, iterable)

# 6. Write a Python program to square and cube every number in a given list of integers using Lambda.
# Original list of integers:
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# my mistake>>>> prathi saari iterable ni outside of function lo pass chestunna adi rectify cheyyali ... list(map(function),a) ani istunna 
# list(map(function),a) >>> this is wrong. arument error will raise.
# list(map(function, a)) >>> this is right.

print("Square of every number of the said list :", list(map(lambda x: x**2, a)))   # **2 is square root .... **3 is cubic root
print("Cube of every number of said list:", list(map(lambda x: x**3, a)))

"""
"""
# Model: start's with specific charecter or not....endswith charecter or not

# 7. Write a Python program to find if a given string starts with a given character using Lambda.

starts_with = lambda x: True if x.startswith('c') else False      # string.startswith('substring')
print(starts_with('chenchu'))
ends_with = lambda x: True if x.endswith('u') else False   # string.endswith('substring')
print(ends_with('chenchu'))

"""
"""
# Important for date time module.

# 8. Write a Python program to extract year, month, date and time using Lambda

import datetime

now = datetime.datetime.now()     # datetime module lo datetime class lo now() function.    

print("Year:", now.year, "\nMonth:", now.month, "\nDate:", now.date(), "\nTime:", now.time()) # date and time both are object's  so we have to give ()

"""
"""
# Model: checking given string is number or not.

# 9. Write a Python program to check whether a given string is number or not using Lambda.

a = lambda x: True if x.isnumeric() else False      # string.isnumeric() >>> True if it is digit...False if not digit
b= lambda x : True if x.isdigit() else False        # string.isdigit() >>>True if it is digit...False if not digit
print(a('ch'))
print(b('10'))

"""

"""
# Model: Fibonacci using lambda

# 10. Write a Python program to create Fibonacci series upto n using Lambda.
# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Fibonacci series upto 6:
# [0, 1, 1, 2, 3, 5]
# Fibonacci series upto 9:
# [0, 1, 1, 2, 3, 5, 8, 13, 21]



# Intersection

# 11. Write a Python program to find intersection of two given arrays using Lambda.
# Original arrays:
list1= [1, 2, 3, 5, 7, 8, 9, 10]
list2= [1, 2, 4, 8, 9]
# Intersection of the said arrays: [1, 2, 8, 9]

# renu list lo common ga vunna items ni filter chesi bayataki teyyali so ...silter function vadali. filter(function, iterable)
intersection = list(filter(lambda x: x in list2, list1))  
print(intersection)

"""

"""
# Model: Rearranging arrays

# ee model matram chala confusing (i/1)(-i/1)(1/i)(-1/i)

# 12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
# Original arrays:
array=[-1, 2, -3, 5, 7, 8, 9, -10]
# Rearrange positive and negative numbers of the said array:
# [2, 5, 7, 8, 9, -10, -3, -1]


# print(sorted([1.0, -0.5, 0.333, -0.2, -0.1429, -0.125, -0.11, 0.1]))

print(sorted(array, key=lambda i: 0 if i == 0 else -1/i))  # [2, 5, 7, 8, 9, -10, -3, -1] positive lo ascending and negitive lo assending vastundi
print(sorted(array, key=lambda i: 0 if i == 0 else 1/i))   # [-1, -3, -10, 9, 8, 7, 5, 2] negative lo desending and positive lo desending


"""
"""
# Model: counting the positive and negative integiers.

# filter function

# 13. Write a Python program to count the even, odd numbers in a given array of integers using Lambda.

# Original arrays:
a= [1, 2, 3, 5, 7, 8, 9, 10]
# Number of even numbers in the above array: 3
# Number of odd numbers in the above array: 5

even= list(filter(lambda x: (x % 2 == 0), a))   
print(even) # list of even numbers
print(len(list(filter(lambda x: (x % 2 == 0), a))))  # number of even numbers
odd = list(filter(lambda x: (x % 2 != 0), a))  
print(odd)  # list of odd numbers
print(len(list(filter(lambda x: (x % 2 != 0), a))))  # number of odd numbers

"""
"""
# Filter using length

# 14. Write a Python program to find the values of length six in a given list using Lambda.

# filter(function, iterable)

weekdays= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Sample Output:
# Monday
# Friday
# Sunday

len_6_days = filter(lambda day: len(day) == 6, weekdays)
for days in len_6_days:
    print(days)

"""

"""
# Model : adding two lists by using map and lambda.

# 15. Write a Python program to add two given lists using map and lambda.

# Original list:
a= [1, 2, 3]
b= [4, 5, 6]
# Result: after adding two list
# [5, 7, 9]


# ikkada map and lambda function renditini kalipi vadali ani chepparu.... vallu cheppakapona map lambda vadalsinde 

# map(function, *iterables) >> map function same length vunde iterables enni iena tesukuntundi...daniki thaginattu manam lambda lo expression ivvali

print(list(map(lambda x, y: x+y, a, b)))  # if you want to add 2 lists 
print(list(map(lambda x, y, z: x+y+z, a, b, c))) # if you want to add 3 lists

"""

"""
# 16.Write a Python program to find the second lowest grade of any student(s) from the given names and grades of each student using lists and lambda.
#     Input number of students, names and grades of each student.
a=[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
# Second lowest grade: 2.0
# Names:
# N KAR

"""

"""
# 17. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
# Orginal list:
a = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# Numbers of the above list divisible by nineteen or thirteen:
# [19, 65, 57, 39, 152, 190]

# filter(function, iterable)

print(list(filter(lambda x: (x % 19 == 0) or (x % 13 == 0), a))) # number divisable by 19 or 13
"""

"""
# Model: polindrome by using lambda

# 18. Write a Python program to find palindromes in a given list of strings using Lambda. Go to the editor
# Orginal list of strings:
a = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
# List of palindromes:
# ['php', 'aaa']

print(list(filter(lambda x: (x == x[::-1]), a)))  # normal word == reversed words then it is a polindrome
print(list(filter(lambda x: (x == ''.join(reversed(x)),a))))
"""
"""
# Model : Finding anagrams using lambda.

# 19. Write a Python program to find all anagrams of a string in a given list of strings using lambda.
# Orginal list of strings:
a=['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# Anagrams of 'abcd' in the above string:
# ['bcda', 'cbda', 'adcb']


from collections import Counter

string = 'abcd'
print(list(filter(lambda x: (Counter(x) == Counter(string)),a)))  

"""

"""
# Model : numbers filtered

# 20. Write a Python program to find the numbers of a given string and store them in a list,
# display the numbers which are bigger than the length of the list in sorted form. Use lambda function to solve the problem.
# Original string:
a='sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'
# Numbers in sorted form:
# 20 23 56

# Explanation : 1.numbers ni list loki sorted form lo store cheyyali 2. store chesina list items lo eavi iethe length kanna peddavo adi print cheyyali

string_number = sorted([int(x) for x in a.split() if x.isnumeric()])

for num in filter(lambda x: (x > len(string_number)), string_number):
    print(num, end=" ")
"""
"""
# Method: multiply all the numbers in the list with specific function.

# 21. Write a Python program that multiply each number of given list with a given number using lambda function. Print the result.
# Original list:
a= [2, 4, 6, 9, 11]
# Given number: 2
# Result:
# 4 8 12 18 22

# Function: map(function, iterable)


# Explanation : 1. First every number ni given number tho multiplication cheyyali by using map function. 2. result line ga kavali 4 8 12 18 22 kabatti
                                                                           # for loop and end =" " parameter.
for x in map(lambda x: x*2, a): # we can extract values from map() function by using for loop.
    print(x, end=" ")

"""
"""
# 22. Write a Python program that sum the length of the names of a given list of names after removing the names that starts with an lowercase letter.
# Use lambda function.

a= ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']

# Explanation: 1. mundu manam list lo nunchi words ni filter cheyyali by using filter() function . filter function iterable object ni return chestundi
# 2. ee iterable object ni map function lo petti prathi element ki length kanukkoni danni sum cheyyali


print(sum(map(len, filter(lambda x: x[0].isupper(), a))))
"""
"""
# Model : Sum of all positive numbers , sum of all negative numbers.

# 23. Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function.
# Original list:
a=[2, 4, -6, -9, 11, -12, 14, -5, 17]
# Sum of the positive numbers: -32
# Sum of the negative numbers: 48

print("The sum of positive integers: ", sum(filter(lambda x: x > 0, a)))
print("The sum of all negative integers :", sum(filter(lambda x: x < 0, a)))
"""

# 24,25 do later.

"""
# 26. Write a Python program to find the list with maximum and minimum length using lambda.
# Original list:
a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])

# Explanation : 1. maximum and minim length anedi map, max function use chesi bayataki tesamu 2. list aneni max() function lo lambda function-
# use chesi dantlo  lenth adharamga list ni get chesamu.


print("The maximum length :", max(map(len, a)), "\nThe minimum length:", max(a, key=lambda x: len(x)))
print("The minimum length :", min(map(len, a)), "\nThe minimum length:", min(a, key=lambda x: len(x)))

"""

"""
# Model: sorting of nested lists.

# list akkade(position not be changed) vundali lopala elemants order sort avvali



# 27. Write a Python program to sort each sublist of strings in a given list of lists using lambda.
# Original list:
a= [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
# After sorting each sublist of the said list of lists:
# [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

print(sorted(a, key=lambda x: x[0]))  # nenu ee logic raste prathi sub list lo vunde 0'th index position lo vunna word adharam ga sort avutundi
# kaani manaki every nested list lo vunna elements sorted order lo vundali. so daniki manam for loop raasi okkoka list ni get chesi sor  t cheyyali

print([sorted(x, key=lambda x:x[0], reverse=False)for x in a])

# for loop vaadi okkoka nested list lambda loki pampi prathi word lo vunna first letter adharam ga sort cheyyali.

"""


"""
# 28. Write a Python program to sort a given list of lists by length and value using lambda.
# Original list:
a = [[2], [0], [1, 3], [0,7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

a.sort(key=lambda x: (len(x), x), reverse=False)

print(sorted(a, key=lambda x: (len(x), x), reverse=False))
print(a)
"""

"""
# Model: Hetro genius elements lo maximum number kanukkovali

# 29. Write a Python program to find the maximum value in a given heterogeneous list using lambda.
# Original list:
a = ['Python', 3, 2, 4, 5, 'version']
# Maximum values in the said list using lambda:
# 5


# Explanation : max function manam iterable pass chesi danni lambda function dwara numbets matram bayataki tesi maximum kanukuntam.

# a lo prathi element lambda function arguments loki veltundi lambda isinstance loki pampistundi ....isinstance function lo adi intaaa kada ani
# choostundi ....int iethe further calculation ki pamputhundi ledante ledu.


# isinstance function::::: it returns boolen >>>> isinstance(item,type) >>>it returns true if specific item and mentioned type is correct
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.

print(max(a, key=lambda x: (isinstance(x, int), x)))
print(min)

"""












"""
#Model: Sorting the matrix(nested_lists) according to the sum of elemnts of matrix

# 30. Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.
# Original Matrix:
# a=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
# Original Matrix:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]


a.sort(key=lambda x: sum(x))  # by using sort() function. 
print(a)
print(sorted(a, key=lambda x: sum(x), reverse=False)) # by using sorted function.

"""




"""
# Model: Extracting list items based on the length.

# 31. Write a Python program to extract specified size of strings from a give list of string values using lambda.
# Original list:
a = ['Python', 'list', 'exercises', 'practice', 'solution']
# length of the string to extract:
# 8
# After extracting strings of specified length from the said list:
# ['practice', 'solution']

print(list(filter(lambda x: (len(x) == 8), a)))  # it will only filter if len of x is equal to 8.

"""

"""
# Model: counting float number

# 32. Write a Python program to count float number in a given mixed list using lambda.
# Original list:
a = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# Number of floats in the said mixed list:
# 3


# Explanation: prathi element check cheyyali and adi float iethe list lo petti danni length kanukkovali

print(len(list(filter(lambda x: (type(x) == float), a))))   # if it is float filter it
print(len(list(filter(lambda x: (type(x) == str), a))))  # if it is str filter it

"""



"""
# 33.Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda.
# Input the string:
# a=W3resource
# ['Valid string.']


# doubt








"""
"""
# Model: Dict lo vunna values sort cheyyali

# 34. Write a Python program to filter the height and width of students, which are stored in a dictionary using lambda.
# Original Dictionary:
a = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height> 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}


print(dict(filter(lambda x: (x[1][0] > 6 and x[1][1] >= 70), a.items())))  

"""
# Model : checking specified list sorted or not.


# 35. Write a Python program to check whether a specified list is sorted or not using lambda.
# Original list:
a=[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# Is the said list is sorted!
# True
# Original list:
# [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# Is the said list is sorted!
# False

# Explanation : ichina list  already sorted order lo vunte manaki True ledante False.

#  not understood.











"""
# 36. Write a Python program to extract the nth element from a given list of tuples using lambda.
# Original list:
a = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# Extract nth element ( n = 0 ) from the said list of tuples:
# ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
# Extract nth element ( n = 2 ) from the said list of tuples:
# [99, 96, 94, 98]

print(list(map(lambda x: x[0], a)))  # every element in a extract 0th element..
print(list(map(lambda x: x[2], a)))  # every element in a extrace 1th element ..
"""











"""
# Model : sorting nested lists by using index


# 37. Write a Python program to sort a list of lists by a given index of the inner list using lambda.
# Original list:
a = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# Sort the said list of lists by a given index ( Index = 0 ) of the inner list
# [('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]
# Sort the said list of lists by a given index ( Index = 2 ) of the inner list
# [('Wyatt Knott', 91, 94), ('Brady Kent', 97, 96), ('Beau Turnbull', 94, 98), ('Greyson Fulton', 98, 99)]


a.sort(key=lambda x: x[0])
print(a)

"""


"""
# Model: Removing elements from the first list which are presented at list2


# 38. Write a Python program to remove all elements from a given list present in another list using lambda.
# Original lists:
# list1:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2:
b = [2, 4, 6, 8]
# Remove all elements from 'list1' present in 'list2:
# [1, 3, 5, 7, 9, 10]

# Explanation: vere list lo vunde elements ee list lo teseyali.


print(list(filter(lambda x: (x not in b), a)))  # x anedi b lo vundakudadu.

"""

"""
# 39. Write a Python program to find the elements of a given list of strings that contain specific substring using lambda.
# Original list:
a = ['red', 'black', 'white', 'green', 'orange']
# Substring to search:
# ack
# Elements of the said list that contain specific substring:
# ['black']
# Substring to search:
# abc
# Elements of the said list that contain specific substring:
# []


print(list(filter(lambda x: ('ack' in x), a)))  # ('ack' in x) means filter if 'ack' in x ....
print(list(filter(lambda x: ('abc' in x), a)))

# # model with normal function
# def find_substring(str1, sub_str):
#     result = list(filter(lambda x: sub_str in x, str1))
#     return result
# colors = ["red", "black", "white", "green", "orange"]
# print("Original list:")
# print(colors)
# 
# sub_str = "ack"
"""
"""
# Model : nested list elements ni inko normal list(without nested) elements ni compare chesi common ni bayataki teyyali.

# first llist : normal..... second list : nested....
# 40. Write a Python program to find the nested lists elements, which are present in another list using lambda.
# Original lists:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
b = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# Intersection of said nested lists:
# [[12], [7, 11], [1, 5, 8]]


# in filter() or map() or reduce() functions we must convert by using constructor functions.

print([list(filter(lambda x: (x in a), sublist)) for sublist in b])  # list function is used for creating nested list
# if you use [] instead of list constructor then output will be like bellow 
# [[<filter object at 0x0000020E9E2CBA90>], [<filter object at 0x0000020E9E2CBA30>], [<filter object at 0x0000020E9E2CB9D0>]]
"""
"""

# Model : Reverse the word's internally in a list

# Explanation: words anni vunna position lone reverse avvli.

# 41. Write a Python program to reverse strings in a given list of string values using lambda.
# Original lists:
a = ['Red', 'Green', 'Blue', 'White', 'Black']
# Reverse strings of the said given list:
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']


# by using slicing function and by using join()and reversed function.

# reversed function anedi iterator object ni return chestundi manam join function use chesi output bayataki teyyavachu.


print(list((map(lambda x: x[::-1], a))))
print(list(map(lambda x: ("".join(reversed(x))), a)))
print("".join(reversed('chenhu')))  # for understanding purpose
"""

"""
# Model: product of all the elements in the list.

# 42. Write a Python program to calculate the product of a given list of numbers using lambda.
# list1:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Product of the said list numbers:
# 3628800
# list2:
b = [2.2, 4.12, 6.6, 8.1, 8.3]
# Product of the said list numbers:
# 4021.8599520000007

from functools import reduce

print("THe multiplication of said list is:", reduce(lambda x, y: x * y, a))

print("The multiplication of said list is:", reduce(lambda x, y: x * y, b))

"""

"""
# Model : multiplication of all elements in a list


# 43. Write a Python program to multiply all the numbers in a given list using lambda.
# Original list:
a = [4, 3, 2, 2, -1, 18]
# Mmultiply all the numbers of the said list: -864
# Original list:
b = [2, 4, 8, 8, 3, 2, 9]
# Mmultiply all the numbers of the said list: 27648


# Explanation : anni elements kalipi oka element ga return cheyyali so manam reduce function vadali

# reduce function lo rendu inputs tesukuntamu adi first rendu list elements ki assign iyyi aa tharuvatha expression ni first elemnt lo store-
# chesukuntundi and 2nd element list lo vunna remeing elements loki traverse avutundi.

# Reduce function : from functools import reduce  ::: reduce(lambda x, y: x*y, iterable)

from functools import reduce

print('The multiplying all elements in the said list:', reduce(lambda x, y: x * y, a))
print("The multiplying all the elements in the said list:", reduce(lambda x, y: x * y, b))

print(reduce(lambda x, y: x + y, a))
"""

"""
# Method:1 Calculating average value in the tuple of tuples by

# 44. Write a Python program to calculate the average value of the numbers in a given tuple of tuples using lambda.
# Original Tuple:
a = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# (30.5, 34.25, 27.0)
# Original Tuple:
# ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# (25.5, -18.0, 3.75)

# Zip function is very important here.

print(tuple((map(lambda x: sum(x) / float(len(x)), zip(*a)))))  # unpacking every tuple element >>> prathi tuple lo 0th elemnts anni add avutundi
# aa tharuvatha prathi tuple lo 1st index position and so on...
# Explanation : zip function is used for parrell iteration
"""

"""
# Map function:  Converting string to the int in tuple of tuples.

# 45. Write a Python program to convert string element to integer inside a given tuple using lambda.
# Original tuple values:
a = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
# New tuple values:
# ((233, 33), (1416, 55), (2345, 34))

# Explanation = oka tuple lo string elements ni intiger ga marchali .... idi nested tuple every tuple ki manam apply cheyyali so map function
# use cheyyali....out put tuple lo kavali kabatti....tuple () function vadali.


print(tuple(map(lambda x: (int(x[0]), int(x[-1])), a)))
print(list(map(lambda x: (int(x[0]), int(x[-1])), a)))

"""
# Model: Extract  Max,Min values fron the list and their index position also.

# 46. Write a Python program to find index position and value of the maximum and minimum values in a given list of numbers using lambda.
# Original list:
# a=[12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
# Index position and value of the maximum value of the said list:
# (5, 89)
# Index position and value of the minimum value of the said list:
# (3, 10.11)

# Formula: max function lo enumerate function rayali.... endukante manam index position get cheyyadaniki...
# enumerate function create cheste (index position , value) deenni lambda function adharam ga manam short chestamu.....
#


# print('The maximum value and index position :',max(enumerate(a), key= lambda x: x[1]))   # 0 for index and 1 for item .....based on item we are getting maximum value
# print("The minimum value and their index:", min(enumerate(a), key=lambda x: x[1]))
"""
"""
# Model : Sorting of mixed list (int & words)

# 47. Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings.
# Original list:
# a = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# Sort the said mixed list of integers and strings:
# [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
# a.sort(key=lambda x: (isinstance(x, str), x))
# print(a)

# Model : sort numbers in a list

# 48. Write a Python program to sort a given list of strings(numbers) numerically using lambda.
# Original list:
# a=['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# Sort the said list of strings(numbers) numerically:
# ['-500', '-12', '0', '4', '7', '12', '45', '100', '200']

# Explanation : normal ga iethe manam list lo vunna prathi element ni int() loki convert chesi aa tharuvatha sort chesi malli str loki marchali
# kaani lambda lo ala kaadu >>> daani intiger value adharamga sort cheyyamani cheppavachu (int(x))....

# print(sorted(a, key=lambda x: int(x), reverse=False))

"""
"""
# Model: frequency using lambda.

# 49. Write a Python program to count the occurrences of the items in a given list using lambda. Go to the editor
# Original list:
# a= [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
# Count the occurrences of the items in the said list:
# {3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}

# print(dict(map(lambda x: (x, a.count(x)), a)))  # (x, a.count(x)) >>> this will returns tuple contains x element and their count...
# with these tuples we can convert to dict by using dict function.
"""

"""
# 50. Write a Python program to remove specific words from a given list using lambda.

# Original list:
# a = ['orange', 'red', 'green', 'blue', 'white', 'black']
# Remove words:
# ['orange', 'black']
# After removing the specified words from the said list:
# ['red', 'green', 'blue', 'white']


# print('The new list :', list(filter(lambda x: x != 'orange' and x != 'black', a)))

# Note: if u have to remove more words then write this words in a list assign to a varible , write logic .... ( words not in) 

"""
"""
# 51. Write a Python program to find the maximum and minimum values in a given list of tuples using lambda function.
# Original list with tuples:
# a=[('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
# Maximum and minimum values of the said list of tuples:
# (74, 62)

# map(function, iterable)

# print("The maximum value :", max(map(lambda x: x[1], a)), "\nThe minimum value:", min(map(lambda x: x[1], a)))
"""

"""
# Model: Remove none value by using lambda

# 52. Write a Python program to remove None value from a given list using lambda function.
# Original list:
# a= [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# Remove None value from the said list:
# [12, 0, 23, -55, 234, 89, 0, 6, -12]

# filter(function, iterable)

# print(list(filter(lambda x: x!= None, a)))
"""
"""