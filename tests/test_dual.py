import pytest
import math
from src.Dual_class import Dual

class DualTest:

  def __init__(self):
    self.dual=Dual(5, {"x1":3})

  def test_dualval(self):
    a = Dual(2, {'x1':1})
    b = Dual(3, {'x2':1})
    assert a.val==2
    assert b.val == 3

  def test_dualder(self, der):
    a = Dual(2, {'x1':1})
    b = Dual(3, {'x2':2})
    assert a.ders["x1"]==1
    assert b.ders["x2"] == 2

  def test_partial(self):
    assert self.dual.partial("x1")==self.dual.ders["x1"]
  
  def test_gradient(self):
    assert self.dual.gradient()==self.dual.ders
 
  def test_getvalue(self): 
    assert self.dual.getvalue()==self.dual.val

  def test_str(self):
    print(self.dual+"test")

  def test_repr(self):
    print(self.dual)

  def test_add(self): 
    testsum=self.dual+self.dual #to test, lets try adding dual to itself
    testders={} 
    for i in self.dual.ders:
      testders[i]=2*self.dual.ders[i]

    assert testsum==Dual(2*self.dual.val,testders)

  def test_radd(self):
    return test_add(self)

  def test_mul(self):
    testmul=self.dual*self.dual #to test, lets multiply it by itself
    assert testmul.val==self.dual.val**2
    assert testmul.ders["x1"]==2*self.dual.val*self.dual.ders["x1"]
    return test_mul

  def test_rmul(self):
    return test_mul(self)

  def test_sub(self):
    nullders={} #to test, lets subtract it from itself
    
    for i in self.dual.ders:
      nullders[i]=0

    assert self.dual-self.dual==Dual(0, nullders)

  def test_rsub(self):
    return test_sub(self)

  def test_div(self):
    test_div=self.dual/self.dual

    assert test_div.val==1
    assert test_div.ders["x1"]==(self.dual.val*(1/self.dual.ders["x1"]+self.dual.ders["x1"]*(1/self.dual.val)))

  def test_rdiv(self):
      return test_div(self)

  def test_truediv(self):
    return test_div(self)

  def test_rtruediv(self):
    return test_div(self)

  def test_pow(self):
    test_mul=self.test_mul(self)
    testpow=self.test_mul(self) *self.dual
    assert test_mul.val >=0
    assert testpow.val==self.dual.val**3
    assert testpow.ders["x1"]==self.dual.val*test_mul.ders["x1"] +self.dual.ders["x1"]*test_mul.val

  def test_neg(self):
    tst=self.dual*-1
    assert tst.val==-self.dual.val
    
  def test_zeroPowerZero(self):
    tst=self.dual**0
    assert tst.val==1
