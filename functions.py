"""
# Model: Finding maximum number from the three numbers

# 1. Write a Python function to find the Max of three numbers.

def max_of_three(n1, n2, n3):
    max_number = -1  # positive matrame iethe 0 tesukovali, positive and negative tesukunte -1 tesukovali
    for number in (n1, n2, n3):  # here we taken in a tuple otherwise we can't iterate through each element
        if number > max_number:
            max_number = number
    return max_number


print(max_of_three(int(input("Enter the numbers :")), int(input("Enter the number: ")), int(input("Enter the number :"))))

"""
"""
# Model: sum of all elements in the list

# 2. Write a Python function to sum all the numbers in a list.
Sample_List = [8, 2, 3, 0, 7]


def sum_of_all_elements_in_a_list(list_obj):
    sum_of_list = 0
    for num in list_obj:
        sum_of_list += num
    return sum_of_list


print(sum_of_all_elements_in_a_list(Sample_List))
"""
"""
# Model: multiplication of all elements in the list
# 3. Write a Python function to multiply all the numbers in a list.
Sample_List = [8, 2, 3, -1, 7]


def multiplication(list_obj):
    multiplication_list = 1
    for num in list_obj:
        multiplication_list *= num
    return multiplication_list


print(multiplication(Sample_List))
"""
"""
# Model: Reverse a string

# 4. Write a Python program to reverse a string.
Sample_String = "1234abcd"
# Expected Output : "dcba4321"


def reverse_string(string):
    new_string = ""
    for ch in string:
        new_string = ch+new_string

    return new_string


print(reverse_string(input("Enter the string: ")))
"""
"""
# Model : finding factorial

# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

# Explanation : factorial of zero is 1 ... we have to mention this specially in if block. remaining logic in else block


def factorial(number):
    if number == 0:
        return 1
    else:
        factorial_number = number*factorial(number-1)
    return factorial_number


print(factorial(int(input("Enter the number:"))))
"""
"""
# Model: check if number exist in a given range.

# 6. Write a Python function to check whether a number falls in a given range.

# Explanation : ichina number specified range lo vunda leda. 

# range function lo end value excluded anduke manam +1 add chestamu


def check_number(number, startrange, endrange):
    if number in range(startrange, endrange+1): 
        return 'Yes the number {} Exists in the given range'.format(number)

    return 'No the number {} Not exists in the given range'.format(number)


print(check_number(int(input("Enter the number :")), int(input("Enter the startrange:")), int(input("Enter the endrange :"))))
"""

"""
# Model : uppercase enni, lowercase enni

# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters


def upper_lower(string):
    upper = lower = 0
    for ch in string:
        if ch.isupper():
            upper += 1
        elif ch.islower():  # ikkada nenu else:petti lower += 1 pedithe akkada empty string vunna,number vunna mariyu special char vunna +1 add 
            lower += 1                                                                                                              # avutundi 
    return 'The number of upper cases :{} \nThe number of lower cases{}'.format(upper, lower)


print(upper_lower(input("Enter the string: ")))
"""
"""
# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Explanation : ichina list nunchi unique charecters kaligina llist okti tayaru cheyyali


def create_unique_list(list_obj):
    new_list = []
    for number in list_obj:
        if number not in new_list:
            new_list.append(number)

    return new_list


print(create_unique_list(eval(input("Enter the list: "))))

"""
"""
# Model : checking prime or not

# 9. Write a Python function that takes a number as a parameter and check the number is prime or not.

# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

# Explanation :
# 1. number 1 kanna ekkuvaga vundali.
# 2. ichina number anedi shound not divisible by (2, number-1)
# 3. For loop with else>>>>>> For, else, break statement


def checking_prime(number):
    if number > 1 :
        for x in range(2, number):
            if number % x == 0:
                print('It is not a prime number')
                break
        else:
            print('It is a prime number')
    else:
        print('It is not prime number')


checking_prime(int(input("Enter the number :")))

"""

"""
# Model : Extract only even numbers

# 10. Write a Python program to print the even numbers from a given list.
Sample_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]


def even_numbers(list_obj):
    return [number for number in list_obj if number % 2 ==0]  # taking only even numbers.


print(even_numbers(Sample_List))

"""
"""
# Model : Finding perfect number.

# 11.Write a Python function to check whether a number is perfect or not.

# According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors,
# that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum).
# Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).

# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6.
# Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6.
# The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.


def finding_perfect_or_not(number):
    sum = 0
    for num in range(1, number):
        if number % num == 0:
            sum += num
    if sum == number:
        return '{} >>>> It is a perfect_number'.format(number)
    return '{} >>>> It is not a perfect_number'.format(number)


print(finding_perfect_or_not(int(input("Enter the perfect number :"))))
"""
"""
# Model : Polindrome

# 12. Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

# Explanation : 1. ichina string nunchi emepty string's ni remove cheyyali
#               2. string ni reverse cheyyali.
#               3. reverse chesina string ni and emepty string's ni remove chesina string ni compare cheyyali. redu okate iethe True ledante False


def check_polindrome(string):
    new_string = ''.join([ch for ch in string if ch != " "])
    reversed_string = ''
    for ch in new_string:
        reversed_string = ch + reversed_string
    if reversed_string == new_string :
        return '{} It is polindrome'.format(string)
    return '{} It is not a polindrome'.format(string)


print(check_polindrome(input("Enter the number :")))

"""

