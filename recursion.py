
# Recursion function: a function call by it self is called recursion
"""
# Model : sum of elements of the list.

#1. Write a Python program to calculate the sum of a list of numbers.


def sum_list(list_obj):
    if len(list_obj) ==1:
        return list_obj[0]
    return list_obj[0]+sum_list(list_obj[1:])
"""
"""

# Model: Adding list items if list contains nested nested objects also

# 3. Write a Python program of recursion list sum.
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21


def sum_list(list_obj):
    total = 0
    for element in list_obj:
        if isinstance(element, list):    # we can also write if type(element) == type([]):
            total += sum_list(element)
        else:
            total += element
    return total


print(sum_list(eval(input("Enter the list object: "))))
"""
"""
# Method: Factorial problem.

# 4. Write a Python program to get the factorial of a non-negative integer.

# Note: 0 factorial is 1, and 1 factorial is 1, two factorial is 2


def factorial(num):
    if num in {0, 1, 2}:     
        return 1
    return num*factorial(num-1)


print(factorial(int(input("Enter the number: "))))
"""

"""
# Model: Sum of first N Fibnocci  numbers using recursion.

# 5. Write a Python program to solve the Fibonacci sequence using recursion.

# Note ::: fibonaci always starts with 0....
# pattren 0,1,1,2,3,5,8....etc  .... number is equal to the sum of its previous two elements.


def fib_recursion(n):
    if n in {0, 1}:
        return n
    return fib_recursion(n - 1) + fib_recursion(n - 2)


print(fib_recursion(3))

"""
"""
# 6. Write a Python program to get the sum of a non-negative integer.
# Test Data:
# sumDigits(345) -> 12
# sumDigits(45) -> 9

# Logic: input modular division of 10 and int(input/10)


def sum_of_digits(number):
    if number == 0:
        return number

    else:
        return number % 10 + sum_of_digits(int(number/10))
"""
"""

# 10. Write a Python program to calculate the value of 'a' to the power 'b'.
# Test Data :
# (power(3,4) -> 81


#  with out any operator:


def pow(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return a*pow(a, b-1)

print(pow(2,3))

# with exponantial operator

def pow(a, b):
    return a**b
print(pow(2,3))
"""

