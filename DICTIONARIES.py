"""
# 1.Write a Python script to sort (ascending and descending) a dictionary by value.

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}


def sort_ascending(item):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=False))


print(sort_ascending(d))

# code explanation:
# 1. sorted function: this function is used to sort the dictionary items. this function takes 3 parameters iterable, key
# reverse.
# iterable: we have to pass iterable here we passed dict items.
# key: key is important role ... we have to pass function here... normal func or lambda function. specify which index
# value should be sorted for each tuple in the list.
# reverse: True-sort ascending, False-sort descending.
# d.items(): here we have to pass list of tuples for sorting purpose.
# dict() : this dict() function is used to convert those list of tuples to the dictionary again if we not use this
# function the output will be the list of tuples only.


def sort(x):        # normal function for specifying index
    return x[1]


def sort_descending(item):
    return dict(sorted(d.items(), key=sort, reverse= True))


print(sort_descending(d))

"""
"""
# 2. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# method:1


def add_key(dictionary, key, value):
    dictionary[key] = value
    return dictionary


print(add_key({0: 10, 1: 20}, 2, 30))


# method:2 by using update method:

def update_dict(dictionary, item):
    dictionary.update(item)           # formula = d.update(iterable) --- the iterable must be in the form of key value
    return dictionary                                                             # pair otherwise it will raise error


print(update_dict({0: 10, 1: 20}, {2: 30}))
"""
"""
# 3. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def update_dict(dict1, dict2, dict3):     # here we are providing the 3 dict's in a tuple, to iterate one by one
    for dit in (dict2, dict3):                     # we can mention in list's also
        dict1.update(dit)
    return dict1


print(update_dict({1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}))


# model:2
def upadte_dict(dict1, dict2, dict3):
    new_dict = {}
    for dit in [dict1, dict2, dict3]:     # we can mention in tuples also
        new_dict.update(dit)

    return new_dict


print(upadte_dict({1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}))

"""

"""
# 4. Write a Python script to check whether a given key already exists in a dictionary.


# method:1
def check_key(dictionary, key):
    return key in dictionary.keys()  # we can mention here dict.keys() or only dict...by default it search only keys


print(check_key({"a": 2, "b": 3, "c": 4}, "a"))

# method:2

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')


is_key_present(5)
is_key_present(9)
"""
"""
# 5.Write a Python program to iterate over dictionaries using for loops.


def dict_iteration(dictionary):
    for dict_key, dict_value in dictionary.items():  # This is the formal way of iterating through dictionary 
        print(dict_key, '->', dict_value)


dict_iteration({'a': 1, 'b': 2, 'c': 3})
"""
"""
# 6. Write a Python script to generate and print a dictionary
# that contains a number (between 1 and n) in the form (x, x*x)
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


def create_dict(n):
    return {x: x*x for x in range(1, n+1)}  # Dict comprehension is best method


print(create_dict(25))
"""
"""
# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys. Go to the editor
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

method:1 dict comprehension
def create_dict(n):
    return {x: x*x for x in range(1, n+1)}


print(create_dict(15))

method:2 Normal method

d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)  
"""
"""
# 8. Write a Python script to merge two Python dictionaries.


def merge_dict(dict1, dict2):
    new_dict = dict1.copy()
    new_dict.update(dict2)
    return new_dict


print(merge_dict({'a': 100, 'b': 200}, {'x': 300, 'y': 200}))


# To merge more dictionaries

def merge_more_dict(*dicts):
    new_dict = dict()
    for dit in dicts:
        new_dict.update(dit)
    return new_dict


print(merge_more_dict({'a': 100, 'b': 200}, {'x': 300, 'y': 200},{'w': 45, 't': 78} ))

"""
"""
# 9.Write a Python program to iterate over dictionaries using for loops.


def iterate_dict(dictionary):
    for key, value in dictionary.items():   # when ever we are iterating dict we must use d.items other wise it will
        print(key, '->', value)                                                                    # raise an error


iterate_dict({'x': 300, 'y': 200})


# W3method:

d = {'Red': 1, 'Green': 2, 'Blue': 3}
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key])

"""

"""
# 10. Write a Python program to sum all the items in a dictionary.

# explanation : sum of all items means add all values in the dictionary

def sum_items(dictionary):
    total_value = 0
    for x in dictionary.values():
        total_value += x

    return total_value


print(sum_items({'a': 1, 'b': 2, 'c': 3}))

"""

"""
# 11. Write a Python program to multiply all the items in a dictionary

def multiply_item(dictionary):
    mul_val = 1
    for x in dictionary.values():
        mul_val *=x
    return mul_val


print(multiply_item({"a": 1, "b": 2}))

# W3method

my_dict = {'data1':100,'data2':-54,'data3':247}
result=1
for key in my_dict:    
    result=result * my_dict[key]

print(result)

"""
"""
# 12. Write a Python program to remove a key from a dictionary.


def remove_key(dictionary, key_name):
    dictionary.pop(key_name)
    return dictionary


print(remove_key({'data1': 100, 'data2': -54, 'data3': 247}, 'data3'))

W3 school:

myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict: 
    del myDict['a']
print(myDict)

"""












