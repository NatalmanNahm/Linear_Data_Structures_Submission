"""Problem-solving algorithms built on the four custom structures."""
from stack import Stack
from queue import Queue
from deque import Deque
from linked_list import LinkedList


def balanced_brackets(text):
    """Check nested brackets with a stack; O(m) time and O(m) space.

    Non-bracket characters are ignored; this is not a source-code parser.
    """
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in text:
        if char in '([{':
            stack.push(char)
        elif char in pairs:
            if stack.isEmpty() or stack.pop() != pairs[char]:
                return False
    return stack.isEmpty()


def process_requests(requests):
    """Serve requests in arrival order; O(m²) time with this list queue."""
    queue = Queue(requests)
    served = []
    while not queue.isEmpty():
        served.append(queue.dequeue())
    return served


def is_palindrome(text):
    """Compare opposite ends after normalization; O(m²) for this deque.

    Ignore punctuation, spacing and case. Extra space is O(m).
    """
    deque = Deque(c for c in text.casefold() if c.isalnum())
    while len(deque) > 1:
        if deque.removeFront() != deque.removeRear():
            return False
    return True


def manage_tasks(tasks, completed):
    """Prepend tasks, then remove completed values; O(m + k*m) worst case.

    Most recently added task appears first; delete removes one match.
    """
    linked = LinkedList()
    for task in tasks:
        linked.insert(task)
    for task in completed:
        linked.delete(task)
    return linked.display()


def run_examples():
    print('Stack: balanced expression ([a + b] * {c}) ->',
          balanced_brackets('([a + b] * {c})'))
    print('Queue: requests served ->', process_requests(['R1', 'R2', 'R3']))
    print('Deque: A man, a plan, a canal: Panama ->',
          is_palindrome('A man, a plan, a canal: Panama'))
    print('Linked list: add Draft, Review, Submit; complete Review ->',
          manage_tasks(['Draft', 'Review', 'Submit'], ['Review']))


if __name__ == '__main__':
    run_examples()
