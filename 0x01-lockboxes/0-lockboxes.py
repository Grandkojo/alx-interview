#!/usr/bin/python3
"""This is the locked boxes problem"""


def canUnlockAll(boxes):
    """This function determines if all boxes can be unlocked"""

    total_boxes = len(boxes)
    unlocked_keys = [False] * total_boxes

    keys = [0]

    while keys:
        new_key = keys.pop()
        if not unlocked_keys[new_key]:
            unlocked_keys[new_key] = True
            for key in boxes[new_key]:
                if key < total_boxes and not unlocked_keys[key]:
                    keys.append(key)
    return all(unlocked_keys)