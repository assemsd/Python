"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
"""

class Solution:
  """
  :type  param_1: {Integer}
  :rtype: integer
  """
  def number_complement(self, param_1):
    x = bin(param_1)
    x_list = list(x)
    for i in range(2, len(x_list)):
      if x_list[i] == '0':
        x_list[i] = '1'
      else:
        x_list[i] = '0'
    x_complement = ''.join(x_list)
    return int(x_complement,2)
