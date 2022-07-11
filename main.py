import pathlib
from _ctypes import sizeof
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


def find_the_minimum_quantity_of_permutations(sequence):
    """
    The function finds the minimum quantity of permutations so that the sequence ends interspersed.
    :param sequence: a list of the sequence of tail or head using the format 0 for tail and 1 for head
    :return: the minimum quantity of permutation as int or if it's not possible a string error message "not possible"
    """
    nb_of_swat = 0
    # check if the sequence can be interspersed.
    if abs(sequence.count(0) - sequence.count(1)) != 0 and len(sequence) % 2 == 0:
        return "not possible"
    elif abs(sequence.count(0) - sequence.count(1)) != 1 and len(sequence) % 2 != 0:
        return "not possible"
    # Start reading the sequence
    for i in range(1, len(sequence)):  # Don't evaluate first element because it's not needed
        if sequence[i] == sequence[i-1]:
            nb_of_swat += 1
            # find the first element different and swap it
            for j in range(i+1, len(sequence)):
                if sequence[i] != sequence[j]:
                    temp = sequence[i]
                    sequence[i] = sequence[j]
                    sequence[j] = temp
                    break
                else:
                    continue
    return nb_of_swat


seq1 = [0,1,1,0,0,0,1]
seq2 = [0,1]
seq3 = [0,0,1]
seq4 = [0,0,1,1]
seq5 = [1,0,1,1]
seq6 = [1,0,0,1,1]
print(find_the_minimum_quantity_of_permutations(seq1))
print(find_the_minimum_quantity_of_permutations(seq2))
print(find_the_minimum_quantity_of_permutations(seq3))
print(find_the_minimum_quantity_of_permutations(seq4))
print(find_the_minimum_quantity_of_permutations(seq5))
print(find_the_minimum_quantity_of_permutations(seq6))

