import random


def rnd():
    return random.randrange(20000) - 10000


def rnd_mm(minimum, maximum):
    return random.randrange(maximum - minimum) + minimum


for _ in range(100):
    print(rnd_mm(-10000, 10000))

    # area = get_duplicated_area(p, q, r, s)
    # print("p = [{}], q = [{}], r =[{}], s = [{}], area = [{}]"
    #       .format(p, q, r, s, area))
    #
    # x_cross_length = get_cross_length(p.x, q.x, r.x, s.x)
    # y_cross_length = get_cross_length(p.y, q.y, r.y, s.y)
    # print("p = [{}], q = [{}], x_len =[{}], y_len = [{}]"
    #       .format(p, q, x_cross_length, y_cross_length))
