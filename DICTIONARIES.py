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




""""""





def func_outer():
    x = "loca"
    def func_inner():
        # x="a"
        x="hello"
        print("inner:", x)
    func_inner()
    print("outer:", x)
func_outer()


def outer_func():
    message = 'Hello'

    def inner_func():
        print(message)

    return inner_func


outer_func()


def outer(x):
    def inner():
        print(x)
        print('!hi')

    return inner


a=outer('hello')
del outer
a()

