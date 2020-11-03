"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""

class Solution:
  """
  :type  param_1: {Integer[]}
  :type  param_2: {Integer}
  :rtype: boolean
  """
  def contains_duplicate_ii(self, param_1, param_2):
    for i in range(len(param_1)):
      for j in range(i+1, len(param_1)):
        if(i!=j and param_1[i]==param_1[j] and abs(i-j)<=param_2):
          return True
    return False
