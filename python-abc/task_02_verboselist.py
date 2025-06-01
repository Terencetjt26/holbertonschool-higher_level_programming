#!/usr/bin/env python3
"""VerboseList: Extension of Python list that logs actions."""

class VerboseList(list):
    """A subclass of list that prints notifications on actions."""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]  # Get item before popping
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
