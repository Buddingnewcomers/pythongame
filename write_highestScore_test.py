import unittest
from unittest import mock

from alieninvasion import AlienInvasion


class MyTestCase(unittest.TestCase):
    """测试mock模拟对象替换真实对象"""
    def test_something(self):
        game = AlienInvasion()
        game.write_high_score = mock.Mock(return_value=10)
        result = game.write_high_score()
        self.assertEqual(10, result)


if __name__ == '__main__':
    unittest.main()
