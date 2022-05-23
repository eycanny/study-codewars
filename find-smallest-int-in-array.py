# Date Started: May 23, 2022
# Date Completed: May 23, 2022

#--------------------------------------------------------------------#
# Kata Description

# Given an array of integers your solution should find the smallest
# integer.

# For example:

# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345

# You can assume, for the purpose of this kata, that the supplied
# array will not be empty.
#--------------------------------------------------------------------#

#Solution 1
def find_smallest_int(arr):
    smallest_int = arr[0]
    
    for num in arr:
        if num < smallest_int:
            smallest_int = num
            
    return smallest_int


#Solution 2
def find_smallest_int(arr):
    return sorted(arr)[0]
