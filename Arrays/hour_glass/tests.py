from .main import get_max_hourglass_sum

def get_list_from_str(string):
    return list(map(int, string.strip().split()))

def test_1():
    sample_input = [
        get_list_from_str("1 1 1 0 0 0"),
        get_list_from_str("0 1 0 0 0 0"),
        get_list_from_str("1 1 1 0 0 0"),
        get_list_from_str("0 0 2 4 4 0"),
        get_list_from_str("0 0 0 2 0 0"),
        get_list_from_str("0 0 1 2 4 0")
    ]
    assert get_max_hourglass_sum(6, 3, sample_input) == 19
