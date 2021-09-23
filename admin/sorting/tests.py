from django.test import TestCase
import unittest


from models import MySum


class TestMySum(unittest.TestCase):

    def test_one_to_ten_sum_1(self):
        instance = MySum()
        instance.start_number = 1
        instance.end_number = 11
        res = instance.one_to_ten_sum2()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 55)


if __name__ == '__main__':
    unittest.main()