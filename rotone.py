"""
Write a program that takes a string, will perform a transformation and return it.
For each of the letters of the parameter string switch it by the next one in alphabetical order.

'z' becomes 'a' and 'Z' becomes 'A'. Case remains unaffected.
"""

class Solution:
  """
  :type  param_1: {String}
  :rtype: string
  """
  def rotone(self, param_1):
    param_1_list = list(param_1)
    
    if len(param_1) == 0:
        return ""
    else:
      for i,c in enumerate(p1_list):
        if param_1_list[i] >= 'a' and param_1_list[i] < 'z' or param_1_list[i] >= 'A' and param_1_list[i] < 'Z':
          param_1_list[i] = chr(ord(param_1_list[i])+ 1)
        elif param_1_list[i] == 'z':
          p1_list[i] = 'a'
        elif param_1_list[i] == 'Z':
          param_1_list[i]= 'A'
      
    param_1 = ''.join(param_1_list)
    return param_1
