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
