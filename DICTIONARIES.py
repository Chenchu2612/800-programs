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

"""
# 13. Write a Python program to map two lists into a dictionary.

keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']


# method:1 by using build_in function.

def create_dict_using_inbuilt(dict1, dict2):
    return dict(zip(keys, values))


print(create_dict_using_inbuilt(keys, values))


# method:2 by using traditional approach

def create_dict_traditional(dict1, dict2):
    new_dict = {}
    for i in range(len(keys)):  # or we can mention key = keys[i], value = values[i]
        new_dict[keys[i]] = values[i]
    return new_dict


print(create_dict_traditional(keys, values))


# method:3 by using dict_comprehension

def create_dict_comp(dict1, dict2):
    return {keys[i]: values[i] for i in range(len(keys))}


print(create_dict_comp(keys, values))

# ***method:4 by using map function

res = dict(map(lambda i,j : (i,j) , keys,values))
"""
"""
# 14. Write a Python program to sort a given dictionary by key.
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

def sort_by_key(item1):
    return dict(sorted(color_dict.items(), key=lambda x: x[0], reverse=False))


print(sort_by_key(color_dict))
"""
"""
# 15. Write a Python program to get the maximum and minimum value in a dictionary.
my_dict = {'x': 500, 'y': 5874, 'z': 560}
print(my_dict.keys())  # it will returns the value as  dict_keys(['x', 'y', 'z'])


def max_min_keys(item):
    max_key = max(item.keys(), key=lambda x: my_dict[x])
    min_key = min(item.keys(), key=lambda x: my_dict[x])
    print("The maximium value from the dictionary is: " ,item[max_key], "the minimum value:", item[min_key])


max_min_keys(my_dict)

model: 2
a= max(my_dict.values())
print(a)

"""
"""
# ***16.Write a Python program to get a dictionary from an object's fields.

class Employee:
    def __init__(self):
        self.name  = 'chenchaiah'
        self.salary = '1200000'
        self.office_area = 'Banglore'
        self.roll = 'Data_analysist'

    def status(self):
        pass


obj = Employee()
print(obj.__dict__)
"""
"""
# 17. Write a Python program to remove duplicates from Dictionary.
student_data = {
                'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
                'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']},
                'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
                'id4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']},
                }


def remove_duplicate_values(item):
    result_dict = {}
    for key, values in student_data.items():
        if values not in result_dict.values():
            result_dict[key] = values    # Or we can use result_dict.update({key:values})
    return result_dict


print(remove_duplicate_values(student_data))
"""
"""
# VERY_IMPORTANT_NOTE:

# d.keys() = It will returns the dict_keys([list_of_all_keys])
# d.values() = It will returns the dict_values([list_of_all values])
# d.items() = it will returns the dict_items([(item1), (item2), (item3), (item4)])... each item contains key,value.
"""
"""
# 18. Write a Python program to check a dictionary is empty or not

# Method:1


def check_len_dict(item):
    if len(item) == 0:
        return True
    return False


# method:2 By using bool function

def check_dictionary(item):
    return bool(item)


print(check_dictionary({1: 'a'}))
"""
"""
# 19. Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

def create_new_dict(dictionary1, dictionary2):
    new_dict = d2
    for key, value in dictionary1.items():
        if key in new_dict:
            new_dict[key]= new_dict[key]+value
        else:
            new_dict[key]=value

    return new_dict

print(create_new_dict(d1, d2))
"""

"""
# 20. Write a Python program to print all unique values in a dictionary.
# Sample Data: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}


def add_unique(item):
    unique_values=set()
    for x in item:
        for key, values in x.items():
            unique_values.add(values)

    return unique_values

print(add_unique([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]))

"""

