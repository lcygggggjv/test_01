
import copy

# try:
#
#     a = int(input("输入整数："))
#     b = int(input("继续输入整数："))
#     c = a / b
#     print(c)
# except ValueError:
#
#     print("不是整数")
#
# except ZeroDivisionError:
#     print("不能输入0")
#
# except BaseException as e:
#     raise e
# finally:
#     print("都会被执行的，结束")

list1 = [1, 3, 4, [2], 8, 9]

list2 = list1.copy()

list2[3][0] = 0

print(list2, list1)


list5 = [1, 3, 4, [3], 8, 9]

list6 = copy.deepcopy(list5)

list6[3][0] = 0

print(list6, list5)


sd = {1, 3, 4, 6, 3}

sd.add(23)
sd.pop()
sd.remove(4)
print(set(sd))


# class TestDemo:
#
#     def __init__(self, student):
#
#         self.stu = student
#         print(self.stu)
#
#
# s = TestDemo('23')
# print(s.stu)
