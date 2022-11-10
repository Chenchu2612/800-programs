"""
# 1.Write a Python program to create a tuple.

# there are tho methods are available to create a tuple

a) x=()  # with paranthesis
b) y= tuple() # with tuple function
"""
"""
# 2. Write a Python program to create a tuple with different data types

method:2
# a= 1, 'apple', True, None, 2.5, (5+2j), False
# print(type(a))
# print(tuple(a))

method:1
def create_tuple(values):
    return tuple(values)


print(create_tuple(eval(input("enter the values for creation of tuple: "))))
"""
"""
# 3.Write a Python program to create a tuple with numbers and print one item.

# note: by default tuple no need paranthesis , in case if we want to create tuple with one item we need to put a comma
#         after the tuple item

# we can print a single item by using index
def create_tuple_num(numbers):
    return numbers


print(create_tuple_num(eval(input("Enter the numbers: "))))
"""
"""
# 4.Write a Python program to unpack a tuple in several variables.

# Note: in case of unpacking the tuples, the number of varibles (i.e left side of the = symbole) must equal to number of
#         items in the tuple otherwise it will raise an error
# if you want to override those error we shoud put * before any varible to assign remaining values accordingly those
    varible values will come in the form of list

# pack = 1, 'apple', True, None, 2.5, (5+2j), False  # packing

# n1, n2, n3, n4, n5, n6, n7 = 1, 'apple', True, None, 2.5, (5+2j), False  # unpacking

# n1, n2, n3, n4, *n5 = 1, 'apple', True, None, 2.5, (5+2j), False
"""
"""
# 5.Write a Python program to add an item in a tuple.

# method:1 by directly adding tuple to a tuple 
# method:2 by using slicing
# method:3 by converting list and do certain modifications and convert to tuple
# Note: while converting one datastructure to another datastructure by using constructor functions(list(), tuple()
#         set(), dict() ) we must assign a varible while converting. otherwise it won't works.

tuple1 = (1, 'apple', True, None, (6+5j))

tuple1 = tuple1+(4,)
print(tuple1)

tuple1 = tuple1[:2]+(4,)+tuple1[2:]
print(tuple1)


list1= list(tuple1)
list1.append(4)
tuple2 = tuple(list1)
print(tuple2)
"""
"""
# 6. Write a Python program to convert a tuple to a string

input = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
output = 'exercises'

method:1

def convertion(tup):
    str = ""
    for ch in tup:
        str += ch
    return str


print(convertion(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')))

method : 2 by using join function

def convert(tup):
    return "".join(tup)


print(convert(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')))

"""
"""
7.Write a Python program to get the 4th element and 4th element from last of a tuple

fourth element = tuple[3]
fourth element from last tuple[-4]
"""
"""
# ***8. Write a Python program to create the colon of a tuple

# we can solve colon of a tuple by  using the deepcopy

tuple1 = (5, True, [], None, (5+4j))

from copy import deepcopy

tuple2 = deepcopy(tuple1)
tuple2[2].append('12_LPA')

print(tuple1)
print(tuple2)

"""
"""
# 9. Write a Python program to find the repeated items of a tuple.

# meaning : number of times it repeats in the tuple

method:1
tuple = 2, 4, 5, 6, 2, 3, 4, 4, 7
print(tuple.count(4))

method:2
def repeated(tup, item):
    return tup.count(item)


print(repeated((2, 4, 5, 6, 2, 3, 4, 4, 7), 4))
"""
"""
# 10. Write a Python program to check whether an element exists within a tuple.

# method:1
def check_element(tuple):

    return "s" in tuple


print(check_element(('a','3')))

# method:2
tuple=('a', 2, True)
print("a" in tuple)

"""
"""
# 11. Write a Python program to convert a list to a tuple.

# Note: while using constructor functions we must assign a varible while converting

list1 = [1, 2, 3]
tuple1 = tuple(list1) # we must assingn  a varible while converting
print(tuple1)
"""
"""
# 12.Write a Python program to remove an item from a tuple.

method1: by converting tuple into list and apply remove method (list.remove(item)) and again convert to tuple 
method2: by using the slicing method :- take slices wich we want and add those slices
"""
"""
# 13. Write a Python program to slice a tuple.
# esay---copied from w3 schools

#create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#used tuple[start:stop] the start index is inclusive and the stop index
_slice = tuplex[3:5]
#is exclusive
print(_slice)
#if the start index isn't defined, is taken from the beg inning of the tuple
_slice = tuplex[:6]
print(_slice)
#if the end index isn't defined, is taken until the end of the tuple
_slice = tuplex[5:]
print(_slice)
#if neither is defined, returns the full tuple
_slice = tuplex[:]
print(_slice)
#The indexes can be defined with negative values
_slice = tuplex[-8:-4]
print(_slice)
#create another tuple
tuplex = tuple("HELLO WORLD")
print(tuplex)
#step specify an increment between the elements to cut of the tuple
#tuple[start:stop:step]
_slice = tuplex[2:9:2]
print(_slice)
#returns a tuple with a jump every 3 items
_slice = tuplex[::4]
print(_slice)
#when step is negative the jump is made back
_slice = tuplex[9:2:-4]
print(_slice)
"""
"""
# 14. Write a Python program to find the index of an item of a tuple

Note: tuple supports only 2 methods i.e count, index 
formula = tuple.index(item)

# method:1
tuple=(1,2,3,4)
print(tuple.index(3))

method:2
def find_index_item(tup, item):
    return tup.index(item)

print(find_index_item((1,2,3,4), 4))

"""
"""
# 15. Write a Python program to find the length of a tuple.


def length_tuple(tup):
    return "The length of a tuple is : {}".format(len(tup))


print(length_tuple((1, 2)))

"""
"""
# 16. Write a Python program to convert a tuple to a dictionary.

method:1

tuple=((1, "a"), (2, "b"))


def tup_to_dict(tup):
    dit={}
    for k,v in tup:
        dit[k]=v
    return dit


method:2


def tuple_dict(tup):
    return dict((y,x) for x,y in tup)


print(tuple_dict(((1, "a"), (2, "b"))))
"""

