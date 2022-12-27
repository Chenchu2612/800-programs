
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

print(sort_list)





print("hello")