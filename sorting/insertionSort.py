#!/bin/python3

def insertionSort(lst):
    for i in range(1, len(lst)):
        tmp = lst[i]
        while lst[i - 1] > tmp and i > 0:
            lst[i] = lst[i - 1]
            i -= 1
        lst[i] = tmp
    return lst


def insertionSortToo(lst):
    for i in range(len(lst) - 1):
        after = lst[i + 1]
        while lst[i] > after and i >= 0:
            lst[i + 1] = lst[i]
            i -= 1
        lst[i + 1] = after
    return lst


if __name__ == '__main__':
    lst = [2, 1, 7, 0, 6, 5, 8, 4, 3, 9]
    print(insertionSort(lst))
    print(insertionSortToo(lst))
