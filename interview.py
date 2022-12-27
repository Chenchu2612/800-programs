# l = [1, 2, {3: [0, {5: [10, 11]}]}, 500]


# def access_element(list_obj):
#     return max([b for x in l if type(x) == dict for y in x.values() for z in y if type(z) == dict for a in z.values() for b in a])
#
#
# print(access_element(l))


# 1. sort() without using sort method

list_obj = [-5, -23, 5, 0, 23, -6, 23, 67]
sort_list = []
while list_obj:
    min_ele = list_obj[0]
    # for x in list_obj:
    #     if x < min_ele:
    #         min_ele = x
    sort_list.append(min_ele)
    list_obj.remove(min_ele)


# print(sort_list)


# print("hello")


# anagram

# anagram by using length

def anagram(str_obj1, str_obj2):
    list1 = [i.lower() for i in str_obj1 if i != ' ']
    list2 = [j.lower() for j in str_obj2 if j != ' ']
    print(list1)  # for understanding purpose
    print(list2)  # for understanding purpose
    for k in list1:
        if k in list2:
            list2.remove(k)
    if len(list2) == 0:
        print("it is a anagram")
    else:
        print("Both strings are not anagrams")


# anagram(input("Enter the string_obj: "), input("Enter the string_obj2 :"))





def anagram_count(str_obj1, str_obj2):
    count = 0
    list1 = [i.lower() for i in str_obj1 if i != ' ']
    list2 = [i.lower() for i in str_obj2 if i != ' ']
    for x in list1:
        if x in list2:
            count += 1
            list2.remove(x)

    if count == len(list1):
        print("It is anagram")
    else:
        print("It is not a anagram")


anagram_count(input("Enter the string_obj :"), input("Enter the string_obj2 :"))









