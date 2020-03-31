#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if array[index] == item: 
        return index
    elif index+1 == len(array):
        return None
    return linear_search_recursive(array, item, index+1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return binary_search_iterative(array, item)
    return binary_search_recursive(array, item, len(array)//2, len(array)//2)


def binary_search_iterative(array, item):
    index = len(array)//2
    array = list(enumerate(array))
    while array[index][1] != item and len(array) != 1:
        if array[index][1] > item: array = array[:index]
        else: array = array[index:]
        index = len(array)//2
    if array[index][1] != item:
        return None
    return array[index][0]
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left, right):
    # Thanks to @ithaghost (Gary) for the bisect equation
    bisect = left + (right - left)//2
    print(bisect)
    if array[bisect] == item:
        return index
    elif bisect+1 == len(array):
        return None

    if array[bisect] > item:
        return binary_search_recursive(array, item, bisect, bisect-1)
    return binary_search_recursive(array, item, bisect, bisect+1)
    # if type(array[index]) != tuple:
    #     return binary_search_recursive(list(enumerate(array)), item)
    
    # # Base cases
    # if array[index][1] == item:
    #     return array[index][0]
    # elif array[index][1] != item and len(array) == 1:
    #     return None
    
    # if left:
    #     return binary_search_recursive(array[:index], item)
    # elif right:
    #     return binary_search_recursive(array[index:], item)
    # elif array[index][1] > item: 
    #     return binary_search_recursive(array, item, left=True)
    # elif array[index][1] < item:
    #     return binary_search_recursive(array, item, right=True)
    
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
