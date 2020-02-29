from piso import pisoC,pisoL

def test_piso_01():
    assert pisoL(3,5) == 23
def test_piso_02():
    assert pisoC(3,5) == 12
def test_piso_03():
    assert pisoL(1,1) == 1
def test_piso_04():
    assert pisoC(1,1) == 0
