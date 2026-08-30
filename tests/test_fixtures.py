import pytest

@pytest.fixture
def setup_list():
    print('\nInside fixture')
    city=['New York', 'London', 'Bengaluru', 'Singapore', 'Paris']
    return city

def test_getitem(setup_list):
    print(f'\n{setup_list}')
    assert setup_list[0]=='New York'
    assert setup_list[::2] == ['New York', 'Bengaluru', 'Paris']

def myreverse(lst):
    lst.reverse()
    return lst

def test_reverselist(setup_list):
    print(f'\nIn reverse - {setup_list}')
    assert setup_list[::-2] == ['Paris', 'Bengaluru', 'New York']
    assert setup_list[::-1] == myreverse(setup_list)
