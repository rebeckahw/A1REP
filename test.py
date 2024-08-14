import unittest
from assignment_x import print_hello

class TestAss1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, 1)

    def hello(self):
        self.assertEqual(print_hello(), 'hello')



if __name__ == '__main__':
    unittest.main()