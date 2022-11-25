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
"""
# 39. Write a Python program to reverse a string.

# By using normal method:


def string_reverse(string):
    rev_string = ''
    for ch in string:
        rev_string=ch+rev_string
    return rev_string


# print(string_reverse(input("Enter the string:")))

# By using join() & reversed method:

# Explanation: reversed() function works on any iterable where as reverse() function only works on the list ...reverse is list method


def rev_join_method(string):
    return "".join(reversed((string)))


print(rev_join_method(input("Enter the string: ")))

"""
"""
# 40. Write a Python program to reverse words in a string

# Explanation: reverse words ante  words ni rreverse order lo print cheyyali.... reverse word internally ante ade vere concept


# Method:1 normal method

def reverse_words(string):
    new_list = []
    for word in string.split():  # by default it splits based on white spaces
        new_list = [word] + new_list
    return " ".join(new_list)


# print(reverse_words(input("Enter the reverse the string: ")))

# method:2

def reverse_string_words(string):
    new_string = ''
    for words in string.split():
        new_string = words+" "+new_string    # Here adding of " " is important....analise how this line is working
    return new_string


print(reverse_string_words(input("Enter the string :")))

"""

"""
# 41. Write a Python program to strip a set of characters from a string.


def strip_specified_charecter(string, specified_charecter):
    new_string = ''
    for ch in string:
        if ch not in specified_charecter:
            new_string += ch
    return new_string


print(strip_specified_charecter(input("Enter the string: "), input("Enter the specified_charecter: ")))

# model:2


def strip_ch(string, char):
    return "".join(ch for ch in string if ch not in char)  # join() function joins srings in the iterable 


print(strip_ch(input("enter the string:")))

"""
"""
# Model : print only repeated charecters.

# 42. Write a Python program to count repeated characters in a string.
sample_string='thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2


# Explanation: count repeated characters ante avevi repeat iyyi vuntato avi matrame chupinchali

def count_repeated_char(string):
    new_dict= {}
    for ch in string:
        if ch not in new_dict:
            new_dict[ch] = 1
        else:
            new_dict[ch] += 1
    for key, value in new_dict.items():
        if new_dict[key] >=2:     # we need repeated charecters only .... for that we can't directly access the values we have to aces the keys
            print(key, 'charecter occuring :', value)


count_repeated_char(sample_string)
"""
"""
# Maths formula ignored

# 43.Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder.
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3

"""

"""
# Method : index()

# 44. Write a Python program to print the index of the character in a string.
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2


# Important: we can find indexing by using 3 methods.

# Method:1 By using formula::::: positive index-negative index=length of string >>>> positive index = length of string-negative index
# Method 2 By using index() method:::::string.index(substring)
# Method 3 By using enumerate function

# index method:

def index_of_specified_charecter(string, charecter):
    return '{} charecter occuring : {}'.format(charecter, string.index(charecter))


# print(index_of_specified_charecter('chenchu', 'h'))

# By using enumerate function()


def index_enum(string):
    for index, ch in enumerate(string):
        print(ch, "charecter occuring at:", index)


# index_enum('chenchu')


"""

"""
# Model: finding string contains all alphabets or not

# 45. Write a Python program to check whether a string contains all letters of the alphabet.

import string


def checking(charecter):
    alphabet = set(string.ascii_lowercase)
    # return set(charecter.lower()) >= alphabet    # >= anthe ekkuva anna vundochu or equal ga anna vundochu.
    return alphabet.issubset(set(charecter))


print(checking('The quick brown fox jumps over the lazy dog'))
"""

"""
# Model : String to list of words.

# 46. Write a Python program to convert a given string into a list of words.


def string_to_list(string):
    return string.split()


print(string_to_list(input("Enter the number of words: ")))

"""
"""
# Method: convert only specific charecters upper case

# 47. Write a Python program to lowercase first n characters in a string.


def n_charecters_lower_case(string, n):
    return string[:n].upper()+string[n:]


print(n_charecters_lower_case(input("Enter the string :"), int(input("Enter the number_of char:"))))  # here we must provide int() otherwise it will 
                                                                                                                # convert to string.

"""

"""
# pending
# 48. Write a Python program to swap comma and dot in a string.

# Sample string: "32.054,23"
# Expected Output: "32,054.23"


def swap_comma_fullstop(a):
    return a.swap('.', ',')


print(swap_comma_fullstop('32.054,23'))

"""
"""
# Model : count and display only vowels

# 49. Write a Python program to count and display the vowels of a given text.

# Explanation : ichina string lo vowels enni vunnai. (aeiouAEIOU)

# This method is for counting the number of times wovel repeating(vowels enni sarlu vunnai ani)

def count_display(string, vowels):
    count_dict = {}
    for ch in string:
        if ch in vowels:
            if ch not in count_dict:
                count_dict[ch] = 1
            else:
                count_dict[ch] += 1
    return count_dict


# print(count_display(input("enter the string:"), input("Enter the vowels:")))


# correct model:

def counting_vowels(string):
    vowels = 'aeiouAEIOU'
    return len([ch for ch in string if ch in vowels]), [ch for ch in string if ch in vowels]


print(counting_vowels('w3resource'))

"""
"""
# 50. Write a Python program to split a string on the last occurrence of the delimiter.


# 51.Write a Python program to find the first non-repeating character in given string.

# Explanation : repeat kakunada vunde charecter lo first di.... dictionary prepare chey tharuvatha value 1 vundedi return chey.
# if dict[key]==1 ani condition pedithe chala 1's vunna kunda andulo first one manaki return chestundi...

def finding_first_non_repeating_char(string):
    char_freq = {}
    for ch in string:
        if ch not in char_freq:
            char_freq[ch] = 1
        else:
            char_freq[ch] += 1
    for key, value in char_freq.items():
        if char_freq[key] == 1:
            return key              # loop stops if value of key ==1....because of return statement

    return 'All are repeated charecters' # this is important because if condition is not satisfied by any value in dict it will returns


print(finding_first_non_repeating_char('ababcdcdeeeeeff'))
"""

