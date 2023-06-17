

import string
import random


class Mock:

    def mock_data(self, strs="cr"):

        all_str = string.digits + string.ascii_letters

        ran_str = ''.join(random.sample(all_str, 3))

        return strs + ran_str


if __name__ == '__main__':

    cs = Mock()

    SS = cs.mock_data()

    print(SS)
