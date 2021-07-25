#!/bin/python3

def interpolationSearch(lst, elem):

    first = 0
    last = len(lst) - 1

    while first <= last and elem >= lst[first] and elem <= lst[last]:

        mid = first + int(((last - first) /
                           (lst[last] - lst[first])) * (elem - lst[first]))

        if lst[mid] == elem:
            return True
        if elem < lst[mid]:
            last = mid - 1

    return False


if __name__ == '__main__':
    lst = [2, 1, 7, 0, 6, 5, 8, 4, 3, 9]
    lst.sort()  # Mandatory for interpolation search
    print(interpolationSearch(lst, 2))
    print(interpolationSearch(lst, 10))
