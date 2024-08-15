import unittest
from assignment_x import print_hello

class TestAss1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, 1)

    def hello(self):
        self.assertEqual(print_hello(), 'hello')

class TestAss2(unittest.TestCase):
    def test_2(self):
        self.assertEqual(2, 1)




if __name__ == '__main__':
    unittest.main()