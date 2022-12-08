"""
# Model :1 Display the name space of the said module.


# 1. Write a Python program to import built-in array module and display the namespace of the said module.


# what is object.__dict__ >>>According to python documentation object.__dict__ is A dictionary or other mapping object used to store an object’s (writable) attributes.

# what is name space ? In general, a namespace is a naming system to create unique names.....Python uses namespaces for identifiers(varibles).


import array

for name in array.__dict__:
    print(name)

"""
"""
# Model : creating instance of a class and display the namespace of the class.


# 3. Write a Python program to create an instance of a specified class and display the namespace of the said instance


class Student:
    def __init__(self, name, age, address, mobile_number):  # initializing the instance varibles.
        self.name = name
        self.age = age
        self.address = address
        self.mobile_number = mobile_number


obj = Student('chenchu', '28', 'karnool', '6303413973')


print(obj.__dict__)
"""

"""

# Model : import abs() module using builtins module, displying documentation of abs() , finding absolute value.


# 4. 'builtins' module provides direct access to all 'built-in' identifiers of Python.
# Write a python program which import the abs() function using the builtins module,
# display the documentation of abs() function and find the absolute value of -155.

# This module provides direct access to all ‘built-in’ identifiers of Python
# for example, builtins.open is the full name for the built-in function open().


# The abs() :- function returns the absolute value of the specified number.



import builtins

print(builtins.abs.__doc__)

#  __doc__ (or) help any we can use.

help(builtins.abs)

# print(builtins.abs(-155))

"""
# Module :

# 5. Define a Python function student(). Using function attributes display the names of all arguments


def students(name, villege, Class):
    return 'name ={}\nvillege = {}\nClass = {}'.format(name, villege, Class)


<<<<<<< Updated upstream
# print(students('chenchu', 'stvd', 12))
<<<<<<< Updated upstream
=======
# print(students('chenchu', 'stvd', 12))



print('iam us resident')
>>>>>>> Stashed changes
=======
print("MAHESH")
>>>>>>> Stashed changes
