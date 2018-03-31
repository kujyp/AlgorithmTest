import io
import unittest
from unittest.mock import patch

from prob02.prob02 import main


class End2EndTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end2end_1(self, captured_output):
        raw_input = """\
7123 4653 10
9288 6714 9S7RZV 30
2619 1434 HMH2YX 39
2588 3374 YWV0JQ 4
6284 8626 CQS1OZ 27
5099 1192 4GWLG6 19
6508 4507 Y5J0Q6 12
3161 2805 IQPY9F 36
47 8930 YC1FWC 44
751 2483 40438H 29
3226 4983 LSPFA8 45
"""
        user_input = raw_input.split("\n")

        with patch('builtins.input', side_effect=user_input):
            main()
            output = captured_output.getvalue()
            output = output.rstrip()

        self.assertEqual("""\
6508 4507 Y5J0Q6 12
9288 6714 9S7RZV 30
3226 4983 LSPFA8 45
6284 8626 CQS1OZ 27
5099 1192 4GWLG6 19
3161 2805 IQPY9F 36
2588 3374 YWV0JQ 4
2619 1434 HMH2YX 39
751 2483 40438H 29
47 8930 YC1FWC 44""", output)

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
