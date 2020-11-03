"""
  Write a program that takes a string as a parameter, and returns its words in reverse order.

  A word is a section of string delimited by spaces/tabs or the start/end of the string. 
  If a word has a single letter, it must be capitalized.

  A letter is a character in the set [a-zA-Z]
"""

class Solution:
  """
  :type  param_1: {String}
  :rtype: string
  """
  def rev_wstr(self, param_1):
    x = param_1.split()
    start = 0
    end = len(x) - 1
    while start < end:
      x[start], x[end] = x[end], x[start]
      start += 1
      end -= 1
    param_1 = ' '.join(x)

    return param_1
