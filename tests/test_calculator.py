import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from calculator import add

def test_add_normal():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0

def test_add_type_error():
    try:
        add("a", 1)
    except TypeError:
        assert True
    else:
        assert False

def test_subtract_normal():
    assert subtract(5, 3) == 2

def test_subtract_boundary():
    assert subtract(0, 0) == 0
    assert subtract(-1e9, 1e9) == -2e9

def test_subtract_type_error():
    import pytest
    with pytest.raises(TypeError):
        subtract("a", 1)

