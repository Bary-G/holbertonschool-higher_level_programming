#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Prints result of division of integers"""
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            if not isinstance(my_list_1[i], (int, float)):
                raise TypeError("wrong type")
            elif not isinstance(my_list_2[i], (int, float)):
                raise TypeError("wrong type")
            if my_list_2[i] == 0:
                raise ZeroDivisionError("division by 0")
            result.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        finally:
            pass
    return result
