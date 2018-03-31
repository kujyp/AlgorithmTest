# -*- coding: utf-8 -*-


THERE_IS_NO_FRIEND = -1


def make_friend_connection_dict(relations):
    conneciton_dict = dict()

    for relation in relations:
        friend_a, friend_b = relation

        if friend_a in conneciton_dict:
            conneciton_dict[friend_a].append(friend_b)
        else:
            conneciton_dict[friend_a] = [friend_b]

        if friend_b in conneciton_dict:
            conneciton_dict[friend_b].append(friend_a)
        else:
            conneciton_dict[friend_b] = [friend_a]

    return conneciton_dict


def get_first_unclassified_friend(connection_dict):
    for friend in connection_dict:
        return friend

    return THERE_IS_NO_FRIEND


def get_answer(relations):
    connection_dict = make_friend_connection_dict(relations)

    count = 0
    while True:
        friend = get_first_unclassified_friend(connection_dict)
        if friend == THERE_IS_NO_FRIEND:
            break

        search_targets = [friend]

        while len(search_targets) != 0:
            eachfriend = search_targets.pop()
            if eachfriend in connection_dict:
                search_targets += connection_dict.pop(eachfriend)

        count += 1

    return count


def main():
    relation_count = int(input())
    relations = []

    for _ in range(relation_count):
        friend_a, friend_b = [int(word) for word in input().split()]
        relations.append((friend_a, friend_b))

    answer = get_answer(relations)

    print(answer)


if __name__ == "__main__":
    main()
