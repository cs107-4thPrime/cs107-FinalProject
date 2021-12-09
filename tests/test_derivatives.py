import pytest
import math

from src.Dual_class import *
from src.Derivatives import *

class TestFunctions:
    # Trig functions tests 

    def test_sin(self):
        x1 = Dual(-3,{'x1':1}) 
        x2 = Dual(0,{'x2':1})
        x3 = Dual(10,{'x3':1})
        x4 = Dual(math.pi/2,{'x4':1})

        f = sin(x1)
        assert f.value == math.sin(-3)
        assert f.ders['x1'] == math.cos(-3)
        f2 = sin(x2)
        assert f2.value == math.sin(0)
        assert f2.ders['x2'] == math.cos(0)
        f3 = sin(x3)
        assert f3.value == math.sin(10)
        assert f3.ders['x3'] == math.cos(10)
        f4 = sin(x4)
        assert f4.value == math.sin(math.pi/2)
        assert f4.ders['x4'] == math.cos(math.pi/2)
        
        

    def test_cos(self):
        x1 = Dual(-3,{'x1':1}) 
        x2 = Dual(0,{'x2':1})
        x3 = Dual(1,{'x2':1})
        x4 = Dual(math.pi/2,{'x4':1})

        f = cos(x1)
        assert f.value == math.cos(-3)
        assert f.ders['x1'] == -math.sin(-3)
        f2 = cos(x2)
        assert f2.value == math.cos(0)
        assert f2.ders['x2'] == -math.sin(0)
        f3 = cos(x3)
        assert f3.value == math.cos(1)
        assert f3.ders['x2'] == -math.sin(1)
        f4 = cos(x4)
        assert f4.value == math.cos(math.pi/2)
        assert f4.ders['x4'] == -math.sin(math.pi/2)

    def test_tan(self):
        x1 = Dual(-3,{'x1':1}) 
        x2 = Dual(0,{'x2':1})
        x3 = Dual(1,{'x2':1})

        f = tan(x1)
        assert f.value == math.tan(-3)
        assert f.ders['x1'] == (1/math.cos(-3))**2
        f2 = tan(x2)
        assert f2.value == math.tan(0)
        assert f2.ders['x2'] == (1/math.cos(0))**2
        f3 = tan(x3)
        assert f3.value == math.tan(1)
        assert f3.ders['x2'] == (1/math.cos(1))**2 

    # Inverse trig functions tests 

    def test_asin(self):

        x1 = Dual(math.pi/4,{'x1':1}) 

        f = asin(x1)
        assert f.value == math.asin(math.pi/4)
        assert f.ders['x1'] == 1/math.sqrt(1-(math.pi/4)**2)

    def test_acos(self):

        x1 = Dual(math.pi/6,{'x1':1}) 

        f = acos(x1)
        assert f.value == math.acos(math.pi/6)
        assert f.ders['x1'] == -1/math.sqrt(1-(math.pi/6)**2)

    def test_atan(self):

        x1 = Dual(math.pi/3,{'x1':1}) 

        f = atan(x1)
        assert f.value == math.atan(math.pi/3)
        assert f.ders['x1'] == 1/(((math.pi/3)**2) + 1)

    # Exponential functions tests

    def test_exp(self):

        x1 = Dual(-3,{'x1':1}) 
        x2 = Dual(4,{'x2':1})

        f = exp(x1)
        assert f.value == math.exp(-3)
        assert f.ders['x1'] == math.exp(-3)

        f2 = exp(x2)
        assert f2.value == math.exp(4)
        assert f2.ders['x2'] == math.exp(4)

    def test_power(self):

        x1 = Dual(4,{'x1':1}) 

        f = power(x1,4)
        assert f.value == math.pow(4,4)
        assert f.ders['x1'] == math.log(4) * math.pow(4,4)

    # Hyperbolic function tests 

    def test_sinh(self):

        x1 = Dual(1, {'x1':1})

        f = sinh(x1)
        assert round(f.value,5) == round(math.sinh(1),5)
        assert round(f.ders['x1'],5) == round(math.cosh(1),5)

    def test_cosh(self):

        x1 = Dual(1, {'x1':1})

        f = cosh(x1)
        assert round(f.value,5) == round(math.cosh(1),5)
        assert round(f.ders['x1'],5) == round(math.sinh(1),5)

    def test_tanh(self):

        x1 = Dual(2, {'x1':1})

        f = tanh(x1)
        assert round(f.value,5) == round(math.tanh(2),5)
        assert round(f.ders['x1'],5) == round((1/math.cosh(2))**2,5)

    # Logistic function test

    def test_logistic(self):

        x1 = Dual(11, {'x1':1})

        f = logistic(x1)
        assert round(f.value,5) == round(1/(1+math.exp(-11)),5)
        assert round(f.ders['x1'],5) == round((math.exp(-11))/(1+math.exp(-11))**2,5)


    # Logarithms tests 

    def test_naturallog(self):
        x1 = Dual(2,{'x1':1}) 
        x2 = Dual(4,{'x2':1})

        f = ln(x1)
        assert f.value == math.log(2)
        assert f.ders['x1'] == 1/2

        f2 = ln(x2)
        assert f2.value == math.log(4)
        assert f2.ders['x2'] == 1/4

    def test_baselog(self):
        x1 = Dual(2,{'x1':1}) 
        x2 = Dual(4,{'x2':1})

        f = log(x1,3)
        assert f.value == math.log(2,3)
        assert f.ders['x1'] == 1/(2*math.log(3))

        f2 = log(x2,10)
        assert f2.value == math.log(4,10)
        assert f2.ders['x2'] == 1/(4*math.log(10))

    # Square root test

    def test_sqrt(self):

        x1 = Dual(16,{'x1':1}) 

        f = sqrt(x1)
        assert f.value == math.sqrt(16)
        assert round(f.ders['x1'],5) == round((1/2)*((16)**(-1/2)),5)


def example_log_domainValueError():
    """If you have code that raises exceptions, pythest can verity them. 
    Assert function is raising correct Error: 
    https://docs.pytest.org/en/6.2.x/getting-started.html
    """
    x1 = Dual(-2,{'x1':1}) 
    x3 = Dual(0,{'x3':1})
  
    with pytest.raises(ValueError):
        f = ln(x1)
    with pytest.raises(ValueError):
        f = ln(x2)
    with pytest.raises(ValueError):
        f = log(x1,3)
    with pytest.raises(ValueError):
        f = log(x2,5)

def example_tan_domainValueError():

    x1 = Dual(math.pi/2,{'x1':1}) 
    x2 = Dual(math.pi/2+math.pi,{'x2':1})
  
    with pytest.raises(ValueError):
        f = tan(x1)
    with pytest.raises(ValueError):
        f = tan(x2)
  

def example_asin_acos_domainValueError():
  
    x1 = Dual(2,{'x1':1}) 
    x2 = Dual(2,{'x2':1})
  
    with pytest.raises(ValueError):
        f = asin(x1)
    with pytest.raises(ValueError):
        f = acos(x2)

def example_sqrt_domainValueError():
  
    x1 = Dual(-1,{'x1':1}) 
  
    with pytest.raises(ValueError):
        f = sqrt(x1)
