#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0]*list_length
    if list_length <= 0:
        print("out of range")
        return new_list

    for i in range(0, list_length):
        div = 0
        try:
            div = (my_list_1[i] / my_list_2[i])
        except TypeError:
            print("Wrong Type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list[i] = div
    return new_list
