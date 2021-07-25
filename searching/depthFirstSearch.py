#!/bin/python3

def depthFirstSearch(graph, root, toFind):

    stack = [root]
    visited = set(stack)

    while stack:

        vertex = stack.pop(-1)

        if vertex == toFind:
            return True

        for item in graph[vertex]:
            if item not in visited:
                visited.add(item)
                stack.append(item)

    return False


if __name__ == '__main__':
    d = {
        'A': ['B', 'C', 'D', 'E'],
        'B': ['A', 'F'],
        'C': ['A'],
        'D': ['A', 'G'],
        'E': ['A'],
        'F': ['B', 'H'],
        'G': ['D'],
        'H': ['F']
    }
    for i in range(10):
        print(depthFirstSearch(d, 'A', chr(ord('A') + i)))