"""
# 17.Write a Python program to unzip a list of tuples into individual lists.

# * is used to unzip the values
input = [(1, 2), (3, 4), (8, 9)]
output = [(1, 3, 8), (2, 4, 9)]


def unzip(item):
    return list(zip(*input))


print(unzip([(1, 2), (3, 4), (8, 9)]))
"""
"""
# 18.Write a Python program to reverse a tuple.

# method:1 by using reversed function.
# this reversed method always returns the reversed object we have to convert it by using constructor functions


def reverse(tup):
    return reversed(tup)


print(tuple(reverse((1, 2))))


# method:2

def tup_reverse(tup):
    tupl=()
    for i in tup:
        tupl = (i,)+tupl    

    return tupl


print(tup_reverse((1, 2, 3)))

"""
"""
# ****19. Write a Python program to convert a list of tuples into a dictionary.


list = [(1, 2), (4, 6), (7, 8)]
dict=dict()
for x, y in list:
    dict[x] = y
print(dict)


input = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
output= {'x': [1, 2, 3], 'y': [1, 2], 'z': [1]}


def list_of_tup_to_dict(item):
    dict={}
    for k, v in item:
        if k not in dict:
            dict[k] = [v]   #output requires every value in list so we set value in list formate
        else:
            dict[k].append(v) # if key already exist the value will appends to the value list

    return dict

print(list_of_tup_to_dict(input))

"""
"""
# 20. Write a Python program to print a tuple with string formatting.
# Sample tuple : (100, 200, 300)
# Output : This is a tuple (100, 200, 300)


def tuple_string_format(item):
    return "This is a tuple {}".format(item)   # we can put {0} in string format method


print(tuple_string_format((1, 2, 3, 4)))

"""
"""
# ***21. Write a Python program to replace last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

# by using slicing concept we can change

def replace_last_value(item):
    return [i[:-1]+(100,) for i in item]

    
print(replace_last_value([(10, 20, 40), (40, 50, 60), (70, 80, 90)]))
"""
"""
# 22. Write a Python program to remove an empty tuple(s) from a list of tuples. Go to the editor
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d',)]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

# method:1 normal
def remove_emepty_tuple(items):
    new_list=[]
    for i in items:
        if len(i)!=0:
            new_list.append(i)
    return new_list

# method:2 super

# ***Note: In list comprehension "if i" it eliminates if i is emepty


def remov_emepty_tuples(items):
    return [ i for i in items if i]


print(remov_emepty_tuples([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d',)]))

"""

"""
# 23. Write a Python program to sort a tuple by its float element.
# Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

# sorted function takes 3 parameters one is iterable, next is key= based on what we have to sort , reverse =True/False
    by default it is False  reverse=True sort decending... reverse = False sort ascending.  

def sort_by_tuple(item):
    return sorted(item, key=lambda a: a[-1], reverse=True)


print(sort_by_tuple([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]))
"""

