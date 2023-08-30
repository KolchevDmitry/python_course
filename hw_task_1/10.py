lst = [2, 4, 5, 8, 9, 13]

for number in range(len(lst)):
    lst[number] *= number
    print(lst)


def f(lst, times=0):
    if len(lst) == 0:
        return
    print(lst[0] * times)
    f(lst[1:], times + 1)

f([2, 4, 5, 8, 9, 13])