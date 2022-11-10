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














