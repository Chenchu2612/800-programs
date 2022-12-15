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
"""
# Model : creating class with specified attributes...add new specified attributes and display attributes and delete some attributes and display remaining attributes...

# 10. Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute
# and their values of the said class. Now remove the student_name attribute and display the entire attribute with values.


# Exp : 1. rendu attributes tho class okati create cheyyali..

# 2. attributes keys and associates values tho print cheyyali...

# 3. kotha attributes ni add cheyali...malli motham attributes keys and values ni print cheyyali

# oka attribute bi delete cheyyali .... malli vunnna motham attributes ni print cheyyali...


class Student:
    student_id = 1
    student_name = 'chenchu mahesh'


# For understanding purpose.....

# print(Student.__dict__.items())
# print(Student.__dict__.values())
# print(Student.__dict__.keys())


for key, val in Student.__dict__.items():
    if not key.startswith('_'):   # key anedi ('_') tho start kakapothe daanni return chey.....
        print(key, '>', val)


#  adding additional attributes.....

Student.student_area = 'banglore'


for key, value in Student.__dict__.items():
    if not key.startswith('_'):   # key anedi ('_') tho start kakapothe daanni return chey.....
        print(key, '>', value)

# deleting attributes.....

del Student.student_id

for key, value in Student.__dict__.items():
    if not key.startswith('_'):     # key anedi ('_') tho start kakapothe daanni return chey.....
        print(key, ">", value)

"""
"""
# Model : creation of class with specified attributes...and add new attributes and createing function to display the entire attributes of the class

# 11. Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class.
# Create a function to display the entire attribute and their values in Student class.


# Exp : 1. mundu manam specified attributes tho class ni create cheyyali...
# 2. function create cheyyali dantlo class attributes anni display avvali...

class Student:
    student_id = 1
    student_name = 'chenchu'

# Note :- manam class lo vunnna varibles ni access cheyyali ante kachithamga Class name ni vadali....example = {Student.student_id}

    def display():
        print(f"student_id  = {Student.student_id}\nstudent_name = {Student.student_name}")  # flower bracket lopala eami pedithe adi vastundi.....


Student.display()

"""
"""
# Model :

# 12. Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes.
# Print all the attributes of student1, student2 instances with their values in the given format.


# Input values of the instances:

# student_1:
# student_id = "V12"
# student_name = "Ernesto Mendez"
# student_2:
# student_id = "V12"
# marks_language = 85
# marks_science = 93
# marks_math = 95

# Expected Output:

# student_id -> V12
# student_name -> Ernesto Mendez
# student_id -> V12
# marks_language -> 85
# marks_science -> 93
# marks_math -> 95



# Exp : 
# 1.class ni create cheyyali....

# 2. daniki refernce(objects) ni create cheyyali.....

# 3. aa reference ki kothaga attributes and values ni add cheyyali...

#  4. mothoam attributes and values ni print cheyyali...

class Student:
    school = 'master school'   # if there is no school there is no student.... so student is the part of the school so we creates the school as static varible
    area = 'sathyavedu'


student1 = Student()
student2 = Student()

# adding attributes along with their values...

student1.student_id = 'V12'
student1.student_name = 'Ernesto Mendez'

student2.student_id = 'V12'
student2.marks_language = 85
student2.marks_science = 93
student2.marks_math = 95

student_details = [student1, student2]  # making list of all objects...

for reference in student_details:  # every object_ref in the student_details
    for key, value in reference.__dict__.items():  # this is important line 
        print(key, '>', value)


# Note = __dict__ method shows key and values in the specified object.

"""

# _________________________________________________Python basic class applictaion_________________________________________________________________

"""
# One and two are pending....

# 1. Write a Python class to convert an integer to a roman numeral.


# 2. Write a Python class to convert a roman numeral to an integer.


# Model : creating class to reverse the given string... 

# 8. Write a Python class to reverse a string word by word.
# Input string : 'hello .py'
# Expected Output : '.py hello'

# Exp : # first string_obj ni split chesi list loki marchukovali.... appudu adi list loki vastundi....danni manam reversed dwara reverse cheyyali...

# join vaadi list lo vunna strings ni space tho join cheyyali...

class Reverse:
    def rev(self, string_obj):
        return ' '.join(reversed(string_obj.split()))


a= Reverse()   # creating object 
print(a.rev('hello .py'))  # calling function rev 
print(a.rev('python class'))

"""
"""
# Model : create class with two methods get_string and print_string ... get_string accepts sring from console...print_string print string in uppercase

# 9. Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.


class IOstring:
    def get_String(self):
        self.str1=input("Enter the string :")
    def print_String(self):
         print(self.str1.upper())


a = IOstring()
a.get_String()
a.print_String()
"""

"""

# Model : code for computation of area of a rectangle...

# 10. Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.


# Exp : first manam length and breath initialize cheyyali... tharuvatha method ni define chesi dantlo area ni calculate cheyyali... 

class Rectangle:
    def __init__(self, l, b):   # ikkada nenu __init__ method vadali nenu __int__ method pettanu....
        self.l = l
        self.b = b

    def area(self):
        print(f'area :{self.l * self.b}')


a = Rectangle(10, 20)
a.area()

"""
"""
# Model : class for computing the area and perimetre of a circle....

# 11. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle


# Exp : oka Circle class ni create cheyyali...dantlo radius ni initialize cheyyali...

# 2. area ni claculate cheyyali and perimeter ni calculate cheyyali...

# formulas :- circle area = 22/7*radius*radius
#             circle perimeter = 2*22/7*radius



class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*22/7

    def perimeter(self):
        return 2*22/7*self.radius


red = Circle(2)
print(red.area())

"""
"""
# Model : getting calss name of an instance ...

# 12. Write a Python program to get the class name of an instance in Python.


class Chenchu:
    pass

a= Chenchu()   #object creation

print(type(a)) # for understandiing purpose ::: the output is :- <class '__main__.Chenchu'> 
print(type(a).__name__)

"""

# model : python class to implemeny power of...

# 7. Write a Python class to implement pow(x, n).




