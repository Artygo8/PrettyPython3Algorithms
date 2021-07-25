#!/bin/python3

def linearSearch(lst, elem):
    for i in lst:
        if i == elem:
            return True
    return False


if __name__ == '__main__':
    lst = [2, 1, 7, 0, 6, 5, 8, 4, 3, 9]
    print(linearSearch(lst, 2))
