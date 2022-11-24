# Fibonacci using recursion
"""
# Fibbonaci numbers are the numbers which starts from 0 and every number is adding of before two numbers.


def fib_recursion(n):
    if n in {0, 1}:
        return n
    return fib_recursion(n - 1) + fib_recursion(n - 2)


print([fib_recursion(i) for i in range(int(input("Enter the range:")))])


# Fibonacci using recursion and lambda.


from functools import reduce

fib_lamb= lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])


print(fib_lamb(int(input("Enter the series of numbers :"))))

"""























