import pytest
import math

from src.Reverse import Variable, Constant, Node
from src.Reverse_deriv import *

class TestFunctions:
    ''' @Jason & @Robert: Please look at the natural log for reference. We have a different way to initialize Variable and Constant and to get the partial derivative.'''
    
    # Trig functions tests 
        
    def test_sin(self):
   
        x1 = Variable('x1',-3) 
        x2 = Variable('x2',0) 
        x3 = Variable('x3',10) 

        f = sin(x1)
        assert f.value == math.sin(-3)
        assert f.partial(x1)  == math.cos(-3)
        f2 = sin(x2)
        assert f2.value == math.sin(0)
        assert f2.partial(x2)== math.cos(0)
        f3 = sin(x3)
        assert f3.value == math.sin(10)
        assert f3.partial(x3) == math.cos(10)

    def test_cos(self):
       
        x1 = Variable('x1',-3) 
        x2 = Variable('x1',0) 
        x3 = Variable('x1',1) 

        f = cos(x1)
        assert f.value == math.cos(-3)
        assert f.partial(x1) == -math.sin(-3)
        
        f2 = cos(x2)
        assert f2.value == math.cos(0)
        assert f2.partial(x2) == -math.sin(0)
        
        f3 = cos(x3)
        assert f3.value == math.cos(1)
        assert f3.partial(x3) == -math.sin(1)

    def test_tan(self):
    
        x1 = Variable('x1',-3) 
        x2 = Variable('x1',0) 
        x3 = Variable('x1',1) 

        f = tan(x1)
        assert f.value == math.tan(-3)
        assert f.partial(x1) == (1/math.cos(-3))**2
        
        f2 = tan(x2)
        assert f2.value == math.tan(0)
        assert f2.partial(x2) == (1/math.cos(0))**2
        
        f3 = tan(x3)
        assert f3.value == math.tan(1)
        assert f3.partial(x3) == (1/math.cos(1))**2 

    # Inverse trig functions tests 

    def test_asin(self):
    
        x1 = Variable('x1', math.pi/4) 

        f = asin(x1)
        assert f.value == math.asin(math.pi/4)
        assert f.partial(x1) == 1/math.sqrt(1-(math.pi/4)**2)

    def test_acos(self):
        
        x1 = Variable('x1',math.pi/6) 
    
        f = acos(x1)
        assert f.value == math.acos(math.pi/6)
        assert f.partial(x1) == -1/math.sqrt(1-(math.pi/6)**2)

    def test_atan(self):
    
        x1 = Variable('x1',math.pi/3) 

        f = atan(x1)
        assert f.value == math.atan(math.pi/3)
        assert f.partial(x1) == 1/(((math.pi/3)**2) + 1)

    # Exponential functions tests

    def test_exp(self):
    
        x1 = Variable('x1',-3) 
        x2 = Variable('x1',4) 

        f = exp(x1)
        assert f.value == math.exp(-3)
        assert f.partial(x1) == math.exp(-3)

        f2 = exp(x2)
        assert f2.value == math.exp(4)
        assert f2.partial(x2) == math.exp(4)

    def test_power(self):

        x1 = Variable('x1',4) 
        c1 = Constant(4)


        f = power(x1,c1)
        assert f.value == math.pow(4,4)
        assert f.partial(x1) == math.log(4) * math.pow(4,4)

    # Hyperbolic function tests 

    def test_sinh(self):

        x1 = Variable('x1',1) 

        f = sinh(x1)
        assert round(f.value,5) == round(math.sinh(1),5)
        assert round(f.partial(x1),5) == round(math.cosh(1),5)

    def test_cosh(self):

        x1 = Variable('x1',1) 

        f = cosh(x1)
        assert round(f.value,5) == round(math.cosh(1),5)
        assert round(f.partial(x1),5) == round(math.sinh(1),5)

    def test_tanh(self):

        x1 = Variable('x1',2) 

        f = tanh(x1)
        assert round(f.value,5) == round(math.tanh(2),5)
        assert round(f.partial(x1),5) == round((1/math.cosh(2))**2,5)

    # Logistic function test

    def test_logistic(self):

        x1 = Variable('x1',11) 

        f = logistic(x1)
        assert round(f.value,5) == round(1/(1+math.exp(-11)),5)
        assert round(f.partial(x1),5) == round((math.exp(-11))/(1+math.exp(-11))**2,5)


    # Logarithms tests 

    def test_naturallog(self):
        """Example for reference"""
        x1 = Variable('x1',2) 
        x2 = Variable('x2',4)

        f = ln(x1)
        assert f.value == math.log(2)
        assert f.partial(x1) == 1/2

        f2 = ln(x2)
        assert f2.value == math.log(4)
        assert f2.partial(x2) == 1/4

    def test_baselog(self):
        
        x1 = Variable('x1',2) 
        x2 = Variable('x2',4)
        x3 = Constant(3)
        x10 = Constant(10)

        f = log(x1,x3)
        assert f.value == math.log(2,3)
        assert f.partial(x1) == 1/(2*math.log(3))

        f2 = log(x2,x10)
        assert f2.value == math.log(4,10)
        assert f2.partial(x2) == 1/(4*math.log(10))

    # Square root test

    def test_sqrt(self):
        
        x1 = Variable('x1',16) 

        f = sqrt(x1)
        assert f.value == math.sqrt(16)
        assert round(f.partial(x1),5) == round((1/2)*((16)**(-1/2)),5)
  
    def test_initNode(self):
        with pytest.raises(Exception) as e_info:
            Node(1)
        with pytest.raises(Exception) as e_info:
            Node(Node(Variable('x1',1)))
        with pytest.raises(Exception) as e_info:
            Node(Variable('x1',1),Variable('x2',1))
        with pytest.raises(Exception) as e_info:
            Node(Variable('x1',1),Variable('x2',1),2,'ln')
    
    def test_inputTypeError(self):
        """The input type has to be Variable, Constant, or Node. Need one for each operator overloading and elementary functions. I gave four examples. Please add more according to the number of functions we have. """
        #     __add__
        with pytest.raises(Exception) as e_info:
            x1 = Variable("x1",1)
            x1+3

        #     __radd__
        with pytest.raises(Exception) as e_info:
            x1 = Variable("x1",1)
            3+x1

        #     __mul__
        with pytest.raises(Exception) as e_info:
            x1 = Variable("x1",1)
            x1*3

        #     __rmul__
        with pytest.raises(Exception) as e_info:
            x1 = Variable("x1",1)
            3*x1
        #__truediv__    
        with pytest.raises(Exception) as e_info:
            x1 = Variable("x1",1)
            x1/3.2
        #__rtruediv__    
        with pytest.raises(Exception) as e_info:
            x1 = Variable("x1",1)
            3.2/x1
        # __sub__    
        with pytest.raises(Exception) as e_info:
            x1 = Variable("x1",1)
            x1-10
        # __rsub__    
        with pytest.raises(Exception) as e_info:
            x1 = Variable("x1",1)
            3-x1
        # __pow__
        with pytest.raises(Exception) as e_info:
            x1 = Variable("x1",1)
            x1**10
            
