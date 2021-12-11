import pytest
import numpy as np
import math

from src.Dual_class import *
from src.Derivatives import *

class TestFunctions:
  def test_sum1(self):
    a = createVariable('x1',1)
    b = createVariable('x2',10)
    c = createVariable('x3',-1)
    d = createVariable('x4',-2.5)
    f1 = 2*a+(-1)*b + c**3 -d-d/5
    print(f1.value)
    assert f1.value == 2*1+ (-1)*10 + (-1)**3 -(-2.5)-(-2.5)/5
    assert f1.partial('x1') == 2
    assert f1.partial('x2') == -1
    assert f1.partial('x3') == 3
    assert f1.partial('x4') == -6/5
    
  def test_trig1(self):
    a = createVariable('x1',1)
    b = createVariable('x2',10)
    c = createVariable('x3',-1)
    d = createVariable('x4',-2.5)
    f1 = sin(a) * cos(b) + tan(c*d)
    
    assert round(f1.value,14) == round(math.sin(1) * math.cos(10) + math.tan((-1)*(-2.5)),14)
    assert round(f1.partial("x1"),15) == round( math.cos(10) * math.cos(1),15)
    assert round(f1.partial("x2"),15) == round(-math.sin(10) * math.sin(1),15)
    assert round(f1.partial("x3"),14) == round(1/math.cos((-1)*(-2.5))**2 * (-2.5),14)
    assert round(f1.partial("x4"),14) == round(1/math.cos((-1)*(-2.5))**2 * (-1),14)
    
    
  def test_exp1(self):
    a = createVariable('x1',1)
    b = createVariable('x2',10)
    c = createVariable('x3',-1)
    d = createVariable('x4',-2.5)
    f1 = exp(a)+pow(b,2) 
#     assert f1.value == math.exp(1) + (2)**10
#     assert f1.partial("x1") == math.exp(1)
#     assert f1.partial("x2") == math.ln(2)*2**10
    
def example_createVariableError():
  with pytest.raises(TypeError):
    x1 = createVariable('x1','x1_value') 
  with pytest.raises(TypeError):
    x1 = createVariable(1,'x1') 
  with pytest.raises(ValueError):
    x1 = createVariable('x1',None) 