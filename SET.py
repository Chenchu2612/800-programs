"""
# 1. Write a Python program to create a set

a = set()  # note inside any constructor function i.e list(),tuple(), set(), dict() We must pass an "iteable" otherwise
b = set([1, 2, 3, 4, 5])                                 # error will raise
c = {1, 2, 3, 4}
"""
"""
# 2. Write a Python program to iteration over sets.


def iterate_set(item):
    for x in item:
        print(x)


iterate_set({1,2,3,4})


num_set = set([0, 1, 2, 3, 4, 5])
for n in num_set:
  print(n, end=' ')

char_set = set("w3resource")  
for val in char_set:
    print(val, end=' ')
"""
"""
# 3.Write a Python program to add member(s) in a set.

# there are two methods are available one is add method and another one is update method
# add = adds single item to the set
# update = all items in the iterable object will add to the set


def add_to_set(old_set, item):
    old_set.add(item)               # with add method --->> set.add(item)
    return old_set


print(add_to_set({1, 2, 3}, 5))


def update_to_set(old_set, iterable):
    old_set.update(iterable)        # with update method --->> set.update(iterable)
    return old_set


print(update_to_set({1,2,3}, [4,5,6]))
"""
"""
# 4. Write a Python program to remove item(s) from a given set.

# There are 5 methods are available to remove elements from the set i.e (cd rp)

# c : clear() : it clears the all elements from the set result will be the empty set.
# d : discard() : it removes the specific element from the set if specific element is not appear in the set it won't
#                  raise an error
# d: del : it deletes the set permanently
# r : remove() : it removes the specified element from the set if specified set is not appear then it will raise an
#                error

# p : pop() : this method will remove the random element from the set and returns the removed element

a = {1, 2, 3, 4, 5, 6}


def clear_the_set(set_obj):
    set_obj.clear()         # set.clear()
    return set_obj


# print(clear_the_set(a))


def discard_the_set(set_obj, element):
    set_obj.discard(element)
    return set_obj


# print(discard_the_set(a, 5))


def del_set(set_obj):
    del set_obj
    return set_obj


# print(del_set(a))


def remove_element(set_obj, element):
    set_obj.remove(element)               # set.remove(element)
    return set_obj


# print(remove_element(a, 5))


def pop_element(set_obj):
    b = set_obj.pop()             # set.pop() --->> the pop method returns the removed item
    return 'The Resultant set: {0}, The removed item : {0}'.format(set_obj, b)


print(pop_element(a))

"""
"""
# 5. Write a Python program to remove an item from a set if it is present in the set.

a = {1, 2, 3, 4, 5, 6}


def discard_item(set_obj, item):
    set_obj.discard(item)           # set.discard(item) -->> it will removes the specified element if it is present
    return set_obj


print(discard_item(a, 8))

"""
"""
# 6. Write a Python program to create an intersection of sets.

a = {1, 2, 3, 4, 5}
b = {5, 6, 4, 9, 10, 1}
c = {20, 34, 1}


def inter_sec(set1, set2, set3):           # we can mention set1 & set2
    # return set1 & set2 & set3  # Note : Intersection and union method will returns the new set (resultant set will
    return set1.intersection(set2, set3)                                # contains the common elements of all sets)


# print(inter_sec(a, b, c))


# method: 2

def inter(item1, item2, item3):
    result = set()
    for i in item1:
        if i in item2 & item3:     # '&' symbole will get correct result
            result.add(i)
    return result


print(inter(a, b, c))
"""
"""
# 7. Write a Python program to create a union of sets.

a = {1, 2, 3, 4, 5}
b = {5, 6, 4, 9, 10, 1}
c = {20, 34, 1}


def union_set(item1, item2, item3):
    return item1 | item2 | item3         # result_set = set1.union(set2)


print(union_set(a, b, c))

"""

"""
# 8. Write a Python program to create set difference.

a = {1, 2, 3, 4, 5}
b = {5, 6, 4, 9, 10, 1}
c = {20, 34, 1}


def diff(item1, item2):
    result = item1.difference(item2)    # Note = difference method will returns the new set
    return result                       # -->> new_set = set1.difference(set2) or set1-set2



print(diff(a, b))

"""
"""
# 9. Write a Python program to create a symmetric difference.


a = {1, 2, 3, 4, 5}
b = {5, 6, 4, 9, 10, 1}
c = {20, 34, 1}


def symic_diff(item1, item2):                         # Note : it will return new set -->> set1.symmetric
    sym_diff = item1.symmetric_difference(item2)      # -->> set1.symmetric_difference(set2) -- other than common will
    return sym_diff                                                                                         #come


print(symic_diff(a, b))

"""
"""
# 10.Write a Python program to check if a set is a subset of another set


def is_sub(item1, item2):
    return item1.issubset(item2)    # It returns True if it is subset  we can use <= symbol also 


print(is_sub({1, 2}, {1, 2, 3, 4}))
"""