# 52.Write a Python program to print all permutations with given repetition number of characters of a given string.

# ignored

# 52. Write a Python program to print all permutations with given repetition number of characters of a given string.
#
# ignored

"""
# 53. Write a Python program to find the first repeated character in a given string

# Explanation: repeat iena dantlo first time eadi repeat iendi ani kanukkovali


def find_first_repeated_ch(string):
    ch_dict={}
    for ch in string:
        if ch not in ch_dict:
            ch_dict[ch] = 1
        else:
            ch_dict[ch] += 1
    for key, value in ch_dict.items():
        if ch_dict[key] > 1:
            return key
    return 'All charecters are unique only'     # this is important because if condition is not satisfied by any value in dict it will returns


print(find_first_repeated_ch("bcdabcd"))

"""
"""
# very important logic
# Finding first repeating charecter and thier index also


# 54. Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest.

# Explanation: repeat iena letters lo renditi madhya indexing eadi thakkuva vundo danni return cheyyali.(first_repeated_char_smallest_distance)

# index() method>>>>string.index(ch)>>>> string lo first time ekkada repeat iendo dani index position return chestundi

def first_reap_ch_smallest_distance(string):
    ch_dict={}
    for ch in string:
        if ch in ch_dict:
            return ch, string.index(ch)
        else:
            ch_dict[ch] = 0
    return None


print(first_reap_ch_smallest_distance('caeghjiabcc'))
"""
"""
# First repeated word

# 55.Write a Python program to find the first repeated word in a given string.

# Explanation: first repeated word kanukkovali


def finding_first_repeated_charecter(string):
    word_dict={}
    for word in string.split():   # splits the strings to list of words
        if word in word_dict:
            return word
        else:
            word_dict[word] = 0

    return 'No repeated words'


print(finding_first_repeated_charecter("ab ca bc ca ab bc"))

"""
"""
# very important
# Method: second repeated word kanukkovali

# 56.Write a Python program to find the second most repeated word in a given string.

a="""
# """   Both of these issues are fixed by postponing the evaluation of annotations.
#    Instead of compiling code which executes expressions in annotations at their definition time,
#    the compiler stores the annotation in a string form equivalent to the AST of the expression in question.
#    If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where
#    this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster.
#  """
"""
def second_most_repeated_word(string):
    word_dict = {}
    for word in string.split():
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return 'The second most repeated key :{}'.format(sorted(word_dict.items(), key= lambda x: x[1], reverse=True)[1][0])
# Explan
ation :
# 1. Find dictionary frequency then sorted ascending or decending...based on index position we can get first most repeated or second mosr repeated

print(second_most_repeated_word(a))

"""
"""
# Removing spaces in the string.

# 57.Write a Python program to remove spaces from a given string.

# By using replace method or by using join method.


def remove_spaces(string):
     return string.replace(" ", "")
     return "".join(string.split())
    

print(remove_spaces("w 3 res ou r ce"))
"""
"""
# Move spaces in the string to the begining

# 58. Write a Python program to move spaces to the front of a given string.

# Explanation:
# 1. new_string = remove spaces in the string (words anni list loki append chesi , danni string loki marchu...join function use chesi)
# 2. number of spaces = len(old_string)-len(new_string)
# 3. numberof spaces*space+newstring


def move_spaces_to_begining(string):
    string_without_space = "".join([word for word in string if word != " "])     # removing whitespaces and converting into string
    # print(string_without_space)   # for difference purpose
    num_of_white_spaces = len(string)-len(string_without_space)   
    return num_of_white_spaces*" "+string_without_space


print(move_spaces_to_begining("   w3resource.com  "))
"""
"""
# Maximum repeating charecter

# 59. Write a Python program to find the maximum occurring character in a given string

# Explanation: ekkuva repeat iena charecter ni return cheyyali.


def most_repeating_charecter(string):
    string_freq = {}
    for ch in string:
        if ch not in string_freq:
            string_freq[ch] = 1
        else:
            string_freq[ch] += 1
    return '{} Is The Most Repeated Charecter In The String'.format(sorted(string_freq.items(), key=lambda x: x[1], reverse=True)[0][0])

# [0] ante maximum repeating charecter and their frequency in the tuple formate (key, value) key is charecter, frequency is value 

print(most_repeating_charecter(input("Enter the string: ")))
"""

