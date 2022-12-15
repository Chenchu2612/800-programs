"""
# Model :1 Display the name space of the said module.


# 1. Write a Python program to import built-in array module and display the namespace of the said module.


# what is object.__dict__ >>>According to python documentation object.__dict__ is A dictionary or other mapping object used to store an object’s (writable) attributes.

#  You can think of a namespace as a dictionary in which the keys are the object names and the values are the objects themselves.

# what is name space ? In general, a namespace is a naming system to create unique names.....Python uses namespaces for identifiers(varibles).


import array

for name in array.__dict__:
    print(name)

"""
"""

# Model : creating class and their namespace.

# 2. Write a Python program to create a class and display the namespace of the said class


# Exp: oka class ni create chesi daani yokka name space ni print cheyyali...


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)

for i in Student.__dict__:
    print(i)
    
"""

"""
# Model : creating instance of a class and display the namespace of the class.


# 3. Write a Python program to create an instance of a specified class and display the namespace of the said instance

# Exp : instance of class ante "object".... create instance of the class ante manam class ki oka object cereate cheyyali... daani yokkka name space create cheyyali.

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

# Exp: abs() function ni import cheyyali (builtins module nunchi)... dantlo nunchi abs() funtion yokka documentation staring ni print cheyyali...


# The abs() :- function returns the absolute value of the specified number.



import builtins

print(builtins.abs.__doc__)

#  __doc__ (or) help any we can use.

help(builtins.abs)

# print(builtins.abs(-155))

# Note : okavela nenu from buildins import abs ani kuda rayavachu ..ala raste nenu prathi chota buildins.abs ani rayalsina pani ledu. direct ga abs ani rayavochu..

"""

"""
# Module : creating function and dixplay the names of arguments...

# 5. Define a Python function student(). Using function attributes display the names of all arguments


# Exp: student ane function ni create cheyyali... function yokka attributes(varibles) ni use chesi...manam all arguments yokka names print cheyyali...

def student(name, area, mobile_num):
    return "name = {}\narea = {}, \nmobile_num = {}".format(name, area, mobile_num)


print(student('chenchu', 'nellore', 6303413973))

"""
"""
# Model : if passes different arguments it will print different arguments...

# 6. Write a Python function student_data () which will print the id of a student (student_id).
# If the user passes an argument student_name or student_class the function will print the student name and class.

# Exp: function lo student_name ani iste student_name ani matrame print avvali...okavela student class and name ani rendu iste rendu print avaali...

# New method: f'{}' edi new method ikkada...


def student_data(student_id, **kwargs):
    print(f"student_ID = {student_id}")
    if 'student_name' in kwargs:
        print(f"student_name = {kwargs['student_name']}")
    if 'student_name' and 'student_class' in kwargs:
        print(f"student_class = {kwargs['student_class']}")


student_data(1, student_name='hari', student_class=5)

"""
"""
# Model : creating class and display its type...display the __dict__ attributes keys and __module__ attribute of a class.

# 7. Write a simple Python class named Student and display its type.
# Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.


# Exp : student class create cheyyali tharuvatha daani yokka...1.type ni print cheyyali 2.__dict__ yokka keys() nio print cheyyalli. 3. values of module attributes


class Student:
    pass


print(type(Student))
print(Student.__dict__.keys()) # keys of dict attributes
print(Student.__module__)  # values of module attributes
"""
"""
# Model : creation of classes and check instances of the classes... create instances(object) and checking they are instances of said class or not...

# and checking weather specified class is subclass of built-in class or not...


# 8. Write a Python program to crate two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not.
# Also, check whether the said classes are subclasses of the built-in object class or not.


# Exp : 1. manam rendu emepty classes ni create cheeyyali...

# 2. daniki instances ante object's ni create cheyyali...

# 3. object anedi aa class ki sambandindchida kaada ani check cheyyali...

# 4. create chesina class build_in object class yokkka subclass na kaada ani check cheyyali...

class Student:
    pass


class Marks:
    pass


a = Student()

b = Marks()


print(isinstance(a, Student))   # checking instances
print(isinstance(a, Marks))
print(isinstance(b, Marks))

print(issubclass(Student, object))  # checking subclass
print(issubclass(Marks, object))

"""
"""
# Model : create class with specified attributes...modify the attribute values and print original values and modified values

# 9. Write a Python class named Student with two attributes student_name, marks.
# Modify the attribute values of the said class and print the original and modified values of the said attributes.

# Exp:

# 1. mundu Student class create cheyyali

# 2. original values ni print cheyyali.

# 3. values ni modify chesi...aa modified values ni print cheyyali.

# settar method and getattr method...

# gettarmethod :- getattr(Classname, 'attribute_name')

# setattr :- setattr(Classname, 'attribute', 'new_attribute name')


class Student:
    student_name = 'harika'
    marks = 95


print(f"student_name = {getattr(Student, 'student_name')}\nmarks = {getattr(Student, 'marks')}")
print("after modifying the attribute values")

setattr(Student, 'student_name', 'chenchu')  # setting new values
setattr(Student, 'marks', 100)

print(f"student_name = {getattr(Student, 'student_name')}\nmarks= {getattr(Student, 'marks')}")  # getting new attribute_values

"""

























