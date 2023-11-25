

# def reverse_string(string):
#     if len(string) == 0:
#         return string
#     else:
#         return reverse_string(string[1:]) + string[0]
#
#
# s = reverse_string('lcy123')
# print(s)


dict1 = {"d": 1}
dict2 = {"c": 2}

dict1.update(dict2)
print(dict1)

a = 10

s = [3, 5, 1, 2]
s.sort()
print(s)


d = [2,6,1,3]
d.reverse()
print(d)


def ad(list1: list):

    u = 0
    for t in list1:

        u += t

    return u


sy = ad([1, 3])
print(sy)
