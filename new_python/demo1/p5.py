

class Fation:

    def __init__(self):

        self.num_dict = {}

    def faction(self, n):
        # 判断第一次递归n是1，返回值1，第二次n=2，乘以上次的结果2*1=2，依次类推，直到n=4，结束
        if n == 0 or n == 1:

            return 1
        else:
            return n*self.faction(n-1)

    def __getitem__(self, key):

        print(f"__getitem__方法被调用， {key}")
        # 判断key是否存在字典里
        if key in self.num_dict:
            # 调用了faction方法传的是字典key值就是上面用到的n
            return self.faction(self.num_dict[key])
        else:
            return 0

    def __setitem__(self, key, value):

        print(f"__setitem__方法被调用， {key}")

        self.num_dict[key] = int(value)

    def __delitem__(self, key):

        print(f"__delitem__方法被调用， {key}")

        del self.num_dict[key]

    def __len__(self):

        print("__len__方法被调用")

        return len(self.num_dict)


d = Fation()

d['4!'] = 4
d['7!'] = 7
d['12!'] = '12'

# 这里调用了__getitem__方法
print('4!', '=', d['4!'])
# len指上面对象里面的，字典的键值对个数，上面新增了3个键值对，所以是3
print('len', '=', len(d))

del d['7!']
print('len', '=', len(d))

print('4!', '=', d['7!'])   # 上面把键7！删除了，所以调用判断返回值是0
