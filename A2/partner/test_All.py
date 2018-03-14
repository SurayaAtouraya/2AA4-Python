from SeqServices import *
from Exceptions import *
from CurveADT import *
from Data import *
import pytest

#Testing SeqServices.py

def test_isAscending():
    
    x = [0,1]
    assert isAscending(x) == True
    x = [1,0]
    assert isAscending(x) == False
    x = [1,1]
    assert isAscending(x) == True

def test_isInBounds():
    
    X = [0,1,2,3]
    assert isInBounds(X, 0) == True
    assert isInBounds(X, 3) == True
    assert isInBounds(X, 4) == False
    assert isInBounds(X, -1) == False

def test_interpLin():
    
    assert interpLin(0,0,2,2,1) == 1

def test_interpQuad():
    
    assert interpQuad(2,4,3,9,5,25,4) >= 16*0.8 or interpQuad(2,4,3,9,5,25,4) <= 16*1.2
    
def test_index():
    
    X = [0,1,4,6,10,11]
    assert index(X,0) == 0
    assert index(X,3) == 1
    assert index(X,11) == 5
    assert index(X,100) == None

#Testing CurveADT.py

def test_CurveADT_init():
    
    with pytest.raises(IndepVarNotAscending):
        CurveT([1,0],[0,1],1)
        
    with pytest.raises(SeqSizeMismatch):
        CurveT([0],[0,1],1)
        
    with pytest.raises(InvalidInterpOrder):
        CurveT([0,1],[0,1],0)
        
    test = CurveT([0,1,2,3],[0,1,4,9],2)

def test_minD():

    test = CurveT([0,1,2,3],[0,1,4,9],2)
    assert test.minD() == 0

def test_maxD():

    test = CurveT([0,1,2,3],[0,1,4,9],2)
    assert test.maxD() == 3

def test_order():

    test = CurveT([0,1,2,3],[0,1,4,9],2)
    assert test.order() == 2

def test_eval_CurveT():

    test = CurveT([0,1,2,3],[0,1,4,9],2)
    with pytest.raises(OutOfDomain):
        test.eval(100)
        
    a = int(((test.eval(1)).take(0)).round())
    assert a == 1
    
    a = int(((test.eval(3)).take(0)).round())
    assert a == 9
    
    a = ((test.eval(2.5)).take(0))
    a = round(a,2)
    assert a == 6.25

def test_dfdx():

    test = CurveT([0,1,2,3],[0,1,4,9],2)
    with pytest.raises(OutOfDomain):
        test.dfdx(4)
        assert int(round(test.dfdx(2))) == 4
        
def test_d2fdx2():

    test = CurveT([0,1,2,3],[0,1,4,9],2)
    with pytest.raises(OutOfDomain):
        test.d2fdx2(4)
        assert int(round(test.d2fdx2(2))) == 2

#Testing Data.py

def test_init():

    Data.init()
    assert Data.S == []
    assert Data.Z == []

def test_add():

    Data.init()
    z = 1
    s = [0]
    Data.add(s,z)
    z = 0
    with pytest.raises(IndepVarNotAscending):
        Data.add(s,z)
    z = 2
    Data.add(s,z)
    z = 3
    Data.add(s,z)
    z = 4
    Data.add(s,z)
    z = 5
    Data.add(s,z)
    z = 6
    Data.add(s,z)
    z = 7
    Data.add(s,z)
    z = 8
    Data.add(s,z)
    z = 9
    Data.add(s,z)
    z = 10
    Data.add(s,z)
    z = 11
    with pytest.raises(Full):
        Data.add(s,z)

def test_getC():

    Data.init()
    with pytest.raises(InvalidIndex):
        Data.getC(1)
    test = CurveT([0,1],[1,2],1)
    Data.add(test,1)
    test2 = Data.getC(0)
    assert test == test2

def test_eval_Data():

    Data.init()
    c1 = CurveT([1,2,3],[1,2,3],1)
    c2 = CurveT([1,2,3],[1,4,9],2)
    Data.add(c2,124)
    Data.add(c1,217)
    assert round(Data.eval(2,130),3) == -0.129
    with pytest.raises(OutOfDomain):
        Data.eval(1000,1000)

def test_slice():

    Data.init()
    c1 = CurveT([1,2,3],[1,2,3],1)
    c2 = CurveT([1,2,3],[1,4,9],2)
    Data.add(c1,10)
    Data.add(c2,20)
    assert int(round(Data.slice(2,1).eval(15).take(0))) == 3
    
