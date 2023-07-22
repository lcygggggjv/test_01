

# class Cos(list):
#
#     def __init__(self, *args):
#
#         super().__init__(*args)
#         self.counter = 0
#
#     def __getitem__(self, index):
#
#         self.counter += 1
#
#         return super().__getitem__(index)
#
#
# c = Cos(range(10))
#
# print(c)
#
# c.reverse()
# print(c)
#
# print(c.counter)
# print(c[1] + c[2])
# print(c.counter)


# class Rectangle:
#
#     def __init__(self):
#
#         self.left = 0
#         self.top = 0
#
#     # 用于监控position属性的“写：”操作， 可以同时设置left，top属性
#     def set_position(self, position):
#         print("position属性已经保存")
#         self.left, self.top = position
#
#     # 用于监控position属性的“读：”操作， 可以同时获取left，top属性
#     def get_position(self):
#         print("position属性被调用")
#         return self.left, self.top
#
#     # 用于监控position属性的“删除”操作，
#     def delete_position(self):
#
#         print("position属性已经被删除")
#         # 重新初始化left和top属性
#         self.left = 0
#         self.top = 0
#
#     # 通过property函数，将上面3个方法与position属性绑定， 对position属性进行相关操作时，就会调用相关方法
#     position = property(get_position, set_position, delete_position)
#
#
# r = Rectangle()
#
# r.left = 10
# r.top = 15
# print('left', '=', r.left)
# print('left', '=', r.top)
# print('left', '=', r.position)
# r.position = 100, 200
# print('left', '=', r.position)


# class Register:
#
#     def __init__(self):
#
#         self.n = 0
#
#     def __next__(self):
#
#         result = '*' * (2 * self.n - 1)
#
#         self.n += 1
#
#         return result
#
#     def __iter__(self):
#
#         return self
#
#
# rs = Register()
#
# for s in rs:
#
#     if len(s) > 20:
#
#         break
#
#     print(s)
#
#
# def my_generator():
#
#     list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#     for a in list1:
#
#         yield a
#
#
# for r in my_generator():
#
#     print(r, end='')


def fuc(cls):

    driver = {}

    def get_driver(*args, **kwargs):

        if cls not in driver:

            driver[cls] = cls(*args, **kwargs)
        else:
            return driver[cls]

    return get_driver


def fx(func):

    def gets(*args, **kwargs):

        return func(*args, **kwargs) + 2
    return gets


@fx
def fc(x, y, z=1):

    return x + y + z


res = fc(1, 2, z=2)
print(res)

