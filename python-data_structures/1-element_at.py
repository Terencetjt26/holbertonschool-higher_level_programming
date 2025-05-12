#!/usr/bin/python3
# 0-main.py
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)


# 1-element_at.py
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]


# 1-main.py
if __name__ == "__main__":
    element_at = __import__('1-element_at').element_at

    my_list = [1, 2, 3, 4, 5]
    idx = 3
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