"""
# 60. Write a Python program to capitalize first and last letters of each word of a given string.

# First word ni and last word ni capital letter loki marchali.

# Functions : upper() >>> string.upper()....>>> join() function

def capitalize_first_and_last_word(string): 
    return " ".join([word[0].upper()+word[1:-1]+word[-1].upper() for word in string.split()])  # all in single line 


print(capitalize_first_and_last_word(input("Enter the string :")))

"""
"""
# Model : remove duplicates.
# 61. Write a Python program to remove duplicate characters of a given string.


def remove_duplicate(string):
    new_string = ""
    for ch in string:
        if ch not in new_string:
            new_string += ch
    return new_string


print(remove_duplicate(input("Enter the string: ")))
"""
"""
# Model : sum all numbers in string
# 62. Write a Python program to compute sum of digits of a given string.


# By using sum function:

#Function: string.isnumeric()>>> it returns true if string is a numeric charecter peranthesis () are compulsary.
# int() funtion to convert integer

def sum_all_numbers(string):
    return sum(int(ch) for ch in string if ch.isnumeric())  # if it is numeric string then convert into int()


# print(sum_all_numbers(input("Enter the string: ")))


# Traditional approach

def sum_by_traditional_approach(string):
    sum_num = 0
    for ch in string:
        if ch.isnumeric():
            sum_num += int(ch)

    return sum_num


print(sum_by_traditional_approach(input("Enter the string: ")))
"""
"""
# Removing Zeros from the Ip adress.

# 63.Write a Python program to remove leading zeros from an IP address.

# Explanation : leading zeros is nothing but preceding zeros ex: 00012,0065 etc., we have to use int() function for removing this.
# again we have to convert this to str().


def removing_leading_zeros(ipadress):
    return '.'.join([str(int(ch))for ch in ipadress.split('.')])  # int() function is used for removing preceding zeros from the number


print(removing_leading_zeros(input("Enter the ipadress: ")))

"""
"""
# very important and little trickey

# 64. Write a Python program to find maximum length of consecutive 0's in a given binary string.

# Explanation : varusaga vunna zeros lo maximum length vundedi entha.


def finding_max_length(binary_string):
    a = [ch for ch in binary_string.split('1') if ch != ""]  # Here we will never give spaces in the string " ".we have to give ""
    b = [ch for ch in binary_string.split('1')]
    print(a)  # for understanding purpose
    print(b) # for understanding purpose
    max_length = 0
    for zeros in a:
        if len(zeros) > max_length:
            max_length = len(zeros)
    return max_length


print(finding_max_length('111000100000110'))
"""
"""
# 65.Write a Python program to find all the common characters in lexicographical order from two given lower case strings.
# If there are no common letters print "No common characters".

# doubt
"""
"""
# Anagrams:

# 66. Write a Python program to make two given strings (lower case, may or may not be of the same length) anagrams removing
# any characters from any of the strings.

# Explanation : anagrams is nothing but if two words have same character of letters may or may not be in same order is called as anagrams
# 1st string lo emi letters iethe vundo same letters 2nd string lo kunda ade vuntundi but different order lo vuntundi.


def string_frequency(string):
    string_freq = {}
    for ch in string:
        if ch not in string_freq:
            string_freq[ch] = 1
        else:
            string_freq[ch] += 1
    return string_freq


def making_anagrams(str1, str2):
    str1_string_freq = string_frequency(str1)
    print(str1_string_freq)
    str2_string_freq = string_frequency(str2)
    print(str2_string_freq)

    count = 0
    for key in str1_string_freq:
        if key not in str2_string_freq:
            count += str1_string_freq[key]
        else:
            count += max(0, str1_string_freq[key] - str2_string_freq[key])
    for key in str2_string_freq:
        if key not in str1_string_freq:
            count += str2_string_freq[key]
        else:
            count += max(0, str2_string_freq[key]-str1_string_freq[key])
    return count


print(making_anagrams(input("Enter the string: "), input("Enter the input string:")))

"""
"""
# very important logic
# 67.Write a Python program to remove all consecutive duplicates of a given string

# Explantion : pakka pakkana vunde duplicates ni remove chesi unique cheyyali.


def remove_consicutive_duplicates(string):
    if len(string) == 1:
        return string

    elif string[0] != string[1]:
        return string[0]+remove_consicutive_duplicates(string[1:]) # again calling and applying function from index 1 to end of string
    return remove_consicutive_duplicates(string[1:])    # again calling and applying function from index 1 to end of string


print(remove_consicutive_duplicates(input("Enter the string:")))

"""
"""
# 68. Write a Python program to create two strings from a given string. Create the first string using those character which occurs only once
# and create the second string which consists of multi-time occurring characters in the said string.

# Explanation: oka string nunchi rendu string's create cheyyali>>>> first string lo only unique(non-repeated) charecters eavi iethe original string lo
# vunnayo avi matrame vundali>>>second string lo Repeated characters (non-unique) eavithe original string lo vunnayo avi matrame vundali.


def create_two_strings(string):
    string_freq = {}
    for ch in string:
        if ch not in string_freq:
            string_freq[ch] = 1
        else:
            string_freq[ch] += 1
    first_string = "".join([key for key in string_freq if string_freq[key] == 1])   # if frequency is equals to 1.
    second_string = "".join([key for key in string_freq if string_freq[key] > 1])   # if frequency is greatherthan 1.
    return "First string = {}\nSecond string = {}".format(first_string, second_string)


print(create_two_strings(input("Enter the string :")))

"""
"""
# 69. Write a Python program to find the longest common sub-string from two given strings.

# doubt
"""
"""
# 70. Write a Python program to create a string from two given strings concatenating uncommon characters of the said strings.

#  Explanation : rendu strings lo common ga leni letters tho string create cheyyali


def create_strings(string1, string2):
    a = "".join([ch for ch in string1 if ch not in string2])
    b = "".join([ch for ch in string2 if ch not in string1])
    return a+b


print(create_strings(input("enter the string1:"), input("enter the string2:")))

"""
"""
# 71. Write a Python program to move all spaces to the front of a given string in single traversal.

# Explanation : spaces anni string first lo move cheyyali nenu chese mistake " " pettali kani "" pettanu... in a single traversal anedi confuse
# cheyyadaniki pettadu..... "" & " " deni madhya difference kinda choodu

def move_spaces_to_the_front(string):
    string_with_out_spaces = ''.join([ch for ch in string if ch != " "])  # "">>> this is not a empty string it's length is zero
    number_of_spaces = len(string)-len(string_with_out_spaces)          # " " >>> this is empty string it's length is one

    return " "*number_of_spaces+string_with_out_spaces


print(move_spaces_to_the_front(input("Enter the string:")))
"""