"""
# 21. Write a Python program to create and display all combinations of letters, selecting each letter from a different
# key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd


Sample_data = {'1': ['a', 'b'], '2': ['c', 'd']}


def combinations_values(dict_item):
    l1, l2 = dict_item.values()              # it assigns first key value to l1 and second key value to l2
    for i in l1:
        for j in l2:                # inner loop will execute fully for each item in the outer loop
            print(i+j)


combinations_values(Sample_data)

"""
"""
# 22. Write a Python program to find the highest 3 values of corresponding keys in a dictionary

my_dict = {'a': 500, 'b': 5874, 'c': 560,'d': 400, 'e': 5874, 'f': 20}
# output = ['b', 'e', 'c']


def highest_three_values_corresponding_keys(dict_item, n):
    a = [i for i, j in sorted(dict_item.items(), key= lambda x:x[1], reverse =True)[:n]]  # note [:n] inside or out side no problem.
    return a


print(highest_three_values_corresponding_keys(my_dict, 3))


"""
"""
# 23. Write a Python program to combine values in python list of dictionaries.
Sample_data= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

old_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]


def adding_item_values(dit_item):
    new_dict = {}
    for dit in old_list:
        if dit['item'] not in new_dict:                 # dit['item'] = item1 ...., dit['amount'] = amount
            new_dict[dit['item']] = dit['amount']
        else:
            new_dict[dit['item']] += dit['amount']
    return new_dict


print(adding_item_values(Sample_data))

"""
"""
# 24. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

# method:1 this is traditional approach:

string= "w3resource"


def count_letters(item):
    new_dict = {}
    for x in string:
        if x not in new_dict:
            new_dict[x]=1
        else:
            new_dict[x]+=1
    return new_dict


print(count_letters(string))


# method: 2 dictionary-comp

new_dict = {x: string.count(x) for x in string}  # string.count(letter) = it counts the number of times it occurs. 

print(new_dict)

"""
# 25. Write a Python program to print a dictionary in table format.
# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# C1 C2 C3
# 1 5 9
# 2 6 10
# 3 7 11

# next time
"""

method: sum function
# 26. Write a Python program to count the values associated with key in a dictionary.
student = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

print(sum(d['id'] for d in student), sum(x['success'] for x in student))      # we have to write inside sum function otherwise it will raise an error
"""
"""
# 27. very_very_very_very_very_very_very important problem

# Write a Python program to convert a list into a nested dictionary of keys.

num_list = [1, 2, 3, 4]
# {1: {2: {3: {4: {}}}}}


def adding_dict_to_nested_dict(item):
    new_dict = current_dict = {}  # in this logic we taken 2 dictionaries
    for x in num_list:
        current_dict[x] = {}
        current_dict = current_dict[x]  # every time we have to add to nested dictionary that's why this statement.
    return new_dict


print(adding_dict_to_nested_dict(num_list))
"""
"""
# 28. Write a Python program to sort a list alphabetically in a dictionary.

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

# output={'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}

Note: where ever we mention k, v we must mention d.items() , otherwise error will come


def sorted_list_in_dictionary(item):
    return {k: sorted(v,reverse= False) for k, v in item.items()}  # we used sorted function here  , here no lambda function bcoz no nested list here
                                                                   # we can mention reverse = True/False for ascending and decending pursose
 

print(sorted_list_in_dictionary(num))
"""
"""
# 29. Write a Python program to remove spaces from dictionary keys
Original_dictionary= {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}


def remove_spaces_from_keys(dit_item):
    return {key.replace(" ", ""): value for key, value in dit_item.items()}     # Note: there is no remove method in strings only replace method
                                                                                # string is immutable
                                                                                # string.replace(old_value, new_value)


print(remove_spaces_from_keys(Original_dictionary))
"""
"""
# 30. Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3


def top_three_items(dict_obj, n):
    sorted_dict = sorted(dict_obj.items(), key= lambda x: x[1], reverse=True)[:n]   # it always returns key,value pair in list in a tuple
    for x, y in sorted_dict:                   # sorted function always returns list.
        print(x, y)
 

top_three_items({'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}, 3)
"""
"""
# 31. Write a Python program to get the key, value and item in a dictionary.
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key  value  count
# 1     10      1
# 2     20      2
# 3     30      3
# 4     40      4
# 5     50      5
# 6     60      6

# explanation : here they did not mention items , they mention item here so item is nothing but item1, item2, item3 etc...,


# method:1
def key_value_item(dict_obj):
    print("count", "key", "value")
    for count, (key, value) in enumerate(dict_obj.items(), 1):  # enumerate function takes iterable as input and adds the counter to the iterable
        print(count, "    ", key, " ", value)                  # returns the enumerate object ...by default it starts counting from 0


key_value_item({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60})


# method:2 Traditional approach

def key_values_item(dict_obj):
    print("key", "value", "count")
    count = 1
    for i, j in dict_obj.items():
        print(i," ", j, " ",count)
        count = count+1

key_values_item({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60})
"""
"""
# 32. Write a Python program to print a dictionary line by line.
students = {'Aex': {'class': 'V', 'rolld_id': 2}, 'Puja': {'class': 'V', 'roll_id': 3}}

# output:
# Aex
# class : V
# rolld_id : 2
# Puja
# class : V
# roll_id : 3   

for key, value in students.items():          # Note : if you type for x in dictionary it takes only keys ...same way if x in dictionary means
    print(key)                               # it only searches the keys ....(same functionality for.....for and if)
    for key1, value1 in value.items():
        print(key1, ":", value1)

"""

