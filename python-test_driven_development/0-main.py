#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))        # 3
print(add_integer(100, -2))     # 98
print(add_integer(2))           # 100 (2 + default 98)
print(add_integer(100.3, -2))   # 98 (int cast)
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)                   # b must be an integer
try:
    print(add_integer(None))
except Exception as e:
    print(e)                   # a must be an integer
