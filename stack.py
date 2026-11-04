"""List-backed Stack; required course API names are preserved."""


class Stack:
    """Store values in a Python list; front is index zero."""

    def __init__(self, values=()):
        self._items = list(values)

    def push(self, value):
        """Amortized O(1)."""
        self._items.append(value)

    def pop(self):
        """O(1); raises IndexError when empty."""
        return self._items.pop()

    def peek(self):
        """O(1); raises IndexError when empty."""
        return self._items[-1]

    def isEmpty(self):
        """Return whether the structure has no items, in O(1)."""
        return not self._items

    def __len__(self):
        return len(self._items)

    def display(self):
        """Return a shallow snapshot in O(n), without exposing storage."""
        return self._items.copy()
