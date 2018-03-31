# -*- coding: utf-8 -*-


def get_answer(first_name, last_name):
    return first_name + " " + last_name


def main():
    first_name, last_name = input().split()
    px, py = [int(word) for word in input().split()]

    case_count = int(input())

    for _ in range(case_count):
        ranks = [int(word) for word in input().split()]
        print(ranks)

    answer = get_answer(first_name, last_name)

    print(answer)


if __name__ == "__main__":
    main()
