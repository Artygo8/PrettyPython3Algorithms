#!/bin/python3

def selectionSort(lst):

    n = len(lst) - 1
    while n:
        maxId = n
        for i in range(n):
            if lst[i] > lst[maxId]:
                maxId = i
        lst[n], lst[maxId] = lst[maxId], lst[n]
        n -= 1

    return lst


if __name__ == '__main__':
    lst = [2, 1, 7, 0, 6, 5, 8, 4, 3, 9]
    print(selectionSort(lst))
