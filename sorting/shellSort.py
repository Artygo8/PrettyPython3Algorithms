#!/bin/python3

def shellSort(lst):
    n = len(lst)
    dist = n // 2
    while dist:
        for i in range(dist, n):
            tmp = lst[i]
            while lst[i - dist] > tmp and i - dist >= 0:
                lst[i] = lst[i - dist]
                i -= dist
            lst[i] = tmp
        dist = dist // 2
    return lst


if __name__ == '__main__':
    lst = [2, 1, 7, 0, 6, 5, 8, 4, 3, 9]
    print(shellSort(lst))
