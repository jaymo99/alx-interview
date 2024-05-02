#!/usr/bin/python3

"""Lockboxes module"""

from collections import deque


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
