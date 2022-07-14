import pathlib
from unittest.mock import patch

import pytest

import main as script

MAX_SIZE = 14 * 2 ** 20
NO_EXECUTION_CODE = 33204
EXECUTION_USER_CODE = 33268


class Stat:
    def __init__(self, size, mode):
        self.st_size = size
        self.st_mode = mode


class TestResource:
    # Function 1
    @pytest.mark.parametrize("input_1, input_2, output",
                             [([8, 5, 2, 3, 4], [3, 8, 4], 3),
                              ([3, 8, 4], [8, 5, 2, 3, 4], 3),
                              ([], [], "No data matching found"),
                              ([1, 2, 3], [-3, 14, 6, 10], "No data matching found")])
    def test_find_first_repeated_number(self, input_1, input_2, output):
        assert script.find_first_repeated_number(input_1, input_2) == output

    # Function 2
    def test_find_the_first_file_owner_admin_executable_lower_than_14_MB_path_not_valid(self):
        with patch.object(pathlib.Path, 'exists') as mock_exists:
            mock_exists.return_value = False
            assert script.find_the_first_file_owner_admin_executable_lower_than_14_MB('.') == "Path not valid"

    def test_find_the_first_file_owner_admin_executable_lower_than_14_MB_valid(self):
        with patch.object(pathlib.Path, 'owner') as mock_owner:
            with patch.object(pathlib.Path, 'stat') as mock_size:
                with patch.object(pathlib.Path, 'is_dir') as mock_dir:
                    mock_size.return_value = Stat(size=MAX_SIZE, mode=EXECUTION_USER_CODE)
                    mock_dir.return_value = False
                    mock_owner.return_value = "admin"
                    assert script.find_the_first_file_owner_admin_executable_lower_than_14_MB(".") == "tests"

    def test_find_the_first_file_owner_admin_executable_lower_than_14_MB_size_upp(self):
        with patch.object(pathlib.Path, 'owner') as mock_owner:
            with patch.object(pathlib.Path, 'stat') as mock_size:
                mock_size.return_value = Stat(size=MAX_SIZE + 1, mode=EXECUTION_USER_CODE)
                mock_owner.return_value = "admin"
                assert script.find_the_first_file_owner_admin_executable_lower_than_14_MB(
                    ".") == "No file matching found"

    def test_find_the_first_file_owner_admin_executable_lower_than_14_MB_owner_not_admin(self):
        with patch.object(pathlib.Path, 'owner') as mock_owner:
            with patch.object(pathlib.Path, 'stat') as mock_size:
                mock_size.return_value = Stat(size=MAX_SIZE, mode=EXECUTION_USER_CODE)
                mock_owner.return_value = "not admin"
                assert script.find_the_first_file_owner_admin_executable_lower_than_14_MB(
                    ".") == "No file matching found"

    def test_find_the_first_file_owner_admin_executable_lower_than_14_MB_only_directories(self):
        with patch.object(pathlib.Path, 'owner') as mock_owner:
            with patch.object(pathlib.Path, 'stat') as mock_size:
                with patch.object(pathlib.Path, 'is_dir') as mock_dir:
                    mock_dir.return_value = True
                    mock_owner.return_value = True
                    mock_size.return_value = Stat(size=MAX_SIZE, mode=EXECUTION_USER_CODE)
                    mock_owner.return_value = "admin"
                    assert script.find_the_first_file_owner_admin_executable_lower_than_14_MB(
                        ".") == "No file matching found"

    # Function 3
    @pytest.mark.parametrize("input_1, output", [
        ([0, 1, 1, 0, 0, 0, 1], 2),
        ([0, 1], 0),
        ([0, 0, 1], 1),
        ([0, 0, 1, 1], 1),
        ([1, 0, 1, 1], "not possible"),
        ([1, 0, 0, 1, 1], 1),
        ([], "not valid"),
        ([1, "1", 0], "not valid"),
        ([1], 0),
    ])
    def test_find_the_minimum_quantity_of_permutations(self, input_1, output):
        assert script.find_the_minimum_quantity_of_permutations(input_1) == output
