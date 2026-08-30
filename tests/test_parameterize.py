import pytest

@pytest.mark.parametrize('test_input',[82, 78, 45, 62])
def test_param01(test_input):
    assert test_input >50