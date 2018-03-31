# -*- coding: utf-8 -*-
import sys


def get_answer(albas):

    return ""


# Time complexity: TODO
# Space complexity: TODO
def main():
    total = int(input())
    # total = int(sys.stdin.readline().strip())
    albas = []
    for i in range(total):
        # line = sys.stdin.readline().strip()
        M, D, I = [int(word) for word in input().split()]
        albas.append((M, D, I))

    answer = get_answer(albas)

    print(answer)


if __name__ == "__main__":
    main()
