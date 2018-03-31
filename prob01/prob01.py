# -*- coding: utf-8 -*-
import sys


def get_answer(input_string):
    result = ""

    if len(input_string) == 0:
        return result

    curr_alphabet = input_string[0]
    count = 0
    for each_alphabet in input_string:
        if curr_alphabet == each_alphabet:
            count += 1
        else:
            result += str(count) + curr_alphabet
            curr_alphabet = each_alphabet
            count = 1

    result += str(count) + curr_alphabet

    return result


# Time complexity: O(n)
# Space complexity: O(n)
def main():

    T = int(sys.stdin.readline().strip())
    # T = int(input())
    for tc in range(T):
        input_string = sys.stdin.readline().strip()
        # input_string = input().strip()
        answer = get_answer(input_string)
        print(answer)


if __name__ == "__main__":
    main()
