list_1 = range(15)


def add(*args):
    value = 0
    for item in args:
        if isinstance(item, (int, float)):
            value += item

    return value


print(list(filter(lambda x: x % add(3) == 0, list_1)))
