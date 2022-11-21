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