"""
# 72. Write a Python code to remove all characters except a specified character in a given string.
# Original string
# Python Exercises
# Remove all characters except P in the said string:
# P
# Original string
# google
# Remove all characters except g in the said string:
# gg
# Original string
# exercises
# Remove all characters except e in the said string:
# eee


# Explanation : ichina specified charecters thappa migatha charecters  anni remove cheyyali. little complicated related to traversal of which elements


def remove_all_except_specified(string, specified_char):
    return "".join([ch for ch in string if ch in specified_char])


print(remove_all_except_specified(input("Enter the string :"), input("Enter the specified_string :")))
"""

"""
# 73. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.


def count_upper_lower_special_number(string):
    upper = lower = special = number = 0
    for ch in string:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            number += 1
        else:
            special += 1

    return'lower_case_letters = {}\nupper_case_letters = {}\nspecial_charecters = {}\nnumbers ={}'.format(lower, upper, special, number)


print(count_upper_lower_special_number(input("Enter the string :")))
"""

# 74 ,75 window problem ignored


# 76 substrings problem doubt


# 77. Write a Python program to count number of non-empty substrings of a given string.
# doubt

"""

# Model: Counting alphabets which are same position in the small abcd and capital ABCD

# 78. Write a Python program to count characters at same position in a given string (lower and uppercase characters) as in English alphabet.


# Explanation : ichina string lo vunna alphabets original alphabet positions lo vunte count+1 cheyyali.


def count_character_position_count(string_obj):
    count = 0
    for i in range(len(str(string_obj))):
        if i == ord(string_obj[i])-ord('A') or i == ord(string_obj[i])-ord('a'):
            count += 1
    return count


print(count_character_position_count(input("Enter the string: ")))

"""
"""
# Model: Finding smallest and largest word in the given string.

# 79. Write a Python program to find smallest and largest word in a given string


# Explanation: 1. string ni list loki marchukovali (marche tappudu emepty strings remove cheyyali)
# 2. smallest and largest word anedi list lo first word ga tesukovali.
# 3. list lo vunna prathi word tesukoni daani yokka length largest word length kanna peddadi ga vunte appudu largest word =word
# 4. list lo vunna prathi word tesukoni danni yokka length smallest word kanna thakkuva vunte smallest word =word.
#  last lo return smallest word and largest word


def finding_smallest_largest_word_in_string(string_obj):
    list_of_words = [word for word in string_obj.split() if word != ""]
    largest_word=smallest_word= list_of_words[0]
    for word in list_of_words:
        if len(word) > len(largest_word):
            largest_word = word
        if len(word) < len(smallest_word):
            smallest_word = word
    return 'The smallest word is: {} \nThe largest word is :{}'.format(smallest_word, largest_word)


print(finding_smallest_largest_word_in_string(input("Enter the string_obj :")))
"""

"""
# 80. Write a Python program to count number of substrings with same first and last characters of a given string.

# it is sub string problem.


# 81. Write a Python program to find the index of a given string at which a given substring starts.
# If the substring is not found in the given string return 'Not found'.

#  it is sub string problem
"""
"""
# Model: filling string with specified width.

# 82. Write a Python program to wrap a given string into a paragraph of given width.
# Sample input:
a='The quick brown fox.'
# Input the width of the paragraph: 10
# Result:
# The quick
# brown fox.

import textwrap

def wrap_string(string_obj):
    a = textwrap.fill(string_obj, width=10)
    return a


print(wrap_string(input("Enter the string: ")))
"""
"""
# Model: converting  Intiger to different values.

# 83. Write a Python program to print four values decimal, octal, hexadecimal (capitalized), binary in a single line of a given integer.
# Sample Output:
# Input an integer: 25
# Decimal Octal Hexadecimal (capitalized), Binary
# 25 31 19 11001


# Explanation: number ni matrame manam decimal, octal, hexadecimal, binary ga marchagalam .... dentlo first two letters matram indication letters 
# denni manam print cheyyalsina paniledu.


def convertion_of_int(i):
    return 'The decimal value is ={},\nThe octal value is ={}\nThe Hexadecimal value is ={},\nThe binary ={}'.format(str(i),
                                                                                                                     oct(i)[2:],
                                                                                                                     str(hex(i)[2:]).upper(),
                                                                                                                     bin(i)[2:])
print(convertion_of_int(25))

"""

"""
# Model: swapping cases (upper to lower , lower to upper)


# 84. Write a Python program to swap cases of a given string.
# Sample Output:
# pYTHON eXERCISES
# jAVA
# nUMpY

def swap_cases(string_obj):
    return ''.join([ch.lower() if ch.isupper() else ch.upper() for ch in string_obj])


print(swap_cases(input("Enter the string : ")))

"""

"""
# Model: Byte array ti hexa decimal.

# 85.Write a Python program to convert a given Bytearray to Hexadecimal string.
# Sample Output:
# Original Bytearray :
# [111, 12, 45, 67, 109]
# Hexadecimal string:
# 6f0c2d436d

# ignored.


"""
"""
# Model: Deleting the all occurance of specified string.

# 86. Write a Python program to delete all occurrences of a specified character in a given string.
# Sample Output:
# Original string:
# Delete all occurrences of a specified character in a given string
# Modified string:
# Delete ll occurrences of specified chrcter in given string

# Explanation: icchina line lo specific charecter delete cheyyali.

# With replace method:

def del_all_occur(string_obj):
    return string_obj.replace('a', "")


# print(del_all_occur(input("Enter the string_obj: ")))


# with join method:

def del_all_occurances(string_obj, specific_charecter):
    return "".join(["" if charecter == specific_charecter else charecter for charecter in string_obj ])


# print(del_all_occurances(input("Enter the string: "), input("Enter the string: ")))


# Normal method:


def normal(string_obj, specific_charecter):
    line =''
    for ch in ["" if charecter == specific_charecter else charecter for charecter in string_obj]:
        line+=ch

    return line


print(normal(input("Enter the string_obj: "), input("Enter the specific_charecter: ")))

"""

