"""Correctness tests: ordering, empty cases, duplicates, and algorithms."""
import unittest
from stack import Stack
from queue import Queue
from deque import Deque
from linked_list import LinkedList
from examples import balanced_brackets, process_requests, is_palindrome, manage_tasks


class StructureTests(unittest.TestCase):
    def test_stack(self):
        s = Stack()
        self.assertTrue(s.isEmpty())
        for method in [s.pop, s.peek]:
            with self.assertRaises(IndexError):
                method()
        for v in [1, 2, 2]:
            s.push(v)
        self.assertEqual(s.peek(), 2)
        self.assertEqual([s.pop(), s.pop(), s.pop()], [2, 2, 1])
        self.assertTrue(s.isEmpty())

    def test_queue(self):
        q = Queue()
        self.assertTrue(q.isEmpty())
        for method in [q.dequeue, q.front]:
            with self.assertRaises(IndexError):
                method()
        for v in [1, 2, 2]:
            q.enqueue(v)
        self.assertEqual(q.front(), 1)
        self.assertEqual([q.dequeue(), q.dequeue(), q.dequeue()], [1, 2, 2])
        self.assertTrue(q.isEmpty())

    def test_deque(self):
        d = Deque()
        self.assertTrue(d.isEmpty())
        for method in [d.removeFront, d.removeRear]:
            with self.assertRaises(IndexError):
                method()
        d.addRear(2)
        d.addFront(1)
        d.addRear(3)
        self.assertEqual(d.display(), [1, 2, 3])
        self.assertEqual(d.removeFront(), 1)
        self.assertEqual(d.removeRear(), 3)
        self.assertEqual(d.removeRear(), 2)
        self.assertTrue(d.isEmpty())

    def test_linked_deletions(self):
        linked = LinkedList()
        self.assertEqual(linked.display(), [])
        self.assertFalse(linked.search(7))
        self.assertFalse(linked.delete(7))
        for v in [1, 2, 3, 4]:
            linked.insert(v)
        self.assertEqual(linked.display(), [4, 3, 2, 1])
        self.assertTrue(linked.search(2))
        for v in [4, 2, 1, 3]:
            self.assertTrue(linked.delete(v))
        self.assertEqual(len(linked), 0)
        self.assertEqual(linked.display(), [])

    def test_duplicates_and_none(self):
        linked = LinkedList()
        for v in [None, 5, 5]:
            linked.insert(v)
        self.assertTrue(linked.delete(5))
        self.assertEqual(linked.display(), [5, None])
        self.assertTrue(linked.search(None))

    def test_snapshots(self):
        for cls in [Stack, Queue, Deque]:
            structure = cls([1, 2])
            snapshot = structure.display()
            snapshot.clear()
            self.assertEqual(structure.display(), [1, 2])

    def test_problem_algorithms(self):
        for text in ['', 'abc', '([]{})']:
            self.assertTrue(balanced_brackets(text))
        for text in ['([)]', '(', ']']:
            self.assertFalse(balanced_brackets(text))
        self.assertEqual(process_requests(['A', 'B', 'C']), ['A', 'B', 'C'])
        self.assertEqual(process_requests([]), [])
        for text in ['', 'x', 'A man, a plan, a canal: Panama']:
            self.assertTrue(is_palindrome(text))
        self.assertFalse(is_palindrome('algorithm'))
        self.assertEqual(manage_tasks(['A', 'B', 'C'], ['B']), ['C', 'A'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
