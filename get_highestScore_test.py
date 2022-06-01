import unittest
from unittest.mock import patch

from alieninvasion import AlienInvasion


class MyTestCase(unittest.TestCase):
    """解除外部依赖测试main中的get_high_score"""

    @patch('alieninvasion.AlienInvasion.write_high_score')
    def test_something(self, mock_writehscore):
        game = AlienInvasion()
        mock_writehscore.return_value = 15
        high_score = game.get_high_score()
        mock_writehscore.assert_called_once_with()

        self.assertEqual("最高分15", high_score)


if __name__ == '__main__':
    unittest.main()