"""
# Model: Compute common values.

# 87. Write a Python program find the common values that appear in two given strings.
# Sample Output:
# Original strings:
# Python3
# Python2.7
# Intersection of two said String:
# Python

# By using list comprehension and join() method.

def common_values(string1, string2):
    return ''.join([ch for ch in string1 if ch in string2])


# print(common_values(input("Enter the string1 :"), input("Enter the string2 :")))


# by using normal method:

def common_values_normal(string1, string2):
    common_word =''
    for ch in string1:
        if ch in string2:
            common_word += ch

    return common_word


# print(common_values_normal(input("Enter the string1:"), input("Enter the string2:")))

# by using set :::: don't use set result will comes in unorderd string.

"""
"""
# Model: Checking given string with certain specifivations.

# 88. Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length.
# Sample Output:
# Input the string: W3resource
# ['Valid string.']

# Explanation: ichina string lo 1. string lo oka capital letter vunda ?  2. oka lower letter vunda ? 3. oka number vunda ? 4. minim length vunda?

# output ikkada list lo kavali so manam list tesukunnam.

# ikkada prathi condition satisfy avvali


def checking_strings(string_obj, minimum_length):
    messege =[]
    if not any(ch.isupper() for ch in string_obj):
        messege.append('The string must have atleast one upper charecter ')
    if not any(ch.islower() for ch in string_obj):
        messege.append('The string must have atleast one lower')
    if not any(ch.isdigit() for ch in string_obj):
        messege.append('The string must have one digit')
    if len(string_obj) < minimum_length:   # length should have atleast specified minimum length.
        messege.append('The string must have minimum_length of:{}'.format(minimum_length))
    else:
        messege.append('This is a valid string.')

    return messege


print(checking_strings(input("Enter the string_obj : "), int(input("Enter the minimum_length :"))))

"""

"""
# Model : removing unwanted charecters.

# 89. Write a Python program to remove unwanted characters from a given string.
# Sample Output:
# Original String : Pyth*^on Exercis^es
# After removing unwanted characters:
# Python Exercises
# Original String : A%^!B#*CD
# After removing unwanted characters:
# ABCD


# Explanation: ikkada unwanted items lo vunna prathi element ni iteration dwara bayataki tesukoni vachi string lo remove cheyyali...
# very very important .... manam replace method ki oka varilbe adikuda function lo define chesina stringobject varible ni assign cheyyali...ledante-
# answer raadu.

def removal_of_unwanted_items(string_obj, unwanted_items):
    for ch in unwanted_items:
        string_obj = string_obj.replace(ch, "")       # here we must assign a varible....other wise we wont get proper answer
    return string_obj


# print(removal_of_unwanted_items(input("Enter the string:"), input("Enter the unwanted items:")))

# Without replace method....

def removal_normal(string_obj, unwanted_items):
    new_string = ''
    for ch in string_obj:
        if ch not in unwanted_items:  # unwanted items lo lekapothe danni add chey.
            new_string += ch

    return new_string


print(removal_normal(input("Enter the new string: "), input("Enter the unwanted items:")))
"""
"""
# Model: removing duplicate words.

# 90. Write a Python program to remove duplicate words from a given string.
# Sample Output:
# Original String:
a = 'Python Exercises Practice Solution Exercises'
# After removing duplicate words from the said string:
# Python Exercises Practice Solution

# By using list and join method.

# split() : it is used to split the words to the list of words...default separator is white space.
# join(): it joins the string items in the iterable as the string by using specific join's


def remove_duplicate_words(string_obj):
    new_list = []
    [new_list.append(word) for word in string_obj.split() if word not in new_list]
    return " ".join(new_list)


print(remove_duplicate_words(input("Enter the string: ")))

# normal method:


def remove_duplicates_normal(string_obj):
    new_string = ''
    for word in string_obj.split():
        if word not in new_string:
            new_string = new_string+" "+word
    return new_string


print(remove_duplicates_normal(input("Enter the strings: ")))

"""
"""
# Model: converting all list object to a single string.

# 91. Write a Python program to convert a given heterogeneous list of scalars into a string.
# Sample Output:
# Original list:
# ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
# Convert the heterogeneous list of scalars into a string:
# Red,100,-50,green,w,3,r,12.12,False


# Important : manam console dwara input enter chesetappudu string object thappa inka ea object manam enter cheyyalanna eval function lopala input func
# rayali ledhante proper output raada.... ea datatype ichina adi string rupamlo tesukuntundi.


def list_obj_to_string_obj(list_obj):
    return ','.join([str(item) if type(item) != str else item for item in list_obj])


print(list_obj_to_string_obj(eval(input("Enter the list of words: "))))

"""

"""
# Model: finding similarity between strings.

# 92. Write a Python program to find the string similarity between two given strings.

# From Wikipedia:
# In computer science, approximate string matching (often colloquially referred to as fuzzy string searching) is the technique of finding strings
# that match a pattern approximately (rather than exactly).


# Explanation: similarity/sequence matching/fuzzy string searching anna okate. rendu strings madhya enni substrings match iyyi vundo daani ratio
# kanukkovali.

# New module : difflib (in difflib we have to import SequenceMatcher function)

# SequenceMatcher function lo manam string pass chesetappudu kachithamga danni oka vatible ki assign cheyyali endukante ratio kanukkovadaniki
# aa tharuvatha ratio kanukkovali (ratio() function dwara)


from difflib import SequenceMatcher


def sequence_matcher(string1, string2):
    return 'The string similarity between two strings are: {}'.format(SequenceMatcher(a=string1, b=string2).ratio())


print(sequence_matcher(input("Enter the string1 :"), input("Enter the string2: ")))

"""