"""
# 33. Write a Python program to check multiple keys exists in a dictionary.

# Explanation : multiple keys exists = all passed keys are exists in the dictionary or not .... multiple keys means not duplicate keys
# by default dictionary does not allows multiple keys.

def all_keys(dict_obj, *keys):   # *args in function
    return all(x in dict_obj for x in keys)   # we will never write if in all function ..... Syntax error will come


print(all_keys({'name': 'Alex','class': 'V','roll_id': '2'}, 'name', 'roll_id'))

"""
"""
# 34. Write a Python program to count number of items in a dictionary value that is a list.
# dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# count=5


def count_items_in_the_values_in_dict(dict_obj):
    total_num_of_items = 0
    for x in dict_obj.values():    # dict.values() returns the = dict_values([['subj1', 'subj2', 'subj3'], ['subj1', 'subj2']])
        total_num_of_items += len(x)
    return total_num_of_items


print(count_items_in_the_values_in_dict({'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}))

"""
"""
# 35. Write a Python program to sort Counter by value.
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]


def sorted_dict(dict_item):
    return sorted(dict_item.items(), key= lambda x:x[1], reverse=True)


print(sorted_dict({'Math':81, 'Physics':83, 'Chemistry':87}))
"""
"""

# very important:
36. Write a Python program to create a dictionary from two lists without losing duplicate values.
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})



def new_dict(list1, list2):
    dit = {}
    for i in range(len(list1)):
        dit[list1[i]] = {list2[i]}
    return dit


print(new_dict(['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]))


# this is original method:

from collections import defaultdict
class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
id_list = [1, 2, 2, 3]
temp = defaultdict(set)
print(temp)
for c, i in zip(class_list, id_list):
    temp[c].add(i)
print(temp)

"""

"""
#37. Write a Python program to replace dictionary values with their average.

student_details= [
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]
# output= [{'subject': 'math', 'id': 1, 'V+VI': 76.0}, {'subject': 'math', 'id': 2, 'V+VI': 73.5}, {'subject': 'math',
#                                                                                                 'id': 3, 'V+VI': 80.5}]


def dict_values_average(list_obj):
    for dit in list_obj:                
        n1 = dit.pop('V')
        n2 = dit.pop('VI')
        dit['V+VI'] = (n1+n2)/2           # Here we no need to append dict_obj to list_obj ...Here we are modifying the list_object

    return list_obj


print(dict_values_average(student_details))
"""
"""
#38. Write a Python program to match key values in two dictionaries.
# x = {'key1': 1, 'key2': 3, 'key3': 2}
# y = {'key1': 1, 'key2': 2}

# method:1 traditional approach

def matching_dict(dict1, dict2):
    for x in dict1.items():
        if x in dict2.items():
            return '{} is present in both dicts'.format(x)
    return 'No matching'


print(matching_dict({'key1': 1, 'key2': 3, 'key3': 2}, { 'key2': 3}))

# method :2 with any() function


def chenchu(dict1, dict2):

    return any(x in dict2.items() for x in dict1.items())


print(chenchu({'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 4, 'key2': 2}))
"""
"""
# very very very imp

# 39. Write a Python program to store a given dictionary in a json file.

dict_obj = {"students":[{"firstName": "Nikki", "lastName": "Roysden"},
               {"firstName": "Mervin", "lastName": "Friedland"},
               {"firstName": "Aron ", "lastName": "Wilkins"}],
    "teachers":[{"firstName": "Amberly", "lastName": "Calico"},
                {"firstName": "Regine", "lastName": "Agtarap"}]}


import json

with open('chenchu', "w") as f:
    json.dump(dict_obj, f, indent=4)   #for dumping purpose (python to json) no need to create object 
print(type(f))
with open('chenchu', 'r') as f:
    dit=json.load(f)                   # for loading purpose (json to python) we need to create an object
print(dit)

"""
"""
# 40. Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively.
# Access the fifth value of each key from the dictionary.
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]


# note : using of range function is very important here.
def making_dict():   # if we type x = range(11, 21) then x:range(11, 21) will come so we have to convert to list
    dict1 = dict(x=list(range(11, 21)), y=list(range(21, 30)), z=list(range(31, 40)))
    print(dict1)
    for key, value in dict1.items():
        print(value[4])
        print(key, "has value", value)

making_dict()
"""
"""
# 41. Write a Python program to drop empty Items from a given Dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

# by using dictionary comprehension : it is a compact way to create new dictionary from the existing dictionary (we can alter existing dict)
old_dict={'c1': 'Red', 'c2': 'Green', 'c3': None} # we are altering old dict
old_dict={key: value for key, value in old_dict.items() if value != None}  # here we can also write if value is not None
print(old_dict)
"""

