def delete_at(my_list=[], idx=0):
    """Find all multiples of 2 in a list"""
    if not isinstance(idx, int):
        return my_list
    if idx < 0 or idx >= len(my_list):
        return my_list
    return my_list[:idx] + my_list[idx+1:]