"""
# Model: Extracting numbers from the string.

# 93. Write a Python program to extract numbers from a given string.
# Sample Output:
# Original string: red 12 black 45 green
# Extract numbers from the said string: [12, 45]


def extracting_numbers(string_obj):
    return [int(ch) for ch in string_obj.split() if ch.isdigit()]


print(extracting_numbers(input("Enter the string_obj :")))

"""
"""
# 94. it is hexa decimal and rgb components problem ...ignored
"""
"""
# 95. it is also a hexa decimal and rgb components problem ... ignored
"""
"""
# Model: camel case.

# 96. Write a Python program to convert a given string to camelcase.
# Sample Output:
# javascript
# fooBar
# fooBar
# foo.Bar
# fooBar
# foobar
# fooBar

# Note: camel case ante :: first word thappa remaining words lo vunna prathi word first letter capital lo vundali...kaani first word lo first letter
# small letter lo vundali.


# we have to do this problem while doing reguular expressions.
"""
"""
# Model: snake case

# 97. Write a Python program to convert a given string to snake case.
# Sample Output:
# java_script
# foo_bar
# foo_bar
# foo.bar
# foo_bar
# foo_bar
# foo_bar

# Note : snake case ante string lo vunna every word underscore '_' tho join iyyi vundali

# regular expressions.
"""
"""
# 98. Write a Python program to decapitalize the first letter of a given string.
# input : 'Java Script' 'Python'

# Sample Output:
# java Script
# python

# capitalise = string lo fisrt letter upper case lo vundali..... decaptilize = string lo first letter lowecase lo vundali.


def de_cap(string_obj):
    return string_obj[0].lower()+string_obj[1:]   # wea are decaptalizing the string.


print(de_cap(input("Enter the string_obj: ")))

"""
"""
# Model : multi line strings ni oka list lo pettali.

# 99. Write a Python program to split a given multiline string into a list of lines.
# Sample Output:
# Original string:
a='''
This
is a
multiline
string.
'''
b=['This', 'is a', 'multiline', 'string']
# Split the said multiline string into a list of lines:
# ['This', 'is a', 'multiline', 'string.', '']

# Note : normal ga split() function anedi white space adharam ga split chestundi.... manam kaani '\n' ni pedithe  new line adharam ga split avutundi

# string.split('\n') anna string.splitlines() anna rendu okate....

# string.split('\n') and string.splitlines() ee rendu commands manaki new line adharamga split chesi list lo pedutundi.

# Model:1 multiline string to a list.


def multiline_to_list(string_obj):
    return string_obj.split('\n')


# print(multiline_to_list(a))

# kinda ichina anni print statements pina rasina code rendu okate.

# print(a.split('\n'))
print(a.splitlines())

# Model:2 convert string to multiline string.

b='This\nis\nmultiline\nstring'
print(b)
"""
"""
# Model : very important model...  Every word in string cna contain repeated word or not.

# 100. Write a Python program to check whether any word in a given sting contains duplicate characrters or not. Return True or False.
# Sample Output:
# Original text:
a = 'Fillter out the factorials of the said list.'


# Check whether any word in the said sting contains duplicate characrters or not!
# False
# Original text:
# Python Exercise.
# Check whether any word in the said sting contains duplicate characrters or not!
# False
# Original text:
# The wait is over.
# Check whether any word in the said sting contains duplicate characrters or not!
# True

# Explanation string lo prathi word lo eadina duplicate charecters vunnaya ani chesk cheyyali.

# without using in built.

# 1. mundu string ni list loki marchukovali  2. tharuvatha prathi word tesukoni daaniki rendu for loops raasi check cheyyali.

def check(string):
    words = string.split()
    for word in words:
        for i in range(len(word)):
            for j in range(i+1, len(word)):
                if word[i] == word[j]:

                    return '{}'.format(' word in a string contains duplicates')
    return "{}".format('each word in a string doesnot contains it does not contains duplicates.')


print(check(input("Enter the string: ")))

# Method :2 set method.


# set method and len() function use chesi kanukkovochu.

# with using inbuilt  set method

def check_buid(string):
    words_list = string.split()
    for word in words_list:
        if len(word) > len(set(word)):
            return '{}'.format('it contains duplicates')


# print(check_buid(input("enter the string:")))

"""
"""
# 101. Write a Python program to add two strings as they are numbers (Positive integer values). Return a message if the numbers are string.
# Sample Output:
# 42
# Error in input!
# Error in input!

# Explanation: string lo vunna numbers ni add cheyyali...
# 2.positive intiger values matrame ani cheppadu so only positive numbers and there is no points

# integers : intigers only 2 types positive and  negative....there is no points.
# digits = is 0 to 9


# what is question ::: ichina string ni numbers elagithe add chestamo ala  add chesi malli string loki convert cheyyali. (as they are numbers ki adi
                                                                                                                                # meaning)

def add_strings(num1, num2):
    num1, num2 = '0'+num1, '0'+num2   # v.imp: okavela input emepty iste 0's print avvadaniki ee line ....this is very imp...'0' ni string lo pettem
    if num1.isdigit() and num2.isdigit():                                       # endukante output manaki string lo ivvali kanuka.
        return str(int(num1)+int(num2))
    return 'Error in input'


print(add_strings(input("Enter the num1 :"), input("Enter the num2 :")))


# very very important point : isnumeric(), isdigit() functions negative values ni allow cheyyavu and point values ni allow cheyyavu ...only postitive
# and without point values matrame allow chestundi.

"""
"""
# Model: Remove punctuation's

102. Write a Python program to remove punctuations from a given string. Go to the editor
Sample Output:
Original text:
String! With. Punctuation?
After removing Punctuations from the said string:
String With Punctuation

From Wikipedia,
Punctuation is the use of spacing, conventional signs, and certain typographical devices as aids to the understanding and correct reading of ---- 
written text. The marks, such as full stop, comma, and brackets, used in writing to separate sentences and their elements and to clarify meaning.


import string


def remove_punc(string_obj):
    for punc in string.punctuation:  # string module lo eamemi punctuvations vunnayo avi vastundi.. print([ch for ch in string.punctuation])
        string_obj = string_obj.replace(punc, '')  # Note: replace method lo kachitham ga varible ni assign cheyyali adi kuda ae string object ni
    return string_obj                                                  # iethe change chestamo danne assign cheyyali idi chala important point.


# print(remove_punc(input("Enter the string_object :")))

"""
"""
# Model: Replace method:::::idi chala  confuse chesindi denni clarity ga chudali.

# 103. Write a Python program to replace each character of a word of length five and more with hash character
# Sample Output:
# Original string:
a='Count the lowercase letters in the said list of words'
# Replace words (length five or more) with hash characters in the said string:
# ##### the ######### ####### in the said list of ######
# Original string:
b= 'Python - Remove punctuations from a string:'
# Replace words (length five or more) with hash characters in the said string:
# ####### - ###### ############ from a #######


# Explanation: length 5 mariyu anthakanna ekkuva vunna strings ni ade length tho '#' symbole tho marchali.


def replace_hash(string_obj):
    for word in string_obj.split():   # string.split() use cheste string lo vunna words anni list loki vastundi ... original string alane vuntundi
        if len(word) >= 5:
            string_obj = string_obj.replace(word, '#'*len(word))    # manam ikkada string_obj lo replace chestunnam anduvalle string_obj.replace
                                                        # manam word lopala replace cheyyadam ledu word= word.replace() ani ivvakudadu
    return string_obj


print(replace_hash(input("Enter the string :")))

"""
"""
# 104. Write a Python program that capitalizes the first letter and lowercases the remaining letters of a given string.
# Sample Data:
a="Red Green WHITE"    #-> "Red Green White"
# ("w3resource") -> "W3resource"
# ("dow jones industrial average") -> "Dow Jones Industrial Average"


# Explanation: first letter ni uppercase cheyyali lower remaining ni lowecase cheyyali..

# 1.mundhu string lo vunna words anni list rupam loki techukovali... 2. emepty string tesukovali 3. slice dwara upper and lower chesi 
#   **** 3. daanni   +" "+ tho add cheyyali ledante words madhyalo spaces raavu.

def cap_lower(string_obj):
    new_string = ''
    for word in string_obj.split():
        new_string = new_string+" "+word[0].upper()+word[1:].lower()
    return new_string


print(cap_lower(input("Enter the string :")))


# *****Method:2 By using capitalize method and join() function.  always prefer this method.

#  capitalize() = string.capitalize() first letter matram upper case ga marustundi remaining motham lower case ga marunstundi...

def test(strs):    
    return ' '.join(word.capitalize() for word in strs.split())  # split() method mana cal calculation purpose kosam matrame vadathamu adi original 
                                                                                                # string ni eami cheyyadu.
                                                                                            
# join() function mundu ''.join() pettala leda ' '.join() ani pettala '' or ' ' ... have a clear vision.
                                                                                                
"""

