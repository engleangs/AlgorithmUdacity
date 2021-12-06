"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort_v2(array):
    if len(array) < 2 :
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot ]
    great = [ i for i in array[1:] if i > pivot]
    less = quicksort_v2(less)
    great = quicksort_v2( great)
    return less +[pivot] + great
    
    

def quicksort(array):
    return quicksort_helper(array, 0, len(array)-1)
def quicksort_helper(array, start , end ):
    if start >= end:
        return array
    mid = start + ( end - start)//2
    pivot = array[mid]
    left = start
    right = end
    while left <=right:
        while left <= right and array[left] < pivot:
            left = left +1
        while left <=right and  array[right]> pivot :
            right = right -1
        if left <= right:
            array[left],array[right] = array[right],array[left]
            left = left +1
            right = right -1
    quicksort_helper( array, start, right)
    quicksort_helper(array,  left, end)
    return array


if __name__ == "__main__":
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print( quicksort(test))
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print ( quicksort_v2( test))
    