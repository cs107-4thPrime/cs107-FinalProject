import numpy as np

from src.Reverse import Variable, Constant, Node

def sin(node) -> Node:
    """sine of the node, using np.sin(x) and np.cos(x)"""
    return Node(node, None, np.sin(node.value), 'sin' )

def cos(node) -> Node:
    """cosine of the node, using np.sin(x) and np.cos(x)"""
    return Node(node, None, np.cos(node.value), 'cos' )

def tan(node) -> Node:
    """tangent of the node, using np.tan(x) and np.cos(x)"""
    return Node(node, None, np.tan(node.value), 'tan' )


# Inverse trig functions

def asin(node) -> Node:
    """inverse of sine or arcsine of the node, using np.asin(x)"""
    return Node(node, None, np.arcsin(node.value), 'asin' )

def acos(node) -> Node:
    """inverse of cosine of the node, using np.acos(x)"""
    return Node(node, None, np.arccos(node.value), 'acos' )

def atan(node) -> Node:
    """inverse of tangent of the node, using np.atan(x)"""
    return Node(node, None, np.arctan(node.value), 'atan' )


# Exponential functions

def exp(node) -> Node:
    """Exponential of the node, using np.exp(x)"""
    return Node(node, None, np.exp(node.value), 'exp' )

def power(node, p) -> Node:
    """power (node) of base p (Constant), using np.power(x, y)"""
    return Node(node, p, p.value**(node.value), 'power' )


# Hyperbolic functions

def sinh(node) -> Node:
    """sinh of the node, using np.sinh(x) and np.cosh(x)"""
    return Node(node, None, np.sinh(node.value), 'sinh' )

def cosh(node) -> Node:
    """cosh of the node, using np.cosh(x)"""
    return Node(node, None, np.cosh(node.value), 'cosh' )

def tanh(node) -> Node:
    """tanh of the node, using np.tanh(x)"""
    return Node(node, None, np.tanh(node.value), 'tanh' )


# Logistic functions

def logistic(node) -> Node:
    """logistic function of the node, using np.exp(x)"""
    return Node(node, None, 1/(1+np.exp(-node.value)), 'logistic' )
  

# Logarithms

def ln(node):
    '''ln function of the node, using np.log(x) '''
    return Node(node, None, np.log(node.value), 'ln' )

def log(node, base):
    '''log function of the node, using np.log'''
    if type(base) != Constant or type(base.value) != int:
        raise Exception('base has to be a Constant with integer value')
    return Node(node, base, 
                np.log(node.value) / np.log(base.value), 
                'log')

# Square root

def sqrt(node) -> Node:
    """square root of the node, np.sqrt"""
    return Node(node, None, np.sqrt(node.value), 'sqrt' )



