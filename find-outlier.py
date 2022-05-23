# Date Started: May 23, 2022
# Date Completed: May 23, 2022

#--------------------------------------------------------------------#
# Kata Description

# You are given an array (which will have a length of at least 3, but
# could be very large) containing integers. The array is either
# entirely comprised of odd integers or entirely comprised of even
# integers except for a single integer N. Write a method that takes
# the array as an argument and returns this "outlier" N.
#--------------------------------------------------------------------#

def find_outlier(integers):
    odds = []
    evens = []
    
    for integer in integers:
        if integer % 2 == 0:
            evens.append(integer)
        else:
            odds.append(integer)
            
    if len(odds) == 1:
        return odds[0]
    else:
        return evens[0]
