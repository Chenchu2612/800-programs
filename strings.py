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
# 9. Write a Python program to remove the nth index character from a nonempty string.


def remove_ch_in_string(string, n):
    return string[:n]+string[n+1:]


print(remove_ch_in_string('chenchu', 0))



























