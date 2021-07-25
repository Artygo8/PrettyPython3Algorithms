#!/bin/python3

def bubbleSort(lst):
    n = len(lst) - 1
    while n:
        for i in range(n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n -= 1
    return lst


if __name__ == '__main__':
    lst = [2, 1, 7, 0, 6, 5, 8, 4, 3, 9]
    print(bubbleSort(lst))
