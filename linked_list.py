"""Singly linked list with constant-time insertion at the head."""
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    """A value and a reference to its successor."""
    value: Any
    next: Optional["Node"] = None


class LinkedList:
    """Insert at head; delete first match; search returns a Boolean."""

    def __init__(self):
        self.head = None
        self._size = 0

    def insert(self, value):
        """Prepend value in O(1). Duplicates are allowed."""
        self.head = Node(value, self.head)
        self._size += 1

    def delete(self, value):
        """Delete first matching value; return success. Worst-case O(n)."""
        previous, current = None, self.head
        while current is not None:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self._size -= 1
                return True
            previous, current = current, current.next
        return False

    def search(self, value):
        """Return whether value exists. Worst-case O(n)."""
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def display(self):
        """Return values from head to tail as a list in O(n)."""
        result, current = [], self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def __len__(self):
        return self._size
