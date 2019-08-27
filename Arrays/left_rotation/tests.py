from .main import get_left_rotated_array

def test_1():
    d = 4
    array = "1 2 3 4 5".split()
    assert ' '.join(get_left_rotated_array(d, array)) == "5 1 2 3 4"