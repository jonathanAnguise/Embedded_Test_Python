from _ctypes import sizeof
import pathlib
from stat import S_IXUSR


def find_first_repeated_number(input1, input2):
    """
    Function will compare 2 vectors and return the first repeated number from the point of view of the smaller vector
    :param input1: vector #1 list
    :param input2: vector #2 list
    :return: first repeated number | string "No data matching found" in case there is no matching data
    """

    # find the smaller vector
    if len(input1) <= len(input2):
        vector1 = input1
        vector2 = input2
    else:
        vector2 = input1
        vector1 = input2

    for i in vector1:
        if i in vector2:
            return i
        else:
            continue
    return "No data matching found"


def find_the_first_file_owner_admin_executable_lower_than_14_MB(user_path):
    """
    The function will find the first file matching these requirements:
       * size < 14MB
       * owner can execute it
       * owner name is "admin"
    :param user_path:path of the directory to scan
    :return: absolute path string of the file or error message string
    """
    path = pathlib.Path(user_path)
    max_size = 14*2**20 #14MB

    if path.exists() == False:
        return "Path not valid"
    for file in path.iterdir():
        # Don't check for directory
        if file.is_dir():
            continue
        # S_IXUSR is a the mask to apply of mode result to know if Owner has execute permission.
        if file.owner() == "admin" and file.stat().st_size <= max_size and file.stat().st_mode & S_IXUSR != 0:
                return file.name
    return "No file matching found"

