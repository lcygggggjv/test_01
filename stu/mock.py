

import string
import random
from faker import Faker

class Mock:

    @staticmethod
    def mock_data(strs="cr"):

        all_str = string.digits + string.ascii_letters

        ran_str = ''.join(random.sample(all_str, 3))

        return strs + ran_str

    @staticmethod
    def faker_name():

        fk = Faker(locale=['zh_CN'])

        sd = fk.name()
        return sd

    @staticmethod
    def faker_str():

        fs = Faker()
        return fs.pystr(min_chars=2, max_chars=5)


if __name__ == '__main__':

    cs = Mock()

    SS = cs.faker_str()

    print(SS)
