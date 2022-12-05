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


"""

"""
# Model : inter leave different length's of lists....

# 157. Write a Python program to interleave multiple given lists of different lengths.
# Original lists:
a = [2, 4, 7, 0, 5, 8]
b = [2, 5, 8]
c = [0, 1]
d = [3, 3, -1, 7]
# Interleave said lists of different lengths:
# [2, 2, 0, 3, 4, 5, 1, 3, 7, 8, -1, 0, 7, 5, 8]


def inter_diff_len(list_obj1, list_obj2, list_obj3, list_obj4):
    length = max(len(list_obj1), len(list_obj2), len(list_obj3), len(list_obj4))
    new = []
    for i in range(length):
        if len(list_obj1) > i:    # ikkada >= pettakudadu endukante ex: oka list length 5 vundi i value ki equal...list[i] element anedi index out of range ---
            new.append(list_obj1[i])    #  ani vastundi... length 5 gala list_obj yokka index anedi 0 to 4 varaku vuntundi...5 index vundadu so >= pettakudadu  
        if len(list_obj2) > i:
            new.append(list_obj2[i])
        if len(list_obj3) > i:
            new.append(list_obj3[i])
        if len(list_obj4) > i:
            new.append(list_obj4[i])
    return new


print(inter_diff_len(a, b, c, d))

"""
"""
# Model : max and min value... from list of tuples...

