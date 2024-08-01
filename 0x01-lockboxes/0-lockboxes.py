#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    seenBoxes = set([0])
    unseenBoxes = set(boxes[0]).difference(set([0]))
    while len(unseenBoxes) > 0:
        boxId = unseenBoxes.pop()
        if not boxId or boxId >= n or boxId < 0:
            continue
        if boxId not in seenBoxes:
            unseenBoxes = unseenBoxes.union(boxes[boxId])
            seenBoxes.add(boxId)
    return n == len(seenBoxes)

