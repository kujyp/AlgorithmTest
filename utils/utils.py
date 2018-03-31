def print_list_on_single_line(lists):
    if len(lists) == 0:
        return

    copy = lists.copy()

    last = copy.pop(-1)
    for each in copy:
        print(each, end=" ")

    print(last)


def print_list_on_multi_line(lst):
    for each_row in lst:
        print(each_row)


def empty_2darr(num_row, num_col):
    return [[0 for _ in range(num_col)] for _ in range(num_row)]


STATE_UNRIPEN = 0


def get_arounds(given_map, tomato):
    results = []
    row_idx, col_idx = tomato

    if row_idx > 0 and given_map[row_idx - 1][col_idx] == STATE_UNRIPEN:
        results.append((row_idx - 1, col_idx))

    if col_idx < (len(given_map[0]) - 1) \
            and given_map[row_idx][col_idx + 1] == STATE_UNRIPEN:
        results.append((row_idx, col_idx + 1))

    if row_idx < (len(given_map) - 1) \
            and given_map[row_idx + 1][col_idx] == STATE_UNRIPEN:
        results.append((row_idx + 1, col_idx))

    if col_idx > 0 and given_map[row_idx][col_idx - 1] == STATE_UNRIPEN:
        results.append((row_idx, col_idx - 1))

    return results


def is_out_of_range(cur_y, cur_x, max_y, max_x):
    if 0 <= cur_y < max_y and \
            0 <= cur_x < max_x:
        return False
    else:
        return True
