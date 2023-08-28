
import pytest


@pytest.fixture()
def test_1():

    return 1



def test_02(test_1):


    return (test_1 + 1)



