#!/bin/python3

def breadthFirstSearch(graph, root, toFind):

    queue = [root]
    visited = set(queue)

    while queue:

        vertex = queue.pop(0)

        if vertex == toFind:
            return True

        for item in graph[vertex]:
            if item not in visited:
                visited.add(item)
                queue.append(item)

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
        print(breadthFirstSearch(d, 'A', chr(ord('A') + i)))
