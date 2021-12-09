import math
import numpy as np

from src.Reverse import Variable, Constant, Node

def sin(node) -> Node:
    """sine of the dual number a, using math.sin(x) and math.cos(x)"""
    return Node(node, None, np.sin(node.value), 'sin' )

def cos(node) -> Node:
    """cosine of the dual number a, using math.sin(x) and math.cos(x)"""
    return Node(node, None, np.cos(node.value), 'cos' )

def tan(node) -> Node:
    """tangent of the dual number a, using math.tan(x) and math.cos(x)"""
    return Node(node, None, np.tan(node.value), 'tan' )


# Inverse trig functions

def asin(node) -> Node:
    """inverse of sine or arcsine of the dual number a, using math.asin(x)"""
    return Node(node, None, np.arcsin(node.value), 'asin' )

def acos(node) -> Node:
    """inverse of cosine of the dual number a, using math.acos(x)"""
    return Node(node, None, np.arccos(node.value), 'acos' )

def atan(node) -> Node:
    """inverse of tangent of the dual number a, using math.atan(x)"""
    return Node(node, None, np.arctan(node.value), 'atan' )


# Exponential functions

def exp(node) -> Dual:
    """Exponential of the dual number a, using math.exp(x)"""
    return Node(node, None, np.exp(node.value), 'exp' )

def power(node, p: int or float) -> Node:
    """power (dual number) of base p (integer or float number), using math.power(x, y)"""
    return Node(node, p, p**(node.value), 'power' )


# Hyperbolic functions

def sinh(node) -> Node:
    """sinh of the dual number a, using math.sinh(x) and math.cosh(x)"""
    return Node(node, None, np.sinh(node.value), 'sinh' )

def cosh(node) -> Node:
    """cosh of the dual number a, using math.cosh(x)"""
    return Node(node, None, np.cosh(node.value), 'cosh' )

def tanh(node) -> Node:
    """tanh of the dual number a, using math.tanh(x)"""
    return Node(node, None, np.tanh(node.value), 'tahn' )


# Logistic functions

def logistic(node) -> Node:
    """logistic function of the dual number a, using math.exp(x)"""
    return Node(node, None, 1/(1+np.exp(-node.value)), 'logistic' )
  

# Logarithms

def ln(node):
    return Node(node, None, np.log(node.value), 'ln' )

def log(node, base):
    if type(base) != Constant or type(base.value) != int:
        raise Exception('base has to be a Constant with integer value')
    return Node(node, base, 
                np.log(node.value) / np.log(base.value), 
                'log'+str(base.value))

# Square root

def sqrt(node) -> Dual:
    """square root of a dual number"""
    return Node(node, None, np.sqrt(node.value), 'sqrt' )