"""
# 42. Write a Python program to filter a dictionary based on values.
# Original Dictionary:
# dict1 = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}


def filter_dict(dict_obj):
    return {key: value for key, value in dict_obj.items() if value > 170}


print(filter_dict(dict1))
"""

"""
# important_problem

# 43. Write a Python program to convert more than one list to nested dictionary.
# Original strings:
# list1=['S001', 'S002', 'S003', 'S004']
# list2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# list3=[85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

#Note = output is in list formate so use list comprehension

# method:1 traditional zip method
def convertion_of_morethan_one_list_to_nested_dictionary(list1, list2, list3):
    return [{x: {y: z}} for x, y, z in zip(list1, list2, list3)]
print(convertion_of_morethan_one_list_to_nested_dictionary(['S001', 'S002', 'S003', 'S004'],
    ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], [85, 98, 89, 92]))


# method:2 by using range_len function
def lists_to_nested_dict(list1, list2, list3):

    return [{list1[i]:{list2[i]:list3[i]}} for i in range(len(list1))]

print(lists_to_nested_dict(['S001', 'S002', 'S003', 'S004'],
    ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], [85, 98, 89, 92]))


# by using *args method:
def convertion(*lists):
    return [{x:{y:z}}for x, y, z in zip(*lists)]

print(convertion(['S001', 'S002', 'S003', 'S004'],
    ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'], [85, 98, 89, 92]))
"""
"""

# double if conditions very important

# 44. Write a Python program to filter the height and width of students, which are stored in a dictionary.
# Original Dictionary:
d={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}


def filtering_dict_items(dict_obj):
    return {key: value for key, value in d.items() if value[0] > 6 and value[1] >= 70}


print(filtering_dict_items(d))

"""
"""
# 45. Write a Python program to check all values are same in a dictionary.


def check_values(dictionary, n):
    return all(value == n for key, value in dictionary.items())  # no if statement in all() and any() function 


print(check_values({'Cierra Vega': 12, 'Alden Cantrell': 11, 'Kierra Gentry': 12, 'Pierre Cox': 12},11))
"""
"""
# 46. Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
# Original list:
list1=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}


def new_dictionary(list_obj):
    d = {}
    for (key, value) in list1:
        if key not in d:
            d[key]=[value]
        else:
            d[key].append(value)
    return d


print(new_dictionary(list1))
"""

"""
# highly important
# lightly difficult : dictionary of list to list of dictionaries [ LD id slightly difficult ]

# 47. Write a Python program to split a given dictionary of lists into list of dictionaries.
# Original dictionary of lists:
x={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]


def dict_of_list_to_list_of_dict(dict_obj):
    b = len(x['Science'])
    return[{key:value[i] for key, value in x.items()} for i in range(b)]


print(dict_of_list_to_list_of_dict(x))
"""
"""
# 48. Write a Python program to remove a specified dictionary from a given list.
# Original list of dictionary:
a=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# Remove id #FF0000 from the said list of dictionary:
# [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]


def removing_dict_in_list(list_obj):
    return [x for x in list_obj if x['id'] != '#FF0000']  # we can remove based on the colour also x['color'] != specify color


print(removing_dict_in_list(a))

"""

"""
# 49. Write a Python program to convert string values of a given dictionary, into integer/float datatypes.
# Original list:
# [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# Original list:
# [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# String values of a given dictionary, into float types:
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]


def string_to_numbers(list_object):
    return [{key: int(value) for key, value in x.items()}for x in list_object]


print(string_to_numbers([{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]))


def string_to_float(list_obj):
    return [{key: float(value) for key, value in x.items()}for x in list_obj]


print(string_to_float([{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]))

"""

