import unittest
import unittest.mock


from add import add

class TestAdd(unittest.TestCase):
    def test_nums(self):
        self.assertEqual(add(1, 3), 4)

    def test_num_and_string(self):
        self.assertRaises(TypeError, add, 1, 'a')
