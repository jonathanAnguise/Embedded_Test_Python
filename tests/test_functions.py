import pytest
from main import find_first_repeated_number


@pytest.mark.parametrize("input_1, input_2, output",
                         [([1, 5, 2, 3, 4], [3, 8, 4], 3),
                          ([1, 2, 3], [-3, 14, 6, 10], "No data matching found")])
def test_find_first_repeated_number(input_1, input_2, output):
    assert find_first_repeated_number(input_1, input_2) == output