"""
# 50. A Python Dictionary contains List as value. Write a Python program to clear the list values in the said dictionary.
# Original Dictionary:
# {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# Clear the list values in the said dictionary:
# {'C1': [], 'C2': [], 'C3': []}

# there are two methods in this clear value of dict >>>> imp point is we have to clear the value by using the key only

# >>>>>>>>> very important we have to clear the value by using key only ... don't touch values<<<<<<<<<<<<<

def clear_dict_value(dict_obj):
    for key in dict_obj:  # by default it will takes keys >>> we can mention dict_obj.keys() also both will give same result
        dict_obj[key].clear()
    return dict_obj


print(clear_dict_value({'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}))


# by using dictionary comprehension


def clear_values(dict_obj):
    return {key: [] for key, value in dict_obj.items()}  # Formula = list.clear()


print(clear_values({'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}))
"""

"""
# 51. A Python Dictionary contains List as value. Write a Python program to update the list values in the said dictionary.
# Original Dictionary:
old_dict = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# Update the list values of the said dictionary:
# {'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}


def sort_values(dict_obj):
    dict_obj['Math'] = [x+1 for x in dict_obj['Math']]    # here we are adding the +1 to values of the dictionaries
    dict_obj['Physics'] = [x-2 for x in dict_obj['Physics']]  # Here we are less -2 to each values of the dictionaries  
    return dict_obj


print(sort_values(old_dict))

"""
"""
#  this is very important problem
# 52. Write a Python program to extract a list of values from a given list of dictionaries.
# Original Dictionary:
dict1=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Science
# [92, 94, 88]
# Original Dictionary:
dict2=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Math
# [90, 89, 92]


def extract_science_values(list_obj):
    return [value for dit_obj in list_obj for key, value in dit_obj.items() if key == "Science"]


print(extract_science_values([{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]))


def extract_maths_values(list_obj):
    return [value for dit_obj in list_obj for key, value in dit_obj.items() if key == "Math"]


print(extract_maths_values(dict2))

"""
"""
# 53. Write a Python program to find the length of a given dictionary values.
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Length of dictionary values:
# {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}


def dict_value_length(dict_obj):
    return {value: len(value) for key, value in dict_obj.items()}


print(dict_value_length({1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}))
print(dict_value_length({'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}))
"""
"""
# 54. Write a Python program to get the depth of a dictionary.


def depth_of_dictionary(dict_obj):
    a=str(dict_obj)
    count=0
    for x in a:
        if x == "{":
            count += 1
    return count


print(depth_of_dictionary({'a': 1, 'b': {'c': {'d': {}}}}))
"""
"""
# 55. Write a Python program to access dictionary key's element by index.
# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# Expected Output:
# physics
# math
# chemistry


def access_keys_element(dict_obj):
    for key in dict_obj:
        print(key)


access_keys_element({'physics': 80, 'math': 90, 'chemistry': 86})
"""

