
import copy


# a = [1, 2, [3, 4], [9, 10], 5]
# b = copy.copy(a)
# b[2][0] = "hai"
# a[2][1]="chenchu"
# a.append(89)
# print("the value of b:", b)
# print("the value of a:", a)


a = [1, 2, [3, 4], [9, 10], 5]
b = copy.copy(a)
b[0] = "hai"
a[0]="chenchu"
a.append(89)
print("the value of b:", b)
print("the value of a:", a)