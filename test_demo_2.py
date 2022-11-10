import pytest

def test_m4():
    assert False

def test_m5():
    assert 100 == 100

@pytest.mark.login
def test_m6():
    assert "naveen" == "NAVEEN"

@pytest.mark.login
def test_loginGMAIL():
    assert "admin"=="admin"

