#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    A function that divides element by element 2 lists.
    """
    result = []
    index = 0
    for index in range(list_length):
        try:
            if not isinstance(my_list_1[index], (int, float)):
                raise TypeError
            elif not isinstance(my_list_2[index], (int, float)):
                raise TypeError
            value = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
            value = 0
        except ZeroDivisionError:
            print("division by 0")
            value = 0
        except IndexError:
            print("out of range")
            value = 0
        finally:
            result.append(value)
    return result
