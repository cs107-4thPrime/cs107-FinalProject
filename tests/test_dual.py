import pytest
import math
from src.Dual_class import Dual

class TestFunctions:

  def test_dualval(self):
    a = Dual(2, {'x1':1})
    b = Dual(3, {'x2':1})
    assert a.value==2
    assert b.value == 3

  def test_dualder(self):
    a = Dual(2, {'x1':1})
    b = Dual(3, {'x2':2})
    assert a.ders["x1"]==1
    assert b.ders["x2"] == 2

  def test_partial(self):
    a = Dual(2, {'x1':1})
    b = Dual(3, {'x2':1})
    c = a*b
    assert a.partial("x1")==a.ders["x1"]
    assert b.partial("x2")==b.ders["x2"]
    assert c.partial("x1")==3
    assert c.partial("x2")==2
    d = a-b
    assert d.partial("x1")==1
    assert d.partial("x2")==-1
    
  
  def test_gradient(self):
    a = Dual(2, {'x1':1})
    temp_dict = dict({'x1':1})
    for k,v in a.gradient().items():
        assert v==temp_dict[k]
    
    b = Dual(3, {'x2':1})
    c = a*b
    temp_dict = dict({'x1':3,'x2':2})
    for k,v in c.gradient().items():
        assert v==temp_dict[k]
        
    d = a-b
    temp_dict = dict({'x1':1,'x2':-1})
    for k,v in d.gradient().items():
        assert v==temp_dict[k]
 
  def test_getvalue(self): 
    a = Dual(2, {'x1':1})
    assert a.getvalue()==2
    
    b = Dual(3, {'x2':1})
    c = a*b
    assert c.getvalue() == 6
    
    d = a-b
    assert d.getvalue() == -1

  def test_str(self):
    a = Dual(2, {'x1':1})
    result = f'Current Value is : 2\n'
    result += 'Partial Derivative with respect to each variable:'
    result += f'variable (x1): 1'
    assert a.__str__() == result

  def test_repr(self):
    a = Dual(2, {'x1':1})
    print(a.__repr__())
    assert type(eval(a.__repr__())) == Dual
    assert isinstance(eval(a.__repr__()), Dual)

  def test_add(self): 
    a = Dual(2, {'x1':1})
    b = Dual(3, {'x1':1})
    testsum=a+b
    
    assert testsum.value==5
    assert testsum.ders=={'x1':2}

  def test_radd(self):
    a = Dual(2, {'x1':1})
    testsum=3+a
    
    assert testsum.value==5
    assert testsum.ders=={'x1':1}

  def test_mul(self):
    a = Dual(2, {'x1':1})
    b = Dual(3, {'x1':2})
    testmul=a*b
    
    assert testmul.value==6
    assert testmul.ders["x1"]==7

  def test_rmul(self):
    a = Dual(2, {'x1':1})
    testmul=2*a
    
    assert testmul.value==4
    assert testmul.ders["x1"]==2


  def test_sub(self):
    a = Dual(2, {'x1':1})
    testsub=a-a
    assert testsub.value==0
    assert testsub.ders=={"x1":0}

  def test_rsub(self):
    a = Dual(2, {'x1':1})
    testsub=a-1
    assert testsub.value==1
    assert testsub.ders=={'x1':1}

  def test_div(self):
    a = Dual(2, {'x1':1})
    b = Dual(3, {'x1':3})
    test_div=a/b

    assert test_div.value==2/3
    assert test_div.ders["x1"]==-1/3


  def test_rdiv(self):
    a = Dual(2, {'x1':1})
    test_div=a/2

    assert test_div.value==1
    assert test_div.ders=={"x1":1/2}

  def test_truediv(self):
    a = Dual(2, {'x1':1})
    b = Dual(3, {'x1':3})
    test_div=a/b

    assert test_div.value==2/3
    assert test_div.ders["x1"]==-1/3

  def test_rtruediv(self):
    a = Dual(2, {'x1':1})
    test_div=a/2

    assert test_div.value==1
    assert test_div.ders=={"x1":1/2}

  def test_pow(self):
    a = Dual(2, {'x1':3})
    testexp=a*a
    testcub=a*a*a
    
    assert testexp.value >=0
    assert testexp.value ==4
    assert testcub.value==8
    assert testexp.ders["x1"]==12
    assert testcub.ders["x1"]==36

  def test_neg(self):
    a = Dual(2, {'x1':3})
    tst=a*-1
    assert tst.value==-2
    assert tst.ders["x1"]==-3
    
  def test_zeroPowerZero(self):
    a = Dual(0, {'x1':3})
    tst=a**0
    assert tst.value==1
    assert tst.ders["x1"]==1
