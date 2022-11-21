"""
# 1. Write a Python program to calculate the length of a string.

# By using count function
def len_string(string):
    return len(string)


print(len_string('chenchu'))


# method:2 without inbuilt

def len_count_string(string):
    count = 0
    for x in string:
        count += 1
    return count


print(len_count_string("chenchu"))

"""

"""
# 2.Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : 'google.com'

# Explanation : string frequency is nothing but number of times the character repeated in the string


def string_frequency(string):
    freq_dict = {}
    for ch in string:
        if ch not in freq_dict:
            freq_dict[ch] = 1
        else:
            freq_dict[ch] += 1
    return freq_dict


print(string_frequency('google.com'))


# By using counter method

from collections import Counter


def freq_using_counter(string):
    return Counter(string)


print(freq_using_counter('chenchu'))

# by using dict_comprehension
 

def dict_comp(string):
    return {x: string.count(x) for x in string}


print(dict_comp('chenchu'))

"""
"""
# 3.Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String


def string_both_ends(string):
   if len(string) < 2:
     return ''

   return str[0:2] + str[-2:]


print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))

"""
"""
# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
# except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'


#Explanation : string loni First character tesukoni adi repeate iena prathi chota '$' marchali ...first charecter ki thappa migathavi marchali


def new_string(string):
    return string[0]+string[1:].replace(string[0], '$')


print(new_string('chenchu'))
"""
"""
# little complicated...Swapping model

# 5. Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each strings
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

# Eplanation: swapping is nothing but marpidi 

def new_string(str1, str2):
    string1 = str2[:2]+str1[-1]
    string2 = str1[:2]+str2[-1]
    return string1+" "+string2


print(new_string("abc", "xyz"))
"""
"""
# very confusing model

# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'


def string_modification(string):
    if len(string)>=3:
        if string[-3:]=='ing':
            string+='ly'
        else:
            string+='ing'

    return string


print(string_modification('str'))
"""

# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor',
# replace the whole 'not'...'poor' substring with 'good'. Return the resulting string
# Sample
# String: 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected
# Result: 'The lyrics is good!'
# 'The lyrics is poor!'
"""
# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# input= ["PHP", "Exercises", "Backend"]
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9


def longestword_and_length(list_of_words):
    new_list=[]
    for x in list_of_words :
        new_list.append((len(x), x)) # append function only append one element at a time here we are appending 2 elements that why we are using
    print(new_list)  # for understanding purpose                                          tuple to insert two elements in one.  
    new_list.sort(key=lambda x: x[0], reverse=True)           # sort function is works only only only only on list>>>>list.sort(key, reverse)
    print(new_list)  # for understanding purpose
    return 'longest_word:{}\nLength of the longest word:{}'.format(new_list[0][1], new_list[0][0]) #\n represent new line


print(longestword_and_length(["PHP", "Exercises", "Backend"]))

"""

"""
# 9. Write a Python program to remove the nth index character from a nonempty string.


def remove_ch_in_string(string, n):
    return string[:n]+string[n+1:]


print(remove_ch_in_string('chenchu', 0))
"""
"""
# 10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

def exchange_first_and_last_letter(string):
    return string[-1:]+string[1:-1]+string[:1]


print(exchange_first_and_last_letter('chenchu'))
"""

"""
# 11. Write a Python program to remove the characters which have odd index values of a given string. Go to the editor


# Explanation: we have to remove only odd index so ....we can take even index ... vise-versa...use join() method

# This is Traditional approach by using range(len()) function


def remove_odd_index(string):
    new_string = ''
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i]

    return new_string


print(remove_odd_index('chenchu'))


# super code:
def remove_odd(string):
    return "".join([string[i] for i in range(len(string)) if i % 2 == 0])


print(remove_odd('chenchu'))
"""
"""
# 12. Write a Python program to count the occurrences of each word in a given sentence.
# a = 'the quick brown fox jumps over the lazy dog.'
# {'the': 2, 'jumps': 1, 'brown': 1, 'lazy': 1, 'fox': 1, 'over': 1, 'quick': 1, 'dog.': 1} 

# Explanation : string tho manam direct ga kanukkolemu ...so list loki marchi manam kanukko galamu

# white spaces having length 1 where emepty string having length 0

# split func===> string.split(separator, maximumsplits)


def number_of_occurence_of_each_word(string):
    freq_dict={}
    for word in string.split():  # by default split() function splits based on white space. it converts string into list of words based on condition
        if word not in freq_dict:
            freq_dict[word] = 1
        else:
            freq_dict[word] += 1
    return freq_dict


print(number_of_occurence_of_each_word(a))
"""

