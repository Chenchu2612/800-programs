"""
# map(function, iterable) >>>> every elemant in the sequesnce applying specific functionality and comming out....length is not changes ...


#1.Write a Python program to triple all numbers of a given list of integers. Use Python map.
nums = (1, 2, 3, 4, 5, 6, 7)

# Triple of said list numbers:
# [3, 6, 9, 12, 15, 18, 21]


# Mistake : ikaada nenu chese mistake x*3 ani rasestha ....ala cheste output raadu.

print(tuple(map(lambda x: x+x+x, nums)))  # in tuple output
print(list(map(lambda x: x+x+x, nums)))  # list output

"""
"""
# Model : parell adding of lists (column wise adding)

# 2. Write a Python program to add three given lists using Python map and lambda.

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

# New list after adding above three lists:
# [12, 15, 18]

# Note: map function is used for parellel iteration but each list  must have same length...

# Explanation: ikkada first iteration lo 0th index lo vunde anni elements x,y,z lo store avutundi...adi add adutundi....next iteration lo 1st index


print(list(map(lambda x, y, z: x + y + z, nums1, nums2, nums3)))
"""
# Model :listify

"""
# 3. Write a Python program to listify the list of given strings individually using Python map.

color = ['Red', 'Blue', 'Black', 'White', 'Pink']

# output=[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]

print(list(map(list, color)))
"""
"""
# Model: Powerof

# 4. Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using
# Python map


bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# output:
# [10, 400, 27000, 2560000, 312500000, 46656000000, 8235430000000, 1677721600000000, 387420489000000000, 100000000000000000000]

# Function: pow 

print(list(map(pow, bases_num, index )))

"""
"""
# Model: square the elements.

# 5. Write a Python program to square the elements of a list using map() function.

# By using normal function and map function

def square_number(n):
    return n*n

print(list(map(square_number, [2, 5])))


# By using lambda function and map() function.

print(list(map(lambda x: x**2, [1, 2, 3, 5, 9])))

"""
"""

# Model: convert every charecter in upper case , lower case, eleminate duplicates

# 6. Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence.
# Use map() function.


# By using normal function and map


def convertion(string_obj):
    return str(string_obj).upper(), str(string_obj).lower()


chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}

print(set((map(convertion, chrars))))

# By using lambda function


print(list(map(lambda x: (x.upper(), x.lower()), chrars)))

"""
"""
# Model: adding two lists and difference between two lists.

# 7. Write a Python program to add two given lists and find the difference between lists. Use map() function

# By using lambda function and map() function

print(list(map(lambda x, y: (x+y, x-y), [1, 2], [5, 6])))

# By using normal function and map() function.


def add_sub(list1, list2):
    return list1+list2, list1-list2


print(list(map(add_sub, [1, 2], [3, 4])))

"""

"""
# 8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.

# map() function is also used for parell iteratrion.


print(list(map(lambda x: str(x), [1, 2, 3, 4])))
print(list(map(lambda x: str(x), (1, 2, 3, 4))))
"""
"""
# 9. Write a Python program to create a new list taking specific elements from a tuple and convert a string value to integer.


student_data = [('Alberto Franco', '15/05/2002', '35kg'),
                ('Gino Mcneill', '17/05/2002', '37kg'),
                ('Ryan Parkes', '16/02/1999', '39kg'),
                ('Eesha Hinton', '25/09/1998', '35kg')]


# map function functionality : every item in the iterable will goes to lambda function argumet one by one. same as filter function also


print("The student names: ", list(map(lambda x: x[0], student_data)))
print("The student dob: ", list(map(lambda x: x[1], student_data)))
print("The weights :", list(map(lambda x: int(x[2][:2]), student_data)))

"""


# Super code.

# Model: list of first N fibonacci numbers by using map()

# 10. Write a Python program to compute the square of first N Fibonacci numbers, using map function and generate a list of the numbers.

# Explanation: 1. N fibnocii number list lo create cheyyali 2.danni map use chesi square cheyyali


def fib_recursion(n):
    if n in {0, 1}:
        return n
    return fib_recursion(n - 1) + fib_recursion(n - 2)


print(list(map(lambda x: x ** 2, [fib_recursion(n) for n in range(int(input("Enter the required number of sequence: ")))])))

"""

# check if the number of terms is valid.


# Model : sum of array of intigers

# 11,12 array problems

# 11. Write a Python program to compute the sum of elements of a given array of integers, use map() function.

# doubt

# array problem
"""
"""
# Model: comparision between  two lists

13. Write a Python program to count the same pair in two given lists. use map() function. 

d1 = [1, 2, 3, 4, 5, 6, 7, 8]
d2 = [2, 2, 3, 1, 2, 6, 7, 9]

print(len(list(filter(lambda x: x == True, list(map(lambda a, b: a == b, d1, d2))))))

"""
# 14, 15 ignored
"""
# Model: list of strings to the list of lists.

# 16. Write a Python program to convert a given list of strings into list of lists using map function.


print(list(map(list, ['apple', 'ball', 'cat'])))  # without lambda
print(list(map(lambda x: list(x), ['apple', 'ball', 'cat'])))  # with lambda
print(list(map(lambda x: [x], ['apple', 'ball', 'cat'])))  # this is not a correct method
"""
# Model: list of tuples to list of strings


# 17.Write a Python program to convert a given list of tuples to a list of strings using map function.

# Original list of tuples:
# a=[('red', 'pink'), ('white', 'black'), ('orange', 'green')]
# Convert the said list of tuples to a list of strings:
# ['red pink', 'white black', 'orange green']

# print(list(map(lambda x: x[0]+" "+x[1], a)))

print("hai prasad")