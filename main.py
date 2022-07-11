from _ctypes import sizeof


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
