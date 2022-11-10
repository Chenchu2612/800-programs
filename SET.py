
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


























