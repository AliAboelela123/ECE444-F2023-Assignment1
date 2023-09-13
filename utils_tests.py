import unittest
from utils import utils

class TestMethods(unittest.TestCase):

    def test_reverser(self):
        self.assertEqual(utils.reverser(123), 321)

    def test_formatter_A(self):
        binary, octal = utils.formatter(3112)
        self.assertEqual(binary, 0b110000101000)
        self.assertEqual(octal, 6050)
    
    def test_formatter_B(self):
        binary, octal = utils.formatter('3112')
        self.assertEqual(binary, 0b110000101000)
        self.assertEqual(octal, 6050)

if __name__ == '__main__':
    unittest.main()