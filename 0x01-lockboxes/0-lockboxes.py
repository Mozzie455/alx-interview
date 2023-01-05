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
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
