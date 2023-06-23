

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):

        print(f"生成的{self.name, self.age}")


class Son(Person):

    def __init__(self, name, age, city):

        super().__init__(name, age)
        # self.name = name
        # self.age = age
        self.city = city

    def info(self):
        super().info()
        print("这是子类的", self.city)


yy = Son('12', 43, 'HZ')

yy.info()


for a in range(1, 10):

    for b in range(1, a+1):

        print(f"{a}*{b}={a*b}", end="\t")

    print()