"""
# 56. Write a Python program to convert a given dictionary into a list of lists.
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Convert the said dictionary into a list of lists:
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]


def dict_to_list_of_lists(dict_obj):
    return [[key, values] for key, values in dict_obj.items()]


print(dict_to_list_of_lists({1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}))
"""
"""
# 57. Write a Python program to filter even numbers from a given dictionary values.
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}


def filter_even_in_keys(dict_obj):
    return {key: [x for x in values if x % 2 == 0]for key, values in dict_obj.items()}


print(filter_even_in_keys({'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}))
"""
"""
# 58. Write a Python program to get all combinations of key-value pairs in a given dictionary.
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Combinations of key-value pairs of the said dictionary:
# [{'V': [1, 4, 6, 10], 'VI': [1, 4, 12]}, {'V': [1, 4, 6, 10], 'VII': [1, 3, 8]}, {'VI': [1, 4, 12], 'VII': [1, 3, 8]}]
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5]}
# Combinations of key-value pairs of the said dictionary:
# [{'V': [1, 3, 5], 'VI': [1, 5]}]


def all_combinations(dict_obj):
    return [{key: value}for key, value in dict_obj.items()]


print(all_combinations({'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}))
"""
"""
# 59. Write a Python program to find the specified number of maximum values in a given dictionary.
# Original Dictionary:
# {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# 1 maximum value(s) in the said dictionary:
# ['f']
# 2 maximum value(s) in the said dictionary:
# ['f', 'i']
# 5 maximum value(s) in the said dictionary:
# ['f', 'i', 'g', 'd', 'c']


def specified_num_maximum_values(dict_obj, n):
    return [key for key, values in sorted(dict_obj.items(), key=lambda x:x[1], reverse=True)][:n]


print(specified_num_maximum_values({'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}, 5))
"""
"""
# 60. Write a Python program to find shortest list of values with the keys in a given dictionary. Go to the editor
# Original Dictionary: {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
# Shortest list of values with the keys of the said dictionary: ['VI', 'VIII', 'X']

# explanation : we have to find  keys which having short list of values(len of values is minimum). 

def sortest_list_of_values(dict_obj):
    return [key for key, values in dict_obj.items() if len(values) <= 1]


print(sortest_list_of_values({'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}))
"""
"""
# 61. Write a Python program to count the frequency in a given dictionary.
# Original Dictionary:
# {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# Count the frequency of the said dictionary:
# Counter({10: 2, 40: 2, 20: 2, 70: 1, 80: 1})

# Explanation: there is no frequency count for key in dict keys are unique ...only frequency for values


def frequency_values(dict_obj):
    dict1 = {}
    for key, values in dict_obj.items():
        if values not in dict1:
            dict1[values]=1
        else:
            dict1[values] += 1

    return dict1


print(frequency_values({'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}))
"""

"""
# important problem
# 62. Write a Python program to extract values from a given dictionaries and create a list of lists from those values. Go to the editor
# Original Dictionary:
a = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
     {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
     {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
     {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
     {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# Extract values from the said dictionaries and create a list of lists using those values:
# [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# [[1, 'Jean Castro'], [2, 'Lula Powell'], [3, 'Brian Howell'], [4, 'Lynne Foster'], [5, 'Zachary Simon']]
# [['Jean Castro', 'V'], ['Lula Powell', 'V'], ['Brian Howell', 'VI'], ['Lynne Foster', 'VI'], ['Zachary Simon', 'VII']]

# method:1


def extract_values(list_obj):
    return [[value for key, value in dict_obj.items() if key != 'student_id']for dict_obj in list_obj]   # were ever key, values there must be a dit.items()


print(extract_values(a))

# method:2 Super method:


def extract(list_obj, *keys):
    return [list(dit[key] for key in keys) for dit in list_obj]


print(extract(a, 'name'))
"""

