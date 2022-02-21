def shift_left(general_list: list):
    """
    :param general_list: a list of objects - LEN = 3
    :return: shifts all cells 1 to the left
    """
    new_list = [general_list[1], general_list[2], general_list[0]]
    return new_list


print(shift_left([1, 2, 3]))
