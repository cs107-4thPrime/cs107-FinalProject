import pytest
import math
from src.cs107_4thprime.Dual_class import *

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
    result += 'Partial Derivative with respect to each variable:\n'
    result += f'variable (x1): 1\n'
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
    
    a = Dual(2, {'x1':1})
    b = 10
    testsum=a+b
    
    assert testsum.value==12
    assert testsum.ders=={'x1':1}
    
    a = Dual(2, {'x1':1})
    b = Dual(-3, {'x2':10})
    testsum=a+b
    
    assert testsum.value==-1
    assert testsum.ders=={'x1':1, 'x2':10}

  def test_radd(self):
    a = Dual(2, {'x1':1})
    testsum=3+a
    
    assert testsum.value==5
    assert testsum.ders=={'x1':1}
    
    a = Dual(2.5, {'x1':10})
    testsum=-13.2+a
    
    assert testsum.value==-10.7
    assert testsum.ders=={'x1':10}

  def test_mul(self):
    a = Dual(2, {'x1':1})
    b = Dual(3, {'x1':2})
    testmul=a*b
    
    assert testmul.value==6
    assert testmul.ders["x1"]==2*2+1*3
    
    testmul=b*3
    assert testmul.value==9
    assert testmul.ders["x1"]==6
    
    b = Dual(-3, {'x2':2})
    testmul=a*b
    assert testmul.value==-6
    assert testmul.ders["x1"]==-3
    assert testmul.ders["x2"]==4

  def test_rmul(self):
    a = Dual(2, {'x1':1})
    testmul=2.5*a
    
    assert testmul.value==5
    assert testmul.ders["x1"]==2.5
    
    testmul=(-2.5)*a
    
    assert testmul.value==-5
    assert testmul.ders["x1"]==-2.5


  def test_sub(self):
    a = Dual(2, {'x1':1})
    testsub=a-a
    assert testsub.value==0
    assert testsub.ders=={"x1":0}
    b = Dual(10, {'x2':2})
    testsub=a-b
    assert testsub.value==-8
    assert testsub.ders=={"x1":1,"x2":-2}
    
    testsub=a-10
    assert testsub.value==-8
    assert testsub.ders=={"x1":1}

  def test_rsub(self):
    a = Dual(2, {'x1':1})
    testsub=1-a
    assert testsub.value==-1
    assert testsub.ders=={'x1':-1}

  def test_div(self):
    a = Dual(2, {'x1':1})
    b = Dual(3, {'x1':2})
    test_div=a/b

    assert test_div.value==2/3
    assert test_div.ders=={'x1':(3*1-2*2)/3**2}
    
    b = Dual(3, {'x2':2})
    test_div=a/b

    assert test_div.value==2/3
    assert test_div.ders=={'x1':1/3, 'x2':-4/9}

    test_div=a/(-4)
    assert test_div.value==-2/4
    assert test_div.ders=={'x1':-1/4}


  def test_rdiv(self):
    a = Dual(2, {'x1':1})
    test_div=2/a

    assert test_div.value==1
    assert test_div.ders=={"x1":-2*1/2**2}

  def test_truediv(self):
    a = Dual(2, {'x1':1})
    b = Dual(3, {'x1':2})
    test_div=a/b

    assert test_div.value==2/3
    assert test_div.ders=={'x1':(3*1-2*2)/3**2}
    
    b = Dual(3, {'x2':2})
    test_div=a/b

    assert test_div.value==2/3
    assert test_div.ders=={'x1':1/3, 'x2':-4/9}

    test_div=a/(-4)
    assert test_div.value==-2/4
    assert test_div.ders=={'x1':-1/4}

  def test_rtruediv(self):
    a = Dual(2, {'x1':1})
    test_div=2/a

    assert test_div.value==1
    assert test_div.ders=={"x1":-2*1/2**2}

  def test_pow(self):
    a = Dual(2, {'x1':1})
    testexp=a**2
    testcub=a**3

    assert testexp.value ==4
    assert testcub.value==8
    assert testexp.ders["x1"]==4
    assert testcub.ders["x1"]==3*2**2
    
    t = a**(1)
    assert t.value == 2
    assert t.partial('x1')==1
    
    t = a**0
    assert t.value ==1
    assert t.partial('x1')==0
    
    t = a**(0.5)
    assert t.value == math.sqrt(2)
    assert t.partial('x1')==0.5*(2**(-0.5))
    
    t = a**(-1)
    assert t.value == 1/2
    assert t.partial('x1')==(-1)*(2**(-2))
    
    a = Dual(2, {'x1':3})
    testexp=a**2
    testcub=a**3

    assert testexp.value ==4
    assert testcub.value==8
    assert testexp.ders["x1"]==4*3
    assert testcub.ders["x1"]==3*2**2*3
    
    t = a**(1)
    assert t.value == 2
    assert t.partial('x1')==1*3
    
    t = a**(0.5)
    assert t.value == math.sqrt(2)
    assert t.partial('x1')==0.5*(2**(-0.5))*3
    
    t = a**(-1)
    assert t.value == 1/2
    assert t.partial('x1')==(-1)*(2**(-2))*3
    

  def test_neg(self):
    tst = -Dual(1, {'x1':1})
    assert tst.value==-1
    assert tst.partial('x1')==-1
    
    tst = -Dual(10, {'x1':1})
    assert tst.value==-10
    assert tst.partial('x1')==-1
    
  def test_zeroPowerZero(self):
    tst=Dual(0, {'x1':1})**0
    assert tst.value==1
    assert tst.partial('x1') == 0
    
  def test_createVariable(self):
    a = createVariable('x1',10)
    assert a.value == 10
    assert a.partial('x1') == 1
    
  def test_vectorize(self):
    a = createVariable('x1',10)
    b = createVariable('x2',10)
    f1 = a+b
    f2 = a+b
    variables,ders = vectorize_ders(np.array([f1,f2]))
    assert variables == ['x1','x2']
    assert ders[0][0] == 1
    assert ders[0][1] == 1
    assert ders[1][0] == 1
    assert ders[1][1] == 1
                         