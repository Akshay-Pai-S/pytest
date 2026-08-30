import pytest

pytestmark = [pytest.mark.smoke, pytest.mark.strtest]

@pytest.mark.sanity
def test_str1():
    num = 9/4
    s1 = 'hi' + ' wellcome'
    print(s1)
    assert str(num) == '2.25'
    assert s1 == 'hi wellcome'
    assert s1 + str(num)== 'hi wellcome2.25'

@pytest.mark.sanity
def test_str2():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert len(letters) == 26

def test_str3():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[0] == 'a'
    assert letters[-1] == 'z' == letters[25]

@pytest.mark.sanity
@pytest.mark.str
def test_strslice():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[:] == letters
    assert letters[10:] == 'klmnopqrstuvwxyz'
    assert letters[-3:] == 'xyz'
    assert letters[:21:5] == 'afkpu'

def test_str4():
    print('test_str4')
    assert str(10) == '10'