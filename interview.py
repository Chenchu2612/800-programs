
l = [1, 2, {3: [0, {5: [10, 11]}]}, 500]


def access_element(list_obj):
    return max([b for x in l if type(x) == dict for y in x.values() for z in y if type(z) == dict for a in z.values() for b in a])


print(access_element(l))
