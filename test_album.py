from album import album

def test_01():
    assert album(car=[4,7],com=[7,1,2,8,3]) == 1
def test_02():
    assert album(car=[4,7],com=[7,1,8,4,9,3]) == 0
def test_03():
    assert album(car=[2,4,6,8],com=[3,1,1,5,3,1,7,7,1,1]) == 4