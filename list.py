# w3 resource programmes

# 1. Write a Python program to sum all the items in a list.
""""
def sum_list(items):
    sum = 0
    for i in items:
        sum += i
    return sum


print(sum_list([1, 2, 3]))

"""
"""
# 2. Write a Python program to multiply all the items in a list.


def mul_list(items):
    mul = 1
    for i in items:
        mul *= i
    return mul


print(mul_list([1, 2]))
"""

# 3. Write a Python program to get the largest number from a list.
"""
def max_num_in_list(items):
    max = items[0]   # we have to initialize the value for "max" for that we have to take first value in list 
    for i in items: # compare each value in list with "max" value
        i > max
        max = i  "if value is greather_than max then .... "max" then max value is that value 
    return max


print(max_num_in_list([1, 0, 90]))
"""

# 4.Write a Python program to get the smallest number from a list

"""
def smallest_num_list(items):
    min = items[0]
    for i in items:
        if i<min:          # this is same as max but we have to write lessthen symbole instead of greateherthen 
            min = i
    return min


print(smallest_num_list([1, -2, 3]))
"""

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and
# last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

"""
def count_items(items):
    count = 0
    for i in items:
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1
    return count


print(count_items(['ab', 'xyz', 'abc', '1222']))
"""

# 6.Write a Python program to get a list, sorted in increasing order by the last element in each tuple
# from a given list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""

# sorted increasing order means ascendeing order
def last(n): return n[-1]   # we have to create a function for the position


def sort_list(tuples):   # for tuples sorted is best
    return sorted(tuples, reverse = True, key=last)


