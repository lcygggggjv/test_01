

class A:

    def __new__(cls, *args, **kwargs):

        print("d")

        instance = super().__new__(cls)

        return instance


def get_driver():

    driver = {}

    def instance(cls, *args, **kwargs):

        if cls not in driver:

            driver[cls] = cls(*args, **kwargs)

        return driver[cls]

    return instance
