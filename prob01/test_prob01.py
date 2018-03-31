import io
import unittest
from unittest.mock import patch

from prob01.prob01 import main


class End2EndTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end2end_1(self, captured_output):
        raw_input = """\
2
AAAAAADDC
WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
"""
        user_input = raw_input.split("\n")

        with patch('builtins.input', side_effect=user_input):
            main()
            output = captured_output.getvalue()
            output = output.rstrip()

        self.assertEqual("""\
6A2D1C
12W1B12W3B24W1B14W""", output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end2end_2(self, captured_output):
        raw_input = """\
1
WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
"""
        user_input = raw_input.split("\n")

        with patch('builtins.input', side_effect=user_input):
            main()
            output = captured_output.getvalue()
            output = output.rstrip()

        self.assertEqual("""\
""", output)
#
#     @patch('sys.stdout', new_callable=io.StringIO)
#     def test_end2end_3(self, captured_output):
#         raw_input = """\
# 1
# 3
# 3 1 2
# 1
# 1 2
# """
#         user_input = raw_input.split("\n")
#
#         with patch('builtins.input', side_effect=user_input):
#             main()
#             output = captured_output.getvalue()
#             output = output.rstrip()
#
#         self.assertEqual("""\
# 3 2 1""", output)
