
from array import array

def splitStringIntoWords(dictonary, longestLength, stringToSplit):
    wordIndicator = array('i', [0]*len(stringToSplit))
    end = False
    wordIndicatorLength = len(wordIndicator)
    front = len(wordIndicator) -1
    back = 1
    while not end:
        if stringToSplit[front:front + back] in dictonary \
        and ((front + back) == wordIndicatorLength  \
        or wordIndicator[front+back] >= 1):
            wordIndicator[front] = True
            front = front - 1
            back = 1
        else:
            back = 1 + back
            if back >= longestLength or front + back > wordIndicatorLength:
                back = 1
                front = front - 1
        if front < 0:
            end = True
    print wordIndicator
    if wordIndicator[0] > 0:
        return True

    return False

