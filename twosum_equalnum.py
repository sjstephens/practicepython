#!/usr/bin/env python3
'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
'''

class Solution(object):
    def twoSum(self, nums, target):
      numMap = {}
      for i, num in enumerate(nums):
          complement = target - num
          if complement in numMap:
            return [numMap[complement], i]
          numMap[num] = i
      return []
    
if __name__ == '__main__':
    
    nums = [3,1,2,3]
    # Print the position of the numbers that equal the target
    print(Solution.twoSum(Solution, nums, 6))
