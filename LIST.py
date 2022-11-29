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


def square_matrix(rows, columns):
    matrix = [[int(input("Enter the elements :")) for j in range(columns)] for i in range(rows)]
    for row in matrix:
        print(' '.join(map(str, row)))
    primary_diagonal = 0
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

# 104. Write a Python program to find the difference between consecutive numbers in a given list.
# Original list:
a = [1, 1, 3, 4, 4, 5, 6, 7]
# Difference between consecutive numbers of the said list:
# [0, 2, 1, 0, 1, 1, 1]
# Original list:
b = [4, 5, 8, 9, 6, 10]
# Difference between consecutive numbers of the said list:
# [1, 3, 1, -3, 4]

# Exp:


def diff_consecutive(list_obj):
    return [list_obj[i+1]-list_obj[i] for i in range(len(list_obj)-1)]


print(diff_consecutive(a))



