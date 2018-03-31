# -*- coding: utf-8 -*-
# import sys


WEIGHT_IDX = 0
HAVE_DID_ALBAS_IDX = 1
MAXIMUM_M = 200

START_DAY_IDX = 0
DURATION_IDX = 1


def get_suboptimal_before_day(sub_optimals, day):
    if day == 0:
        return [0, []]

    return sub_optimals[day - 1]


def get_weight_before_day(sub_optimals, day):
    return get_suboptimal_before_day(sub_optimals, day)[WEIGHT_IDX]


def get_answer(albas, last_day):
    sub_optimals = [(0, [])] * MAXIMUM_M

    for day in range(1, last_day + 1):
        if day != 1:
            sub_optimals[day] = sub_optimals[day - 1]

        if len(albas[day]) == 0:
            continue

        for each_alba in albas[day]:
            start_day, _, weight = each_alba

            before_weight, before_albas = get_suboptimal_before_day(sub_optimals, start_day)
            curr_weight = weight + before_weight
            if curr_weight > get_weight_before_day(sub_optimals, day):
                curr_albas = before_albas.copy()
                curr_albas.append(each_alba)
                sub_optimals[day] = (curr_weight, curr_albas)

    return sub_optimals[last_day]


# Time complexity: TODO
# Space complexity: TODO
def main():
    total = int(input())
    # total = int(sys.stdin.readline().strip())
    albas = [[] for _ in range(MAXIMUM_M)]

    last_day = 0
    for i in range(total):
        # line = sys.stdin.readline().strip()
        # start_day, duration, weight = [int(word) for word in line.split()]
        start_day, duration, weight = [int(word) for word in input().split()]
        end_day = start_day + duration - 1
        albas[end_day].append((start_day, duration, weight))

        last_day = max(end_day, last_day)

    answer = get_answer(albas, last_day)

    print(answer[WEIGHT_IDX])
    for alba in answer[HAVE_DID_ALBAS_IDX]:
        print("{} {}".format(alba[START_DAY_IDX], alba[DURATION_IDX]))


if __name__ == "__main__":
    main()
