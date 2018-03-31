# -*- coding: utf-8 -*-


def get_distance(user_x, user_y, store_x, store_y):
    return ((user_x - store_x) ** 2 + (user_y - store_y) ** 2) ** (1/2)


def simplify_distance(distance):
    return int(distance / 100)


def get_answer(user_x, user_y, stores):
    will_be_sorted_stores = []
    for idx, store in enumerate(stores):
        store_x, store_y, store_name, store_coupon = store
        distance = get_distance(user_x, user_y, store_x, store_y)
        cutted_distance = simplify_distance(distance)
        will_be_sorted_stores.append(
            (cutted_distance, -store_coupon, store_name, idx))

    will_be_sorted_stores.sort()
    sorted_idx = []

    for _, _, _, idx in will_be_sorted_stores:
        sorted_idx.append(idx)

    return sorted_idx


def print_store(store):
    store_x, store_y, store_name, store_coupon = store
    print("{} {} {} {}".format(store_x, store_y, store_name, store_coupon))


def main():
    user_x, user_y, store_count = [int(word) for word in input().split()]
    stores = []

    for _ in range(store_count):
        store_x, store_y, store_name, store_coupon =\
            [word for word in input().split()]

        store_x, store_y, store_coupon =\
            int(store_x), int(store_y), int(store_coupon)
        stores.append((store_x, store_y, store_name, store_coupon))

    answer = get_answer(user_x, user_y, stores)

    for sorted_idx in answer:
        print_store(stores[sorted_idx])


if __name__ == "__main__":
    main()