"""
# 11. Write a Python program to create a shallow copy of sets


# Note : Shallow copy is a bit-wise copy of an object. 
# A new object is created that has an exact copy of the values in the original object.

setp = set(["Red", "Green"])
setq = set(["Green", "Red"])

#A shallow copy

setr = setp.copy()
print(setr)
"""

"""
# 12. Write a Python program to remove all elements from a given set

a = {1, 2, 3, 4, 5}


def remove_all(item):
    item.clear()
    return item


print(remove_all(a))
"""
"""
# 13. it is frozen set problem


# 14. Write a Python program to find maximum and the minimum value in a set.

# This is my approach

a = {1, 2, -5, 9, 0}
max = 1        # initializing max value by taking one value from the set
for i in a:
    if i > max:
        max = i
print(max)

min = 1

for i in a:
    if i< min :
        min = i
print(min)


# w3 schools 
#Create a set
setn = {5, 10, 3, 15, 2, 20}
print("Original set elements:")
print(setn)
print(type(setn))
print("\nMaximum value of the said set:")
print(max(setn))
print("\nMinimum value of the said set:")
print(min(setn))

"""
"""
# 15. Write a Python program to find the length of a set.

method:1
def len_set(item):
    return len(item)


print(len_set({1, 2}))


method : 2


def len_set1(item):
    length=0
    for i in item:
        length += 1

    return length

print(len_set1({1,2,3}))
"""

"""
# 16. Write a Python program to check if a given value is present in a set or not.


def present_or_not(set1, item):
    for i in set1:
        if i == item:
            return True
    return False


print(present_or_not({1, 2, 3}, 2))


# in w3 resource they used in and not in operator

"""

"""
# 17. Write a Python program to check if two given sets have no elements in common.


def no_ele_common(item1, item2):     # isdisjoint returns True of there are no common element is present
    return item1.isdisjoint(item2)   # formula = set1.isdisjoint(set2)
                                     # we can use in operator also

print(no_ele_common({1, 2}, {3}))

"""

"""
# 18. Write a Python program to check if a given set is superset of itself and superset of another given set.

# issuperset function returns true if s function is superset of another function

def super_set(set1, set2):
    return set1.issuperset(set2)   # Formula = set1.issuperset(set2)
                                   # set1>set2

print(super_set({1, 2, 3, 4}, {1}))

"""

"""
# 19.Write a Python program to find the elements in a given set that are not in another set.

#  return elements that are in set1 but not in set2

# method:1 we can use not in operator

# method:2  by using difference function


sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("Difference of sn1 and sn2 using difference():")
print(sn1.difference(sn2))
print("Difference of sn2 and sn1 using difference():")
print(sn2.difference(sn1))
print("Difference of sn1 and sn2 using - operator:")
print(sn1-sn2)
print("Difference of sn2 and sn1 using - operator:")
print(sn2-sn1)

"""

"""
# 21.Write a Python program to remove the intersection of a 2nd set from the 1st set.

# elobration: elements coming from the intersection of second set .... those elements will be removed from the first
# set

# we can use difference_update method  "-="



sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("\nRemove the intersection of a 2nd set from the 1st set using difference_update():")
sn1.difference_update(sn2)
print("sn1: ",sn1)
print("sn2: ",sn2)
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("\nRemove the intersection of a 2nd set from the 1st set using -= operator:")
sn1-=sn2
print("sn1: ",sn1)
print("sn2: ",sn2)


method:2 

sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("\nRemove the intersection of a 2nd set from the 1st set using remove():")
for i in sn1&sn2:
    sn1.remove(i)

print("sn1: ",sn1)
print("sn2: ",sn2)

"""

# _____________________________________________FORMULAS FOR SET METHODS_________________________________________________


# part:-1


# 1.difference() "-" --- set1.difference(set2) --- it returns the new set contains the elements of set1-set2
# 2.difference_update "-=" ---- set1.difference_update(set2) --- updates the set1 by removing the difference elements


# part:-2

# 1.intersection() --- set1.intersection(set2) it returns new set containing only intersection elements
# 2.intersection_update() -- set1.intersection_updates(set2) it takes intersection elements updates in set1 vise-versa


# part:-3

# 1.symmetric_difference: set1.symmetric_difference(set2) it returns new set contains the uncommon items of both sets
# 2. symmetric_difference_update(): set1.symmetric_difference_update(set2) it takes symmetric_difference elements
#                                  and updates in the set1 vise_versa.

# part:-4

# 1.issubset() = set1.issubset(set2) = it returns boolean value -- meaning is set1 is subset of set2
# set1<=set2 (issubset)
# 2.issuperset() = set1.issuperset(set2) = it returns the boolean -- set1 is super set of set2
# set1>set2 (issuperset)
# 3.isdisjoint() = set1.isdisjoint(set2) = it returns the boolean -- True if set1 and set2 have different elements

