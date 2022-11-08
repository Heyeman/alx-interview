#!/usr/bin/python3
def canUnlockAll(boxes):
    '''returns true if all boxes are able to be opened'''

    if len(boxes) < 2:
        return True
    visited = set()

    def dfs(key):
        '''is a dfs function that searches the boxes in depth'''

        visited.add(key)
        for box in boxes[key]:
            if 0 <= box < len(boxes) and box not in visited:
                dfs(box)
    dfs(0)

    return len(visited) == len(boxes)
