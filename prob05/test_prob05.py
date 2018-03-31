import io
import unittest
from unittest.mock import patch

from prob05.prob05 import main


class End2EndTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end2end_1(self, captured_output):
        raw_input = """\
5
0 4 5
3 4 20
6 6 3
8 5 35
10 4 12
"""
        user_input = raw_input.split("\n")

        with patch('builtins.input', side_effect=user_input):
            main()
            output = captured_output.getvalue()
            output = output.rstrip()

        self.assertEqual("""\
55
3 4
8 5""", output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end2end_2(self, captured_output):
        raw_input = """\
8
1 6 10
2 4 10
6 3 5
7 4 9
9 4 11
10 6 7
11 6 9
13 6 4
"""
        user_input = raw_input.split("\n")

        with patch('builtins.input', side_effect=user_input):
            main()
            output = captured_output.getvalue()
            output = output.rstrip()

        self.assertEqual("""\
30
2 4
6 3
9 4
13 6""", output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end2end_3(self, captured_output):
        raw_input = """\
6
0 99 30
75 46 29
80 20 28
99 62 29
120 11 31
130 51 29
"""
        user_input = raw_input.split("\n")

        with patch('builtins.input', side_effect=user_input):
            main()
            output = captured_output.getvalue()
            output = output.rstrip()

        self.assertEqual("""\
61
0 99
120 11""", output)

#     @patch('sys.stdout', new_callable=io.StringIO)
#     def test_end2end_2(self, captured_output):
#         raw_input = """\
# 1
# 4
# 3 4 2 1
# 1
# 1 4
# """
#         user_input = raw_input.split("\n")
#
#         with patch('builtins.input', side_effect=user_input):
#             main()
#             output = captured_output.getvalue()
#             output = output.rstrip()
#
#         self.assertEqual("""\
# IMPOSSIBLE""", output)
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
