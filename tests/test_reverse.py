import pytest
import math

from src.Reverse import Variable, Constant, Node
from src.Reverse_deriv import *


class TestFunctions:


    def test_dualval(self):
        a = Variable('x1',2)
        b = Variable('x2',3)
        assert a.value == 2
        assert b.value == 3


    def test_partial(self):
        a = Variable('x1',2)
        b = Variable('x2',3)
        c1 = Constant(10)
        assert a.partial(a) == 1
        assert a.partial(b) == 0
        assert c1.partial(a) == 0
        
        c = a*b
        
        assert c.partial(a)==3
        assert c.partial(b)==2
        d = a-b
        assert d.partial(a)==a.partial(a)
        assert d.partial(b)==-b.partial(b)


    def test_getvalue(self): 
        a = Variable('x1',2)
        assert a.getvalue()==2

        b = Variable('x2',3)
        c = a*b
        assert c.getvalue() == 6

        d = a-b
        assert d.getvalue() == -1

    def test_str(self):
        a = Variable('x1',2)
        assert a.__str__() == 'x1=2'
        b = Variable('x2',3)
        c = a+b 
        assert c.__str__() == ' - +\n  - x1=2\n  - x2=3\n'
        
        d = Constant(4)
        assert d.__str__() == 'Constant=4'

    def test_repr(self):
        a = Variable('x1',2)
        assert type(eval(a.__repr__())) == Variable
        assert isinstance(eval(a.__repr__()), Variable)
        
        t = a+Constant(2)
        print(t.__repr__())
        assert t.__repr__()=='Node(Variable("x1", 2), Constant(2), 4, "+")'
        assert type(eval(t.__repr__())) == Node
        assert isinstance(eval(t.__repr__()), Node)

    def test_add(self): 
        
        a = Variable('x1',2)
        b = Variable('x2',3)
        testsum=a+b

        assert testsum.value==5
        assert testsum.partial(a)==1

        a = Variable('x1',2)
        b = Constant(10)
        testsum=a+b

        assert testsum.value==12
        assert testsum.partial(a)==1


    def test_radd(self):
        a = Variable('x1',2)
        c1 = Constant(3)
        testsum=c1+a

        assert testsum.value==5
        assert testsum.partial(a)==1

        a = Variable('x1',2.5)
        c2 = Constant(-13.2)
        testsum=c2+a

        assert testsum.value==-10.7
        assert testsum.partial(a)==1

    def test_mul(self):
        a = Variable('x1',2)
        b = Variable('x2',3)
        testmul=a*b

        assert testmul.value==6
        assert testmul.partial(a)==3
        
        c1 = Constant(3)
        testmul=b*c1
        assert testmul.value==9
        assert testmul.partial(b)==3

        d = Variable('x3',-3)
        testmul=a*d*Constant(2)
        assert testmul.value==-6*2
        assert testmul.partial(a)==-3*2
        assert testmul.partial(d)==4

    def test_rmul(self):
        a = Variable('x1',2)
        testmul=Constant(2.5)*a

        assert testmul.value==5
        assert testmul.partial(a)==2.5

        testmul=Constant(-2.5)*a

        assert testmul.value==-5
        assert testmul.partial(a)==-2.5


    def test_sub(self):
        a = Variable('x1',2)
        testsub=a-a
        assert testsub.value==0
        assert testsub.partial(a)==0
        b = Variable('x2',10)
        testsub=a-b
        assert testsub.value==-8
        assert testsub.partial(a)==1
        assert testsub.partial(b)==-1

        testsub=a-Constant(10)
        assert testsub.value==-8
        assert testsub.partial(a) == 1

    def test_rsub(self):
        a = Variable('x1',2)
        testsub=Constant(1)-a
        assert testsub.value==-1
        assert testsub.partial(a) == -1


    def test_truediv(self):
        a = Variable('x1',2)
        b = Variable('x2',3)
#         test_div=a/b

#         assert test_div.value==2/3
#         assert test_div.ders=={'x1':(3*1-2*2)/3**2}

#         c = Variable('x3',-2)
#         test_div=a/c

#         assert test_div.value==-1
#         assert test_div.partial(a)=='x1':1/3, 'x2':-4/9}

        test_div=a/Constant(-4)
        assert test_div.value==-2/4
        assert test_div.partial(a)==-1/4

    def test_rtruediv(self):
        a = Variable('x1',2)
        test_div=Constant(2)/a

        assert test_div.value==1
        assert test_div.partial(a)==-2*1/2**2

    def test_pow(self):
        a = Variable('x1',2)
        testexp=a**Constant(2)
        testcub=a**Constant(3)

        assert testexp.value ==4
        assert testcub.value==8
        assert testexp.partial(a)==4
        assert testcub.partial(a)==3*2**2

        t = a**Constant(1)
        assert t.value == 2
        assert t.partial(a)==1

        t = a**Constant(0)
        assert t.value ==1
        assert t.partial(a)==0

        t = a**Constant(0.5)
        assert t.value == math.sqrt(2)
        assert t.partial(a)==0.5*(2**(-0.5))

        t = a**Constant(-1)
        assert t.value == 1/2
        assert t.partial(a)==(-1)*(2**(-2))


    def test_neg(self):
        a = Variable('x1',1)
        tst = -a
        assert tst.value==-1
        assert tst.partial(a)==-1
        
        b = Variable('x2',10)
        tst = -b
        assert tst.value==-10
        assert tst.partial(b)==-1

    def test_zeroPowerZero(self):
        a=Variable('x1',0)
        tst=a**Constant(0)
        assert tst.value==1
        assert tst.partial(a) == 0
        
    def test_integral(self):
        a = Variable('x1',1)
        b = Variable('x2',10)
        t = a+b
        t1 = a*b
        t2 = t+t1
        assert t2.partial(a) == 11
        assert t2.value == 11+10
        assert t2._getvariable() =={a,b}
       