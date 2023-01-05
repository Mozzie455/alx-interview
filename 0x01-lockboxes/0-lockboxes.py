#!/usr/bin/python3
"""
    Determines if all boxes can be unlocked.

    Args:
    a list of boxes, represents a box containing other boxes.
    2. A key with the same number as a box opens that box.

    Returns:
        True if all boxes can be opened, False otherwise.
    """


def canUnlockAll(boxes):
    # Set of boxes that have been unlocked
    unlocked = set()

    # Start with the first box
    queue = [0]

    # Keep track of the boxes that have been checked
    visited = set()

    # Perform BFS
    while queue:
        box = queue.pop(0)
        unlocked.add(box)
        visited.add(box)
        for key in boxes[box]:
            if key not in visited:
                queue.append(key)

    # Return True if all boxes have been unlocked, False otherwise
    return len(unlocked) == len(boxes)
