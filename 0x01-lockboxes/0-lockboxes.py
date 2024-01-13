#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened"""
    # base cases
    # if there are no boxes, return false
    if len(boxes) == 0:
        return False

    # if boxes is not a list
    if not isinstance(boxes, list):
        return False

    # if boxes only has the first box, which is unlocked
    if len(boxes) == 1:
        return True
    # end base cases

    # store all found keys in keys, the first box included
    keys = [0]

    # only open boxes whose keys have been found/or are unlocked
    for key in keys:
        # for each key found in the box
        for found_key in boxes[key]:
            # if the found key isnt stored in keys,
            # and the key opens a valid box, i.e a box within bounds of boxes
            if found_key not in keys and found_key < len(boxes):
                keys.append(found_key)

    return len(keys) == len(boxes)
