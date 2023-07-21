

class A:

    def __init__(self):

        print("爷爷类")


class B(A):

    def __init__(self, hs):

        super().__init__()

        self.hs = hs

    def eat(self):

        if self.hs:

            print("存在了")

        else:

            print("不存在")

    def sing(self):

        print('fulei')


class C(B):

    def __init__(self, hs):

        super().__init__(hs)

        self.zs = 'xin'

    def sing(self):
        super().sing()
        print(self.zs)


zs = C(True)
zs.eat()
zs.sing()



