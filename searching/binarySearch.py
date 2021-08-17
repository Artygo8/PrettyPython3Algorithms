#!/bin/python3

def binarySearch(lst, elem):

    first = 0
    last = len(lst) - 1

    while first <= last:

        mid = (first + last) // 2

        if lst[mid] == elem:
            return True
        if elem < lst[mid]:
            last = mid - 1
        if elem > lst[mid]:
            first = mid + 1

    return False


def binarySearchFirstLowerThan(lst, elem):

    first = 0
    last = len(lst) - 1

    while first <= last:

        mid = (first + last) // 2

        if elem <= lst[mid]:
            last = mid - 1
        if elem > lst[mid]:
            first = mid + 1

    return last


if __name__ == '__main__':
    lst = [2, 1, 7, 0, 6, 5, 8, 4, 3, 9]
    lst.sort()  # mandatory for binary search
    print(lst)
    print(binarySearchFirstLowerThan(lst, 2))
