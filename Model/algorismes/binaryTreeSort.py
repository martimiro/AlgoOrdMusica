from AlgoOrdMusica.Model.node import Node

'''
BUBBLE SORT
COMPLEXITAT: O(n²) no balancejat || O(n) balancejat
'''

class SortTree:
  def __init__(self, value):
    self.left = None
    self.value = value
    self.right = None
  def insert_val(self, _value):
    if _value < self.value:
       if self.left is None:
           self.left = SortTree(_value)
       else:
           self.left.insert_val(_value)
    else:
       if self.right is None:
          self.right = SortTree(_value)
       else:
          self.right.insert_val(_value)