# 158. Write a Python program to find the maximum and minimum values in a given list of tuples.
# Original list with tuples:
a = [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
# Maximum and minimum values of the said list of tuples:
# (78, 60)


# Exp: 

def max_min(list_obj):
    max_val = list_obj[0][1]
    min_val = list_obj[0][1]
    for x, y in list_obj:
        if y > max_val:
            max_val = y
        elif y < min_val:
            min_val = y
    return max_val, min_val


print(max_min(a))

"""
"""
# Model : append same value multiple times in  a list ...

# 159. Write a Python program to append the same value /a list multiple times to a list/list-of-lists.
# Add a value(7), 5 times, to a list:
# ['7', '7', '7', '7', '7']
# Add 5, 6 times, to a list:
# [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
# Add a list, 4 times, to a list of lists:
# [[1, 2, 5], [1, 2, 5], [1, 2, 5], [1, 2, 5]]
# Add a list, 3 times, to a list of lists:
# [[5, 6, 7], [1, 2, 5], [1, 2, 5], [1, 2, 5], [1, 2, 5]]


def append_multiple_times(list_obj, element, number_of_times):
    list_obj += [element] * number_of_times     # ikkada manam  element ni kachithamga list lo pettali ledante type error >>> we can't add element to list---
    return list_obj             # ani error vatundi....same tpe ni matrame manam add cheyyagalam...


print(append_multiple_times(eval(input("Enter the list_obj :")), eval(input("Enter the element :")), int(input("Enter the number of times :"))))
"""
"""
# Model : removing n number of elements based on certain condition....

# 160. Write a Python program to remove first specified number of elements from a given list satisfying a condition.
# Remove the first 4 number of even numbers from the following list:
a = [3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]
# Output:
# [3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]
# Original list:
b = [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]
# Remove first 4 even numbers from the said list:
# [3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]


# Exp: ichina list lo nunchi  only 'n' number of even numbers matrame remove cheyyali...
 
# remaining elements alane vundali...

def remove_specified(list_obj, number):
    count = 0
    for x in a:
        if x % 2 == 0:
            list_obj.remove(x)
            count += 1
            if count == number:
                break
    return list_obj


print(remove_specified(a, int(input("Enter the number of elements to be removed :"))))

"""

# Model : list is increasing sequence or not...if you remove one element from the list result list is strightly increasing or not...


# 161. Write a Python program to check if a given list is strictly increasing or not. Moreover,
# If removing only one element from the list results in a strictly increasing list, we still consider the list true.
# True
# True
# True
# True
# True
# True
# True
# True
# True
# True
# True
# False
# False
# False
# False
# False


# def strightly_increasing(list_obj):
#     if len(list_obj) < 3:
#         return True
#     a, b, *sequence = list_obj
#     skipped = 0
#     for c in list_obj:
#         if a < b < c:
#             a, b = b, c
#         elif b < c :
#             a, b = b, c
#         elif a < c :
#             a, b =
#


'''

# Model : last occurance of specified element....

# 162. Write a Python program to find the last occurrence of a specified item in a given list.
# Original list:
a = ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
# Last occurrence of f in the said list:
# 7
# Last occurrence of c in the said list:
# 15
# Last occurrence of k in the said list:
# 14
# Last occurrence of w in the said list:
# 12


# Exp : manam ichina element last ga ekkada occur iendo kanukkovali.... daniki method vachi rindex...

# str.rindex(element) >>> ichina list items ni manam str loki marchukoni oka string laga chesukuntamu....already string rupam lo vunte marchhukovalsina pani ledu...


def finding_last_occur(list_obj, element):
    return ''.join(list_obj).rindex(element)   # new method  :: rindex() >>> string.rindex >>> join method makes the string and rindex method finds the index...


print(finding_last_occur(a, input("Enter the specific list object :")))

'''
'''

# 163. Write a Python program to get the index of the first element which is greater than a specified element.
# Original list:
a = [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
# Index of the first element which is greater than 73 in the said list:
# 4
# Index of the first element which is greater than 21 in the said list:
# 1
# Index of the first element which is greater than 80 in the said list:
# 5
# Index of the first element which is greater than 55 in the said list:
# 3

# Exp: icchina specified element kanna peddadi ga vunde first element ...aa first highest element yokka index number return cheyyali....

# Note ::: vimp -> ekkada ithe first highest elemnt vastundo akkada break cheyyali ...ledante loop end varaku runavutundi....

def index_specified(list_obj, specified_element):
    for x in list_obj:
        if x > specified_element:
            first_highest = x
            break       # manam ikkaada break rayakapothe loop last element varaku run iyyi ....last lo vunde specified element kanna ekkuva vunde alament vatsundi..
    return list_obj.index(first_highest)


print(index_specified(a, int(input("Enter the specified element :"))))

'''
'''
# Model : getting items with specified condition...

# 164. Write a Python program to get the items from a given list with specific condition.
# Original list:
a = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Number of Items of the said list which are even and greater than 45
# 5


# Exp : enni items vunnai ....even and greather than 45.

def even_gr_ff(list_obj):
    count = 0
    for x in list_obj:
        if x % 2 == 0 and x > 45:
            count += 1
    return count


print(even_gr_ff(a))


'''
'''
----vimp-----....
# Model : list into specified sized chunks....

# chunks =  ముక్క భాగం

# 165. Write a Python program to split a given list into specified sized chunks.
# Original list:
a = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Split the said list into equal size 3
# [[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
# Split the said list into equal size 4
# [[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]
# Split the said list into equal size 5
# [[12, 45, 23, 67, 78], [90, 45, 32, 100, 76], [38, 62, 73, 29, 83]]

# Exp : oka list ni cheppina length prakaram  chinna chinna nested list's ga create cheyyali... daanikosam manam slicing cheyyali...

# confucing part :::

# slicing ante mukkalu cheyyadam... ani ardham ::: manam ea object ni mukkalu cheste aa object vastundi....

# list ni slicing cheste list output vastundi... string ni mukkalu cheste string output vastundi....etc


# Exp: manam ikkada range() lo start , stop ,step mudu vadali.... formula === > list_obj[i:i+chunk_size or step] >>> it will return mini list

# Ela slice cheyyali anedi chala important...


def creating_chunks(list_obj, chunk_size):
    return [list_obj[i:i+chunk_size]for i in range(0, len(list_obj), chunk_size)]  # list_obj[i:i+chunk_size] >>> returns mini list... we are slicing the list_obj


# print(creating_chunks(a, int(input("Enter the chunk size :"))))


def create(list_obj, chunk_size):
    new =[]
    for i in range(0, len(list_obj), chunk_size):
        new.append(list_obj[i:i+chunk_size])     # list_obj[i:i+chunk_size] return's mini list's......we are slicing the list_obj

    return new


print(create(a, int(input("Enter the  chunk_size:"))))

  

# by using generator function ::::

def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


'''
'''
# Model : removing sprcifies value.

# 166. Write a Python program to remove None value from a given list.
# Original list:
a = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# Remove None value from the said list:
# [12, 0, 23, -55, 234, 89, 0, 6, -12]


# By using list_comp :::

def remove_specified(list_obj, specified_value):
    return [i for i in list_obj if i != specified_value]


# print(remove_specified(a, eval(input("Enter the specified_item : "))))  # ikkada eval chala important...list lo None, string, number vundi...soo---
# list lo None vundi None anedi string kaadu...list contains different data types...eval vadithe daani yokka internal charecter ni batti input nunchi bayataki tesukoni vastundi


# By using lambda :::

def remove_lambda(list_obj, specified_value):
    return list(filter(lambda x: x != specified_value, list_obj))


print(remove_lambda(a, eval(input("Enter the specific_value_to_remove : "))))

'''
'''
# Model :

# 167. Write a Python program to convert a given list of strings into list of lists.
# Original list of strings:
a = ['Red', 'Maroon', 'Yellow', 'Olive']
# Convert the said list of strings into list of lists:
# [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]

# by using list comp

def list_of_strings_to_list_of_lists(list_obj):
    return [list(i) for i in list_obj]


# print(list_of_strings_to_list_of_lists(a))


# by using noraml append method...

def str_list(list_obj):
    new = []
    for x in list_obj:
        new.append(list(x))
    return new

print(str_list(a))

'''

'''

# 168. Write a Python program to display vertically each element of a given list, list of lists.
# Original list:
a = ['a', 'b', 'c', 'd', 'e', 'f']
# Display each element vertically of the said list:
# a
# b
# c
# d
# e
# f
# Original list:
b = [[1, 2, 5], [4, 5, 8], [7, 3, 6]]
# Display each element vertically of the said list of lists:
# 1 4 7
# 2 5 3
# 5 8 6

# for normal objects...


def vertical(list_obj):
    for i in list_obj :
        print(i)


vertical(a)


# for nested objects...

# VIMP ::: nested lists ni iterate chese tapudu manaki list lopala enni elements vunte anni i, j, k, l, m, lu rasukovocchu.... zipping and unzipping vimp...

def nested_lists(list_obj):
    for i, j, k in list_obj:    # ikkada 3 elements vundi sooo....i, j, k mudu rasamu....
        print(i, j, k)


nested_lists(b)


# by using zip function:

def using_zip(list_obj):
    for x, y, z in zip(*list_obj):   # unzipping kosam manam star pettali ledante unzip avvadu...
        print(x, y, z)
        
        
------see the concept of zipping and unzipping in bellow the codes ::::  tuple of lists, tuples, normal 
a=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for x in zip(a):  # we are not unzipping here
#     print(x)
#
# # output will be like this..
#
# ([1, 2, 3],)
# ([4, 5, 6],)
# ([7, 8, 9],)

for x, y, z in zip(a):
    print(x, y, z) >>> error ...too many values
a=[[1, 2, 3], [4, 5, 6], [6, 7, 8]]

for x in zip(*a):
    print(x)

(1, 4, 6)
(2, 5, 7)
(3, 6, 8)

conclusion ===>>> unzip cheyyakunda oke element isthe list of tuples ustundi

# unzip chesi oke element iste only tuple lo vastundi

# unzip chesi equal elements iste normal ga vastundi....


for x, y, z in zip(*a):
    print(x, y, z)

# 1 4 7
# 2 5 8
# 3 6 9

'''
'''
# Model : list of strings and characters to list of characters...

# 169. Write a Python program to convert a given list of strings and characters to a single list of characters.
# Original list:
a = ['red', 'white', 'a', 'b', 'black', 'f']
# Convert the said list of strings and characters to a single list of characters:
# ['r', 'e', 'd', 'w', 'h', 'i', 't', 'e', 'a', 'b', 'b', 'l', 'a', 'c', 'k', 'f']

# By using list comprehension...


def list_of_char(list_obj):
    return [y for x in list_obj for y in x]  # inko forr loop ::: for y in x anedi list lo vunna strings ni charecters ga marchadaniki 


print(list_of_char(a))


# by using constructor method:::

def list_strings(list_obj):
    new = []
    for x in list_obj:
        new += list(x)   # idi simple method....every string ni list() constructor lo petti strings ga vidagottatam... 
    return new


print(list_strings(a))

'''
'''
# Model : inserting element after every nth element...

# vimp...

# 170. Write a Python program to insert an element in a given list after every nth position.
# Original list:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# Insert a in the said list after 2 nd element:
# [1, 2, 'a', 3, 4, 'a', 5, 6, 'a', 7, 8, 'a', 9, 0]
# Insert b in the said list after 4 th element:
# [1, 2, 3, 4, 'b', 5, 6, 7, 8, 'b', 9, 0]


# Vimp : manam while loop tesukovali....

# 1. first i value ni initialize chesukovali...

# 2. insert function vaadali

# 3. i value ni position +1 tho increment cheyyali..... why +1 ? prathi saari k include cheyyadam valla length increasing avutundi anduvalla..


def insert_after_nth_pos(list_obj, position, element):
    i = position
    while i < len(list_obj):
        list_obj.insert(i, element)   # ikkada position ani ivvakudadu...position value change kaadu ...i value matrame change avutundi...i value matrame ivvali..
        i += position+1    #>>> v.imp  +1 add cheyyali...

    return list_obj


print(insert_after_nth_pos(a, int(input("Enter the positions:")), input("Enter the element")))

'''

'''
# model : concatinate element wise...



# 171. Write a Python program to concatenate element-wise three given lists.
# Original lists:
a = ['0', '1', '2', '3', '4']
b = ['red', 'green', 'black', 'blue', 'white']
c = ['100', '200', '300', '400', '500']
# Concatenate element-wise three said lists:
# ['0red100', '1green200', '2black300', '3blue400', '4white500']


# By using list comprehension...

def concatenate_element_wise(list_obj1, list_obj2, list_obj3):
    return [list_obj1[i]+list_obj2[i]+list_obj3[i] for i in range(len(a))]


print(concatenate_element_wise(a, b, c))


# by using ...append method

def con_zip(list_obj1, list_obj2, list_obj3):
    new = []
    for i in range(len(list_obj1)):
        new.append(list_obj1[i]+list_obj2[i]+list_obj3[i])

    return new


print(con_zip(a, b, c))

# normal list method

def con_normal(list_obj1, list_obj2, list_obj3):
    new = []
    for i in range(len(list_obj1)):
        new += [list_obj1[i]+list_obj2[i]+list_obj3[i]]
    return new


print(con_normal(a, b, c))

# Vimp...


def using_zip(list_obj1, list_obj2, list_obj3):
    new = []
    for x, y, z in zip(*(list_obj1, list_obj2, list_obj3)):
        new.append(x+y+z)
    return new


print(using_zip(a, b, c))

# By using map function....

def using_map(list_obj1, list_obj2, list_obj3):
    return list(map(lambda x, y, z: x+y+z, list_obj1, list_obj2, list_obj3))


print(using_map(a, b, c))


'''

'''

# Little trickey...

# Model : removing last N numbers.

# 172. Write a Python program to remove the last N number of elements from a given list.
# Original lists:
a = [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
# Remove the last 3 elements from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]
# Remove the last 5 elements from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]
# Remove the last 1 element from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]


def remove_elements(list_obj, n_positions):
    return list_obj[0:-n_positions]


print(remove_elements(a, int(input("Enter the n_th_position :"))))


'''
'''
# Model : merging some list items based in the index value...

# 173. Write a Python program to merge some list items in given list using index value.
# Original lists:
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


# Merge items from 2 to 4 in the said List:
# ['a', 'b', 'cd', 'e', 'f', 'g']
# Merge items from 3 to 7 in the said List:
# ['a', 'b', 'c', 'defg']


def merge_list_obj(list_obj, start, stop):
    list_obj[start:stop] = [''.join(list_obj[start:stop])]     # deeeni ardham ... list[start:stop] anedi list_obj lo join iyyi vundali...---
    return list_obj                                             # ade [''.join(list_obj([start:stop]] ki meaning


print(merge_list_obj(a, int(input("Enter the start :")), int(input("Enter the end :"))))
'''
"""
# Model : adding a number to each item in a list...

# 174. Write a Python program to add a number to each element in a given list of numbers.
# Original lists:
a = [3, 8, 9, 4, 5, 0, 5, 0, 3]
# Add 3 to each element in the said list:
# [6, 11, 12, 7, 8, 3, 8, 3, 6]
# Original lists:
b =[3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
# Add 0.51 to each element in the said list:
# [3.71, 8.51, 10.41, 4.71, 5.51, 0.61, 5.51, 3.62, 0.51]


def add_each(list_obj, specify_number):
    return list(map(lambda x: x+specify_number, list_obj))


# print(add_each(a, eval(input("Enter the number to add :"))))    # a ki intiger add cheyyali... b ki float add cheyyali...so better ga eval ani isthe no problem


def add(list_obj, specify_number):
    return [x+specify_number for x in list_obj]


# print(add(a, eval(input("Enter the number to add :"))))



def normal_add(list_obj, specify_element):
    new = []
    for x in list_obj:
        new += [x+specify_element]   #ikkada kachithamga list lo pettali ledante list_obj and int error vastundi
    return new


print(normal_add(a, eval(input("Enter the element :"))))

"""
"""
# Model : minimum and maximum value for each tuple position...

# 175. Write a Python program to find the minimum, maximum value for each tuple position in a given list of tuples.
# Original list:
a = [(2, 3), (2, 4), (0, 6), (7, 1)]
# Maximum value for each tuple position in the said list of tuples:
# [7, 6]
# Minimum value for each tuple position in the said list of tuples:
# [0, 1]

# Note :

# ichina list of tuples lo ....tuples lo 0th position lo vunna elements lo maximum eadi and minimum eadi......1st position lo maximum eadi and minimum eadi

# 0th position ni antha oka list lo petti max and min kanukko and 1st posistion ni antha oka list lo petti max and min kanukko...

# 0th lonu, 1st lonu max ni and 0th lonu, 1st lonu min ni return chey.

def finding_min_max(list_obj):
    zeroth = [x for x, y in list_obj]
    first = [y for x, y in list_obj]
    max_zero = zeroth[0]
    min_zero = zeroth[0]
    max_first = first[0]
    min_first = first[0]
    for x in zeroth:
        if x > max_zero:
            max_zero = x
        elif x < min_zero:
            min_zero = x
    for x in first:
        if x > max_first:
            max_first = x
        elif x < min_first:
            min_first = x
    return 'maximum value for eachtuple position {}\nmaximumfor first position of list of tuples {}'.format([max_zero, max_first],[min_zero,min_first])


print(finding_min_max(a))

"""

"""

# Model : dividing two lists.

# 176. Write a Python program to create a new list dividing two given lists of numbers.
# Original list:
a = [7, 2, 3, 4, 9, 2, 3]
b = [9, 8, 2, 3, 3, 1, 2]
# [0.7777777777777778, 0.25, 1.5, 1.3333333333333333, 3.0, 2.0, 1.5]


def div_of_two_lists(list_obj1, list_obj2):
    return list(map(lambda x, y: x/y, a, b))


# print(div_of_two_lists(a, b))


def div(list_obj1, list_obj2):
    return [x/y for x, y in zip(list_obj1, list_obj2)]


print(div(a, b))


"""
"""
# Model : common elements in the nested lists.

# 177. Write a Python program to find common elements in a given list of lists. Go to the editor
# Original list:
a = [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
# Common elements of the said list of lists:
# [2, 3]
# Original list:
b = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
# Common elements of the said list of lists:
# ['c']



# by using reduce function...

from functools import reduce


def common_in_nested(list_obj):
    return list(reduce(lambda x, y: x & y, (set(i)for i in list_obj)))   # every nested list oka set gammari lambda func loki veltundi... '&'> anedi intersection...


print(common_in_nested(b))

"""
"""
# 178. Write a Python program to insert a specified element in a given list after every nth element.
# Original list:
a = [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# Insert 20 in said list after every 4 th element:
# [1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]
# Original list:
b = ['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
# Insert Z in said list after every 3 th element:
# ['s', 'd', 'f', 'Z', 'j', 's', 'a', 'Z', 'j', 'd', 'f', 'Z', 'd']


# by while loop ::::: >>>> insert after nth element anna nth element ann okkate.....same logic gollow avvu

def inserting(list_obj, position, element):
    i = position
    while i < len(list_obj):
        list_obj.insert(i, element)
        i += position+1  # ikkada okkoka element insert avvadam valla length 1 perugutundi...
    return list_obj


print(inserting(b, int(input("Enter the position :")), eval(input("Enter the element :"))))  # NEW : eval function lo list anna , tupple anna, set anna,---
# string with quotationslo ivvali... int, float lo ivvali... manam ee function lo eami iethe mention chetsamo ade datastructure object tesukuntundi...


# Note : in eval function we must mention the datastructure type while giving input to this function....

"""
"""
# Model : biggest possible number....


# 179. Write a Python program to create the largest possible number using the elements of a given list of positive integers.
# Original list:
a = [3, 40, 41, 43, 74, 9]
# Largest possible number using the elements of the said list of positive integers:
# 9744341403
# Original list:
b = [10, 40, 20, 30, 50, 60]
# Largest possible number using the elements of the said list of positive integers:
# 605040302010
# Original list:
c = [8, 4, 2, 9, 5, 6, 1, 0]
# Largest possible number using the elements of the said list of positive integers:
# 98654210


# Exp: list lo ichina numbers annintini tesukoni dantlo manam peddaga vache number ni form cheyyali....

# lambda func lo len mothanni  *2 cheyyali... daanni // lan(x) chesi aa mothanni lambda x tho multiply cheyyali... ikkada x aneni lambda argument...

# this is important...

def biggest_number(list_obj):
    return ''.join(sorted((str(x) for x in list_obj), reverse=True, key=lambda x: x*((len(str(max(list_obj))))*2//len(x))))


print(biggest_number(a))

"""
"""

# Model : minimum possible number.

# 180. Write a Python program to create the smallest possible number using the elements of a given list of positive integers.
# Original list:
a = [3, 40, 41, 43, 74, 9]
# Smallest possible number using the elements of the said list of positive integers:
# 3404143749
# Original list:
b = [10, 40, 20, 30, 50, 60]
# Smallest possible number using the elements of the said list of positive integers:
# 102030405060
# Original list:
c=[8, 4, 2, 9, 5, 6, 1, 0]
# Smallest possible number using the elements of the said list of positive integers:
# 01245689


# Exp : list lo vunna numbers anninti kalipi small possible number ni create cheyyali...

def smallest(list_obj):
    return ''.join(sorted((str(x)for x in list_obj), reverse=False, key=lambda x: x * ((len(str(min(list_obj)))) * 2//len(x))))


print(smallest(c))

"""
"""
# Model : iterate given list cyclically on specific index...


# Super problem....

# 181. Write a Python program to iterate a given list cyclically on specific index position.
# Original list:
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# Iterate the said list cyclically on specific index position 3 :
# ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
# Iterate the said list cyclically on specific index position 5 :
# ['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']


def iterate_cyclically(list_obj, in_pos):
    new_list = []
    for x in range(len(list_obj)):
        new_list.append(list_obj[in_pos % len(list_obj)])  # Note : ikkada manam slicing cheyyadam ledu indexind dwara access chestunnamu...
        in_pos += 1       # specific position nunchi manam cyclic cheyyali kabatti...manam in_pos ki +1 add chestamu...
    return new_list


print(iterate_cyclically(a, int(input("Enter the specific position : "))))

"""
"""
# Model : finding maximum nested list element and minimum nested list element....

# 182. Write a Python program to calculate the maximum and minimum sum of a sublist in a given list of lists.
# Original list:
a = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
# Maximum sum of sub list of the said list of lists:
# [2, 3, 5, 4]
# Minimum sum of sub list of the said list of lists:
# [1, 2, 1, 2]


# by using reduce function....

from functools import reduce

def max_min_sum_element(list_obj):
    max= reduce(lambda x, y: x if sum(x) > sum(y) else y, list_obj)
    min = reduce(lambda x, y : y if sum(x) > sum(y) else x, list_obj)

    return 'The maximum sum of element is : {}\nThe minimum sum of sum of element is : {}'.format(max, min)


# print(max_min_sum_element(a))



# by using max and min func:


def max_min(list_obj):
    maxi = max(list_obj, key=sum)
    mini = min(list_obj, key=sum)
    return maxi, mini


print(max_min(a))

"""
"""
# Model : list motham  lo unique values kanukkovali...

# 183. Write a Python program to get the unique values in a given list of lists.
# Original list:
a = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
# Unique values of the said list of lists:
# [0, 1, 2, 3, 4, 5, 7]
# Original list:
b = [['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'], ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]
# Unique values of the said list of lists:
# ['e', 'd', 'c', 'b', 'x', 'k', 'n', 'h', 'g', 'j', 'i', 'a', 'l', 'y', 'v', 'z']


# Exp :  ikkada unique values adigaadu ... so vunna elements annintilonu okkokati  get cheyyali....

def getting_unique(list_obj):
    new = [y for x in list_obj for y in x]
    result = []
    for x in new:
        if x not in result:
            result.append(x)
    return result


print(getting_unique(b))

"""
"""

# Model : big grams model.

# 184. Write a Python program to form Bigrams of words in a given list of strings.
# From Wikipedia:
# A bigram or digram is a sequence of two adjacent elements from a string of tokens, which are typically letters, syllables, or words. A bigram is an n-gram for n=2.
# The frequency distribution of every bigram in a string is commonly used for simple statistical analysis of text in many applications,
# including in computational linguistics, cryptography, speech recognition, and so on.
# Original list:
a = ['Sum all the items in a list', 'Find the second smallest number in a list']
# Bigram sequence of the said list:
# [('Sum', 'all'), ('all', 'the'), ('the', 'items'), ('items', 'in'), ('in', 'a'), ('a', 'list'), ('Find', 'the'), ('the', 'second'),
#  ('second', 'smallest'), ('smallest', 'number'), ('number', 'in'), ('in', 'a'), ('a', 'list')]


def big_gram(list_obj):
    return [y for x in list_obj for y in zip(x.split(" ")[:-1], x.split(" ")[1:])]   # split()[:-1] ante starting nunchi -1 varaku...
                                                                                     # split()[1:] ante 1 nunchi ending varaku... 


# Doubts : ikkada manam split daggara slicing chesamu... out put list lo tavali kada ?

a) manam chesindi slice iena zip function aa slice chesina list lo nunchi okkoka element ni tesukoni y lo pedutundi....

# [:-1] starting nunchi -1 varsku... -1 excluded -2 varaku.....[1:] ante 1 nunchi ending varaku....

print(big_gram(a))


# example::: for split()[:-1], split()[1:]
# a= "chenchu mahesh"
 
#  print(a.split()[1:])
# print(a.split()[:-1])
 
"""

"""
# Model : decimal to binary list...

# 185. Write a Python program to convert a given decimal number to binary list.
# Original Number: 8
# Decimal number ( 8 ) to binary list:
# [1, 0, 0, 0]
# Original Number: 45
# Decimal number ( 45 ) to binary list:
# [1, 0, 1, 1, 0, 1]
# Original Number: 100
# Decimal number ( 100 ) to binary list:
# [1, 1, 0, 0, 1, 0, 0]


# Exp : idi gurthu pettuko '{0:0b}'.format(number)

def decimal_to_binary(number):
    if number == 1:
        return 1
    return [int(x) for x in '{0:0b}'.format(number)]   # format lo number string formate lo vuntundi... daanni manam int() loki marchukovali...


print(decimal_to_binary(int(input("Enter the number :"))))


"""
"""
# Model : swapping two sub lists in a given list .

# 186. Write a Python program to swap two sublists in a given list.
# Original list:
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Swap two sublists of the said list:
# [0, 6, 7, 8, 9, 3, 4, 5, 1, 2, 10, 11, 12, 13, 14, 15]
# Swap two sublists of the said list:
# [0, 9, 3, 8, 6, 7, 4, 5, 1, 2, 10, 11, 12, 13, 14, 15]

# Exp : ikkada manam sub list ni original list nunchi manam decide cheyyali...start position and end position icchi...

# a, b = b, a (lagane... but ikkada manam a, b place lo slicing lists range pedataham...) 

def swap_list(list_obj):
    list_obj[4:8], list_obj[10:14] = list_obj[10:14], list_obj[4:8]

    return list_obj


print(swap_list(a))

"""
"""
# Model : list of tuples to list of strings.

# 187. Write a Python program to convert a given list of tuples to a list of strings.
# Original list of tuples:
a = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
# Convert the said list of tuples to a list of strings:
# ['red green', 'black white', 'orange pink']
# Original list of tuples:
b = [('Laiba', 'Delacruz'), ('Mali', 'Stacey', 'Drummond'), ('Raja', 'Welch'), ('Saarah', 'Stone')]
# Convert the said list of tuples to a list of strings:
# ['Laiba Delacruz', 'Mali Stacey Drummond', 'Raja Welch', 'Saarah Stone']

# Exp : list a lo anni tuples same length lo vunnai....  Normal manaki telisina method raste chalu....
# but list b lo matram different length's lo vunnai... but ikkada koncham critical..


def list_of_tuples_to_lists_of_strings(list_obj):
    return [x+y for x, y in list_obj]     # here we no need to convert x, y to str bcoz it is already in str formate.


# print(list_of_tuples_to_lists_of_strings(a))


def uneven_length_tuples_to_list_of_strings(list_obj):
    new_list = []
    for x in list_obj:
        new_list += (' '.join(y for y in x)for x in list_obj)   # tuple length uneven ga vunte manam += join function vaadali...
    return new_list                                              # for every string in tuple join string...                    


print(uneven_length_tuples_to_list_of_strings(b))

"""
"""
# 188. Write a Python program to sort a given list of tuples on specified element.
# Original list of tuples:
a = [('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
# Sort on 1st element of the tuple of the said list:
#  [('item1', 11, 24.5), ('item2', 10, 10.12), ('item3', 15, 25.1), ('item4', 12, 22.5)]
# Sort on 2nd element of the tuple of the said list:
# [('item2', 10, 10.12), ('item1', 11, 24.5), ('item4', 12, 22.5), ('item3', 15, 25.1)]
# Sort on 3rd element of the tuple of the said list:
# [('item2', 10, 10.12), ('item4', 12, 22.5), ('item1', 11, 24.5), ('item3', 15, 25.1)]


# Exp : manam ikkada ichedi index kaadu position so manaki index kavali ante manam position nunchi -1 ni tesi veyyali...

def sort_using_position(list_obj, position):
    return sorted(list_obj, key=lambda x: x[position-1], reverse=False)


print(sort_using_position(a, int(input("Enter the specify the position : "))))

"""
"""
# Model : first element to last last element to first....

# 189. Write a Python program to shift last element to first position and first element to last position in a given list.
# Original list:
a = [1, 2, 3, 4, 5, 6, 7]
# Shift last element to first position and first element to last position of the said list:
# [7, 2, 3, 4, 5, 6, 1]
# Original list:
b = ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']


# Shift last element to first position and first element to last position of the said list:
# ['f', 'd', 'f', 'd', 's', 's', 'd', 's']


# By using slicing model :::

def position_change(list_obj):
    return [list_obj[-1]] + list_obj[1:len(list_obj) - 1] + [list_obj[0]]  # ikkada list_obj[-1], list_obj[0] anedi element's list_obj[1:len(list_obj)] oka list
    # soo.... manam element ni list tho add cheyyakudadu...danni list loki marchi add cheyyali.
    # ikkada length nunchi length ani iste adi(ex: len = 6 anukundam slice ending lo adi 5 avutundi so last element ni access chestundi...---
    # manaki last element access cheyyanavasaramledu last element iis replaced by first element..so manam last before element ni access cheyyali..--
    # danike manam length-1 chesam


print(position_change(a))


# Very very important......

# pop() : it will remove and return specific index position value...

def position_by_pop(list_obj):
    x = list_obj.pop(0)  # ikkada oka element tesesam length okati thakkuva iendi
    y = list_obj.pop(-1)  # ikkada malli inko element tesesam langth malli okati thakkuva iendi...
    list_obj.insert(0, y)  # ikkada length okati perigindi...
    list_obj.insert(len(list_obj), x)  # ante last place lo manam insert cheyyali..so manam length tesukunnam...it will insert element at last
    return list_obj

# last lo element pettali ante len(list_obj)

print(position_by_pop(a))

"""
"""
# 190. Write a Python program to find the specified number of largest products from two given list, multiplying an element from each list.
# Original lists:
a =[1, 2, 3, 4, 5, 6]
b =[3, 6, 8, 9, 10, 6]
# 3 Number of largest products from the said two lists:
# [60, 54, 50]
# 4 Number of largest products from the said two lists:
# [60, 54, 50, 48]


# Exp: sorted function vaadi manam ee code ni solve cheyyochu... 1. sorted function lo list_obj ga product ni enter chesi reverse true pettamu ante--

# product's value decending order lo vastundi...sorted return list kabatti manam slice vaadi enni kabvalante anni list loki extract cheyyochu...

# sorted lo list_obj ga manam comprehension ni use chesi... products ni pettali...


def largest_prod(list_obj1, list_obj2, specified_numbers):
    return sorted([x*y for x in list_obj1 for y in list_obj2], reverse=True)[:specified_numbers]

# [x*y for x in list_obj1 for y in list_obj2] >>>>> this part returns the product of x*y elements in list form...


print(largest_prod(a, b, int(input("Enter the specified_numbers :"))))

"""

"""
# 191. Write a Python program to find the maximum and minimum value of the three given lists.
# Original lists:
a = [2, 3, 5, 8, 7, 2, 3]
b = [4, 3, 9, 0, 4, 3, 9]
c = [2, 1, 5, 6, 5, 5, 4]
# Maximum value of the said three lists:
# 9
# Minimum value of the said three lists:
# 0

# Exp: logic: ee mudu lists ni add chesi normal ga ela iehe kaunukuntamo alane kaunkkovali..


def finding_min_with_three_lists(list_obj1, list_obj2, list_obj3):
    new_list = list_obj1+list_obj2+list_obj3
    max_value = new_list[0]
    min_value = new_list[0]
    for x in new_list:
        if x > max_value:
            max_value = x
        elif x < min_value:
            min_value = x
    return 'The maximum value of given three lists is : {}\nThe minimum value of given three lists is : {}'.format(max_value, min_value)


print(finding_min_with_three_lists(a, b, c))

"""

"""

# V.imp model

# Model : list of tuples lo manam str type ni remove cheyyali...

# 192. Write a Python program to remove all strings from a given list of tuples.
# Original list:
a = [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
# Remove all strings from the said list of tuples:
# [(100,), (80,), (90,), (88, 89), (90, 92)]


Exp : ikkada list of tuples lo manam str ni remove chesi migatha vi pettali...

# list lo vunde prathi tuple ni extract chesi danni tuple() constructor lo type check cheyyali...

# kinda ichina logic laga tuple() constructor lo filter chestene manaki correct output vastundi ...ledante every element saparate ga single tuple lo vastundi...

def remove_str_in_list_of_tuples(list_obj):
    return [tuple(y for y in x if type(y) != str)for x in list_obj]    


print(remove_str_in_list_of_tuples(a))


"""
"""
# Model : finding the dimentions of an array(matrix)

# 193. Write a Python program to find the dimension of a given matrix.
# Original list:
a = [[1, 2], [2, 4]]
# Dimension of the said matrix:
# (2, 2)
# Original list:
b = [[0, 1, 2], [2, 4, 5]]
# Dimension of the said matrix:
# (2, 3)
# Original list:
c = [[0, 1, 2], [2, 4, 5], [2, 3, 4]]
# Dimension of the said matrix:
# (3, 3)


# Exp : row = list yokka length len(list_obj)
#       column  = number of elements in the row  len(list_obj[0]) ....understand this concept...


def dimentions_of_matrix(list_obj):
    return 'The dimentions of a matrix is : {}X{}'.format(len(list_obj), len(list_obj[0]))


print(dimentions_of_matrix(c))

"""
"""
# Model : sum of  uneven length of a nested lists.


# 194. Write a Python program to sum two or more lists, the lengths of the lists may be different.
# Original list:
a = [[1, 2, 4], [2, 4, 4], [1, 2]]
# Sum said lists with different lengths:
# [4, 8, 8]
# Original list:
b = [[1], [2, 4, 4], [1, 2], [4]]
# Sum said lists with different lengths:
# [8, 6, 4]


def add_uneven(list_obj):
    return list(zip(sum, list_obj))


print(add_uneven(a))

"""
"""
# Model : traverse element in reverse order.

# 195. Write a Python program to traverse a given list in reverse order, also print the elements with original index.
# Original list:
a = ['red', 'green', 'white', 'black']
# Traverse the said list in reverse order:
# black
# white
# green
# red
# Traverse the said list in reverse order with original index:
# 3 black
# 2 white
# 1 green
# 0 red


# positive_index : positive index access cheyyali ante range(len(list_obj)) pedithe saripotundi....negative index ni access cheyyali ante range(1, len(list_obj)+1)

# range lo okati nunnchi start chesi length ki okati add cheyyali...


def traverse_reverse(list_obj):
    for i in range(1, len(list_obj)+1):  # NOTE : reverse order lo print cheyyali ante range() lo 1 nunchi start avvali and end lo length ki +1 add cheyyali....
        print(list_obj[-i])


# traverse_reverse(a)

# W3 method:

# for i in reversed(a):
#     print(i)

# My method:::

def reversed_with_index(list_obj):
    i = len(list_obj)-1   # -1 ani enduku pettamu ante positive index ki , length ki okati thakkuvaga vuntundi anduvalla...
    for x in range(1, len(list_obj)+1):
        print(i, list_obj[-x])
        i -= 1  # every time manam okati thaginchali ....ledante same index vastundi...

"""

"""
# Model : moving specific element to the end of the list.

# 196. Write a Python program to move a specified element in a given list.
# Original list:
a = ['red', 'green', 'white', 'black', 'orange']
# Move white at the end of the said list:
# ['red', 'green', 'black', 'orange', 'white']
# Original list:
b = ['red', 'green', 'white', 'black', 'orange']
# Move red at the end of the said list:
#  ['green', 'white', 'black', 'orange', 'red']
# Original list:
c = ['red', 'green', 'white', 'black', 'orange']
# Move black at the end of the said list:
# ['red', 'green', 'white', 'orange', 'black']


# pop() method lo index matrame ivvali...

# insert() method lo mundu manam index positin ichi tharuvatha element ivvali.... guddi_gurthu::: insert ante illu >>> nelani batti illu kattali...

# nela anedi index illu anedi element....so first nela tharuvatha illu....(jagananna housing colony)

def remove_specific_element_to_end_of_list(list_obj, element):
    ele = list_obj.pop(list_obj.index(element))   # it removes specific element based on the index() method and return it...
    list_obj.insert(len(list_obj), ele)
    return list_obj


print(remove_specific_element_to_end_of_list(a, eval(input("Enter the element :"))))


"""
"""
# Model : average of list of list's with different lengths....

# 197. Write a Python program to compute the average of nth elements in a given list of lists with different lengths.
# Original list:
a = [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# Average of n-th elements in the said list of lists with different lengths:
# [4.8, 5.8, 6.8, 8.0, 11.0]

# Exp: zip_longest function is used for the uneven length objects.

import itertools

def average(list_obj):
    return sum([i for i in list_obj if i != None])/len(list_obj)   
    
# Note :::--  ikkada None ni remove cheyyakapothe zip longest function lo length thakkuvaga vunna elements place lo None vastundi...None ni manam 

# add cheyyalemu kada anduvalla... None ni remove cheyyali....


print(list(map(average, itertools.zip_longest(*a))))

"""

"""
# Model : comparing the both lists and print the matching values index value.



# 198. Write a Python program to compare two given lists and find the indices of the values present in both lists.
# Original lists:
a = [1, 2, 3, 4, 5, 6]
b = [7, 8, 5, 2, 10, 12]
# Compare said two lists and get the indices of the values present in both lists:
# [1, 4]
# Original lists:
c = [1, 2, 3, 4, 5, 6]
d = [7, 8, 5, 7, 10, 12]
# Compare said two lists and get the indices of the values present in both lists:
# [4]
# Original lists:
e = [1, 2, 3, 4, 15, 6]
f = [7, 8, 5, 7, 10, 12]
# Compare said two lists and get the indices of the values present in both lists:
# []


# Exp : mundu manam common elements ni saparate cheyyali... tharuvatha comomon element's ki index kanukkovali...


def printing_matching_value_index(list_obj1, list_obj2):
    matching = [x for x in list_obj1 if x in list_obj2]
    matching_elements_index = []
    for x in matching:
        matching_elements_index.append(list_obj1.index(x))
    return matching_elements_index


# print(printing_matching_value_index(e, f))


# W3 method by using enumerate function....

def matching(list_obj1, list_obj2):
    return [x for x,el in enumerate(list_obj1) if el in list_obj2]


print(matching(a, b))

"""
"""
# Model : convertion of unicode to string...

# 199. Write a Python program to convert a given unicode list to a list contains strings.
# Original lists:
a = [u'S001', u'S002', u'S003', u'S004']
# Convert the said unicode list to a list contains strings:
# ['S001', 'S002', 'S003', 'S004']
  
#Exp : This is unicode string : [u'S001', u'S002', u'S003', u'S004'] 
  

def conversion_uni_to_str(list_obj):
    return [str(x) for x in list_obj]


print(conversion_uni_to_str(a))
"""
"""
# model : paring up consicutive links....

# 200. Write a Python program to pair up the consecutive elements of a given list.
# Original lists:
a =[1, 2, 3, 4, 5, 6]
# Pair up the consecutive elements of the said list:
# [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
# Original lists:
b = [1, 2, 3, 4, 5]
# Pair up the consecutive elements of the said list:
# [[1, 2], [2, 3], [3, 4], [4, 5]]


# Exp: manam index position adaharam   ga access chestam ....ikkada purthi length isthe last element kada i+1 ki out of range vastundi...---

# so manam length anedi -1 chestamu...


def pairing_up_con(list_obj):
    return [[list_obj[i], list_obj[i+1]] for i in range(len(list_obj)-1)]


print(pairing_up_con(b))

"""
"""
# Model : checking string contains the list elements.....

# 201. Write a Python program to check if a given string contains an element, which is present in a list.
# The original string and list:
string1 = 'https://www.w3resource.com/python-exercises/list/'
a =['.com', '.edu', '.tv']
# Check if https://www.w3resource.com/python-exercises/list/ contains an element, which is present in the list ['.com', '.edu', '.tv']
# True
# The original string and list: https://www.w3resource.net
string2 = 'https://www.w3resource.net'
b = ['.com', '.edu', '.tv']
# Check if https://www.w3resource.net contains an element, which is present in the list ['.com', '.edu', '.tv']
# False


# Exp: ichina string list lo vunna  elements lo edo okati vunna True ledante False...

def checking(str_obj, list_obj):
    return bool([x for x in list_obj if x in str_obj])   # bool of emepty anything is false... bool([]) >>> False...
 

print(checking(string2, b))
"""
"""
# Model : indeces of all None

# 202. Write a Python program to find the indexes of all None items in a given list.
# Original list:
a = [1, None, 5, 4, None, 0, None, None]
# Indexes of all None items of the list:
# [1, 4, 6, 7]

# Exp: ekkadekkada None vundo daani index value return cheyyali.... deniki while loop perfect....


# my mistake....i+=1 anedi if conditio lo ivvakudadu ala iste i value None iethe adi incriment avutundi ledante ledu ....ikkada first element ---

# first element 1 so i value increment avvadu ...loop infinite loop loki vellipotundi.... 

# always give incremented value in only while loop not in any condition...

def finding_index(list_obj):
    index_list =[]
    i = 0
    while i < len(list_obj):  # i anedi list length kanna thakuvaga vunte kindi code of block runchey...
        if list_obj[i] is None:
            index_list.append(i)
        i += 1           # increment value must be given under while block not in if condition               
    return index_list


print(finding_index(a))

"""
"""
# 203. Write a Python program to join adjacent members of a given list.
# Original list:
a = ['1', '2', '3', '4', '5', '6', '7', '8']
# Join adjacent members of a given list:
# ['12', '34', '56', '78']
# Original list:
b = ['1', '2', '3']
# Join adjacent members of a given list:
# ['12']


# Exp : oka list lo elements rendu renditini oka pair cheyyali... 1st,2nd element kalipi okati, 3rd,4th kalipi okati,5th,6th kalipi okati...

# ikkada range length function vaadi index adharamga manam kaluputhamu...

# rangefunction lo step kachithamga vadali ledante 1st+2nd, 2nd+3rd, 3rd+4th ani add avutundi....so range 2 pettali appude prathi sari index skip avutundi...

# Note : compulsari step 2 pettali appude 0th nunchi 2nd ki, 2nd nunchi 4th ki index value velthuvuntundi.... 


def join_adj(list_obj):
    return [list_obj[i]+list_obj[i+1]for i in range(0, len(list_obj)-1, 2)]


print(join_adj(b))

"""
"""
# Model : checking every 0th character in the elements of the list is same or not ?

# 204. Write a Python program to check if first digit/character of each element in a given list is same or not.
# Original list:
a = [1234, 122, 1984, 19372, 100]
# Check if first digit in each element of the said given list is same or not!
# True
# Original list:
b =[1234, 922, 1984, 19372, 100]
# Check if first digit in each element of the said given list is same or not!
# False
# Original list:
c = ['aabc', 'abc', 'ab', 'a']
# Check if first character in each element of the said given list is same or not!
# True
# Original list:
d = ['aabc', 'abc', 'ab', 'ha']
# Check if first character in each element of the said given list is same or not!
# False


# Exp: list lo vunna prathi element lo 0th index charecter same or not ani check cheyali...

# manam list lo vunna prathi element ni check cheyyali  kabatti all function ni vadali...


def checking_index_element(list_obj):
    return all(str(x)[0] == str(list_obj[0])[0] for x in list_obj)

# Clarity ::: list[0] ante list lo first element str(list[0]) ante 0th index position lo vunde elemnt ni string ga marustundi...str(list_obj[0])[0] ante aa string lo ---

# first element ani ardham ...

# every element ni x rupam lo str ga marchi daani first element ni index dwara check chestunnam...equal ki right side vundedi constant...left side vundedi marutundi...

# equal ki rendu sides manam str ga marchali..


print(checking_index_element(a))
"""
"""
# Model : index of elements which satisfies the condition....

# 205. Write a Python program to find the indices of elements of a given list, greater than a specified value.
# # Original list:
a =[1234, 1522, 1984, 19372, 1000, 2342, 7626]
# Indices of elements of the said list, greater than 3000
# [3, 6]
# Original list:
b=[1234, 1522, 1984, 19372, 1000, 2342, 7626]
# Indices of elements of the said list, greater than 20000
# []


def finding_indeces(list_obj, specified_value):
    i = 0     # initializing the index varible...
    index_list = []
    while i < len(list_obj):
        if list_obj[i] > specified_value:
            index_list.append(i)
        i+=1   # incrimenting of i is always outside of the if condition but inside of while loop
    return index_list


print(finding_indeces(b, int(input("Enter the value :"))))

"""
"""
# Model : removing additional spaces.

# 206. Write a Python program to remove additional spaces in a given list.
# Original list:
a = ['abc ', ' ', ' ', 'sdfds ', ' ', ' ', 'sdfds ', 'huy']
# Remove additional spaces from the said list:
# ['abc', '', '', 'sdfds', '', '', 'sdfds', 'huy']


# Exp: elemnt lo ' ' vunte '' denni return chey ledante normal element ni return chey...

def removing_additional_spaces(list_obj):
    return ['' if i == ' ' else i for i in list_obj]


print(removing_additional_spaces(a))


"""

"""
# Model : common tuples between two two lists

# 207. Write a Python program to find the common tuples between two given lists.
# Original lists:
a = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
b = [('red', 'green'), ('orange', 'pink')]
# Common tuples between two said lists
# [('orange', 'pink'), ('red', 'green')]
# Original lists:
c = [('red', 'green'), ('orange', 'pink')]
d = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
# Common tuples between two said lists
# [('orange', 'pink'), ('red', 'green')]



# By using list_comp


def common_tupples(list_obj1, list_obj2):
    return [x for x in list_obj1 if x in list_obj2]


print(common_tupples(c, d))


# By uisng set_method..

def common_using_set(list_obj1, list_obj2):
    return set(list_obj1) & set(list_obj2)


print(common_using_set(a, b))

"""

"""
# Model : sum of consecutive numbers and avg also


# 208. Sum a list of numbers. Write a Python program to sum the first number with the second and divide it by 2, then sum the second with the third and divide by 2,
# and so on.
# Original list:
a = [1, 2, 3, 4, 5, 6, 7]
# Sum the said list of numbers:
# [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
# Original list:
b = [0, 1, -3, 3, 7, -5, 6, 7, 11]
# Sum the said list of numbers:
# [0.5, -1.0, 0.0, 5.0, 1.0, 0.5, 6.5, 9.0]

# Exp : first number and next number ni kalipi add cheyyali and ee mothanni 2 tho devide cheyyali...ala pothu vundali....


def sum_avg(list_obj):
    return [(list_obj[i]+list_obj[i+1])/2 for i in range(len(list_obj)-1)]


print(sum_avg(b))

"""
"""
# Vimp logic

# Model : count the group of non zero numbers.

# 209. Write a Python program to count the number of groups of non-zero numbers separated by zeros of a given list of numbers
# Original list:
a = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
# Number of groups of non-zero numbers separated by zeros of the said list: 4


# Exp : zeros tho saparate iyye number group kanukkovali.... so manam logic gurthupettuko >>> previous value zero avvali current number non zero avvali..

# every iteration ki previous value ni current number tho replace cheyyali...>> anthe kadha prathi sari iteration jarigi nappudu current value previous value avutundi...


# Doubt : ikkada manam chustene ardham avutundi...zeros tho saparate iyye groups 4 ani....kaani first group ki previous zero kaadu kada ani doubt ravali

# manam previous value ni zero ga initialize chesam anduvalle count 1 add iendi... ala previuos value ni initialize ceyyakapothe oka group thakkuva vastundi

#  previous value initialize cheyyakpothe first group mundara zeros lekapothe adi add avvadu.... so logic baga gurthu pettuko

def counting_non_zero_group(list_obj):
    count = 0
    previous = 0
    for num in list_obj:
        if previous == 0 and num != 0:
            count += 1
        previous = num
    return count


print(counting_non_zero_group(a))

"""
"""
# Model : sum of non zero groups

# Little complicated...

# 210. Write a Python program to compute the sum of non-zero groups (separated by zeros) of a given list of numbers.
# Original list:
a = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]
# Compute the sum of non-zero groups (separated by zeros) of the said list of numbers: [15, 38, 15, 27]



# Exp : We just traverse the list each element to test for it’s succeeding element to be non-zero value and perform the summation ---
# once we find a next value to be zero and append it in result list.

# prathi element ni traverse cheyyali.... numbers lo zero iyyi vundakudadu... daani next number kuda zero iyyi vundakudadu...then manamu summation--

# cheyyali...manam next value zero vaste appudu aa sum ni list loki append cheyyali...


# conclusion : successiding element (tharuvatha vache element) zero kakapothe sum ki add cheyyali.... succeding element zero iethe sum ni list ki append cheyyali.


def sum_list_of_non_zero_group(list_obj):
    sum_list = []
    sum = 0  #initializing the sum
    for x in list_obj:
        if x == 0:  # x value zero iethe sum ni append cheyyali....
            if sum != 0:   # sum anedi zero iyyi vundakudadu...edo okati iyyi vundali...ledante proper result raadu...
                sum_list.append(sum)   # sum ni append cheyyali...
                sum = 0    # ikkada sum append chesina tharuvatha sum ni append cheyyali.... ledante previous sum group ki add avutundi...to separate every group sum
                # oka group sum ni append chesina tharuvatha next group sum ni zero numchi start cheyyali ledante previous sum ki element add avutundi...
        else:
            sum += x
    return sum_list


print(sum_list_of_non_zero_group(a))

"""
"""
# Model : remove specific element...

# 211. Write a Python program to remove an element from a given list.
# Original list:
a = ['Ricky Rivera', 98, 'Math', 90, 'Science']
# After deleting an element:, using index of the element: [98, 'Math', 90, 'Science']


# Model : by using remove method

def removing_specific_element(list_obj, element):
    list_obj.remove(element)
    return list_obj


# print(removing_specific_element(a, eval(input("Enter the value :"))))


# Model : by using list comprehension

def removing_by_using_list_comp(list_obj, element):
    return [x for x in list_obj if x != element]


# print(removing_specific_element(a, eval(input("Enter the element to remove :"))))

# By using lambda and filter...


def removing_by_lambda(list_obj, element):
    return list(filter(lambda x: x != element, list_obj))


print(removing_by_lambda(a, eval(input("Enter the element :"))))
"""
"""
# Model : removing all except int values....

# 212. Write a Python program to remove all the values except integer values from a given array of mixed values.
# Original list: \
a =[34.67, 12, -94.89, 'Python', 0, 'C#']
# After removing all the values except integer values from the said array of mixed values: [12, 0]

# Normal method..

def removing_all_except_int(list_obj):
    return [x for x in list_obj if type(x) == int]


print(removing_all_except_int(a))


# isinstance(x, type) >>> isintance() method returns only boolen value >>> is it used for type check >>> six>>x so first is element next is type...

def removing_by_using_isinstance(list_obj):
    return [x for x in list_obj if isinstance(x, int)]


print(removing_by_using_isinstance(a))

"""
"""
# 213. Write a Python program to calculate the sum of two lowest negative numbers of a given array of integers.
# An integer (from the Latin integer meaning "whole") is colloquially defined as a number that can be written without a fractional component. For example, 21, 4, 0, and -2048 are integers.
# Original list elements:
a = [-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]
# Sum of two lowest negative numbers of the said array of integers: -27
# Original list elements:
b = [-4, 5, -2, 0, 3, -1, 4, 9]
# Sum of two lowest negative numbers of the said array of integers: -6

# By using sum and sorted


def sum_lowest(list_obj):
    return sum(sorted(list_obj)[:2])


print(sum_lowest(b))


def sum_negative(list_obj):
    result = sorted([x for x in list_obj if x < 0])   # manam ikkkada sorted cheyyakapothe list lo negative elements ea order lo iethe vundo ade order lo vastundi
    return result[0]+result[1]                                          # so compulsory ga sorted vaadali...


print(sum_negative(a))

"""

"""
# 214. Write a Python program to sort a given positive number in descending/ascending order.
# Descending -> Highest to lowest.
# Ascending -> Lowest to highest
# Original Number:
a = 134543
# Descending order of the said number: 544331
# Ascending order of the said number: 133445
# Original Number:
b = 43750973
# Descending order of the said number: 97754330
# Ascending order of the said number: 3345779


def ascending_decending_string_num(number):
    ascending_order = ''.join(sorted([x for x in str(number)], reverse=False))
    descending_order = ''.join(sorted([x for x in str(number)], reverse=True))

    return 'The ascending order of a given number{}\nThe decending order of a given number is {}'.format(ascending_order, descending_order)


print(ascending_decending_string_num(b))

"""
"""
# Very important and merging concept...

# Model : merging two or more uneven length (uneven_length's) of list's to lists of lists...

# 215. Write a Python program to merge two or more lists into a list of lists, combining elements from each of the input lists based on their positions.
# Sample Output:
# After merging lists into a list of lists:
# [['a', 1, True], ['b', 2, False]]
# [['a', 1, True], [None, 2, False]]
# [['a', 1, True], ['_', 2, False]]


# Exp: uneven lenghth kaligina lists vuntundi daantlo index adharamga list of list's ga marchali...

#merge = kalapadam (విలీనం)


# Exp: ikkada manam length equal ga vundedi first merge chestam tharuvatha length ekkuvaga vunna elements ki vaatiki length thakkuvaga vunna pairs ki---

# manam ichhina fill_value vastundi...

# i, k are very important here... 

def merge_two_or_more_uneven(*args, fill_value=None):
    max_length = max([len(x) for x in args])  # ikkada manam * ani loop lo ivvakudadu.
    result_list = [] 
    for i in range(max_length):  # i anedi maximum length samdinchina value...
        result_list.append([args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))]) # k anedi present vunna list yokka value...
    return result_list


print(merge_two_or_more_uneven(['a', 'b'], [1, 2], [True, False, None], fill_value='_'))

"""

"""
# 216 is not understand...

# Model : splitting the list based on the filtering function....

# 217. Write a Python program to split values into two groups, based on the result of the given filtering function. Go to the editor
# Sample Output:

a = ['red', 'green', 'black', 'white']

# [['white'], ['red', 'green', 'black']]


# Exp : ichina list ni function adharam ga split cheyyali....

# New : if if not ( manam ikkkada lambda lo condition ichestamu...so malli list compreshenion lo conditions ivvakudadu)

# 1. fn satisfy chese list_obj anni oka group and fn satisfy cheyyani elements anni inko group...


def splitting_function(list_obj, fn):
    return [[x for x in list_obj if fn(x)], [x for x in list_obj if not fn(x)]]


print(splitting_function(a, lambda d: d[0] == 'w'))


"""

# Model : sort the list based on another list

# Not understanding...

# 218. Write a Python program to sort one list based on another list containing the desired indexes.



Sample Output:
['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
['oranges', 'milk', 'jam', 'eggs', 'bread', 'apples']









