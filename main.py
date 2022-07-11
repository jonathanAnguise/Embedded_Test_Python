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
