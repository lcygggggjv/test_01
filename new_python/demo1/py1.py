

# a = "Let'go!. \"一起学python\" "
# print(a)

# a = '22'
# b = '33'
# c = '-'.join(a+b)
# print(c)

# print("<hello\\nworld>")

# print("""i
# '21'\
# "kkk"
# """)

# name = input("请输入:")
# age = int(input("输入年龄："))
# salary = float(input("shou:"))
#
# print(type(str(age)))

# print(bin(12345))  # 把十进制转换为二进制
# print(oct(12345))  # 把十进制转换为八进制
# print(hex(12345))  # 把十进制转换为十六进制
#
# print(int("F98A", 16))  # 把十6进制转换为十进制
# print(bin(0xF98A))  # 把十6进制转换为二进制
# print(oct(0xF98A))  # 把十6进制转换为八进制
#
# print(int("1100010110", 2))  # 把2进制转换为十进制
# print(hex(0b1100010110))  # 把2进制转换为十6进制
# print(oct(0b1100010110))  # 把2进制转换为8进制
#
#
# x = 1234.5787
# print(format(x,'0.2f'))
# print(format(x, ','))


# aw = bool('21')
# print(aw)
# ax= bool([])
# print(ax)

# a = 12
#
# b = 2
#
# if a+b == 17:
#     print("错误")
# else:
#     print("ok")

# name = input("名称:")
#
# if name.startswith("b"):
#     if name.endswith("great"):
#         print("名字以b开头")
#
# elif name.startswith("c"):
#     print("c开头")
# else:
#     print("其他开头")

# x = y = [1, 2, 4, 6]
# z = [1, 2, 4, 6]
#
# print(x is y)
# print(x is z)
# print(x == z)

# x = [1, 4, 6, 5]
# y = 1
# print(y in x)
#
# s = 'helloword'
# p = 'h'
#
# print(p in s)

# a = 1
# c = '错误的'
# assert a == 2, c
# print('Hello', end='')
# print('World')

# x = 0
# while x <= 10:
#     if x == 6:
#         break
#     print(x)
# #     x += 1
# x = 0
# while x <= 10:
#     x += 1
#     if x == 6:
#
#         continue
#     print(x)


# while True:
#     a = input("请输入数字：")
#
#     if a == 'end':
#         break
#     a = int(a)
#
#     if a % 2 == 0:
#         print(f"{a}是偶数")
#     else:
#         print(f"{a}是奇数")
#
# layer = int(input("请输入你要打印的层数（奇数）："))
#
# # 条件判断：打印的层数必须为奇数
# while layer % 2 == 0:
#     layer = int(input("输入错误，请再次输入："))
#
# # 上半部分
# for i in range(1, (layer // 2) + 2):
#     space = (layer // 2) + 1 - i
#     star = 2 * i - 1
#     print(" " * space + "*" * star)
#
# # 下半部分
# for i in range(layer // 2, 0, -1):
#     space = (layer // 2) + 1 - i  # 根据行号递减，如果是layer=2，加1，减i =1,就是空格2个
#     star = 2 * i - 1  # 行号的2倍减一的增加
#     print(" " * space + "*" * star)

# for i in range(10, 0, -1):
#     print(i)
# num = [1, 2, 3, 4, 5, 6, 7, 8]
#
# print(num[-3:len(num)])


# values = 10, 20, 30
# x, y, z = values
# print(x, y, z)
# print(type(values))


# a =['222']
# b =['ld']
#
# print(a+b)

# ps = ['12.3', '23']
#
# print('23' in ps)
#
# s = '212sdkfk'
#
# print('1' in s)


# clas = [12, 3, 34, 45, 4]
#
# clas.insert(3,9)
# print(clas)
# # s = list('mike')
# # print(s)
# # s[1:] = list('mary')
# # print(s)

#
# a = [1, 3, 65, 8, 90, 0]
# a.sort()
# print(a)
# a.reverse()
# print(a)
# print(sorted('ckasie'))
# value = tuple([1,2,45,6])
# print(value)
#
# num = 1, 2, 3
# print(num)

# a_tuple = ("李宁", "anta", "tb")
#
# for value in a_tuple:
#
#     print(f"当前品牌是：{value}")
#
# print("-----------------------")
#
# new_list = [12, 3.3, 25, 1.3, True, 'helloword', 78, "china", 'anta']
#
# sum = 0
# my_count = 0
# for values in new_list:
#
#     # 如果改元素是整数或者float
#     if isinstance(values, int) or isinstance(values, float):
#         print(values)
#         # 累加该元素
#         sum += values
#         # 数值元素个数加1
#         my_count += 1
#
# print(f"综合：{sum}")
# print(f"平均数：{sum/my_count}")

# my_list = [x for x in range(10)]
#
# print(my_list)
#
# my_list2 = []
#
# for x in range(10):
#
#     my_list2.append(x)
#
# print(my_list2)

# new_list = []
#
# while True:
#
#     a = input("请输入数值：")
#
#     if a == 'end':
#         break
#
#     try:
#         new_list.append(int(a))
#     except ValueError:
#         print("无效")
#
# new_list.reverse()
#
# print(new_list)

num1 = [1, 2, 3, 6, 7]
num2 = [12, 3, 8, 9, 23]
num = []
for a in num1[1:4]:

    num2.append(a)

num2.sort()
NUM = num2
print(NUM)