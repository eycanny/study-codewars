// Date Started: May 23, 2022
// Date Completed: May 23, 2022

// #--------------------------------------------------------------------#
// Kata Description

// Given an array of integers your solution should find the smallest
// integer.

// For example:

// Given [34, 15, 88, 2] your solution will return 2
// Given [34, -345, -1, 100] your solution will return -345

// You can assume, for the purpose of this kata, that the supplied
// array will not be empty.
// #--------------------------------------------------------------------#

#Solution 1
class SmallestIntegerFinder {
  findSmallestInt(args){
    let smallestInt = args[0];
    
    for (let number of args) {
      if (number < smallestInt) {
        smallestInt = number;
      }
    }
    
    return smallestInt;
  }
}


#Solution 2
class SmallestIntegerFinder {
  findSmallestInt(args){
    return args.sort((a,b) => a-b)[0];
  }
}