"""
# Model: Extraction of name from email adress.

# 105. Write a Python program to extract and display the name from a given email address.
# Sample Data:
a = "john@example.com"    #-> ("john")
b = "john.smith@example.com"  #-> ("johnsmith")
c = "fully-qualified-domain@example.com"  # -> ("fullyqualifieddomain")


# Model:1 By using index and join method.

def extract_name(email_obj):
    return ''.join([ch for ch in email_obj[:email_obj.index('@')] if ch.isalpha()])



# Note: join function bayata space pettala vodda ani doubt ravali .... emailadress lo by default ga google spaces accept cheyyavu...so no spaces in
                                                                                                            # mail_id.

print(extract_name(input("Enter the email_address :")))


# Model:2 by using split() method and join() function.


def extrt_name(email_obj):

    return ''.join([ch for word in email_obj.split('@')[0] for ch in word if ch.isalpha()])


# Silly points : inni saarlu chesina tharuvatha naku telisindi join() functio enni forloops iena pettochu ani. 

print(extrt_name(input("Enter the email_address :")))

"""
"""

# Model : Eleminating repeated consicutive. (pakka pakkana vunna duplicates ni remove cheyyali)

# 106. Write a Python program to remove repeated consecutive characters and replace with the single letters and print new updated string.
# Sample Data:
# ("Red Green White") -> "Red Gren White"
# ("aabbbcdeffff") -> "abcdef"
# ("Yellowwooddoor") -> "Yelowodor"


# Explanation : new_string,old_string ni string_obj[0] ga tesukoni, string lo second letter  comparision cheyyali if previous value != string_obj[i]
# iethe string ki add chey ang previous value = string_obj[i].

def remove_only_con_duplicates(string_obj):
    new_string = prev_value = string_obj[0]     # initilize new_string, prev_value as string_obj[0]
    for i in range(1, len(string_obj)):      # 1st index nunchi manam compare cheyyali. anduke 1 nunchi range tesukunnam.
        if string_obj[i] != prev_value:
            new_string += string_obj[i]
            prev_value = string_obj[i]
    return 'The value of the new_string after removing consicitive duplicates is = {}'.format(new_string)


print(remove_only_con_duplicates(input("Enter the string_obj :")))

"""

