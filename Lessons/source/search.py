#!python
# recursive linear search
# iterative binary search
# Recursive Binary search

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # implement linear search recursively here
    if len(array) <= index:
        return None
    elif array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # implement binary search iteratively here
    halved = len(array) // 2
    likley_hood = len(array) -1
    while likley_hood != 0:
        if item == array[halved]:
            return halved
        elif item < array[halved]:
            halved = halved // 2
            likley_hood -= 1
        else item > array[halved]:
            halved = halved + (len(array) - halved) // 2
            likley_hood -= 1
    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    #implement binary search recursively here
    if right == None:
        right = len(array) - 1
    elif left > right:
        return None

    med_index = (right + left) // 2
    med_value = array[med_index]

    if med_value == item:
        return med_index
    elif item > med_value:
        left = med_index + 1
    elif item < med_value:
        right = med_index -1

    return binary_search_recursive(array, item, left, right)
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
