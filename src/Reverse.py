import numpy as np
import math
INPUT_ERROR = "Input should be one of Variable, Constant, or Node"
VAR_TYPE_ERROR = "Invalid input type: var should be a Variable"
MISSING_OP = 'Operator should not be None when child1 is Node'
ROOT_C2_ERROR = "Should not initialize child2 on the root."    
OPERATOR_TYPE_ERROR = "Operator type not supported"
SINGLE_VAR_ERROR = "Operator type only operates on single variable (child 1)"

    
class Node:
    SINGLE_VAR = ['ln','sqrt', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'exp', 'sinh', 'cosh', 'tanh', 'logistic', 'ln', 'sqrt'] 
    MULTI_VAR = ['+', '-', '*', '/', '**', 'power', 'log'] 
    
    
    def __init__(self, child1, child2=None, value = None, operator = None):
        self.child1 = child1
        if child1 is None or not self._isValid(child1) :
            raise Exception(INPUT_ERROR)
        self.isroot = operator is None
        self.operator = operator
        if self.isroot and type(self.child1) == Node:
            raise Exception(MISSING_OP)
        if self.isroot and child2 is not None:
            raise Exception(ROOT_C2_ERROR)
            
         
        self.child2 = child2
        self.value = value  
        if self.value is None:
            self.value = self.child1.value

        self.variables = child1._getvariable()
        if child2 is not None:
            self.variables = set.union(self.variables,
                                   child2._getvariable())
        
        # If the operator is in the SINGLE_VAR category: 
        # check that the first child should not be None and the second child should be None 
        if operator in self.SINGLE_VAR:
            if self.child1 == None or self.child2 is not None:
                raise Exception(SINGLE_VAR_ERROR)
        
    def getvalue(self) -> float: 
        """return the current value"""
        return self.value
    
    def _isValid(self,c):
        return type(c) in [Variable, Constant, Node]
    

    def _getvariable(self):
        return self.variables

    
    def _str(self, i):
        dash = ' '*i+"-"
        
        result = f'{dash} {self.operator}\n'
        result += self.child1._str(i+1)
        if self.child2 is not None:
            result += self.child2._str(i+1)
        return result
            
    def __str__(self) :
        i = 1
        result = self._str(i)
        return result
    
    def __repr__(self) -> str: 
        """return string which can be used to reconstruct """
        class_name = type(self).__name__
        return f'''{class_name}({self.child1.__repr__()}, {self.child2.__repr__()}, {self.value}, "{self.operator}")'''
    
    def __add__(self, other):
        if not self._isValid(other):
            raise Exception(INPUT_ERROR)
            
        return Node(self, other, self.value+other.value, "+")

    
    def __mul__(self, other):
        print(self.value)
        if not self._isValid(other):
            raise Exception(INPUT_ERROR)
            
        return Node(self, other, self.value*other.value, "*")

    
    def __truediv__(self,other):
        if not self._isValid(other):
            raise Exception(INPUT_ERROR)
            
        return Node(self, other, self.value/other.value, "/")

    
    def __neg__(self):
        return Node(self, None, -self.value, "-")
    
    def __sub__(self,other):
        if not self._isValid(other):
            raise Exception(INPUT_ERROR)
        return Node(self,other, self.value-other.value,'-')
    
    def __pow__(self,other):
        if not type(other) == Constant:
            raise Exception('Exponent of a Node has to be a Constant.')
        return Node(self,other, self.value**other.value,'**')
    
    def _reverse(self, target_var, node):
        if node is None:
            return 0
        else:
            return node.reverse(target_var)
    
    def partial(self, var) :
        return self.reverse(var)
        
    def reverse(self, var):
            
        v1 = self.child1.value
        d1 = self._reverse(var, self.child1)
        
        if self.child2 is not None:
            v2 = self.child2.value
            d2 = self._reverse(var, self.child2)

        # Some operations (multiple vars)
        if self.isroot:
            return d1
        elif self.operator == '+':
            return d1+d2
        elif self.operator == '*':
            return d1*v2 + d2*v1
        elif self.operator == '/':
            return -(v1*d2 - v2*d1)/ (v2**2)
        elif self.operator == '-':
            if self.child2 is not None:
                return d1-d2
            else:
                return -d1
        elif self.operator == '**':
            if v2 == 0:
                return 0
            return v2 * v1 **(v2-1) * d1
        
        # Trig functions
        elif self.operator == 'sin':
            return np.cos(v1)*d1
        elif self.operator == 'cos':
            return (-1)*np.sin(v1)*d1
        elif self.operator == 'tan':
            return 1/((np.cos(v1))**2)*d1

        # Inverse trig functions
        elif self.operator == 'asin':
            if abs(v1) >= 1:
                raise ValueError('Arcsin cannot be evaluated at {}.'.format(v1))
            return 1/(np.sqrt(1-v1**2))*d1
        elif self.operator == 'acos':
            if abs(v1) >= 1:
                raise ValueError('Arccos cannot be evaluated at {}.'.format(v1))
            return (-1)/(np.sqrt(1-(v1)**2))*d1
        elif self.operator == 'atan':
            return 1/(1+(v1)**2)*d1

        # Exponential functions
        elif self.operator == 'exp':
            return np.exp(v1)*d1
        elif self.operator == 'power':
            return math.pow(v2,v1)*math.log(v2)*d1

        # Hyperbolic functions
        elif self.operator == 'sinh':
            return np.cosh(v1)*d1
        elif self.operator == 'cosh':
            return np.sinh(v1)*d1
        elif self.operator == 'tanh':
            return 1/(np.cosh(v1)**2)*d1

        # Logistic functions
        elif self.operator == 'logistic':
            return (np.exp(v1)/((1 + np.exp(v1))**2))*d1

        # Logarithms
        elif self.operator == 'ln':
            return 1/(v1) * d1
        elif self.operator == 'log':
            return 1/(v1 * np.log(v2))*d1

        # Square root
        elif self.operator == 'sqrt':
            return (1/2)*(v1**(-1/2))*d1
        
        # If entered operator does not match with the existing implementation list of variables in this library, raise Error
        else:
            raise Exception(OPERATOR_TYPE_ERROR)
        return None
        
class Variable(Node):
    def __init__(self, name, value):
        self.name =name
        self.value = value
        
    def _getvariable(self):
        return {self}
        
    def partial(self,var):
        if var is self:
            return 1
        return 0
    
    def reverse(self,var):
        if var is self:
            return 1
        return 0
        
    def _str(self, i):
        dash = ' '*i+"-"
        return f'{dash} {self.name}={self.value}\n'
    
    def __str__(self):
        return f'{self.name}={self.value}'
    
    def __repr__(self):
        class_name = type(self).__name__
        return f'''{class_name}("{self.name}", {self.value})'''
    
class Constant(Node):
    def __init__(self, value):
        self.value = value
        self.name = 'Constant'
    def _getvariable(self):
        return {self}
        
    def partial(self,var):
        return 0
    def reverse(self,var):
        return 0
    
    def _str(self, i):
        dash = ' '*i+"-"
        return f'{dash} Constant={self.value}\n'
    
    def __str__(self):
        return f'Constant={self.value}'
    
    def __repr__(self):
        class_name = type(self).__name__
        return f'''{class_name}({self.value})'''
