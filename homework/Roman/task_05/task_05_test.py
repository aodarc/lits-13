import unittest
import task_05


class TestCases(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(task_05.sort_odd([13, 2, 29, 0, 8, 4, 12, 43, 1, -5]), [-5, 2, 1, 0, 8, 4, 12, 13, 29, 43])


if __name__ == '__main__':
    unittest.main()