
def test_a1():
    assert 4>=3

def test_a2():
    assert 1

def test_a3():
    assert 'abcd' is 'abcd'

def test_a4():
    assert ((3-1)*4/2) == 4

def test_a5():
    assert ((3 - 1) * (4 / 2)) is 4

def test_a6():
    assert 1 in divmod(9, 5)
    assert 'py' in 'this is pytest'