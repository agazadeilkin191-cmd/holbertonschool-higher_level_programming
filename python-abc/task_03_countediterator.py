#!/usr/bin/env python3

class CountedIterator:
    """
    A class that extends an iterator to track the number of items retrieved.
    """

    def __init__(self, some_iterable):
        # Initialize the iterator and a counter to track iterations
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        # Returns the current number of items iterated
        return self.counter

    def __next__(self):
        # Get the next item from the original iterator
        # This will raise StopIteration automatically if no items are left
        item = next(self.iterator)
        
        # Increment the counter only after successfully retrieving an item
        self.counter += 1
        return item

    def __iter__(self):
        # Return self to ensure this object behaves as an iterator
        return self
