import copy

d = [1, 5, [6, 4]]

s = d.copy()

d[2][1] = 2

print(s)


x = [1, 4, [3, 9]]

u = copy.deepcopy(x)

x[2][1] = 8

print(u)
