#!/usr/bin/env python3

class VerboseList(list):
    """
    VerboseList class that extends the built-in list class
    and prints notifications when the list is modified.
    """

    def append(self, item):
        # First, call the original method to add the item to the list
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        # Calculate the number of items being added
        count = len(iterable)
        # Call the original extend method
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        # Print the message before removing the item
        print(f"Removed [{item}] from the list.")
        # Call the original remove method
        super().remove(item)

    def pop(self, index=-1):
        # Find the item to be popped before removing it
        item = self[index]
        print(f"Popped [{item}] from the list.")
        # Call the original pop method
        return super().pop(index)