"""
# Model : check Pangram or not

#14. Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

# Mistakes : ikkakda nenu strings ni import chesthanu so... function definition lo parameter string ane name ivvakuadadu.

# logic: 1. string ni import cheyyali 2.import chesina string dwara lowe/upper alphabets ni get chesi set() loki marchali 3. origina string ni
# set loki marchali 3. marchina original string ni and get chesina daniki subset/super set kanukkovali.(issubset/issuperset)(>=)


import string


def check_pangrams(string_obj):
    get_string = set(string.ascii_lowercase)   # here we have to provide ascii_lowercase compulsory
    if set(string_obj)>=get_string: # Finding superset or not
        return '{}>>>>>> The given string is the pangrams'.format(string_obj)
    return '{}>>>>> The given string is not pangrams'.format(string_obj)


print(check_pangrams(input("Enter the string: ")))

 """
"""
# Model:1 sort words between '-'.


# 15. Write a Python program that accepts a hyphen-separated sequence of words as input
# and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

# Explanation : 1. hypen saparated words ga tesukovali  2. danni sort chesi hypen saparate tho ouput return cheyyali


def sort_words(string_object):
    return '-'.join(sorted(string_object.split('-'), reverse=False))


# split() function returns the string to list string.split()
# sort() method eami return cheyyadu so manam denni varible ki assign cheyya kudadu
# a= items.sort() ilaga and join() function lo kuda pettakudadu  "".join(list.sort()) ilaga.
# join() function lo sorted vadadam manchidi.

print(sort_words(input("Enter the string :")))
"""

"""
# Model : creating a list

# 16. Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).

def creating_list(start_number, end_number):
    return [num**2 for num in range(start_number, end_number+1)]


print(creating_list(int(input("Enter the number:")), int(input("Enter the number :"))))

"""
"""
# Very_Very_Very important problem
# Model: @decorator
# 17. Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python.


def make_bold_outer(func):
    def bold_wrapper(b):
        return '<b>'+func(b)+'</b>'
    return bold_wrapper


def make_italic_outer(func):
    def italic_wrapper(i):
        return '<i>'+func(i)+'</i>'
    return italic_wrapper


def make_underline(func):
    def underline_wrapper(u):
        return '<u>'+func(u)+'</u>'
    return underline_wrapper


@make_bold_outer
@make_italic_outer
@make_underline
def chain_bold_italic_underline(string_obj):
    return string_obj

# Note: Main function lo parameter pass cheste inner decorator function lo edo oka positional argument pass cheyyali (same name or different name)
# inner decorator function main function ni call chestundi ee place lo kuda manam positional argument pass cheyyali ex:func(b) in bold_wrapper.

print(chain_bold_italic_underline(input("Enter the string :")))

"""
"""
# Model: Code String rupam lo vunte danni executecheyyali.

# New_function : exec() it is same as print() function .... 
# exec() function is used for the dynamic execution of "Python programs" which can either be a string or object code.

# 18. Write a Python program to execute a string containing Python code.

# my_code = """
# for x in range(10):
#     print(x, end=" ")
"""

exec(my_code)


def execute_code_in_string(string_code):
    return exec(string_code)


execute_code_in_string(my_code)
"""
"""
# Model : acccessing function inside another function

# 19. Write a Python program to access a function inside a function.


# see this two models.

# concept : outer function ki sambandinchina prathi okka vatibles inner function lo access cheyyochu but daani value inner function lo marchalante
# nonlocal keyword use cheyyali.

# Model:1(a) Without modifying the nonlocal varible

def outer_function(parameter1):
    def inner_function(parameter2):
        return parameter1
    return inner_function


x= outer_function('hello')     #>>> deeni output >>>inner_function
print(x(5))

print(outer_function('hello')('2'))  #>>>> model.2

# Model:1(b) with modifying the nonlocal varible

def outer_func(a):
    def inner_func(b):
        nonlocal a
        a+=b
        return a
    return inner_func

print(outer_func(5)(5)) # >>> not a good approach

c=outer_func(5)
print(c(5))
"""
"""
# Mothod: finding number of local varibles in the function.

# 20. Write a Python program to detect the number of local variables declared in a function.

def detect_local_varible():
    x = 1
    y = 2
    str1 = "w3resource"


print(detect_local_varible.__code__.co_nlocals)


# not understanding
"""
"""
21. Write a Python program that invoke a given function after specific milliseconds.
Sample Output:
Square root after specific miliseconds:
4.0
10.0
158.42979517754858

"""


with open("lambda.py", 'w+') as f:
    print("file_opened")




