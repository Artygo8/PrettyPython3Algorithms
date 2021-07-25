#!/bin/python3

def mergeSort(lst):

    if len(lst) > 1:
        mid = len(lst) // 2
        left, right = lst[:mid], lst[mid:]

        mergeSort(left)
        mergeSort(right)

        for i in range(len(lst)):
            should_take_from_right = not left or (right and left[0] > right[0])
            lst[i] = (right if should_take_from_right else left).pop(0)

    return lst


if __name__ == '__main__':
    lst = [2, 1, 7, 0, 6, 5, 8, 4, 3, 9]
    print(mergeSort(lst))
