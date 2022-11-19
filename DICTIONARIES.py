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
















