from unittest import TestCase


class UnitTestCase(TestCase):
    def test_methods_1(self):
        expected = [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0]
        ]
        result = [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0]
        ]

        self.assertEqual(expected, result)
