"""List-backed Deque; required course API names are preserved."""


class Deque:
    """Store values in a Python list; front is index zero."""

    def __init__(self, values=()):
        self._items = list(values)

    def addFront(self, value):
        """O(n)."""
        self._items.insert(0, value)

    def addRear(self, value):
        """Amortized O(1)."""
        self._items.append(value)

    def removeFront(self):
        """O(n); raises IndexError when empty."""
        return self._items.pop(0)

    def removeRear(self):
        """O(1); raises IndexError when empty."""
        return self._items.pop()

    def isEmpty(self):
        """Return whether the structure has no items, in O(1)."""
        return not self._items

    def __len__(self):
        return len(self._items)

    def display(self):
        """Return a shallow snapshot in O(n), without exposing storage."""
        return self._items.copy()
