#!/usr/bin/python3
"""peak-finding algorithm."""

def find_peak(list_of_integers):
    """Find the peak element in a list of integers."""
    if not list_of_integers: return None
    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = (left + right) // 2
        # If the middle is smaller than its adjacent elements, it can't be the peak.
        if list_of_integers[mid] > list_of_integers[mid+1]:
            right = mid 
        else:
            left = mid + 1
    return list_of_integers[left]

