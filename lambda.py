# Note: lambda function never start's with def keyword it start's with lambda keyword

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
print(sorted(array, key=lambda i: 0 if i == 0 else i/-1)) # [9, 8, 7, 5, 2, -1, -3, -10] total desending (i/-1)
print(sorted(array, key=lambda i: 0 if i == 0 else i/1))  # [-10, -3, -1, 2, 5, 7, 8, 9] total ascending  (i/1)

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



21. Write a Python program that multiply each number of given list with a given number using lambda function. Print the result. Go to the editor
Original list: [2, 4, 6, 9, 11]
Given number: 2
Result:
4 8 12 18 22





