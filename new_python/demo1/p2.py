

# def sy(**ss):
#
#     for item in ss.items():
#         print(f"{item}")
#
#
# dicts = {"a": 12, "v": 12}
#
# print(sy(**dicts))
#
#
# def syw(*ss):
#
#     for item in ss:
#         print(f"{item}")
#
#
# list1 = ['ok', 'dsa']
#
# syw(*list1)

# x = 12
#
# def f6():
#
#     x =9
#
#     def f8():
#
#         print(x)
#
#         print("f8")
#
#     return f8()
#
#
# f6()


# class tt:
#
#     def set_name(self, name):
#
#         self.name = name
#
#     def get_name(self):
#
#         return self.name
#
#     def yy(self):
#
#         print("hello word")
#
#
# # a = tt()
# #
# # a.set_name('12')
# #
# # s = a.get_name()
# # print(s)
#
# q = tt().yy()
# print(q)

# class Y:
#
#     def methods(self):
#
#         print("外部可以访问")
#
#         self.__mt()
#     def __mt(self):
#
#         print("外部无法访问")
#
#
# a =Y()
#
# a.methods()
# a.Y.__mt()


class A:

    def method1(self):
        print("111")

    def default(self):
        print("默认值")


my = A()

if hasattr(my, 'method1'):
    # 判断my对象是否存在method1方法
    print("cz")
else:
    print("no")

# 获取my对象里是否有method2方法，没有返回default函数
method = getattr(my, "method2", my.default)
method()

def method2():

    print("新添加方法")


setattr(my, 'method2', method2)
my.method2()