print(sort_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
"""

# 7. Write a Python program to remove duplicates from a list.
"""
def remove_dup(items):
    new_list = []
    for i in items:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(remove_dup([1, 2, 'a', 3, 1, 3, 'a']))
"""

#  by using list comprehension method

"""
def remove_dup_comp(items):
    l = []   # initialise emepty list 
    [l.append(i) for i in items if i not in l]  # we are using list comprehension
    return l


print(remove_dup_comp([1, 2, 3, 1]))
"""
# 8. Write a Python program to check a list is empty or not.

"""
def emepty_not(items):
    if len(items) != 0:
        print("list is not emepty")
    else:
        print("list is emepty")

emepty_not([1])
"""

# 9.Write a Python program to clone or copy a list.

# copiclone

# copy and cloning both are same we can do those with copy function and by using slice operator
"""
new_list = list(oid_list)   # by using list function
        or
new_list = old_list.copy()  # by using copy method
        or
new_list = old_list[:]    # by using slice operator    
"""

# 10.Write a Python program to find the list of words that are longer than n from a given list of words.

# list lo vunde words length anedi ichina number kante ekkuva vundali.

"""
def new_word_list(n, items):
    new_list = []
    [new_list.append(i) for i in items if len(i) > n]
    return new_list


print(new_word_list(4, ["apple", "ant", "ball", "cat"]))
"""

# model: 2 -- incase if they give string of word line

"""
def new_list_words(n, items):
    st_to_list = items.split() # splitting the string into list (by default split function splits based on spaces)
    new_list = []
    [new_list.append(i) for i in st_to_list if len(i) > n]
    return new_list


print(new_list_words(4, "The quick brown fox jumps over the lazy dog"))
"""

"""
# 11.Write a Python function that takes two lists and returns True if they have at least one common member.


def common_items(list1, list2):
    for i in list1:  # by using in operator and if condition
        if i in list2:
            return True
    return False


print(common_items([1, 2, 3], ['a', 4, 5]))

# by using two for loops and compare items.


def common_data(list1, list2):
    result = False    # initialise the result
    for i in list1: 
        for j in list2:
            if i == j:  # we can give != also here....if we give result True at begining
                result = True
    return result


print(common_data([1, 2, 3, 4, 5], ['k', 6, 7, 8, 9]))
"""

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']


#  we can use by using enumerate function

"""
def remove(items):
    a = [j for i, j in enumerate(items) if i not in (0, 4, 5)]
    return a


print(remove(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

"""

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
"""  # it is very important 
array = [[['*' for col in range(6)]for col in range(4)]for row in range(3)]
print(array)
"""

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

"""
def remove_even(items):
    return [i for i in items if i % 2 == 0]   # we can write directly by using list comprehension method


print(remove_even(eval(input("enter the list :"))))
"""

# 15. Write a Python program to shuffle and print a specified list.

"""
from random import shuffle


def jig_jag(items):
    shuffle(items)   # here we are shuffling the items
    return items


print(jig_jag(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))
"""
# 16.Write a Python program to generate and print a list of first and last 5 elements where the values
# are square of numbers between 1 and 30 (both included).

# 1 to 30 (both included) we need first 5 and last five numbers squares....
"""

def first_last_square():
    return [i**2 for i in range(1, 31) if i < 6 or i > 25]  # i value must be less than 6 or greather than 25


print(first_last_square())

"""

# 17. Write a Python program to generate and print a list except for the first 5 elements,
# where the values are square of numbers between 1 and 30 (both included).

"""
def list_except():
    return [i**2 for i in range(1, 31) if i > 6]


print(list_except())
"""

# ** 18.Write a Python program to generate all permutations of a list in Python.

"""
from itertools import permutations


def per(items):  # here we can provide 'n' also to print set of items.
    return list(permutations(items))


print(per([1, 2, 3]))  # if we want to provide user input type eval(input("enter the numbers":)
"""

# 19.Write a Python program to get the difference between the two lists
"""

def difference(li1, li2):
    return [i for i in li1 + li2 if i not in li1 or i not in li2]  # add two lists 
 

print(difference([1, 3, 5, 7, 9], [1, 2, 4, 6, 7, 8]))
"""

# 20. Write a Python program access the index of a list.

# model:1 by using enumerate

"""
def index(items):
    return [i for i in enumerate(items)]


print(index([1, 2, 3, 4]))
"""
# model2:

"""
def index(items):
    for i, j in enumerate(items):
        print(i, j)


index([1, 2, 3])
"""

"""
def index(items):
    positive = 0
    a=len(items)
    for i in items:
        print(i, "items at positive index is:{} negative index is{}".format(positive, positive-len(items)))
        positive += 1


index([1, "a", "r"])
"""

# 21.Write a Python program to convert a list of characters into a string

"""
def list_string(items):
      return "".join(items)   # in join function iterable must be inside the join function 


print(list_string(["a","b"]))
"""
# 22.Write a Python program to find the index of an item in a specified list.

"""
def index(items, item):
    return items.index(item)  # list.index(list_item)


print(index([1, 30, 40, 50], 40))
"""
# 23.  Write a Python program to flatten a shallow list

"""
def add_all_lists(items):

    return [j for i in items for j in i]  # here we can square the value and (where ever nested list arise then we 
                                            should treat those lists as shallow lists


print(add_all_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
"""

# 24. Write a Python program to append a list to the second list.

"""
def append_new_list(list1, list2):
    [list1.append(i) for i in list2]
    return list1    # we can append by using "return list1+list2" 

doubt: return [list1.append(i) for i in list2] why it is coming none

print(append_new_list([1, 2], [3, 4]))
"""

# 25.Write a Python program to select an item randomly from a list.
"""
from random import choice

# here we are importing random module on that we are using choice function


def select_choice(items):    
    return choice(items)

print(select_choice([1,2,3,4,5,6]))

"""

# 26. Write a python program to check whether two lists are circularly identical.
"""
# circularly identical = if u put two list items in a two circles separately then the items must be in same order

# step:1 double the list1
# step:2 iterate by using new list1 & range function (we doubled previously)
# step:3 compare list2 with list1 by using slice the list1

def compare(list1, list2):
    list1.extend(list1) # we can use by list1*2
    for i in range(len(list1)): 
        if list2 == list1[i:i+len(list2)]:  # slicing the list1 and comparing 
            return True
    return False


print(compare([10, 10, 0, 0, 10], [10, 10, 10, 0, 0]))
"""

# 27. Write a Python program to find the second smallest number in a list.
# 28. second largest number


# taking first element and comparing to remaining elements
"""

def single_short(items):
    largest = items[0]
    largest2 = None
    smallest = items[0]
    smallest2 = None
    for i in items[1:]:
        if i > largest:
            largest2 = largest
            largest = i
        elif largest2 is None or i > largest2:
            largest2 = i

        if i < smallest:
            smallest2 = smallest
            smallest = i
        elif smallest2 is None or i<smallest2:
            smallest2 = i

    print("largest", largest)
    print("largest2", largest2)
    print("smallest", smallest)
    print("smallest2", smallest2)


single_short([-1.2, -2.8, -2.1, -4.5, -2.5, ])
"""

# 29.Write a Python program to get unique values from a list.

#  it means remove duplicates

"""
def unique_values(items):
    list=[]
    [list.append(i) for i in items if i not in list]
    return list


print(unique_values([1, 2, 3, 1, 4, 5, 6]))
"""

# 30.Write a Python program to get the frequency of the elements in a list.

# it means count's the number of times repeated each element in the list.
# where ever  the name frequency exists we must use the dict method
"""

def frequency(items):
    freq = {}
    for i in items:
        if i not in :
            freq[i] = 1
        else:
            freq[i] += 1
        
    return freq


print(frequency([10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]))

"""

# 31. Write a Python program to count the number of elements in a list within a specified range.

# with in qa specific range we have to count the numers.

"""
def count_range(items, min_val, max_val):
    count=0
    for x in items:
        if min_val <= x <= max_val:
            count += 1
    return count


print(count_range([10, 20, 30, 40, 40, 40, 70, 80, 99], 30, 40))
"""

# 32.Write a Python program to check whether a list contains a sublist.

# very important
"""
def is_sublist(item1, item2):
    sub_list = False

    if item2 == []:
        sub_list = True
    elif item2 == item1:
        sub_list = False
    elif len(item2) > len(item1):
        sub_list = False

    else:
        for i in range(len(item1)):
            if item1[i] == item2[0]:  # comparing first element in list2 with list1
                n = 1
                while (len(item2) > n) and item1[i+n] == item2[n]: 
                    n += 1
                if n == len(item2):
                    sub_list = True

    return sub_list


print(is_sublist([2, 4, 3, 5, 7], [4, 3, 5]))
"""

# 33. ignored

# 34. prime number program


# 35.Write a Python program to create a list by concatenating a given list which range goes from 1 to n.

# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

# we are iterating and using format method also
"""
def new_list(list1, number):
    return ["{}{}".format(x, y) for y in range(1, number+1)for x in list1]


print(new_list(["p", "q"], 5))
"""


# 36.Write a Python program to get variable unique identification number or string.
# less important
"""
x = 100
print(format(id(x), 'x'))
s = 'w3resource'
print(format(id(s), 'x')) 
"""

# 37.Write a Python program to find common items from two lists.

# common means i must contains in both lists
"""
def common_items(list1, list2):
    return [x for x in list1 if x in list2]


print(common_items(["Red", "Green", "Orange", "White"], ["Black", "Green", "White", "Pink"]))
"""

# 38.Write a Python program to change the position of every n-th value with the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]

# every value is replace by its next value(i.e n+1 th value)
# here we are using swaping principle

"""
def position_change(items):
    for i in range(0, len(items), 2):
        items[i], items[i+1] = items[i+1], items[i]
    return items


print(position_change([1, 2, 3, 4, 5, 6, 7]))
"""

# 39. Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50] ------> Expected Output: 113350

# method :1
"""

def conversion(item):
    new_number = ""
    for x in item:
        new_number += str(x)
    return int(new_number)


print(conversion([11, 33, 50]))


# method:2
# by using map function and join method
a= "".join(map(str, [11, 33]))
print(a)
"""

























