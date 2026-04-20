#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        div = 0
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                div = 0
            elif not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                print("wrong type")
                div = 0
            else:
                div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        finally:
            new_list.append(div)
    return new_list
