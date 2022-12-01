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
import random

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

# 40 Write a Python program to split a list based on first character of word.
#
# Sample Input:
#
# word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
#      'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

# ignored

# 41.Write a Python program to create multiple lists.

# by using dict comprehension

"""
def create_mul_lists(n1, n2):
    return {str(i): [] for i in range(n1, n2)}


print(create_mul_lists(1, 21))
"""

# 42. Write a Python program to find missing and additional values in two lists.
# list1 = ['a', 'b', 'c', 'd', 'e', 'f']
# list2 = ['d', 'e', 'f', 'g', 'h']
# missing values in second list = ['a', 'b', 'c']
# additional values in second list = ['g', 'h']

# method:1
"""
def missing_additional(list1, list2):
    missing_in_list2 = [i for i in list1 if i not in list2]
    additional_in_list2 = [i for i in list2 if i not in list1]
    return missing_in_list2, additional_in_list2


print(missing_additional(['a', 'b', 'c', 'd', 'e', 'f'], ['d', 'e', 'f', 'g', 'h']))

# method:2

a=["missing_in_list2:", [i for i in list1 if i not in list2], "additional_in_list2:", [i for i in list2 if i not in list1]]
print(a)
"""
# 43. ignored
# 44.Write a Python program to generate groups of five consecutive numbers in a list.
# i represents the number of sub_lists in a list
# j represents the consicutive numbers in the sublist

"""

def consecutive_numbers():
    return [[j+5*i for j in range(1, 6)]for i in range(9)]


print(consecutive_numbers())
"""

# 45.Write a Python program to convert a pair of values into a sorted unique array.

# sample_input = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
# output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
def pair_to_unique_array(items):
    new=[]
    for i in items:
        for j in i:
            if new.count(j)==0:   # or we can write j not in new
                new.append(j)
    return sorted(new)   # we are using sorted to arrange numbers in ascending order

print(pair_to_unique_array([(1, 2), (3, 4), (7, 2), (5, 11), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]))
"""

# 46. Write a Python program to select the odd items of a list.

"""
def only_odd(items):
    return [i for i in items if i % 2 != 0]


print(only_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]))
"""

# 47.Write a Python program to insert an element before each element of a list.
# sample_input = ['Red', 'Green', 'Black']
# output = ['c', 'Red', 'c', 'Green', 'c', 'Black']

"""
def adding_new(items):
    new=[]
    for i in items:
        new += 'c', i   # if you want to add next to each element new+= i, 'c'  
    return new


print(adding_new(['Red', 'Green', 'Black']))
"""
# 48.Write a Python program to print a nested lists (each list on a new line) using the print() function.
# input= [['Red'], ['Green'], ['Black']]
# output = ['red']
#          ['green']
#          ['black']
"""

def nested_list(item):
    for i in item:
        print(i)


nested_list([['Red'], ['Green'], ['Black']])

# model:2

print('\n'.join([str(lst) for lst in colors]))
a=[str(lst) for lst in colours]

colours =[['red'], ['green'], ['yellow']]
a=[str(lst) for lst in colours]  # we are converting nested lists into strings ,join function only supports str in list

print('\n'.join(a))  # here we are joining with each element with new line thats why its print line by line

"""

# 49. Write a Python program to convert list to list of dictionaries. Go to the editor
# input = ["Black", "Red", "Maroon", "Yellow"]
# input1 = ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'},
#                   {'color_name': 'Red', 'color_code': '#FF0000'},
#                   {'color_name': 'Maroon', 'color_code': '#800000'},
#                   {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
"""
 # method 1:
def create_dict(list1, list2):

    dict, list = {}, []
    for i in range(len(list1)):
        dict['colour_name'] = list1[i]  # adding key and values to the dictionary
        dict['colour_code'] = list2[i]
        list.append(dict) # appending the dictionary to the list
    return list


# print(create_dict(["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]))

# method:2
# by using zip function

def create_dict(list1, list2):
    return [{'colour_name': i, 'colour_code': j}for i, j in zip(list1, list2)]