"""
# 63. Write a Python program to convert a given list of lists to a dictionary.
# Original list of lists:
a = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]


# Convert the said list of lists to a dictionary:
# {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}

# method:1 this is my method.


def list_of_lists_to_dictionaries_of_list(list_obj):
    return {x[0]: [x[1], x[2]] for x in list_obj}


print(list_of_lists_to_dictionaries_of_list(a))


# ***** method:2 w3 method


def list_to_dict(list_obj):
    return {x[0]: x[1:] for x in list_obj}  # why it comes values in list formate bcoz >>> if we access one element in list no list will comes...
    # if we access  morethan one element in slicing the list list will come


print(list_to_dict(a))
"""
"""
# super method 
# 64. Write a Python program to create a key-value list pairings in a given dictionary.
# Original dictionary:
a = {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]


def key_value_list_paring(dict_obj):  
    return [{key: x for x in value} for key, value in dict_obj.items()]

# Explanation : if you writes value directly in the x place value comes in list so again one more for loop for extracting values in the list 


print(key_value_list_paring(a))
"""
"""
# 65. Write a Python program to get the total length of all values of a given dictionary with string values.
# Original dictionary:
a = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
# Total length of all values of the said dictionary with string values:
# 20
# Click me to see the sample solution

# method:1 without using in_built


def total_length_of_all_values(dict_obj):
    total_length = 0
    for value in dict_obj.values():
        total_length += len(value)

    return total_length


print(total_length_of_all_values(a))


# method:2 with sum() function

def length_of_values(dict_obj):
    return sum(len(values) for values in dict_obj.values())


print(length_of_values(a))
"""
"""
# 66. Write a Python program to check if a specific Key and a value exist in a dictionary.
# Original dictionary:
a= [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
 {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
 {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
 {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
 {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# Check if a specific Key and a value exist in the said dictionary:

# Explanation : We have to find specific key and along with its value in the given dictionary.  manam ichina key vundali daniki manam ichina value
                                                                                                                                    # vundali

def specific_key_value(list_obj, key, value):
    return any(dict_obj[key] == value for dict_obj in list_obj)


print(specific_key_value(a, 'class', 'VII'))

"""
"""
# THIS IS VERY VERY VERY VERY IMPORTANT PROBLEM.
# 67. Write a Python program to invert a given dictionary with non-unique hashable values.
a = {'Ora Mckinney': 8, 'Theodore Holland': 7, 'Mae Fleming': 7, 'Mathew Gilbert': 8, 'Ivan Little': 7}
# Sample Output:
# {8: ['Ora Mckinney', 'Mathew Gilbert'], 7: ['Theodore Holland', 'Mae Fleming', 'Ivan Little']}

# Explanation: invert means reverse key>> value , value >> key


def invert_non_unique_hashable_values(dict_obj):
    new_dict={}
    for key, value in dict_obj.items():
        if value not in new_dict: # it searches given value in new_dict keys.
            new_dict[value]=[key]   # reversing(inverting) key and values
        else:
            new_dict[value].append(key)
    return new_dict


print(invert_non_unique_hashable_values(a))

"""
"""
# 68. Write a Python program to combines two or more dictionaries, creating a list of values for each key.
# Sample Output:
# Original dictionaries:
# {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
# {'x': 300, 'y': 'Red', 'z': 600}
# Combined dictionaries, creating a list of values for each key:
# {'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}


def adding_dictionaries(*dict_obj):  # this is tuple object so inside tuple object we have to extract dict_object.
    new_dict={}
    for x in dict_obj:
        for key, values in x.items():
            if key not in new_dict:
                new_dict[key]=[values]
            else:
                new_dict[key].append(values)
    return new_dict


print(adding_dictionaries({'w': 50, 'x': 100, 'y': 'Green', 'z': 400}, {'x': 300, 'y': 'Red', 'z': 600}, {'z': 100}))
"""
"""
# 69. Write a Python program to group the elements of a given list based on the given function.
# Sample Output:
# Original list & function:
# [7, 23, 3.2, 3.3, 8.4] Function name: floor:
# Group the elements of the said list based on the given function:
# {7: [7], 23: [23], 3: [3.2, 3.3], 8: [8.4]}
# Original list & function:
# ['Red', 'Green', 'Black', 'White', 'Pink'] Function name: len:
# Group the elements of the said list based on the given function:
# {3: ['Red'], 5: ['Green', 'Black', 'White'], 4: ['Pink']}


def group_of_elements(list_obj):
    new_dict={}
    new_list = [int(z) for z in list_obj]
    print(new_list)
    for y in new_list:
        new_dict[y] =
    return new_dict


print(group_of_elements([7, 23, 3.2, 3.3, 8.4]))

"""
"""
# 70. Write a Python program to map the values of a given list to a dictionary using a function,
# where the key-value pairs consist of the original value as the key and the result of the function as the value.
# Sample Output:
# {1: 1, 2: 4, 3: 9, 4: 16}

def list_to_dictionary(list_obj):
    return {x: x**2 for x in list_obj}


print(list_to_dictionary([1, 2, 3, 4, 5]))
"""
"""
users = {'Carla': {'name': {'first': 'Carla ', 'last': 'Russell'}, 'postIds': [1, 2, 3, 4, 5]}}

# 72. Write a Python program to invert a dictionary with unique hashable values.
# input:
students = {'Theodore': 10, 'Mathew': 11, 'Roxanne': 9,}
# Sample Output:
# {10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}


def invert_dict(dict_obj):
    return {value: key for key, value in dict_obj.items()}


print(invert_dict(students))

"""
"""
# very important 
# 73. Write a Python program to convert a list of dictionaries into a list of values corresponding to the specified key.
# Sample Output:
# Original list of dictionaries:
a= [{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
# Convert a list of dictionaries into a list of values corresponding to the specified key:
# [18, 22, 20, 18]


def list_of_values(list_obj, key):
    new_list = [x[key] for x in list_obj]  # simple logic but little complicated
    return new_list


print(list_of_values(a, 'age'))

"""
"""
# 74. Write a Python program to create a dictionary with the same keys as the given dictionary and values generated by running the given function
# for each value.
# Sample Output:
# Original dictionary elements:
a = {'Theodore': {'user': 'Theodore', 'age': 45}, 'Roxanne': {'user': 'Roxanne', 'age': 15}, 'Mathew': {'user': 'Mathew', 'age': 21}}
# Dictionary with the same keys:
# {'Theodore': 45, 'Roxanne': 15, 'Mathew': 21}


def new_dict(dict_obj, keys):
    return {key: value[keys] for key, value in dict_obj.items()}


print(new_dict(a, 'age'))
"""
"""
# New model =>>>> based on value we are getting keys.

# 75. Write a Python program to find all keys in the provided dictionary that have the given value.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Find all keys in the said dictionary that have the specified value:
# ['Roxanne', 'Betty']


def dict_keys(dict_obj, values):
    return [x for x in dict_obj if dict_obj[x] == values]   #  Here we no need to mention the dict.items() only keys is enough...
                                                            # For getting keys based on values only keys is enough in forloop.


print(dict_keys({'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}, 20))

"""
"""
# 76. Write a Python program to combine two lists into a dictionary, where the elements of the first one serve as the keys
# and the elements of the second one serve as the values. The values of the first list need to be unique and hashable.
# Sample Output:
# Original lists:
# ['a', 'b', 'c', 'd', 'e', 'f']
# [1, 2, 3, 4, 5]
# Combine the values of the said two lists into a dictionary:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


# method: 1 My own method

def list_to_dict(list1, list2):
    return {list1[i]: list2[i] for i in range(min(len(list1), len(list2)))}


print(list_to_dict(['a', 'b', 'c', 'd', 'e', 'f'], [1, 2, 3, 4, 5, 6, 7, 8]))

# method:2 by using Zip function


def list_to_dict_by_zip_func(list1, list2):
    return {x: y for x, y in zip(list1, list2)}


print(list_to_dict_by_zip_func(['a', 'b', 'c', 'd', 'e', 'f'], [1, 2, 3, 4, 5]))

# method:3 by using zip function
 
def creating_dict(list1, list2):
    return dict(zip(list1, list2)

"""
"""
# 77. Write a Python program to convert given a dictionary to a list of tuples.
# Sample Output:
# Original Dictionary:
# {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# Convert the said dictionary to a list of tuples:
# [('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]


def dict_to_list_of_tuples(dict_obj):
    return [x for x in dict_obj.items()]   # dit.items() always returns the list of tuples ...

# We can also provide return list(dict_obj.items())


print(dict_to_list_of_tuples({'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}))

"""
"""
# model: creating list of all keys....

# 78. Write a Python program to create a flat list of all the keys in a flat dictionary.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Create a flat list of all the keys of the said flat dictionary:
# ['Theodore', 'Roxanne', 'Mathew', 'Betty']


def flat_list_of_all_keys_in_flat_dict(dict_obj):
    return [key for key in dict_obj]

# We can also provide list(dict_obj) or list(dict_obj.keys())


print(flat_list_of_all_keys_in_flat_dict({'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}))

"""

"""
# model: creating list of all values....


# 79. Write a Python program to create a flat list of all the values in a flat dictionary.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Create a flat list of all the values of the said flat dictionary:
# [19, 20, 21, 20]


def create_list_of_all_values(dict_obj):
    # return list(dict_obj.values())
    return [x for x in dict_obj.values()]


print(create_list_of_all_values({'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}))

"""
"""
# Getting key having of maximum value and minimum value in the dictionary

# 80. Write a Python program to find the key of the maximum value in a dictionary. Go to the editor
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# Finds the key of the maximum and minimum value of the said dictionary:
# ('Roxanne', 'Theodore')


# method:1 it is normal method
def getting_max_key(dict_obj):
    return tuple(key for key, value in dict_obj.items() if value == max(dict_obj.values())) # for minimum
    # return tuple(key for key, value in dict_obj.items() if value == max(dict_obj.values())) # for maximum


print(getting_max_key({'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}))


# method:2

# By using get_key method.

def getting_max_key_and_min_key(dict_obj):
    return max(dict_obj, key=dict_obj.get), min(dict_obj, key=dict_obj.get)


print(getting_max_key_and_min_key({'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}))
"""




################################################.....FORMULAS WITH EXPLANATION.....##################################################################


