"""
# 13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

# Explanation: console through dwara input tesukoni danni upper and lower case lo print cheyyali.

# Functions = string.upper() , input()

# manam input() function use cheste parameter ki arguments manam console dwara istam 

def display_upper_and_lower(string):
    return 'who is your favorate Hero ? {}\nwho is your favorate Hero ? {}'.format(string.upper(), string.upper())


print(display_upper_and_lower(input("who is your favourate hero ?: ")))
"""
"""
# pending
# 14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red


def unique_words_in_sorted_form(words):
    new_list=[]
    for word in words.split():
        if word not in new_list:
            new_list.append(word)
    sorted(new_list)
    return "".join(new_list)


print(unique_words_in_sorted_form(input("enter the list of words: ")))
"""

"""
# 15. Write a Python function to create the HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'


# Note: For html closing we always use forward slash i.e '/'

# used format function
def adding_html_tags(tag, string):
    return '<{}>{}</{}>'.format(tag, string, tag)   


print(adding_html_tags(input('enter the tag:'), input("enter the string:")))
"""

"""
# 16. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}


# my method
def insert_the_string_into_middle_of_the_string(string):
    return '{{{}}}'.format(string)


print(insert_the_string_into_middle_of_the_string(input("enter the string: ")))


# w3 schools method.

def insert_the_string(symbol, string):
    return symbol[:2]+string+symbol[-2:]


print(insert_the_string(input("Enter the symbol :"), input("Enter the string :")))
"""
"""
# 17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

# Explanation: last 2 charecters 4 times repeate ayyivundali.


def get_string(string):
    return string[-2:]*4


print(get_string(input("Enther the string:")))
"""

"""
# 18. Write a Python function to get a string made of its first three characters of a specified string.
# If the length of the string is less than 3 then return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt

# Explanation: string lo first three charecters kavali.


def getting_string(string):
    return string[:3]


print(getting_string(input("enter the string:")))
"""
"""
# 19. Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python

# Explanation : oka  specific charecter ki mundu vunde part kavali. 

def last_part_before_specified_character(string, character):
    return string.split(character)[0]    # string.split() anedi list lo vastundi danni nenu index adharam ga access chesa


print(last_part_before_specified_character('https://www.w3resource.com/python-exercises', '/'))

"""
"""
# 20. Write a Python function to reverses a string if it's length is a multiple of 4.


def reverse_if_divisible_by_4(string):
    new_string = ""
    if len(string) % 4 == 0:
        for ch in string:
            new_string = ch+new_string
    else:
        return '{} It is not divisible by {}'.format(string, 4)
    return new_string


print(reverse_if_divisible_by_4(input("Enter the string:")))

# w3 method:

def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print(reverse_string('abcd'))
print(reverse_string('python'))
"""
"""
# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters

# Explanation : first 4 charecters lo 2 upper cases vunte aa string mothanni upper cases loki marchali


def convertion_of_upper_case(string):
    number_upper=0
    for ch in string[:4]: # first 4 letters lo enni upper vundo count chestunnam
        if ch.isupper():
            number_upper += 1

    if number_upper >= 2:   # first 4 letters lo 2 upper vunte motham string ni upper case chestunnam
        return string.upper()
    return string


print(convertion_of_upper_case(input("Enter the string:")))
"""
"""
#model : lexiographical order.

# 22.Write a Python program to sort a string lexicographically.

# Explanation: lexographical order means >>> first sort number next: capital alphabet next:small alphabets oka daani tharuvatha okati.
# ex: all numbers then after all acpital A's then after small a's then after capital B's then after small b's and so on. Dictionary order annamata
# this order is different from sorted() function in sorted function first num next all capitals next all small but here different


def lexicographically(string):
    print(sorted(string)) # for difference purpose print this
    return sorted(sorted(string), key=str.upper)   # here str.upper will plays crucial roll.


print(lexicographically('w3reaSsouRce'))
"""
"""
# model: Removing new line

# 23. Write a Python program to remove a newline in Python.

# there are two methods are the one is replace method another one is strip()method , strip()

# Functions = strip() very imp ....with the help of strip we can also do lstrip()and rstrip() and string.strip('string') this will remove the string.


def removing_white_space(string):
    return string.strip()     # string.replace('\n', '') we can use replace method also  


print(removing_white_space('Python Exercises\n'))

"""
"""
# model : Starts with

# 24. Write a Python program to check whether a string starts with specified characters

# Function: startswith('charecter') >>>> it returns the boolean if starts with specified charecter.


def check_starts_with(string, charecter):
    return string.startswith(charecter)


print(check_starts_with('w3resource', 'w3'))
"""