"""
# Model : Same charecters at same index..... super method....

# 107. Write a Python program to that takes two strings. Count the number of times each string contains the same three letters at the same index

# Sample Data:
# ("Red RedGreen") -> 1
# ("Red White, Red White) -> 7
# ("Red White White Red") -> 0
#
# Explanation: rendu strings tesukoni dantlo first  three words match ienda leda tharuvatha oka charecter vadilesi next three words ala check ----
#  chesukuntuu povale.


def check_three(str1, str2):
    count = 0
    for i in range(len(str1)-2):  # manam threee charecters matrame check chestunnam and kinda +3 pedutuunam anduvalla ikkada -2 ...
        if str1[i:i+3] == str2[i:i+3]:                                        # ledante out of range vastundi...
            count += 1
    return count


print(check_three(input("Enter the str1 : "), input("Enter the str2 :")))

"""

"""
# 108. Write a Python program to that takes a string and returns # on both sides each element, which are not vowels.
# Sample Data:
# ("Green" -> "-G--r-ee-n-"
# ("White") -> "-W--h-i-t-e"
# ("aeiou") -> "aeiou"


# Explanation : string lo charecter wowel kakapothe aa string ki mundu, venakala edo okati kalipi add chey ledante  normal ga add chey

# Model:1 traditinal approach.

def add_both_sides(string_obj):
    new_str = ''
    for ch in string_obj:
        if ch not in "AEIOUaeiou":
            new_str += '-' + ch + '-'
        else:
            new_str += ch
    return new_str


# print(add_both_sides(input("Enter the string_obj: ")))


# Method :2 by using list comprehension.

def add_symb(string_obj):
    print(['-'+ch+'-' if ch not in 'AEIOUaeiou' else ch for ch in string_obj])  # for understanding purpose.
    return ''.join(['-'+ch+'-' if ch not in 'AEIOUaeiou' else ch for ch in string_obj])


print(add_symb(input("Enter the string :")))

"""

"""
# Model : Counting the number of leaf years with in the range

# 109. Write a Python program that counts the number of leap years within the range of years. The range of years should be accepted as a string.
# Sample Data:
# ("1981-1991") -> 2
# ("2000-2020") -> 6

# Explanation : ichina range lo enni leaf years vunnayo kanukkovali.


# date time module problem.


# Model: Insert space before specified char.

# 110. Write a Python program to insert space before every capital letter appears in a given word.
# Sample Data:
# ("PythonExercises") -> "Python Exercises"
# ("Python") -> "Python"
# ("PythonExercisesPracticeSolution") -> "Python Exercises Practice Solution"


def insert_space(string_obj):
    print([' ' + ch if ch.isupper() else ch for ch in string_obj]) # for clarity purpose.
    return "".join([' ' + ch if ch.isupper() else ch for ch in string_obj])    # prathi saaeri join mundu confusion '' or ' ' ani...output choosi
                                                                                                    # daani adharamga pettali...

print(insert_space(input("Enter the string_obj : ")))


"""

"""
# Model : Replacing charecters with their alphabatical numbers values


# 111. Write a Python program that takes a string and replaces all the characters with their respective numbers

# Sample
# Data:
# ("Python") -> "16 25 20 8 15 14"
# ("Java") -> "10 1 22 1"
# ("Python Tutorial") -> "16 25 20 8 15 14 20 21 20 15 18 9 1 12"


# Explanation : ch yokka alphabatic order number ni print cheyyali
# 1. string motham ni upper case or lower case loki marchali.
# 2. prathi charecter tesukoni adi alpha bet iethe daani ordinal value nunchi teseyali. capital = ord(capital_letter-64)
# small_letter = ord(small_letter - 96)

def replace_char_ord(string_obj):
    return " ".join([str(ord(ch)-96) for ch in string_obj.lower() if ch.isalpha()])


# Formula : upper iethe 64 ni ...lower iethe 96 ni ordinal values nunchi teseyali.


# print(replace_char_ord(input("Enter the string_obj : ")))
"""

"""
# Model : adding two string numbers.

# 112. Write a Python program to calculate the sum of two numbers given as strings. Return the result in the same string representation.
# Sample Data:
# ( "234242342341", "2432342342") -> "236674684683"
# ( "", "2432342342") -> False ( "1000", "0") -> "1000"
# ( "1000", "10") -> "1010"


def add_str(str1, str2):
    if str1 == '' or str2 == '':
        return False
    return str(int(str1) + int(str2))


# print(add_str(input("Enter the str1 :"), input("Enter the str2 :")))

#  Note : there is one big method also available.
"""

"""

Model : Sorted alphabatically by first charecter.


# 113. Write a Python program that returns a string sorted alphabetically by the first character of a given string of words.


# Sample Data:
# ("Red Green Black White Pink") -> "Black Green Pink Red White"
# ("Calculate the sum of two said numbers given as strings.") -> ("Calculate as given numbers of sum said strings. the two")
# ("The quick brown fox jumps over the lazy dog.") -> ("The brown dog. fox jumps lazy over quick the")


# Explanation : string lo vunde prathi word aa word lo vunna first letter adharamga sort cheyyali.... daaniki rendu methods sort(),sorted()


def sorted_alphabatically(string_obj):
    return ' '.join(sorted(string_obj.split(), key=lambda x: x[0], reverse=False))   # 0 means first charecter 1 means second charecter and so on...


# print(sorted_alphabatically(input("Enter the string value: ")))


# sort() function lo nenu chese thappulu ::: danni nenu vere varible ki assign chestunna....

# list.sort(key= lambda x:x[n], reverse =False/True) 


def sort_alphabaticall(string_obj):
    a = string_obj.split()
    a.sort(key=lambda x: x[0], reverse= False)  # ekkada iethe manam sort() ani rastamo  aa line ni vere varible ki assign cheyyakudadu ...
    return " ".join(a)


print(sort_alphabaticall(input("Enter the string value: ")))

# Note : ekkadithe sort() function rastamo aa line ni manam vere varible ki assign cheyyakudaddu.

"""