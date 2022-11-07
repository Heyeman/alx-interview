#!/usr/bin/python3
def canUnlockAll(boxes):
    if len(boxes) < 2:
        return True
    visited = set()

    def dfs(key):
        visited.add(key)
        for box in boxes[key]:
            if 0 <= box < len(boxes) and box not in visited:
                dfs(box)
    dfs(0)
    return len(visited) == len(boxes)
