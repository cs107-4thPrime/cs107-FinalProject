import math
from collections import defaultdict
import numpy as np

class Dual(object):
  def __init__(self,value, ders):
    """
    - value (real number): the current value of the function
    - ders (dict): {'variable name': 'partial derivative wrt. the variable'} 
    """
    self.value = value 
    self.ders = ders

  def partial(self,variable_name) -> float:
    """
    Get the partial derivative with respect to the given variable_name
    input: 
        - `variable_name`: string
    return :
        - output : float or int, the corresponding partial at current stage wrt. variable_name"""
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
    result += 'Partial Derivative with respect to each variable:\n'
    for k,v in self.ders.items():
      result += f'variable ({k}): {v}\n'
    return result

  def __repr__(self) -> str: 
    """return the type which is class which can construct the Dual with eval()"""
    class_name = type(self).__name__
    return f"{class_name}({self.value},{self.ders})"


  def __add__(self, other): 
    """
    = self + other
    Description: a Dual(self) plus other
    input: 
        - `self`: a dual class
        - `other`: another Dual or a constant, float or int
    result:
        - self with updated value and ders
    """
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
    """
    = other + self
    Description: a constant(other) plus a Dual(self) 
    input: 
        - `self`: a dual class
        - `other`: a constant , float or int
    result:
        - self with updated value and ders
    """
    return self.__add__(other)

  def __mul__(self,other):
    """
    = self * other
    Description: a Dual(self) times a constant or another Dual(other) 
    input: 
        - `self`: a dual class
        - `other`: another Dual or a constant , float or int
    result:
        - new Dual with updated value and ders
    """
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
    """
    = other * self
    Description: a constant(other) times a Dual(self) 
    input: 
        - `self`: a dual class
        - `other`: a constant , float or int
    result:
        - new Dual with updated value and ders
    """
    return self.__mul__(other)

  def __sub__(self,other) :
    """
    = self - sub
    Description: a Dual(self) minus a constant or another Dual(other) 
    input: 
        - `self`: a dual class
        - `other`: another Dual or a constant , float or int
    result:
        - self with updated value and ders
    """
    return self + (-1)*other


  def __rsub__(self,other):
    """
    = other - self
    Description: a constant(other) minus a Dual(self) 
    input: 
        - `self`: a dual class
        - `other`: a constant , float or int
    result:
        - self with updated value and ders
    """
    return self.__neg__()+other

  def __truediv__(self,other):
    """
    = self/other
    Description: a Dual (self) divided by a constant or Dual (other) 
    input: 
        - `self`: a dual class
        - `other`: another Dual or a constant , float or int
    result:
        - a new Dual class
    """
    return self * (other ** (-1))

  def __rtruediv__(self,other):
    """
    = other/self
    Description: a constant (other) divided by a Dual (self) 
    input: 
        - `self`: a dual class
        - `other`: a constant , float or int
    result:
        - a new Dual class
    """
    return self.__pow__(-1)*other

  def __pow__(self,other):
    """
    self**other
    Description: Dual class (self) to the power of a constant (other) 
    input: 
        - `self`: a dual class
        - `other`: a constant , float or int
    result:
        - a new Dual class
    """
    if type(other) == float or type(other) ==  int:
      value = self.value**other
      new_ders = defaultdict(float)
      if other != 0:
        for k,v in self.ders.items():
          new_ders[k] = (other*(self.value)**(other-1))*v
      else:
        for k,v in self.ders.items():
          new_ders[k] = 0
          
    elif type(other) == Dual:
      raise TypeError('Exponent of a Dual class can not be another Dual class')
    return Dual(value,new_ders)


  def __neg__(self):
    """
    = -self
    Description: negation of Dual(self) 
    input: 
        - `self`: a dual class
    return:
        - self with value and ders updated
    """
    self.value = -self.value
    for k,v in self.ders.items():
      self.ders[k] = -v

    return self

def createVariable(variable_name, value):
    """Create a variable of type Dual with the given value and variable name
    and the derivative of it being 1.
    input:
        -`variable_name`: string, the unique name for the variable
        -`value`: float or int, the current value sotred in the variable
    return :
        - Dual: a Dual number that represents the created variable 
        by only storing the information of the variable name with slope of 1
        and value"""
    if type(variable_name) != str:
        raise TypeError('variable_name should be of type string')
    if value is None:
        raise ValueError("value should not be None")
#     if type(value) != int and type(value) != float:
#         raise TypeError("value should be in type float or int")
    return Dual(value,{variable_name:1})

def vectorize_ders(fs):
    variable_set = set()
    for i in range(fs.shape[0]):
        for k in fs[i].ders.keys():
            variable_set.add(k)
    output = []
    for i in range(fs.shape[0]):
        temp = []
        for v in sorted(variable_set):
            
            if v in fs[i].ders.keys():
                temp.append(fs[i].ders[v])
            else:
                temp.append(0)
        output.append(temp)
    return sorted(variable_set),np.array(output)