print(create_dict(["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]))
"""
# 50. Write a Python program to sort a list of nested dictionaries.

# while doing dict codes you can understand it more

"""
def sort_nest_dict(items):
    items.sort(key=lambda val : val['key']['subkey'], reverse=False)
    return items


print(sort_nest_dict([{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]))
"""

# **51. Write a Python program to split a list every Nth element
#
# Sample_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

# model:1
"""
def split_list_every_nth(items, nth):
    return [items[i::nth] for i in range(nth)]  


print(split_list_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5))

# model:2


def split_list(item, nth):
    new_list=[]
    for i in range(nth):           
        new_list.append(Sample_list[i::nth])
    return new_list
"""

"""
# 52. Write a Python program to compute the difference between two lists. Go to the editor
# colour1=["red", "orange", "green", "blue", "white"]
# colour2=["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']

# here we are using list comprehension and not in operator
def difference(colour1, colour2):
    a = [words for words in colour1 if words not in colour2]
    b = [words for words in colour2 if words not in colour1]
    c = "Colour1-Colour2 :{} and Colour2-Colour1:{}".format(a, b)
    return c


print(difference(["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]))
"""
"""
# 53.Write a Python program to create a list with infinite elements.

# ignored


def infinite_list():
    lst = []
    c = 0
    while True:
       lst.append(c)
       c+=1
       print(lst)

print(infinite_list())
"""

# 54. Write a Python program to concatenate elements of a list.
# input:
# color = ['red', 'green', 'orange']
# output:
# red-green-orange
# redgreenorange

# print("-".join(color))         # join function takes an iterable and joins the strings in the iterable
# print("".join(color))


"""
# **55. Write a Python program to remove key values pairs from a list of dictionaries.

# Original List:
# [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]
# New List:
# [{'key2': 'value2'}, {'key2': 'value4'}]


def remove_key_value(items):
    new_list_dict = [{k : v for k, v in x.items() if k != 'key1'}for x in items]
    return new_list_dict


print(remove_key_value([{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]))
"""
"""
# 56. Write a Python program to convert a string to a list.

# input = "['red', 'green', 'yellow']"
# output= ['red', 'green', 'yellow']

# model:1 ---> here we are importing ast module
import ast


def string_list(item):

    return ast.literal_eval(input)

print(string_list("['red', 'green', 'yellow']"))

# model:2 we are using string replace method
# input.replace('"', "")
# print(input)

"""
"""
# 57.Write a Python program to check if all items of a given list of strings is equal to a given string.

# meaning: every element in the list is equals to the given string

# color1 = ["red", "red", "black", "white"]

# method1 : by using all function inside the list
print(all(word == 'green' for word in color1))
print(all(word == 'green' for word in color1))

# method:2 break and continue method

for i in color1:
    if i == 'red':
        continue
    else:
        print(False)
        break
"""
"""
# 58. Write a Python program to replace the last element in a list with another list.
# Sample data :
list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

# method:1 by using pop() function


def list_insertion(list1 , list2):
    list1.pop()
    list1.extend(list2)
    return list1


print(list_insertion([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))

# method:2 by using slicing method:

def list_insec(list1, list2):
    list1[-1:]=list2
    return list1

print(list_insec([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))
"""

# 59.Write a Python program to check whether the n-th element exists in a given list.

# i dont understand this question copied from w3 school
# x = [1, 2, 3, 4, 5, 6]
# xlen = len(x)-1
# print(x[xlen])

# 60.Write a Python program to find a tuple, the smallest second index value from a list of tuples.
# not understanding

# x = [(4, 1), (1, 2), (6, 5)]
# print(min(x, key=lambda n: (n[1], -n[0])))

"""
# 61.Write a Python program to create a list of empty dictionaries.

# inside a list we have to cresate a emepty dict


def create_emepty_dict_in_list(n):
    return [{} for i in range(n)]

print(create_emepty_dict_in_list(10))

"""

"""
# 62.Write a Python program to print a list of space-separated elements.

# it means every element in a list should be printed  in same line with space saperator(space should be there 
# between listelements) 

input = [1, 2, 3, 4, 5]
# output= 1 2 3 4 5

# method:1  by using * operator inside print statement

# print(*input)


method : 2

# by using end separator

def space_sep(item):
    for i in input:
        print(i, end=" ")
"""

"""
# 63.Write a Python program to insert a given string at the beginning of all items in a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

# bellow method returns the abnormal results i.e : ['hello1', 'hello12', 'hello123', 'hello1234']
def con_cat(list, string):
    new_list=[]
    for x in list:
        string+=str(x)
        new_list.append(string)
    return new_list


print(con_cat([1,2,3,4],"hello"))

# this is correct method we used the format string


def con_cat(list, string):
    return [string+"{}".format(i) for i in list]


print(con_cat([1, 2, 3, 4], "hello"))
"""
"""
# 64. Write a Python program to iterate over two lists simultaneously.

# with using zip function


def parlell(list1, list2):
    for i, j in zip(list1, list2):
        print(i, j)

parlell([1,2,3],[4,5,6])


# with using zip function

def parlel(list1, list2):
    for i in range(len(list1)):
        print(list1[i], list2[i])

parlel([1,2],[3,4])

"""
"""
# 65. Write a Python program to move all zero digits to end of a given list of numbers.
# Expected output:
# Original list:
#old_list = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# Move all zero digits to end of the said list of numbers:
# new_list = [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# by using swapping technique


def move_zeros(item):
    count=0
    for i in range(len(item)):
        if item[i] != 0:  # if item[i] == 0 this block won't be executed  
            item[i], item[count] = item[count], item[i]  # here we are doing swapping
            count += 1  # if it is not zero then only count will increase by 1
    return item


print(move_zeros([3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]))

"""
"""

# 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
# Sample lists: [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# Expected Output: [10, 11, 12]

# explanation: we have to add all elements in a list and pic maximum value --> how to pic maximum value ?
#                 based on index __ so initialize sum,max_sum, index and max_index

def max_sum_list(item):


    max_sum = 0
    index = 0
    index_max = 0
    for sub_list in item:
        sum_list = 0       # in which loop you are doing sum on above loop only wehave to initialize the varible
        for num in sub_list:
            sum_list += num
        if sum_list > max_sum:
            max_sum = sum_list
            index_max = index
        index+=1
    return item[index_max]


print(max_sum_list([[109, 2, 3], [40, 5, 6], [10, 11, 12]]))
"""
"""
# 67. Write a Python program to find all the values in a list are greater than a specified number.

# explanation: all values in alist are greather then the  specified number or not
# about all() function:
# The all() function returns True if all items in an iterable are true, otherwise it returns False.
# syntax: all(iterable)
# If the iterable object is empty, the all() function also returns True.


def find_greater(list, number):       # it returns true if all num is list is greather then the specified number
    return all(i >= number for i in list)


print(find_greater([1, 2, 3, 5], 2))
"""
"""
# 68. Write a Python program to extend a list without append. Go to the editor
# list1 = [10, 20, 30]
# list2 = [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]

# method:1 by using + operator
def adds(list1, list2):
    return list1+list2


print(adds([1, 2, 3], [4, 5, 6]))

# method:2 by using slicing

def add(item1, item2):
    item2[:0] = item1
    return item2
print(add([1, 2],[3, 4]))
"""
"""
# 69. Write a Python program to remove duplicates from a list of lists. Go to the editor
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]


def remove_duplicates(item):
    
    list=[]
    [list.append(i) for i in item if i not in list]
    return list


print(remove_duplicates([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]))
"""
"""
# 70. Write a Python program to find the items starts with specific character from a given list. Go to the editor
# Expected Output:
# Original list:
# ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# Items start with a from the said list:
# ['abcd', 'abc', 'acjd']
# Items start with d from the said list:
# ['dagfa']
# Items start with w from the said list:
# []

def starts_letter(item, letter):
    return [word for word in item if word[0] == letter]


print(starts_letter(['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd'], 'd'))
"""
"""
# 71. Write a Python program to check whether all dictionaries in a list are empty or not. Go to the editor
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False
   

def check(item):
    return all(dict=={} for dict in item)   # if i == {} true


print(check([{},{},{}]))
"""
"""
72. Write a Python program to flatten a given nested list structure.
# this code is suitable when all items in the list are only nested list
# this code is not worked if the items in the list are single elements i.e 1,2,'a','b' etc.


# def flatten(item):
#     return [x for sublist in item for x in sublist]


# print(flatten([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))


# if all items in list are mixings i.e nested+normal items

# we can compute by using recursion method

flatten=[]


def flatten_list(items):
    for item in items:
        if type(item) == list:     
            flatten_list(item)      # we have to be aware of diclaring varibles incase of recursive function
        else:
            flatten.append(item)
    return flatten


print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))
"""
"""
# ** 73. Write a Python program to remove consecutive duplicates of a given list. Go to the editor
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After removing consecutive duplicates:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

note= where ever the concept of consicutive arise the previous value concept comes
new_list=[]

def remove_con_duplicates(item):
    previous_value = None
    for i in item:
        if i!= previous_value:
            new_list.append(i)
            previous_value = i

    return new_list


print(remove_con_duplicates([0, 0, 1, 2, 3, 0, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))
"""
"""
# 74. Write a Python program to pack consecutive duplicates of a given list elements into sublists.
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After packing consecutive duplicates of the said list elements into sublists:
# [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
list=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
previous_value=None
new_list=[]
for i in list:
    if i != previous_value:
        new_list.append([i])
        previous_value=i


print(new_list)
"""

"""

# 80. Write a Python program to insert an element at a specified position into a given list.
# Original list:
a = [1, 1, 2, 3, 4, 4, 5, 1]
# After inserting an element at kth position in the said list:
# [1, 1, 12, 2, 3, 4, 4, 5, 1]


# By using slicing concept.

def inserting_an_element(ele, list_obj, pos):
    return list_obj[:pos]+[ele]+list_obj[pos:]


print(inserting_an_element(12, a, 2))


# By using insert method...

# insert method = list.insert(index_pos, element)   >>> withou removing any elemnt it will insert the list... it returns nothing it only modify the original list.

def insert_using_inbuilt(ele, list_obj, pos):
    list_obj.insert(ele, pos)
    return list_obj


print(insert_using_inbuilt(2, a, 12))
"""
"""
# 81. Write a Python program to extract a given number of randomly selected elements from a given list.
# Original list:
a = [1, 1, 2, 3, 4, 4, 5, 1]
# Selected 3 random numbers of the above list:
# [4, 4, 1]


# Exp: iccina list lo nunchi manam randoom ga n numbers tesukovali.

# New : random.sample(list_obj, num)


import random


def rand_select(list_obj, n):
    return random.sample(list_obj, n)


print(rand_select(a, 3))
"""
"""
# Model : combination of n distinct objects.

# Little trickey.

# 82. Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list.
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def combination(n, list_obj):
    if n <= 0:
        yield []
        return
    for i in range(len(list_obj)):
        first_num = list_obj[i:i+1]
        for last_num in combination(n-1, list_obj[i+1:]):
            yield first_num+last_num


result = combination(2, a)


for i in result:
    print(i)
"""
"""
# 83. Write a Python program to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
# Original list:
a = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# Result:
# 243

# Exp: oka list lo vunna elements anni round off cheyyali ....round off chesina number ni list yokka length tho multiply cheyyali... multiply chesina danni 
# sum cheyyali.


def sum_new_list(list_obj):
    new_list = []
    sum_of_new = 0
    for num in list_obj:
        new_list.append(round(num)*len(list_obj))
    for new_num in new_list:
        sum_of_new += new_num
    return sum_of_new


print(sum_new_list(a))

print(sum([round(x)*len(a) for x in a]))
"""

"""
# 84. Write a Python program to round the numbers of a given list, print the minimum and maximum numbers and multiply the numbers by 5.
# Print the unique numbers in ascending order separated by space.
# Original list:
a = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# Minimum value: 4
# Maximum value: 22
# Result:
# 20 25 45 55 60 70 80 90 110


# Exp: prathi number ni round off cheyyali.... max, min numbers ni print cheyyali... round off chesina every number ni 5 tho multiply chesi oka line lo print cheyyali.


def max_min(list_obj):
    new_list = [round(i) for i in list_obj]
    max_value = new_list[0]
    min_value = new_list[0]

    for num in new_list:
        if num > max_value:
            max_value = num
        elif num < min_value:
            min_value = num
    new_list_1 = sorted([x*5 for x in new_list])
    print('Result_list :')
    for x in new_list_1:
        print(x, end=" ")

    return '\nThe maximum value = {}\nThe minumum value ={}'.format(max_value, min_value)


print(max_min(a))
"""
# W3 resource method:
"""
nums = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print("Original list:", nums)
numbers=list(map(round,nums))
print("Minimum value: ",min(numbers))
print("Maximum value: ",max(numbers))
numbers=list(set(numbers))
numbers=(sorted(map(lambda n:n*5,numbers)))
print("Result:")
for numb in numbers:
    print(numb,end=' ')

"""
"""
# Model : creating multi_dimention list.

# 85. Write a Python program to create a multidimensional list (lists of lists) with zeros.
# Multidimensional list: [[0, 0], [0, 0], [0, 0]]

# Exp: mundu rows next columns ni initialize cheyyali...okkoka nested list okkoka row....nested list lo vunna items columns loni items ni suchistundi.

# 3X2 matrix ante 3 rows(3 nested lists) 2 columns ( nested list lo 2 items ani ardham) 


def creating_multi_dimentional_list(rows, columns):
    new_list = []
    for i in range(rows):
        new_list.append([])
        for j in range(columns):
            new_list[i].append(0)

    return new_list


print(creating_multi_dimentional_list(3, 2))


# Model :2 by using list comprehension.

def multi_dim_com(rows, columns):
    return [[0 for j in range(columns)]for i in range(rows)]


print(multi_dim_com(int(input("Enter the number of rows :")), int(input("Enter the number of columns : "))))
"""

"""
# Model : matrix model

# 86. Write a Python program to create a 3X3 grid with numbers.
# 3X3 grid with numbers:
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


def create_matrix(rows, columns):
    new =[]
    for i in range(rows):
        new.append([])
        for j in range(1, columns+1):
            new[i].append(j)
    return new


# print(create_matrix(3, 3))


def mat_using_list_comp(rows, columns):
    return [[j for j in range(1, columns+1)]for i in range(rows)]


print(mat_using_list_comp(int(input("Enter the number of rows : ")), int(input("Enter the number of columns: "))))
"""
"""
# Model :  Matrix model rows from console, column from console, add every row and add every column ....


# 87.Write a Python program to read a matrix from console and print the sum for each column.
# Accept matrix rows, columns and elements for each column separated with a space(for every row) as input from the user.
#


# Note : sum of each rows/columns ni chesetappudu manam sum varible loops madhya lo pettali ledante manaki cumulative sum vastundi...

# iko row/column malli daiki add avutundi ....so manam sum varible loops madhayalo ivvali.... 

def create_matrix(rows, columns):
    matrix = [[int(input("Enter the column element: ")) for j in range(columns)]for i in range(rows)]
    for row in matrix:
        print(' '.join(map(str, row)))        # this line is very very very important ..... to print matrix with out any square braces.

    for i in range(rows):
        sum_rows = 0
        for j in range(columns):
            sum_rows += matrix[i][j]
        print('sum of' + str(i+1), ':' + str(sum_rows))
    for i in range(rows):
        sum_columns = 0
        for j in range(columns):
            sum_columns += matrix[j][i]
        print('sum of' + str(i+1), ":" + str(sum_columns))


# create_matrix(int(input("Enter the number of rows :")), int(input("Enter the number of columns :")))


def mat(rows, columns):
    matrix = [[int(input("Enter the elements for each column : "))for j in range(columns)]for i in range(rows)]
    for row in matrix:
        print(' '.join(map(str, row)))

    for i in range(rows):
        sum_rows = 0
        for j in range(columns):
            sum_rows += matrix[i][j]
        print('The sum of ', str(i+1), 'row is :', sum_rows)

    for i in range(rows):
        sum_columns = 0
        for j in range(columns):
            sum_columns += matrix[j][i]
        print('The sum of ', str(i+1), sum_columns)


print(mat(int(input("Enter the number of rows :")), int(input("Enter the number of columns :"))))




# 88. Write a Python program to read a square matrix from console and print the sum of matrix primary diagonal.
# Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user.
# Input the size of the matrix: 3
# 2 3 4
# 4 5 6
# 3 4 7
# Sum of matrix primary diagonal:
# 14


# Exp : square matrix : If a matrix order is n x n, then it is a square matrix. ex: 3X3, 4X4, 5X5, 6X6 etc.

# Note : primary diagonals ni add chese tappudu sum varible rendu loops bayata vundali.

def square_matrix(rows, columns):
    matrix = [[int(input("Enter the elements :")) for j in range(columns)] for i in range(rows)]
    for row in matrix:
        print(' '.join(map(str, row)))
    primary_diagonal = 0  # sun varible rendu loops bayata vundali.
    for i in range(len(matrix)):

        for j in range(len(matrix[i])):
            if i == j:
                primary_diagonal = primary_diagonal + matrix[i][j]

    return primary_diagonal


print(square_matrix(int(input("Enter the number of rows :")), int(input("Enter the number of columns :"))))

"""
"""
# 89. Write a Python program to Zip two given lists of lists.
# Original lists:
a=[[1, 3], [5, 7], [9, 11]]
b=[[2, 4], [6, 8], [10, 12, 14]]
# Zipped list:
# [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]
# Click me to see the sample solution


# Exp: map function use chesi manam parell iteration cheyyadaniki vadathamu but ikkada anni lists same length lo vundali ....

# Model :1

def zipped(list1, list2):
    return list(map(list.__add__, list1, list2))


print(zipped(a, b))

# Model:2


def zipp(list1, list2):
    for i in range(len(list1)):
        list1[i].extend(list2[i])
    return list1


print(zipp(a, b))
"""

"""
# 90. Write a Python program to count number of lists in a given list of lists.
# Original list:
a = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# Number of lists in said list of lists:
# 4
# Original list:
b = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
# Number of lists in said list of lists:
# 3

# Without inbuld

def count_num_of_lists(list_obj):
    count =0
    for x in list_obj:
        count+=1
    return count


print(count_num_of_lists(b))

# with len() func

def count_num(list_obj):
    return len(list_obj)


print(count_num_of_lists(b))

"""
"""
"""
# Model : max, min length kaligina lists kanukkovali.

# 91. Write a Python program to find the list with maximum and minimum length.
# Original list:
# a = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])
# Original list:
# b= [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
# List with maximum length of lists:
# (3, [3, 5, 7])
# List with minimum length of lists:
# (1, [0])
# Original list:
# c=[[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
# List with maximum length of lists:
# (4, [1, 34, 5, 7])
# List with minimum length of lists:
# (1, [12])

# Model : 1  

# Exp: list lo vunns edo oka object ni max or min ga tesukoni dani adharamga compare cheyyadam
#
# def max_min(list_obj):
#
#     maxa = list_obj[0]
#     mina = list_obj[0]
#     for x in list_obj:
#         if len(x) > len(maxa):
#             maxa = x
#         elif len(x) < len(mina):
#             mina = x
#
#     return [(maxa, len(maxa)), (mina, len(mina))]
#
# print(max_min(b))
#

# Model: 2

# NEW : max(object, key =len) max function lo key pass cheyyadam.
#
# def max_list(list_obj):
#     max_len = max(len(x)for x in list_obj)
#     max_list = max(list_obj, key=len)
#
#     return max_len, max_list
#
# print(max_list(b))
#
#
# def min_list(list_obj):
#     min_length = min(len(x) for x in list_obj)
#     min_list = min(list_obj, key=len)
#
#     return min_length, min_list
#
# print(min_list(b))
"""
"""
# 92. Write a Python program to check if a nested list is a subset of another nested list.
# Original list:
# a = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# b =[[1, 3], [13, 15, 17]]
# If the one of the said list is a subset of another.:
# True
# Original list:
# c = [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
# d = [[[3, 4], [5, 6]]]
# If the one of the said list is a subset of another.:
# True
# Original list:
# e = [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
# f = [[[3, 4], [5, 6]]]
# If the one of the said list is a subset of another.:
# False


# what is subset? : subset ante oka object(object a) lo vunde prathi element inko object(object b) lo kachithamga vundali. prathi element vundali.

# Appudu object(a) anedi subset avutundi object(b) anedi super set avutundi.

# Model: 1
#
# def check(list1, list2):
#
#     exist = True
#     for x in list2:
#         if x not in list1:
#             exist = False
#     return exist
#
#
# print(check(c, d))
#
#
# def checking(list1, list2):
#     return all(x in list1 for x in list2)    # Note: all function lo condition jagrathaga rayali
#

# print(checking(a, b))

"""
"""
"""
# Model: Counting number of sublists contains a particular element.


# 93. Write a Python program to count the number of sublists contain a particular element.
# Original list:
a=[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# Count 1 in the said list:
# 3
# Count 7 in the said list:
# 2
# Original list:
b=[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
# Count 'A' in the said list:
# 3
# Count 'E' in the said list:
# 1

# Exp : manam ichina element enni sublists lo vundo count cheyyali.


def count_particular_element(list_obj, element):
    count = 0
    for sub_list in list_obj:
        if element in sub_list:   # element sublists lo vunte.
            count += 1
    return count


print(count_particular_element(b, "E"))

"""
"""
"""
# Model : Counting unique sublist's in a lists

# 94. Write a Python program to count number of unique sublists within a given list.
# Original list:
# a = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
# Number of unique lists of the said list:
# {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
# Original list:
# [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
# Number of unique lists of the said list:
# {('green', 'orange'): 2, ('black',): 1, ('white',): 1}


# Exp: count unique sublists ante frquency kanukkovli (bu using dict concept)

# Note : ikkada vundedi nested list's so dictionary keys ga nested pettalemu .... because dict keys are immutable and hashable ... tuple can be a dict keys...


# Concept : list's cannot be act as a dict keys.
#
#
# def count_unique(list_obj):
#     result = {}    # initializing dictionary
#     for i in a:
#         if tuple(i) not in result:  # manam ikkada tuple loki marchali ledante dict keys ga nested lists aaccept cheyyadu.
#             result[tuple(i)] = 1    # manam ikkada tuple loki marchali ledante dict keys ga nested lists aaccept cheyyadu.
#         else:
#             result[tuple(i)] += 1  # manam ikkada tuple loki marchali ledante dict keys ga nested lists aaccept cheyyadu.
#     return result
#
#
# print(count_unique(a))

"""
"""
"""
# 95. Write a Python program to sort each sublist of strings in a given list of lists.
# Original list:
a = [["green", "orange"], ["black", 'apple'], ["white", "black", "orange"]]
# Sort the list of lists by length and value:
# [['green', 'orange'], ['apple', 'black'], ['black', 'orange', 'white']]


# Exp: sorted or sort function lo nested list ni enter chesinappudu adi list lopala nested list's yokka position ni matrame  marustundi...

# okavela nested lists lo elements order kuda sort avvalante manam list comprehension lo loop rundhesi okkoka list ni sorted function loki pampali.



def sort_sublists(list_obj):
    return [sorted(x, reverse=False) for x in a]


print(sort_sublists(a))
"""
"""
"""
# Model : sort list by length and value

# 96. Write a Python program to sort a given list of lists by length and value.
# Original list:
# a = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]


# Exp: rendu saarlu sort cheyyali ::: okati normal sorting (value) redodhi length adharamga sort
#
#
# def sort_lists_len_and_value(list_obj):
#     list_obj.sort()                         # sort function nested list's ichinappudu prathi lists lo first elemant adharamga nested lists order ni sort chestundi
#     # print(list_obj)     # for understanding purpose.
#     list_obj.sort(key=len)  # based on length it is sorted.
#     return list_obj
#
#
# print(sort_lists_len_and_value(a))

"""
"""
"""
# Model : remove list's if element's of list's does not contain the specified range.

# 97. Write a Python program to remove sublists from a given list of lists, which contains an element outside a given range.
# Original list:
a=[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
# After removing sublists from a given list of lists, which contains an element outside the given range:
# [[13, 14, 15, 17]]


# Exp: oka nested list lo chala lists vunatai ....aa list's lo elemants manam icchina left range, right range madhyalo vundaa ani chudali.


def remove_lists(list_obj, left_range, right_range):
    return [x for x in a if(min(x) >= left_range and max(x) <= right_range)]


print(remove_lists(a, int(input("Enter the left range :")), int(input("Enter the right range : "))))
"""
"""
"""
# Method : list lo vunna prathi word scramble cheyyali..

# scramble =  to put things such as words or letters in the wrong order so that they do not make sense

# 98. Write a Python program to scramble the letters of string in a given list.
# Original list:
a = ['Python', 'list', 'exercises', 'practice', 'solution']
# After scrambling the letters of the strings of the said list:
# ['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']


# shuffle()

# The shuffle() method takes only list and reorganize the order of the items.

# Note: This method changes the original list, it does not return a new list.

# shuffle function only list ni matrame tesukuntundi list lo vunna shuffle objects ni shuffle chestundi... ee method denni return cheyyadu

# original list lo vunn elements ni matrame marustundi.

#
#
# from random import shuffle, sample
#
#
# def shuff_items(list_obj):
#     list_obj = list(list_obj)  # ['p', 'y', 't', 'h', 'o', 'n']  >>>> string ni list loki maariste ee vidham ga vastundi.
#     shuffle(list_obj)     # ['h', 't', 'n', 'o', 'y', 'p']  >>> original list lo vunna elemants ee vidhamga
#     return ''.join(list_obj)  # 'htnoyp' >>>>> ee vidham ga list lo vunnavanni join avutundi.
#

# Note : join lo shuffle rayakudadu >>> shuffle function returns nothing.

# print([shuff_items(x)for x in a])   # print() function lo manam list comprehension raasi andulo manam shuffle functio ni call cchestam.

# Method : By using sample function.

# The sample() method returns a list with a randomly selection of a specified number of items from a sequnce.

#  sample(sequence, k)    >>>> k is nothing but size of returned list.

# print([''.join(sample(x, len(x))) for x in a])

"""


"""
# 99. Write a Python program to find the maximum and minimum values in a given heterogeneous list.
# Original list:
a = ['Python', 3, 2, 4, 5, 'version']
# Maximum and Minimum values in the said list:
# (5, 2)


# Exp: manam list lo edo oka value ni max ga and edo oka value ni min ga tesukovali....

# list ni iteration lo run chesi prathi element type() check chesi adi number type iethe (type(element) != str) danni condition check cheyyali

# same thing with minimum tho.

# def max_min_in_hetro(list_obj):
#     maximum = 3
#     minimum = 2
#     for x in a:
#         if type(x) != str and x > maximum:
#             maximum = x
#         elif type(x) != str and x < minimum:
#             minimum = x
#
#     return 'The maximum value is = {} The minimum value is = {}'.format(maximum, minimum)
#
#
# print(max_min_in_hetro(a))


# Model 2 with max() and min() func:
#
# def max_min(list_obj):
#     return 'The maximum value = {} The minimum value is = {}'.format(max([x for x in list_obj if type(x) != str]), min([x for x in list_obj if type(x) != str]))


# print(max_min(a))

# W3 method: isinstance


# *** isinstance = it is used to check if specific element if of specific type...
#
# def max_min_val(list_val):
#     max_val = max(i for i in list_val if isinstance(i, int))    # int iethene i loki vastundi
#     min_val = min(i for i in list_val if isinstance(i, int))
#     return max_val, min_val
#

"""
"""
"""
# Model : Finding common index elements

# 100. Write a Python program to extract common index elements from more than one given list.
# Original lists:
a = [1, 1, 3, 4, 5, 6, 7]
b = [0, 1, 2, 3, 4, 5, 7]
c = [0, 1, 2, 3, 4, 5, 7]
# Common index elements of the said lists:
# [1, 7]


# Exp:  common index values annadu kabatti manam index ni compare cheyyali ..... index ni access cheyyali ante range len function vadali.

# i dwara manam prathi llist lo vunde element ni compare cheyyali.

# Method : 1 ... by using list comprehension.

def common_values_by_index(list1, list2, list3):
    new = [a[i] for i in range(len(a)) if a[i] == b[i] == c[i]]  # accessing through index...ikkada manam a[i] anna or b[i] anna or c[i] anna pettochu
    return new


print(common_values_by_index(a, b, c))


# Method : 2  normal method

def common_index_values(list1, list2, list3):
    result = []
    for i in range(len(a)):
        if a[i] == b[i] == c[i]:
            result.append(a[i])       # ikkada manam a[i] anna or b[i] anna or c[i] anna pettochu
    return result


print(common_index_values(a, b, c))


# by using zip function.

def common_by_zip(list1, list2, list3):
    new_list = []
    for x, y, z in zip(list1, list2, list3):
        if x == y == z:
            new_list.append(x)    # ikkada manam x anna or y anna or z anna pettochu
    return new_list


print(common_by_zip(a, b, c))
"""
"""

# Model : nested list's sorting.


# 101. Write a Python program to sort a given matrix in ascending order according to the sum of its rows.
# Original Matrix:
a = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
#  [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
# Original Matrix:
b = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]


# Sort the said matrix in ascending order according to the sum of its rows
# [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]


def sorted_mat(list_obj):
    return sorted(list_obj, key = lambda x:sum(x))

print(sorted_mat(a))

def sorted_matrix(list_obj):
    return sorted(list_obj, key=sum)

"""
"""
# 102. Write a Python program to extract specified size of strings from a give list of string values.
# Original list:
a = ['Python', 'list', 'exercises', 'practice', 'solution']
# length of the string to extract:
# 8
# After extracting strings of specified length from the said list:
# ['practice', 'solution']


def extract_specified_size(list_obj, size):
    return [x for x in list_obj if len(x) == size]


print(extract_specified_size(a, 8))
"""
"""
# 103. Write a Python program to extract specified number of elements from a given list, which follows each other continuously.
# Original list:
a = [1, 1, 3, 4, 4, 5, 6, 7]
# Extract 2 number of elements from the said list which follows each other continuously:
# [1, 4]
# Original lists:
b = [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
# Extract 4 number of elements from the said list which follows each other continuously:
# [4]

from itertools import groupby

def extract_num(list_obj, num):
    return [i for i, j in groupby(list_obj) if len(list(j)) == 2]


print(extract_num(a, 2))


# Q) what is meany by groupby function ?

# it groups the consicutive elements .... itertools.groupby(iterable_obj, key) 
# the output of the function consists of keys and groups from the iterable.

# it returns keys and its itrator object in tuples (these tuples contains all the consicutive items) 
a = "aaabbbccccd"
x = itertools.groupby(a)
for k,g in x:
    print(k, g)

keys            iterator_objects
a <itertools._grouper object at 0x000001E59C28DBE0>
b <itertools._grouper object at 0x000001E59C28D9E8>
c <itertools._grouper object at 0x000001E59C28DC18>
d <itertools._grouper object at 0x000001E59C28DBE0>


import itertools
a = "aaabbbccccd"
x = itertools.groupby(a)
for k,g in x:
    print(k, list(g))
    
a ['a', 'a', 'a']
b ['b', 'b', 'b']
c ['c', 'c', 'c', 'c']
d ['d']    
"""

"""

# Model : consicutive numbers differences.

# 104. Write a Python program to find the difference between consecutive numbers in a given list.
# Original list:
# a = [1, 1, 3, 4, 4, 5, 6, 7]
# Difference between consecutive numbers of the said list:
# [0, 2, 1, 0, 1, 1, 1]
# Original list:
# b = [4, 5, 8, 9, 6, 10]
# Difference between consecutive numbers of the said list:
# [1, 3, 1, -3, 4]

# Exp: pakka pakka vunna elements differsnts kavali....

# NOTE: VIMP :::: ikkada manam range(length) dwara elements ni access chestamu...ikkada length okati thagginchakapothe last element ki index out of range
#  vastundi.... last elemant ki +1 ledu kada ....so manam length okati thagginchali.....appudu last elemant ni vadilestundi i+1 petti manam access cheyyochu.


def diff_consecutive(list_obj):
    return [list_obj[i+1]-list_obj[i] for i in range(len(list_obj)-1)]


print(diff_consecutive(b))

"""
"""
# Model : average of two lists.

# 105. Write a Python program to compute average of two given lists.
# Original list:
# a = [1, 1, 3, 4, 4, 5, 6, 7]
# b = [0, 1, 2, 3, 4, 4, 5, 7, 8]
# Average of two lists:
# 3.823529411764706


def average_part(list1, list2):          # a+b ante rendu lists kalipi okalist avutundi...
    return sum(a+b)/len(a+b)


print(average_part(a, b))

"""

"""
# 106. Write a Python program to count integer in a given mixed list.
# Original list:
a = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# Number of integers in the said mixed list:
# 6


# Exp : integer ante positive number (positive integer) iena vundavochu leda(negative integer) iena vundavocchu kaaani float matram vundakudadu.


def count_int(list_obj):
    count = 0
    for x in list_obj:
        if type(x) == int:
            count+=1
    return count


# print(count_int(a))

# Model : 2 isinstance method.

def is_in(list_obj):
    count = 0
    for x in list_obj:
        if isinstance(x, int):
            count += 1
    return count


print(is_in(a))
"""
"""
# Model : removing specific column for matrix.

# VIMP

# 107. Write a Python program to remove a specified column from a given nested list.
# Original Nested list:
a = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# After removing 1st column:
# [[2, 3], [4, 5], [1, 1]]
# Original Nested list:
b = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# After removing 3rd column:
# [[1, 2], [-2, 4], [1, -1]]


def remove_specific_column(list_obj, column):
    for x in list_obj:
        del x[column]
    return list_obj


print(remove_specific_column(a, int(input("Enter the specific column :"))))

"""
"""
# Model : extracting specified column from matrix

# 108. Write a Python program to extract a specified column from a given nested list.
# Original Nested list:
a = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Extract 1st column:
# [1, 2, 1]
# Original Nested list:
b = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Extract 3rd column:
# [3, -5, 1]
# Click me to see the sample solution

# Exp: ikkada manam coloumn ni index dwara access chestam.

def extracting(list_obj, specified_column):
    return [x[specified_column] for x in list_obj]  # every nested list x loki veltundi daanni index dwara access chestam.


print(extracting(a, int(input("Enter the specific column: "))))

"""
"""
# 109. Write a Python program to rotate a given list by specified number of items to the right or left direction.
# original List:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Rotate the said list in left direction by 4:
# [4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
# Rotate the said list in left direction by 2:
#  [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
# Rotate the said list in Right direction by 4:
# [8, 9, 10, 1, 2, 3, 4, 5, 6]
# Rotate the said list in Right direction by 2:
# [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]

# Left direction ante positive and right direction ante negative.

# left direction by 4 :

print(a[4:]+a[:4])

print(a[2:]+a[:2])
print(a[-4:]+a[:-4])

print(a[-2:]+a[:-2])

"""
"""
# Model : highest repeated element.

# 110. Write a Python program to find the item with maximum occurrences in a given list.
# Original list:
a = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 9, 9, 9, 9, 1, 2]


# Item with maximum occurrences of the said list:
# 2

def max_occur_element(list_obj):
    d = {}
    for x in list_obj:
        if str(x) not in d.keys():
            d[str(x)] = 1
        else:
            d[str(x)] += 1

    return sorted(d.items(), key=lambda x: x[1], reverse=False)[-1][0]  # dict loni items() ni vaule base meeda manam sorted chesamu output list lo vuntundi.
    # last tuple maximum occurance key and value so...-1 ante max occur key value pair daantlo 0 ante key and 1 ante value ani ardham


# print(max_occur_element(a))

# By using count funtion:

# Exp: ikkada manaki rendu kavali ....okati maximum occurance item daani value... maximum occurance item ni result ga tesukoni and daani occurance ni---
# max_occur ga tesukuntamu.


def max_occurance(list_obj):
    result = list_obj[0]
    max_occur_value = 0
    for x in list_obj:
        max_occur_value_of_x = list_obj.count(x)
        if max_occur_value_of_x > max_occur_value:
            result = x
            max_occur_value = max_occur_value_of_x
    return 'The maximum occurance items : {}\n The number of times occured :{}'.format(result, max_occur_value)


print(max_occurance(a))

"""
"""
# Model : accessing multiple elements of specified index.


# 111. Write a Python program to access multiple elements of specified index from a given list.
# Original list:
a = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# Index list:
b = [0, 3, 5, 7, 10]
# Items with specified index of the said list:
# [2, 4, 9, 2, 1]


# Exp: index list istadu aa list lo vunna index adharamga original list lo vunna items ni access cheyyali.

def access_items(list_obj, index_obj):
    result = [list_obj[i] for i in index_obj]
    return result

print(access_items(a, b))

"""
"""
#***Model : checking list is in sored order or not.

# Vimp.

# 112. Write a Python program to check whether a specified list is sorted or not.
# Original list:
a = [1, -2, 4, 6, 8, 10, 12, 14, 16, 17]
# Is the said list is sorted!
# True
# Original list:
b = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5]
# Is the said list is sorted!
# False


# Exp: oka previous value ni initialize chesukovali...tharuvatha logic ravai...

def check_sorted(list_obj):
    previous_element = list_obj[0]
    for x in list_obj[1:]:
        if x > previous_element:
            previous_element = x
            result = True
        else:
            result = False
            break
    return result


print(check_sorted(a))
"""
"""
# Model : removing duplicate dictionary in the list.

# 113. Write a Python program to remove duplicate dictionary from a given list.
# Original list with duplicate dictionary:
a = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
# After removing duplicate dictionary of the said list:
# [{'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]

def removing_dup_dict(list_obj):
    new_list = []
    for x in list_obj:
        if x not in new_list:
            new_list.append(x)

    return new_list


print(removing_dup_dict(a))
"""

"""
# Model : extracting elements in the list of tuples...

# 114. Write a Python program to extract the nth element from a given list of tuples.
# Original list:
a = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# Extract nth element ( n = 0 ) from the said list of tuples:
# ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
# Extract nth element ( n = 2 ) from the said list of tuples:
# [99, 96, 94, 98]


# simple list comprehension:


def extracting_list(list_obj, n):
    return [x[n] for x in list_obj]


print(extracting_list(a, int(input("Enter the list_obj : "))))

def extracting(list_obj, n):
    return list(map(lambda x: x[n], list_obj))


# print(extracting(a, int(input("Enter the element : "))))

"""
"""
# Model : checking elements are unique or not

# 115. Write a Python program to check if the elements of a given list are unique or not.
# Original list:
a = [1,2,3,4]
# Is the said list contains all unique elements!
# False
# Original list:
# [2, 4, 6, 8, 10, 12, 14]
# Is the said list contains all unique elements!
# True

# Exp : elements repeated ga vundakudadu.


# Exp: new_list okati tesukoni daantlo not in operator vaadi append chestamu...tharuvatha condition check chestamu....

# Model: 1

def check_unique(list_obj):
    new_list = []
    for x in list_obj:
        if x not in new_list:
            new_list.append(x)   # ikkada append chestene ee element vunda leda ani new list lo chudagalam.
            result = True
        else:
            result = False
            break
    return result


# print(check_unique(a))

"""

"""
# Model : sort list of tuples based on given index.


# 116. Write a Python program to sort a list of lists by a given index of the inner list.
# Original list:
a = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# Sort the said list of lists by a given index ( Index = 0 ) of the inner list
# [('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]
# Sort the said list of lists by a given index ( Index = 2 ) of the inner list
# [('Wyatt Knott', 91, 94), ('Brady Kent', 97, 96), ('Beau Turnbull', 94, 98), ('Greyson Fulton', 98, 99)]
# Click me to see the sample solution

# Exp : ikkada manam tuple objects ni sort cheyyali.... kaani tuple object lo vunna elements ni kaadu.... so manam direct ga sort and sorted function rayavochu.

# sort : it is list method it does not retens nothing.....sorted : it is applicable on any iterable... it returns the modified iterable.


# By using sort function:


def sort_list_of_lists(list_obj, n):
    list_obj.sort(key=lambda x: x[n], reverse=False)  # sort function retrns nothing it modifes the original lists only.
    return list_obj


print(sort_list_of_lists(a, int(input("Enter the index number :"))))


# By using sorted function:


def sorted_list_tuples(list_obj, n):
    return sorted(list_obj, key=lambda x: x[n], reverse=False)


print(sorted_list_tuples(a, int(input('Enter the index_number :'))))

"""

"""

# Model : removing elements. which are present in the another list.


# 117. Write a Python program to remove all elements from a given list present in another list.
# Original lists:
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
# Remove all elements from 'list1' present in 'list2:
# [1, 3, 5, 7, 9, 10]


def remove_elements(list_obj1, list_obj2):
    return [x for x in list_obj1 if x not in list_obj2]


# print(remove_elements(list1, list2))


def remove_ele(list_obj1, list_obj2):
    for x in list_obj2:
        if x in list_obj1:
            list_obj1.remove(x)

    return list_obj1


print(remove_ele(list1, list2))
"""
"""

# Model : differnece between nth element and n+1th element.


# 118. Write a Python program to find the difference between elements (n+1th - nth) of a given list of numeric values.
# Original list:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Dfference between elements (n+1th - nth) of the said list :
# [1, 1, 1, 1, 1, 1, 1, 1, 1]
# Original list:
b = [2, 4, 6, 8]
# Dfference between elements (n+1th - nth) of the said list :
# [2, 2, 2]


# Exp: manam range length adharamga access chesi difference kanukkuntamu... length tesukune tappudu -1 cheyyali ledante index out of range vastudi

# range(len(list)-1)

def difference(list_obj):
    return [list_obj[i+1]-list_obj[i] for i in range(len(list_obj)-1)]


print(difference(b))

"""
"""
# Model : substrings present in the given list of strings.

# 119. Write a Python program to check if a substring presents in a given list of string values.
# Original list:
a = ['red', 'black', 'white', 'green', 'orange']
# Substring to search:
# ack
# Check if a substring presents in the said list of string values:
# True
# Substring to search:
# abc
# Check if a substring presents in the said list of string values:
# False

# Exp : ichina substring....list lo vunna words lo vunte true ledante false...so true vaste akkaditho break cheseddam ledante daani tharuvatha vunna elements ni kuda
# check chestundi.


def check(list_obj, substring):
    for word in list_obj:
        if substring in word:  
            result = True
            break            # break ivvakapothe loop end varaku veltundi.
        else:
            result = False
    return result


print(check(a, input("Enter the value : ")))

"""
"""
# Model : creating list with alternative elements....

# 120. Write a Python program to create a list taking alternate elements from a given list.
# Original list:
a = ['red', 'black', 'white', 'green', 'orange']
# List with alternate elements from the said list:
# ['red', 'white', 'orange']
# Original list:
b = [2, 0, 3, 4, 0, 2, 8, 3, 4, 2]
# List with alternate elements from the said list:
# [2, 3, 0, 8, 4]

# Exp:  1. by using range and step  2. by using index value. 

# okkoka element vadili list create cheyyali.... range function lo start, stop, step ki madhya lo comma(,) ivvali .... slicing laga colons(:) ivvakudadu.

def create_alternative(list_obj):
    return 'New_list = {}'.format([list_obj[i] for i in range(0, len(list_obj), 2)])


print(create_alternative(b))


# W3 model:


def alternate_elements(list_data):
    result=[]
    for item in list_data[::2]:  # start from beginig end to end of the list and step is 2  
        result.append(item)
    return result 


"""
"""
# Model : finding nestedlist elements which are present in another given list

# 121. Write a Python program to find the nested lists elements which are present in another list.
# Original lists:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
b = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# Intersection of said nested lists:
# [[12], [7, 11], [1, 5, 8]]

# Exp: oka nested lists lo vunna elements ichina vere list lo vunte danni vunchukovali.  List_comp.


def checking_lists(list_obj1, list_obj2):
    return 'The new lists : {}'.format([[ele for ele in n_l if ele in list_obj1]for n_l in list_obj2])


print(checking_lists(a, b))

"""
"""

Model : Extract  common elements in all the nested lists.....

# 122. Write a Python program to find common element(s) in a given nested lists.
# Original lists:
a = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
# Common element(s) in nested lists:
# [18, 12]

# Exp : anni nested lists lo vunna common elements ni bayataki teyyali.
1. first point  nested list lo duplicates remove cheyyali daiki set vadathamu(loop raasi prathi list ni set ga marustamu)...ee set ni reduce function lo pampinchi
# common ga vundevi intersection method '&' use chesi common elements bayataki testamu.


# reduce(lambda x,y :x&y, set)  >>> this is formula

from functools import reduce


def common_elements(list_obj):
    return tuple(reduce(lambda i, j : i & j, (set(x) for x in list_obj)))


print(common_elements(a))

"""
"""
# Model : reverse the every word in the list.


# 123. Write a Python program to reverse strings in a given list of string values.
# Original lists:
a =['Red', 'Green', 'Blue', 'White', 'Black']
# Reverse strings of the said given list:
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']


def str_reverse(str_obj):
    new_str = ''
    for x in str_obj:
        new_str = x+new_str
    return new_str

# print("The reverse of each word in the string is :", [str_reverse(x) for x in a])  # if you have object
print('The reverse of each word in the string is :', [str_reverse(x) for x in eval(input("Enter the list_obj :"))])  # input from the console...
"""
"""
# Model : maximum product and minimum product of the list of tuples.

# Exp: mundu manam list comprehension vaadi prathi tuple lo vunde elements ni product chesukuntam tharuvatha max ela kanukkovalo logic rastamu

# list comprehension lo x,y ani kotha model tesukunnamu...

# max_pro and min_pro ni initialize chesukuntam....



def max_min_product(list_obj):
    list1 = [x*y for x, y in list_obj]   # This is new for me... oka object lo rendu elemnts vunte adi x, y ki assign avutundi...okavela 3 vunte x,y,z
    max_pro = list1[0]
    min_pro = list1[0]
    for x in list1[1:]:
        if x > max_pro:   # x kanna ekkuva iethe max_pro = x ani tesukuntam 
            max_pro = x
        elif x < min_pro:
            min_pro = x
    return max_pro, min_pro


print(max_min_product([(2, 7), (2, 6), (1, 8), (4, 9)]))

"""
"""

# Model : product of unique numbers in a list.

# 125. Write a Python program to calculate the product of the unique numbers of a given list.
# Original List :
a = [10, 20, 30, 40, 20, 50, 60, 40]
# Product of the unique numbers of the said list: 720000000
# Click me to see the sample solution

# Exp : unique numbers ante duplicates ni remove cheyyali...remove chesina duplicates ni mltiplication cheyyali...don't use count method.

def prod_list(list_obj):
    new_list = []
    prod = 1
    for x in list_obj:
        if x not in new_list:
            new_list.append(x)
    for x in new_list:
        prod *= x

    return prod


print(prod_list(a))
"""
"""

# VIMP
# Model : interleave multiple lists

# interleave =  mixing together different topics

# 126. Write a Python program to interleave multiple lists of the same length.
# Original list:
# list1:
a = [1, 2, 3, 4, 5, 6, 7]
# list2:
b = [10, 20, 30, 40, 50, 60, 70]
# list3:
c = [100, 200, 300, 400, 500, 600, 700]
# Interleave multiple lists:
# [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]

# Exp: interleave ante first indexing position lo prathi lists


def inter_leave_list(list1, list2, list3):
    return [y for x in zip(list1, list2, list3) for y in x]   # x value lo prathi list loni 1st index element's vastundi daani nunchi manam okko elemant
# manam tesukoni okkoka element ga vestam....


# print(inter_leave_list(a, b, c))


i=0
new_list = []
while i <= len(a)-1:  # maam oka list ni index dwara access cheyyali ante len-1 cheyyali lednte list index out of range veltundi...
    new_list.extend([a[i], b[i], c[i]])  # extend function lo eami rasina adi iterable lone vundali.....
    i += 1

print(new_list)

"""

# ******* *****vvvvviiiiimmmmmppppp........

# Model :

# # 127. Write a Python program to remove words from a given list of strings containing a character or string.
# # Original list:
# # list1:
a = ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
# # Character list:
b = ['#', 'color', '@']


# # New list:
# # ['Red', '', 'Green', 'Orange', 'White']
#


def remove_words(list_obj1, list_obj2):
    new_list = []
    for words in list_obj1:
        new_words = ''.join([word for word in words.split() if not any([phrase in word for phrase in list_obj2])])
        new_list.append(new_words)
    return new_list


# print(remove_words(a, b))


"""
# 128. Write a Python program to calculate the sum of the numbers in a list between the indices of a specified range.
# Original list:
a = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
# Range: 8 , 10
# Sum of the specified range:
# 29

# Exp : ikkada indices ni highlight cheyyali... ichina range of numbers nunchi  index ni access chesi sum cheyyali...

# Range : 8 , 10 ani ichadu so manam 10+1 ani pettalli.(end_index+1) other wise end index not includes.


def sum_of_ele(list_obj, start_index, end_index):
    sum = 0
    for i in range(start_index, end_index+1):  # end index+1 otherwise it won't includes...
        sum += list_obj[i]

    return sum


print(sum_of_ele(a, int(input("Enter the start_index :")), int(input("Enter the end_index :"))))

"""

"""
# Model: nested lists items reverse.

# 129. Write a Python program to reverse each list in a given list of lists.
# Original list of lists:
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# Reverse each list in the said list of lists:
# [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]


# Exp: manam prathi list lo vunna nested lists ni tesukoni danni sort() function dwara reverse chestamu....

# With sort method. 

def reverse_list(list_obj):
    for x in list_obj:
        x.sort(reverse= True)  # sort() dwara reverse chestamu....
    return list_obj


# print(reverse_list(a))

# WIthout sort method.

def reverse_new(list_obj):
    new = []
    for x in list_obj:
        nest = []           
        for y in x:
            nest = [y]+nest
        new.append(nest)         # ikkada for loop bayata nenu new.append(nest) ani raastunnanu.....adi first forloop ki rayali.....

    return new

print(reverse_new(a))
"""

"""
# 130. Write a Python program to count the same pair in three given lists.
# Original lists:
a=[1, 2, 3, 4, 5, 6, 7, 8]
b=[2, 2, 3, 1, 2, 6, 7, 9]
c=[2, 1, 3, 1, 2, 6, 7, 9]
# Number of same pair of the said three given lists:
# 3


def count_pair(l1, l2, l3):
    count =0
    for i in range(len(a)-1):
        if a[i] == b[i] == c[i]:
            count += 1
    return count


print(count_pair(a, b, c))
"""

"""

# Model : frequency of consicutive duplicates.

# 131. Write a Python program to count the frequency of consecutive duplicate elements in a given list of numbers.
# Original lists:
a = [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
# Consecutive duplicate elements and their frequency:
# ([1, 2, 4, 5], [1, 3, 3, 4])

# Exp : 1. mundu elements, frequency and running_count = 1 ani initialize chestamu...
# 2. condition rastamu 3. consicutive frequency vunna elemnts ni loop bayata append cheyyali ledante anni elements frequency vachestundi.....


def freq_cons(list_obj):
    elements = []
    frequency = []
    running_count = 1
    for i in range(len(list_obj)-1):
        if list_obj[i] == list_obj[i+1]:
            running_count += 1

        else:
            elements.append(list_obj[i])
            frequency.append(running_count)
            running_count = 1
    frequency.append(running_count)
    elements.append(list_obj[i+1])

    return elements, frequency


print(freq_cons(a))

"""
"""
# Model : index of maximum value and index of minimum value.

# 132. Write a Python program to find all index positions of the maximum and minimum values in a given list of numbers.
# Original list:
a = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
# Index positions of the maximum value of the said list:
# 7
# Index positions of the minimum value of the said list:
# 3, 11


# Exp : maximum value and min_value.... max_index and min_index kanukkovali....condition raasi check chesukovali...

# max_value, min_value ni list lo first object ga tesukovali...max_index, min_index ni 0th index ga tesukovali... tharuvatha logic rayali...

def index_max_min(list_obj):
    max_val = list_obj[0]
    min_value = list_obj[0]
    max_index = 0
    min_index = 0
    for i in range(len(list_obj)-1):
        if list_obj[i+1] > max_val:
            max_val = list_obj[i+1]
            max_index = i+1
        elif list_obj[i+1] < min_value:
            min_value = list_obj[i+1]
            min_index = i+1

    return (max_val, max_index), (min_value, min_index)


print(index_max_min(a))
"""
"""

# 133. Write a Python program to check common elements between two given list are in same order or not.
# Original lists:
a = ['red', 'green', 'black', 'orange']
b = ['red', 'pink', 'green', 'white', 'black']
c = ['white', 'orange', 'pink', 'black']
# Test common elements between color1 and color2 are in same order?
# True
# Test common elements between color1 and color3 are in same order?
# False
# Test common elements between color2 and color3 are in same order?
# False


# Exp : common ga vunnna elements order and list lo vunna elemants order commmon ga vunnaya leda ani chudali

# 1. first manam common elements ni kannukkovali.... 

# 2. ee common elements order and list lo vunna common elements same order lo vunda leda ani kanukkovali.....

# 3. list comprehension vaadi common elements adharam ga list lo vunna elemants ni bayataki tiyyali...ee vidhamga rendu list's lo saparate cheyyali...

# 4. ee rendu lists same order lo vunte common elements same order lo vunnattu ledante same order lo lenattu...


def common(list_obj1, list_obj2):
    common_elements = [x for x in list_obj1 if x in list_obj2]
    print(common_elements)
    l1 = [x for x in list_obj1 if x in common_elements]
    print('The l1 : ', l1)
    l2 = [x for x in list_obj2 if x in common_elements]
    print('The l2 :', l2)
    return l1 == l2


print(common(c, a))


"""
"""
# 134. Write a Python program to find the difference between two list including duplicate elements.
# Original lists:
a = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
b = [1, 1, 2, 4, 5, 6]
# Difference between two said list including duplicate elements):
# [3, 3, 4, 7]


# Exp : cancellation method laga ...first list lonunchi second list ni cancell cheyyali... so manam mumdu 1st list ni tesukovali daantlo nunchi second list lo vunna ---
# elements ni cancell cheyyali....ila chesukuntu povali...result ni return cheyyali...

def diff(list_obj1, list_obj2):
    result = list_obj1
    for ele in list_obj2:
        result.remove(ele)
    return result


print(diff(a, b))

"""
"""

# Model : iterate over consicutive elements.....

# what is mean  by consicutive...

Ans)  వరుస క్రమంలో వచ్చుచున్న  .....one after another....

# 135. Write a Python program to iterate over all pairs of consecutive items in a given list.
# Original lists:
a = [1, 1, 2, 3, 3, 4, 4, 5]
# Iterate over all pairs of consecutive items of the said list:
# [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]


# Exp : first element & daani thruvatha elemant oka pair ga ravali ...aa tharuvatha di daani next di oka pair ga ravali....ala pothu vundali...

# list comprehension vaadi range and index adharam ga cheyyali....

def iterate_consicutive(list_obj):
    return [(list_obj[i], list_obj[i+1]) for i in range(len(list_obj)-1)]


print(iterate_consicutive(a))


# W3 method:

def pairwise(l1):
    temp = []
    for i in range(len(l1) - 1):
        current_element, next_element = l1[i], l1[i + 1]
        x = (current_element, next_element)
        temp.append(x)
    return temp


"""
"""
# Model : removing duplicates from the list...

# 136. Write a Python program to remove duplicate words from a given list of strings.
# Original String:
a = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
# After removing duplicate words from the said list of strings:
# ['Python', 'Exercises', 'Practice', 'Solution']

# Exp: list com prehension vaadi duplicates ni remove cheyyali...

# list comprehension ni vaadi duplicates ni remove cheyyali ante mundu oka emepty list tesukoni tharuvatha daani kinda list comprehension raasi
# emepty list lo leni elements ni emepty list ki append cheyyali....last lo emepty list return cheyyali...kinda vunna code chudu neeku ardham avutundi....


def duplicates_list(list_obj):
    res = []
    [res.append(word) for word in list_obj if word not in res]
    return res


print(duplicates_list(a))
"""
"""
# Model : first even numbers and first odd numbers in a list...

# 137. Write a Python program to find a first even and odd number in a given list of numbers.
# Original list:
a = [1, 3, 5, 7, 4, 1, 6, 8]
# First even and odd number of the said list of numbers:
# (4, 1)

# Exp : loop raasi break statement vadali...


def first_even_first_odd(list_obj):
    first_even = None
    first_odd = None
    for x in list_obj:
        if x % 2 == 0:
            first_even = x
            break
    for x in list_obj:
        if x % 2 != 0:
            first_odd = x
    return first_even, first_odd


print(first_even_first_odd(a))

"""
"""
# Model : sorting of hetro genious elements.

# 138. Write a Python program to sort a given mixed list of integers and strings. Numbers must be sorted before strings.
# Original list:
a = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# Sort the said mixed list of integers and strings:
# [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']

# Exp : list lo num and str type rendu istadu manam str ni saparate chesi sorted and int ni saparate chesi sorted chesi ee mothanni kalipi oka list ---

#  ga chestamu.... so see bellow code.


def sorting_lists(list_obj):
    return sorted([x for x in list_obj if type(x) == int], reverse=False) + sorted([x for x in list_obj if type(x) == str], reverse=False)



print(sorting_lists(a))

"""

"""
# Model : sort numarical strings based on their numarical values

# 139. Write a Python program to sort a given list of strings(numbers) numerically.
# Original list:
a = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# Sort the said list of strings(numbers) numerically:
# [-500, -12, 0, 4, 7, 12, 45, 100, 200]


def sorting(list_obj):
    # return sorted(list_obj, key=lambda x: int(x), reverse=False)     # it is for string output
    # ( we can speccify sort ascending or sort decending by specify True or False)
    list_obj.sort(key=lambda x:int(x), reverse=False)   # sorting by using sort() method str output

    return list_obj


# print(sorting(a))


def sorting_int_output(list_obj):
    # return sorted([int(x) for x in list_obj], reverse=False)   # this is int output
    new_list = [int(x) for x in list_obj]    # for int output...
    new_list.sort(reverse=False)
    return new_list


print(sorting_int_output(a))

"""

"""
# 140. Write a Python program to remove the specific item from a given list of lists.
# Original list of lists:
a = [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
# Remove 1st list from the saod given list of lists:
# [['Maroon', 'Yellow', 'Olive'], ['#800000', '#FFFF00', '#808000'], ['rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
# Remove 2nd list from the saod given list of lists:
# [['Red', 'Yellow', 'Olive'], ['#FF0000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
# Remove 4th list from the saod given list of lists:
# [['Red', 'Maroon', 'Yellow'], ['#FF0000', '#800000', '#FFFF00'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)']]


# ikkada specific item ni remove cheyyamannadu so.. manam remove method ni vadavochu or slicing ni vada vochu....

def remove_specific(list_obj, item):
    new=[]
    for x in list_obj:
        x.remove(x[item-1])  # remove method....
        new.append(x)
    return new


# print(remove_specific(a, int(input("Enter the item : "))))

# Edi koddiga trickey :::: item no 1 annadante adi daani yokka index number 0 annamata....appudu item nunnchi -1 cheyyali ...rendo slicing lo manam

# item ani iste chalu index ki manam iche item ki okati ekkuvaga vunntundi.... ee problem baga chudu...idi little trickey.... 


def remove_slice(list_obj, item):
    new = []
    for x in list_obj:
        new.append(x[:item-1]+x[item:])
    return new


print(remove_slice(a, int(input("Enter the item :"))))
"""

"""
# Model : remove empty list

# 141. Write a Python program to remove empty lists from a given list of lists.
# Original list:
a = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
# After deleting the empty lists from the said lists of lists
# ['Red', 'Green', [1, 2], 'Blue']


# Exp : manam len function base chesukoni vadathamu ..... kothaga list comprehension method kanukkunam chudu

def remove_empty_list(list_obj):
    # return [x for x in list_obj if len(x) >= 1]
    return [x for x in list_obj if x]   # new for me by W3 schools.


print(remove_empty_list(a))

"""

"""
# Model : sum of specific column......edemi pedda brahma vidhya kaadu.....

# 142. Write a Python program to sum a specific column of a list in a given list of lists.
# Original list of lists:
a = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
# Sum: 1st column of the said list of lists:
# 12
# Sum: 2nd column of the said list of lists:
# 15
# Sum: 4th column of the said list of lists:
# 9


# Exp: list lo vunde prathi element okkoka column ni suchistundi ex : first list tesukuntam andulo 1st column 1, 2nd column 2, 3rd column 3 and 4th column 2

# ade vidhmga prathi nested list's ki varthistudi.... ikkada column ki index ki difference vundi 1 column ante daani yokka index lists lo 0

# ade vidhamga 2nd column ante daani yokka index every list lo 1 annamanta..... idi ardham chesukunte chalu manam.....

# ee problem lo manam mundhu ea column kavalo danni  extract chesukoni daani tharuvatha sum chesukovali....

def sum_of_specific(list_obj, column):
    specific_column_items= [x[column-1]for x in list_obj]
    sum = 0
    for x in specific_column_items:
        sum += x
    return sum


print(sum_of_specific(a, int(input("Enter the specific column:"))))



"""

"""
# Model : Frequency of nested lists.

# 143. Write a Python program to get the frequency of the elements in a given list of lists.
# Original list of lists:
a = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
# Frequency of the elements in the said list of lists:
# {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
# Click me to see the sample s

# Exp: mundhu nestes lists lo vunnavanni oka normal list loki techukovali( by using list comprehension) aa tharuvatha daaniki frequesncy ni kanukkovali..


def freq_of_nested(list_obj):
    freq = {}
    new_list = [y for x in a for y in x]
    for x in new_list:
        if x not in freq:
            freq[x] = 1
        else:
            freq[x] += 1
    return freq


print(freq_of_nested(a))
"""
"""
# Model : extract specific element's from the matrix

# 144. Write a Python program to extract every first or specified element from a given two-dimensional list.
# Original list of lists:

a = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
# Extract every first element from the said given two dimensional list:
# [1, 4, 7]
# Extract every third element from the said given two dimensional list:
# [3, 6, 9]


def ext_specific(list_obj, specific):
    return [x[specific-1] for x in a]


print(ext_specific(a, int(input("Enter the number specific item :"))))

"""
"""
# Exp : generating one number....from a range.... that number must not contains in the specific list

# 145. Write a Python program to generate a number in a specified range except some specific numbers.
# Generate a number in a specified range (1, 10) except
a = [2, 9, 10]
# 7
# Generate a number in a specified range (-5, 5) except
b = [-5, 0, 4, 3, 2]
# -4

# Exp : ikkada generate a number annadu kabatti...manam oka number ni generate cheyyali...so random functio vadali....manam print chese number anedi

# ichina specific list lo vundakudadu...


# choice::: it will extract the random element from the given iterable() >>>> random.choice(iterable)  

from random import choice


def generate_num(start_range, end_range, list_obj):
    return random.choice([i for i in range(start_range, end_range+1) if i not in list_obj])  # we have to include end number so +1 must be includes..

# the specific object is must not be in the specified list.... 


print(generate_num(int(input("Enter the start range :")), int(input("Enter the end range:")), eval(input(":Enter the list_obj"))))
"""

"""
# 146. Write a Python program to compute the sum of digits of each number of a given list.
# Original tuple:
a= [10, 2, 56]
# Sum of digits of each number of the said list of integers:
# 14
# Original tuple:
b =[10, 20, 4, 5, 'b', 70, 'a']
# Sum of digits of each number of the said list of integers:
# 19
# Original tuple:
c = [10, 20, -4, 5, -70]
# Sum of digits of each number of the said list of integers:
# 19

# Exp : sum of digits ante number lo vunde prathi didgit ni add cheyyali...positive vunna negative vunna add cheyyali...

# ichina number ni string loki marchukovali... dantlo nunchi neagtive symbole ni remove cheyyadaniki isdigit() ni vaadi str nunchi int loki marchukoni add cheyyali...

# manam isinstance mathod kuda vadocchu......isinstance(num, type)


def add_digit(list_obj):   #### we can use isinstance() mathod also...
    new = ''.join([str(num) for num in list_obj if type(num) != str])  # removing alphabets and extracting only numbers with signs also... it is in straing formate.
    print(new)  # for understanding purpose...see the join function output....
    sum = 0  # initializing sum varible...
    for num in new:
        if num.isdigit():  # removing the negative signs by using isdigit function()....
            sum += int(num)  # converting the str to int...and adding...
    return sum


print(add_digit(a))

"""

"""
# 147. Write a Python program to interleave two given list into another list randomly.
# Original lists:
a = [1, 2, 7, 8, 3, 7]
b = [4, 3, 8, 9, 4, 3, 8, 9]
# Interleave two given list into another list randomly:
# [4, 1, 2, 3, 8, 9, 4, 3, 7, 8, 9, 8, 3, 7]


# The sample() method returns a list with a randomly selection of a specified number of items from a sequnce.

# idi new list ni create chestundi.....random ga iterable lo vunde numbers ni select chesukoni...

# Note: This method does not change the original sequence.

# random.sample(sequence, k)   >>>>> k >Required. The size of the returned list... sequence and k is for length of the returned list...

from random import shuffle
 

def inter_leave_randomly(list_obj1, list_obj2):
    return random.sample((list_obj1+list_obj2), len(list_obj1+list_obj2))


print(inter_leave_randomly(a, b))
"""
"""
# Model : remove words from specific words from a given list...

# 148. Write a Python program to remove specific words from a given list.
# Original list:
a = ['red', 'green', 'blue', 'white', 'black', 'orange']
# Remove words:
b = ['white', 'orange']
# After removing the specified words from the said list:
# ['red', 'green', 'blue', 'black']


# We can do it by using list comprehension and by using lambda and filter function

# By using list_comprehension.

def new_list(list_obj1, list_obj2):
    return [x for x in list_obj1 if x not in list_obj2]


# print(new_list(a, b))

#  By using lambda

# filter(function, iterable) 


def new_list_lambda(list_obj1, list_obj2):
    return list(filter(lambda x: x not in list_obj2, list_obj1))  # lambda function and iterable....

# >>>>>>>>>>>>>>>>>>>>>ikkada varaku lambda function..<>>idi iterable>>><<<<<<


print(new_list_lambda(a, b))

"""

"""

# *********Moodel : all possible combinations...


# 149. Write a Python program to get all possible combinations of the elements of a given list.
# Original list:
a = ['orange', 'red', 'green', 'blue']
# All possible combinations of the said list's elements:
# [[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red']
#  ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]

# Exp: manam all posiible combinations ni kannukkovali....

# 1. mundu manam len of list == 0 iethe emepty list ni retur cheyyali [[]]

# 2. recursive function dwara ee logic rayali...


def all_possible_comb(list_obj):
    if len(list_obj) == 0:
        return [[]]
    result = []
    for x in all_possible_comb(list_obj[1:]):
        result += [x, x+[list_obj[0]]]     # This is very important line.....i dont understand...

    return result


print(all_possible_comb(a))

"""
"""
# Model : reverse the original list...

# 150. Write a Python program to reverse a given list of lists.
# Original list:
a = [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]
# Reverse said list of lists:
# [['white', 'black', 'pink'], ['green', 'blue'], ['orange', 'red']]
# Original list:
b = [[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]]
# Reverse said list of lists:
# [[2, 3, 4, 2, 4], [0, 2, 4, 5], [1, 2, 3, 4]]


# Exp: original list ni reverse cheyyali....

# by using lambda.

def reverse_list(list_obj):
    new_list = [] #>>> my mistake...range function lo length raste correct ga access every element ni access cheyyochu...ikkada
    for i in range(1, len(list_obj)+1):
        new_list += [list_obj[-i]]  # manam ikkada 1 nunci start chesam sooo end ki +1 kalapali...  ikkada add chese element ki kachithamga list[]--
    return new_list           # ani pettali appude adi nested list laga consider chestundi ledante []+[] = [] .... []+[[]] = [[]] <<<Vimp...

print(reverse_list(a))



def reverse_list(list_obj):
    new_list = []
    for x in list_obj:
        new_list = [x]+new_list
    return new_list


print(reverse_list(a))

"""
"""
# Model : max, min with in the given range...


# 151. Write a Python program to find the maximum and minimum values in a given list within specified index range.
# Original list:
a = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
# Index range:
# 3 to 8
# Maximum and minimum values of the said given list within index range:
# (5, 0)


# by using slicing...

def max_min_in_range(list_obj, start, end):
    max = list_obj[start]
    min = list_obj[start]
    for x in list_obj[start:end+1]:   # print(list_obj[start:end+1]) print chesi chudu for understanging purpose....
        if x > max :
            max = x
        elif x < min:
            min = x
    return max, min


print(max_min_in_range(a, int(input("Enter the start range :")), int(input("Enter the end range :"))))


# by using range function...

def max_min_range_ranfun(list_obj, start, end):
    new= [list_obj[i] for i in range(start, end+1)]    # mistake ikkada list_obj(i) ani pettanu ....list_obj[i] ani pettali....
    max= new[0]
    min= new[0]
    for x in new:
        if x > max:
            max = x
        elif x < min:
            min = x
    return max, min


print(max_min_range_ranfun(a, int(input("Enter the start :")), int(input("Enter the end :"))))
"""
"""
# Model : heapq model

# this is new model

# 152. Write a Python program to combine two given sorted lists using heapq module.
# Original sorted lists:
a = [1, 3, 5, 7, 9, 11]
b = [0, 2, 4, 6, 8, 10]
# After merging the said two sorted lists:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


from heapq import merge


# merge returns generator object we can conver into this by list or tuple, by list constructor tuple constructor

def heap_tech(llist_obj1, list_obj2):
    return list(merge(llist_obj1, list_obj2)) # it returns jenetaor object soo we have converted into list by using list conteructor..   


print(heap_tech(a, b))


"""

"""
# Model : join two list of lists....

# 154. Write a Python program to join two given list of lists of same length, element wise.
# Original lists:
a = [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
b = [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
# Join the said two lists element wise:
# [[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
# Original lists:
# [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
# [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
# Join the said two lists element wise:
# [['a', 'b', 'p', 'q'], ['b', 'c', 'd', 'p', 's', 't'], ['e', 'f', 'u', 'v', 'w']]


# Exp : list of lists ante nested lists....same length ante rendu pedda lists(outer lists) same length lo vundali....

# join list of lists ante list lo vunna nested lists add cheyyali...

# element wise ante oke index position lo vundevi kalapali >>>> i.e list[1]+list[1], list[2]+list[2]


# accessing by using range length function...


def merge_list_of_lists(list_obj1, list_obj2):
    return [list_obj1[i]+list_obj2[i] for i in range(len(list_obj1))]   # >>> here also mistake again []+[]=[]...[[]]+[[]]=[[]]
                                                                     # list_obj[i] anthe list lo 'i'-th element ikkada 'i'th element oka list...


print(merge_list_of_lists(a, b))

# By using zip function...

def mrege(list_obj1, list_obj2):
    return [x+y for x, y in zip(list_obj1, list_obj2)]


print(mrege(a, b))

"""

"""
# Model : adding of two list elements... from left to right... dentlo rendu models vunnai ...okati left lo add cheyyandi ani ...rendu right lo add cheyyandi ani

# 155. Write a Python program to add two given lists of different lengths, start from left.
# Original lists:
a = [2, 4, 7, 0, 5, 8]
b = [3, 3, -1, 7]
# Add said two lists from left:
# [5, 7, 6, 7, 5, 8]
# Original lists:
c = [1, 2, 3, 4, 5, 6]
d = [2, 4, -3]
# Add said two lists from left:
# [3, 6, 0, 4, 5, 6]


# Exp : index adharam ga add cheyyali....rendu lists lo eadithe thakkuva length vuntundo daani length tesukovali...iteration jaripi add chesi pedda list---
# ni return cheyyali

def adding_list_left_to_right(list_obj1, list_obj2):
    for i in range(len(list_obj2)):
        list_obj1[i] += list_obj2[i]

    return list_obj1    # len eadi iethe ekkuva vuntundo danni return cheyyali...


print(adding_list_left_to_right(c, d))

"""

# Model : different lengths of lists .... add from right..


# 156. Write a Python program to add two given lists of different lengths, start from right.
# Original lists:
a = [2, 4, 7, 0, 5, 8]
b = [3, 3, -1, 7]
# Add said two lists from left:
# [2, 4, 10, 3, 4, 15]
# Original lists:
c = [1, 2, 3, 4, 5, 6]
d = [2, 4, -3]


# Add said two lists from left:
# [1, 2, 3, 6, 9, 3]


# MISTAKES : manam oka list ni normal ga access cheyyalante range(len(list)) ani raste chalu ....

# ade oka list ni reverse nunchi access cheyyali ante range 1 nunchi start cheyyali len()+1 cheyyali...range lo starting ki okati penchithe length ki--

# kuda okati penchali... if u start from 1 add +1 to length.... range(1, len(list)+1)


def add_from_right(list_obj1, list_obj2):
    for i in range(1, len(list_obj2)+1):   # akkada okati penchithe ikkada kuda okati penchali....
        list_obj1[-i] += list_obj2[-i]

    return list_obj1   # len eadi ithe peddado danni return cheyyali...


print(add_from_right(c, d))