# Model:  Caesar encryption(not understood)
# 25. Write a Python program to create a Caesar encryption.
"""
# 26.Write a Python program to display formatted text (width=50) as output.

# medel: Textwrap

# this module is used for modifying charecters in a string in a given line 

sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
'''
import textwrap


def modifying_the_text(string):
    return textwrap.fill(string, width=50)


print(sample_text)  # see the difference.
print(modifying_the_text(sample_text))
"""

"""
# model: remove indentation

# 27. Write a Python program to remove existing indentation from all of the lines in a given text.

sample_text = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''


import textwrap


def removing_indentation_from_each_line(string):
    return textwrap.dedent(string)    # dedent function is used to remove the indentation from each line in the string


print(sample_text)  # to see the difference
print(removing_indentation_from_each_line(sample_text))
"""

"""
# model: adding something to all the lines of the string.

# 28. Write a Python program to add a prefix text to all of the lines in a string.

# input:
sample_text ='''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''

# output:
'''
>  Python is a widely used high-level, general-                                                               
> purpose, interpreted, dynamic programming                                                                   
> language. Its design philosophy emphasizes code                                                             
> readability, and its syntax allows programmers to                                                           
> express concepts in fewer lines of code than                                                                
> possible in languages such as C++ or Java.
'''

# Explanation: for adding any ch to prefix of each line of a string we have to follow this steps

# step(1): remove indentation from each line >>> textwrap.dedent(string)
# step(2): allign each line with specific width >>> textwrap.fill(string, width=number)
# step(3): add specific charecter in each line >>> textwrap.indent(string, inserting_charecter)


import textwrap


def add_prefix_word_to_each_line(string, insert_charecter):
    remove_indentation = textwrap.dedent(string)  # removing indentation
    print(remove_indentation)
    align_string = textwrap.fill(remove_indentation, width=50)  # aligning each_line correctly
    print(align_string)
    adding_prefix = textwrap.indent(align_string, insert_charecter) # adding specific charecter to each line

    return adding_prefix

print(sample_text)

print(add_prefix_word_to_each_line(sample_text, '>'))

"""
"""
# Model : setting indentation of firstline

# 29. Write a Python program to set the indentation of the first line.

# Explanation : indentation set cheyyali ante mundu prathi line ki begining lo vunna unequal spaces ni remove challi aa tharuvatha indentation
# set cheyyali .... indetation function anni lines ki kalipi okesari indentation istundi ....so manam fill function vadali

 
sample_text ='''
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    '''
import textwrap


def add_indentation_to_first_line(string):
    remove_indetation = textwrap.dedent(string)
    adding_indentation = textwrap.fill(string, initial_indent=" ", subsequent_indent= " "*4)
    return adding_indentation


print(add_indentation_to_first_line(sample_text))
"""
"""
# model: decimal model

# 30. Write a Python program to print the following floating numbers upto 2 decimal places.

# Explanation : point tharuvatha 2 decimals matrame kavali so :.2f pettali .....
#  manam console through dwara input isthe float rupamlo ivvali

# number adjusting : ikkada 2 floating point number adugamuu ...2 numbers tharuvatha vunde 3rd number  (ante 3rd number) 5<= iethe manaku kavalsina
# second number ki +1 add avuthundi

# input console lo float ivvali

def floating_numbers_upto_2_decimals(number):
    return "{:.2f}".format(number)


print(floating_numbers_upto_2_decimals(float(input("enter the number:"))))  # very important ....float rupamlo ivvali.
"""
"""
# decimal model with sign.


# 31. Write a Python program to print the following floating numbers upto 2 decimal places with a sign.

# Explanation: sign kavalante colon(:) ki,point(.) ki madhya + pedathamu..... positive , negative kina + vadathamu

def decimal_with_sign(number):
    return "{:+.2f}".format(number)


print(decimal_with_sign(float(input("entre the number:"))))

"""
"""
# removing decimals model

# 32. Write a Python program to print the following floating numbers with no decimal places.

# Explanation: floating ni remove cheyyali .... so point tharuvatha float point number ni 0 pettali ...+1 concept ikkada kuda vastundi
# int() function proper function kaadu so manam format method use chestam  ....with sign kavali ante :+. add chestamu

# input console lo float ivvali

def remove_decimals(number):
    return "{:.0f}".format(number)


print(remove_decimals(float(input("Enter the number :"))))

"""

