# -*- coding: utf-8 -*-
"""Derivatives

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lgKPUisx1cm7ZNmzYdkuCZPBHKLT_J1s
"""

import math
import numpy as np
from Dual_class import Dual

def ln(a: Dual) -> Dual:
  """Natural log of Dual number a, using math.log(x)"""
  value = math.log(a.value)
  ders = dict()
  for k,v in a.ders.items():
    ders[k] = 1/(a.value) * v
  return Dual(value, ders)

def log(a: Dual, base: int) -> Dual:
  """Log of Dual number a with base n, using math.log(x, base)"""
  value = math.log(a.value, base)
  ders = dict()
  for k,v in a.ders.items():
    ders[k] = 1/(a.value * math.log(base))*v
  return Dual(value, ders)

def exp(a: Dual) -> Dual:
  """Exponential of the dual number a, using math.exp(x)"""
  value = math.exp(a.value)
  ders = dict()
  for k,v in a.ders.items():
    ders[k] = math.exp(a.value)*v
  return Dual(value, ders)  

def power(a: Dual, p: int or float) -> Dual:
   """power (dual number) of base p (integer or float number), using math.power(x, y)"""
   """test for the power(a: Dual, p: int or float) function is not yet implemented in test_derivatives.py"""
   value = math.power(p, a)
   ders = dict()
   for k,v in a.ders.items():
     ders[k] = a*(p**(a-1))*v
   return Dual(value, ders)

def sin(a: Dual) -> Dual:
  """sine of the dual number a, using math.sin(x) and math.cos(x)"""
  value = math.sin(a.value)
  ders = dict()
  for k,v in a.ders.items():
    ders[k] = math.cos(a.value)*v
  return Dual(value, ders)

def cos(a: Dual) -> Dual:
  """cosine of the dual number a, using math.sin(x) and math.cos(x)"""
  value = math.cos(a.value)
  ders = dict()
  for k,v in a.ders.items():
    ders[k] = (-1)*math.sin(a.value)*v
  return Dual(value, ders)

def tan(a: Dual) -> Dual:
  """tangent of the dual number a, using math.tan(x) and math.cos(x)"""
  value = math.tan(a.value)
  ders = dict()
  for k,v in a.ders.items():
    ders[k] = 1/((math.cos(a.value))**2)*v
  return Dual(value, ders)

def asin(a: Dual) -> Dual:
  """inverse of sine or arcsine of the dual number a, using math.asin(x)"""
  if abs(a.value) >= 1:
    raise ValueError('Arcsin cannot be evaluated at {}.'.format(a.value))
  value = math.asin(a.value)
  ders = dict()
  for k,v in a.ders.items():
    ders[k] = 1/(math.sqrt(1-a.value**2))*v
  return Dual(value, ders)

def acos(a: Dual) -> Dual:
  """inverse of cosine of the dual number a, using math.acos(x)"""
  if abs(a.value) >= 1:
    raise ValueError('Arccos cannot be evaluated at {}.'.format(a.value))
  value = a.value
  print(value)
  value = math.acos(a.value)
  print(value)
  ders = dict()
  for k,v in a.ders.items():
    ders[k] = (-1)/(math.sqrt(1-(a.value)**2))*v
  return Dual(value, ders)

def atan(a: Dual) -> Dual:
  """inverse of tangent of the dual number a, using math.atan(x)"""
  value = math.atan(a.value)
  ders = dict()
  for k,v in a.ders.items():
    ders[k] = 1/(1+(a.value)**2)*v
  return Dual(value, ders)

def sinh(a: Dual) -> Dual:
   """sinh of the dual number a, using math.sinh(x) and math.cosh(x)"""
   """test for the sinh(a: Dual) function is not yet implemented in test_derivatives.py"""
   value = math.sinh(a.value)
   ders = dict()
   for k,v in a.ders.items():
     ders[k] = math.cosh(a.value)*v
   return Dual(value, ders)

def cosh(a: Dual) -> Dual:
   """cosh of the dual number a, using math.cosh(x)"""
   """test for the cosh(a: Dual) function is not yet implemented in test_derivatives.py"""
   value = math.cosh(a.value)
   ders = dict()
   for k,v in a.ders.items():
     ders[k] = math.sinh(a.value)*v
   return Dual(value, ders)

def tanh(a: Dual) -> Dual:
   """tanh of the dual number a, using math.tanh(x)"""
   """test for the tanh(a: Dual) function is not yet implemented in test_derivatives.py"""
   value = math.tanh(a.value)
   ders = dict()
   for k,v in a.ders.items():
     ders[k] = 1/(math.cosh(a.value)**2)*v

def sqrt(a: Dual) -> Dual:
  """square root of a dual number"""
  value = math.sqrt(a.value)
  ders = dict()
  for k,v in a.ders.items():
    ders[k] = (1/2)*(a.value**(-1/2))*v
  return Dual(value, ders)