"""
# 24. Write a Python program to count the elements in a list until an element is a tuple

# stop count  when an tuple item comes .



def count_item(item):
    count = 0
    for x in item:
        if type(x) == tuple:             # here we can use isinstance function also    if isinstance(n, tuple):
            break                                                                          #break
        count += 1         #The isinstance() function returns True if the specified object is of the specified type
    return count                         # isinstance(object, type)


print(count_item([10, 20, 30, (10, 20), 40]))

"""
"""
# 25. Write a Python program convert a given string list to a tuple. Go to the editor
# Original string: python 3.0
# <class 'str'>
# Convert the said string to a tuple:
# ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
# <class 'tuple'>

# Note: In output there is no space ....so in our code we have to eliminate the spaces we can use isspace() function
#     string.isspace()


def convert(item):
    return tuple(ch for ch in item if not ch.isspace())    # by default tuple comprehension returns the generator object
                                                             # we have to convert this object to tuple by using tuple()
                                                             # constructor
print(convert('python 3.0'))
"""
"""
# 26. Write a Python program calculate the product, multiplying all the numbers of a given tuple. Go to the editor
# Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product - multiplying all the numbers of the said tuple: -864
# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product - multiplying all the numbers of the said tuple: 27648


def multiplying(item):
    number = 1
    for i in item:
        number *= i
    return number

print(multiplying((2, 4, 8, 8, 3, 2, 9)))
"""
"""
# ****27. Write a Python program to calculate the average value of the numbers in a given tuple of tuples. 
# Original Tuple:
# ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# Average value of the numbers of the said tuple of tuples:
# [30.5, 34.25, 27.0, 23.25]
# Original Tuple:
# ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# [25.5, -18.0, 3.75]



def average(item):
    return [sum(x)/len(x) for x in zip(*item)]    # visuvalize how zip function works  see bellow for loop for better 
                                                        understanding.

print(average(((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))))


for x in zip(*((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))):
    print(x)
"""

"""
# ***28. Write a Python program to convert a tuple of string values to a tuple of integer values. Go to the editor
# Original tuple values:
# (('333', '33'), ('1416', '55'))
# New tuple values:
# ((333, 33), (1416, 55))

def conversion(item):
    return tuple([(int(x[0]), int(x[-1])) for x in item])


print(conversion((('333', '33'), ('1416', '55'))))
"""

"""
# 29. Write a Python program to convert a given tuple of positive integers into an integer. Go to the editor
# Original tuple:
# (1, 2, 3)
# Convert the said tuple of positive integers into an integer:
# 123
# Original tuple:
# (10, 20, 40, 5, 70)
# Convert the said tuple of positive integers into an integer:
# 102040570

# method:1 traditional approach
def conversion(item):
    st = ""
    for i in item:
        st += str(i)
    return st


print(conversion((10, 20, 40, 5, 70)))


# method:2 formal approach.

# by using map function: The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.
# map(function, iterables)


def str_to_int(item):
    return int("".join(map(str, item)))  # explanation: map(str, item) = converting every element in iterable to str 

                                            # "".join(map(str, item)) = it joins the strings in the iterable    
print(str_to_int((10, 20, 40, 5, 70)))

"""
"""
# 30. Write a Python program to check if a specified element presents in a tuple of tuples. Go to the editor
# Original list:
# (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
# Check if White presenet in said tuple of tuples!
# True
# Check if White presenet in said tuple of tuples!
# True
# Check if Olive presenet in said tuple of tuples!
# False


def check(items, item):
    return any(item in x for x in items)  # any() function and all() function is important


print(check((('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime')), 'Yellow'))
"""
"""
# 31.Write a Python program to compute element-wise sum of given tuples.
# input:
# x = (1,2,3,4)
# y = (3,5,2,1)
# z = (2,2,3,1)
#
# output: (6, 9, 8, 6)


def parlell_addition(item1,item2, item3):   # or here we can use *item  instead of writing all 3 items
    return tuple(sum(x) for x in zip(item1, item2, item3))  # here also we can provide *item ,if we provide *item at 
                                                                        # function definition


print(parlell_addition((1, 2, 3, 4), (3, 5, 2, 1),(2, 2, 3, 1)))

"""
"""
# 32. Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.
# Original list of tuples:
# [(1, 2), (2, 3), (3, 4)]
# Sum of all the elements of each tuple stored inside the said list of tuples:
# [3, 5, 7]
# Original list of tuples:
# [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
# Sum of all the elements of each tuple stored inside the said list of tuples:
# [9, -1, 7, 8]

# method:1 by using map function

def sum_of_all_items(item):
    return list(map(sum, item))


print(sum_of_all_items([(1, 2), (2, 3), (3, 4)]))


# method:2


def sum_of_all(item):
    list = []
    for x in item:
        list.append(sum(x))
    return list


print(sum_of_all([(1,2,6), (2,3,-6), (3,4), (2,2,2,2)]))
"""
"""
# 33. Write a Python program to convert a given list of tuples to a list of lists. Go to the editor
# Original list of tuples: [(1, 2), (2, 3), (3, 4)]
# Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
# Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]

# method:1 by using map function


def tuples_to_lists(item):
    return list(map(list, item))


print(tuples_to_lists([(1, 2), (2, 3), (3, 4)]))

# method:2 with Using list Comprehension


def tup_to_list(item):
    return [list(x) for x in item]


print(tup_to_list([(1, 2), (2, 3), (3, 4)]))

"""

