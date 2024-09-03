def func(x):
    return x + 1

class TestCases:
    def test_1(self):
        assert func(3) == 4

    def test_2(self):
        assert func(4) == 5

    def test_3(self):
        assert func(5) == 6

# pytest .\Pytest\test_demo1.py
# pytest .\Pytest\test_demo1.py -k 'test_1'
# python -m pytest .\Pytest\test_demo1.py