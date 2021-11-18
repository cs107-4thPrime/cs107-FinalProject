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

#   def test_add(self): 
#     testsum=self.dual+self.dual #to test, lets try adding dual to itself
#     testders={} 
#     for i in self.dual.ders:
#       testders[i]=2*self.dual.ders[i]

#     assert testsum==Dual(2*self.dual.val,testders)
#     pass

#   def test_radd(self):
#     return test_add(self)

#   def test_mul(self):
#     testmul=self.dual*self.dual #to test, lets multiply it by itself
#     assert testmul.val==self.dual.val**2
#     assert testmul.ders["x1"]==2*self.dual.val*self.dual.ders["x1"]
#     return test_mul

#   def test_rmul(self):
#     return test_mul(self)

#   def test_sub(self):
#     nullders={} #to test, lets subtract it from itself
    
#     for i in self.dual.ders:
#       nullders[i]=0

#     assert self.dual-self.dual==Dual(0, nullders)

#   def test_rsub(self):
#     return test_sub(self)

#   def test_div():
# #     test_div=self.dual/self.dual

# #     assert test_div.val==1
# #     assert test_div.ders["x1"]==(self.dual.val*(1/self.dual.ders["x1"]+self.dual.ders["x1"]*(1/self.dual.val)))
#     pass

#   def test_rdiv(self):
# #       return test_div(self)
#     pass

#   def test_truediv(self):
# #     return test_div(self)

#   def test_rtruediv():
# #     return test_div(self)

#   def test_pow(self):
#     test_mul=self.test_mul(self)
#     testpow=self.test_mul(self) *self.dual
#     assert test_mul.val >=0
#     assert testpow.val==self.dual.val**3
#     assert testpow.ders["x1"]==self.dual.val*test_mul.ders["x1"] +self.dual.ders["x1"]*test_mul.val

#   def test_neg(self):
#     tst=self.dual*-1
#     assert tst.val==-self.dual.val
    
#   def test_zeroPowerZero(self):
#     tst=self.dual**0
#     assert tst.val==1