"""
# Model: Number shifting model (shifting operator)
# very important
# 33. Write a Python program to print the following integers with zeros on the left of specified width.

# Explanation : specific width lo number vundali kaali place lo 0's vundali adi kuda left side vundali.
# manam ikkada d vadathamu.

# greatherthan symbole (>) deni vipu vunte adi first lo vuntundi.


def shift_number_with_specified_width(number):
    return "{:0<6d}".format(number)


print(shift_number_with_specified_width(int(input("Enter the specifies nnumber: "))))

"""
"""
# 34. Write a Python program to print the following integers with '*' on the right of specified width


def right_specified_width(number):
    return "{:*<6d}".format(number)


print(right_specified_width(int(input("Enter the specified nunmber: "))))
"""
"""
# model: comasaparates number

# 35. Write a Python program to display a number with a comma separator.

# It separates three three number's

def comma_saparated_number(number):
    return "{:,}".format(number)


print(comma_saparated_number(int(input("Enter the number :"))))

"""
"""
# percentage model

# 36. Write a Python program to format a number with a percentage.


def formate_with_decimals(number):
    return"{:.1%}".format(number)


print(formate_with_decimals(float(input("Enter the number:"))))

"""
"""
# very important concept's

# model: 1 : Numbers after points >>> "{:.spicify number f}".format(number)
# model: 2 : Numbers after points with sign >>> "{:+.spicify number f}".format(number)
# model: 3 : shifting numbers with shift operator ....   "{:specified_symbole>d}".format(number) ... here left align and right align ... > decides
                                                                                                                        # which side
# model: 4 : percentage model "{:.specifynumber%}".format(number)

# note: where ever .f exists mumust enter : spicifynumber and +1 concept applicable
"""
"""
# model: alignment (right, left and center)


# 37. Write a Python program to display a number in left, right and center aligned of width 10.

# Explanation:  for center alignment ^ is used.

def right_left_center_align(number):
    return "right_align :", '{:0>10d}'.format(number), "left_align:" "{:0<10d}".format(number), "center_align" "{:0^10d}".format(number)


print(right_left_center_align(int(input("Enter the number number:"))))
"""
"""
# model: number of coourences of substring in a given string.

# 38. Write a Python program to count occurrences of a substring in a string.

# Explanation: oka string lo ichina sub strings enni sarlu repeat iendi....

#  Function = count() >>>> string.count(substring) >>> it returns number.


def counting_number_of_occurence(string, substring):
    return string.count(substring)


print(counting_number_of_occurence(input("Enter the string:"), input("Enter the substring:")))

"""
"""
# Note : 

# There are two requirements :

# 1. number of occurences of each charecter: string frequency : manam each charecter ennisarlu repeat iendo chudali: dict method
# 2. number of occurences of  specified substring: count() method use cheyyali
"""

# 39. Write a Python program to reverse a string.