import pytest


@pytest.mark.skip
def test_firstprogram():
    msg="hello"
    assert msg=="Hello"

def test_secondCreditcardprogram():
    a=4
    b=6
    assert a+2 ==6,"Addition did not match"
