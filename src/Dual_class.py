# -*- coding: utf-8 -*-
"""Dual_class

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EsOCWSZ07hWL3p-QMjDbN97zItNijrde
"""

import math
from collections import defaultdict
class Dual(object):
  def __init__(self,value, ders):
  # value (real number): the current value of the function
  # ders (dict): {'variable name': 'partial derivative with respect to the variable'} 
    self.value = value 
    self.ders = ders

  def partial(self,variable_name) -> float:
    """return the corresponding partial derivative with respect to the given 
    variable_name (e.g. self.ders[variable_name])"""
    return self.ders[variable_name]

  def gradient(self) -> dict:
    """return the self.ders, the dictionary that contains the current partial 
    derivative with respect to each variable"""
    return self.ders

  def getvalue(self) -> float: 
    """return the current value"""
    return self.value

  def __str__(self) -> str: 
    """return a string that shows the current value, and gradient"""
    result = f'Current Value is : {self.value}\n'
    result += 'Partial Derivative with respect to each variable:'
    for k,v in self.ders.items():
      result += f'variable ({k}): {v}'
    return result



  def __repr__(self) -> str: 
    """return the type which is class, and the class name which is Dual"""
    class_name = type(self).__name__
    return f"{class_name}({self.value},{self.ders})"


  def __add__(self, other): 
    """Add two Dual numbers or add a scaler to a Dual number"""
    if isinstance(other, Dual):
      new_ders = defaultdict(float)
      for k,v in self.ders.items():
        new_ders[k]+=v
      for k,v in other.ders.items():
        new_ders[k]+=v
      return Dual(self.value+other.value,new_ders)
    else:
      return Dual(self.value+other,self.ders)

  def __radd__(self,other):
    """right add function """
    return self.__add__(other)

  def __mul__(self,other):
    """Product Rule & Multiplication by constant"""
    if isinstance(other, Dual):
      new_ders = dict()
      for k,v in self.ders.items():
        if k in other.ders.keys():
          new_ders[k] = v*other.value+self.value*other.ders[k]
        else:
          new_ders[k] = v*other.value
      
      for k,v in other.ders.items():
        if k not in self.ders.keys():
          new_ders[k]=v*self.value
      return Dual(self.value*other.value,new_ders)

    else:
      new_ders = dict()
      for k,v in self.ders.items():
        new_ders[k] = v*other
      return Dual(self.value*other,new_ders)



  def __rmul__(self,other): 
    """Product Rule & Multiplication by constant"""
    return self.__mul__(other)

  def __sub__(self,other) :
    """Subtract other from self and return result"""
    return self + (-1)*other


  def __rsub__(self,other):
    """Difference rule"""
    return self.__sub__(other)

  def __div__(self,other):
    """Quotient Rule & Reciprocal Rule: python 2"""
    return self * (other ** (-1))

  def __rdiv__(self,other):
    """Quotient Rule & Reciprocal Rule: python 2"""
    return self.__div__(other)


  def __truediv__(self,other):
    """Quotient Rule & Reciprocal Rule: python 3"""
    return self * (other ** (-1))

  def __rtruediv__(self,other):
    """Quotient Rule & Reciprocal Rule: python 3"""
    return self.__truediv__(other)

  def __pow__(self,other):
    """Power rule"""
    if type(other) == float or type(other) ==  int:
      value = self.value**other
      new_ders = defaultdict(float)
      for k,v in self.ders.items():
        new_ders[k] = (other*(self.value)**(other-1))*v
          
    else:
      raise Exception('No Dual class')
    return Dual(value,new_ders)


  def __neg__(self,other):
    """Multiplication by constant"""
    self.value = -self.value
    for k,v in self.ders.items():
      self.ders[k] = -v

    return self

if __name__ == "__main__":
  x1 = Dual(2,{'x1':1}) 
  x2 = Dual(4,{'x2':1})
  x3 = Dual(5,{'x3':1})

  # Second is to implement a function with the initialized variables. The returned value (f)  is itself a Dual as well. 
  f = x1 * 3 + (x1)*x3 

  # Get the partial derivative of function with respect to variable x1 
  partial_x1 =  f.partial('x1') # return a single real number
  print("The derivative of f with respect to x1:",partial_x1)

  # Get all the gradients of the function 
  gradient =  f.gradient() # return a dictionary with key being variable name and value being the respective partial derivative
  print("The gradients of f:",gradient)
  f = x1 * 3
  partial_x1 =  f.partial('x1') # return a single real number
  print("The derivative of f with respect to x1:",partial_x1)

  # Get all the gradients of the function 
  gradient =  f.gradient()



