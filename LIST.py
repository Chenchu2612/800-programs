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
































