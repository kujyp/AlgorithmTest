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
jae young
3 5
3
5 4 3 2 1
2 3 1
1 2 3 4
"""
        user_input = raw_input.split("\n")

        with patch('builtins.input', side_effect=user_input):
            main()
            output = captured_output.getvalue()
            output = output.rstrip()

        self.assertEqual("""\
[5, 4, 3, 2, 1]
[2, 3, 1]
[1, 2, 3, 4]
jae young""", output)

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
