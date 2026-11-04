"""Interactive terminal demonstration; no third-party dependencies."""
from stack import Stack
from queue import Queue
from deque import Deque
from linked_list import LinkedList
from examples import run_examples


def sample_demo():
    """Show every required operation with reproducible sample data."""
    s = Stack()
    print('STACK empty:', s.isEmpty())
    for value in [10, 20, 30]:
        s.push(value)
    print('push 10,20,30:', s.display(), 'peek:', s.peek(), 'pop:', s.pop())
    q = Queue()
    print('QUEUE empty:', q.isEmpty())
    for value in ['A', 'B', 'C']:
        q.enqueue(value)
    print('enqueue A,B,C:', q.display(), 'front:', q.front(),
          'dequeue:', q.dequeue())
    d = Deque()
    print('DEQUE empty:', d.isEmpty())
    d.addRear(20)
    d.addFront(10)
    d.addRear(30)
    print('addFront/addRear:', d.display())
    print('removeFront:', d.removeFront(), 'removeRear:', d.removeRear())
    linked = LinkedList()
    for value in [10, 20, 30]:
        linked.insert(value)
    print('LINKED LIST insert 10,20,30:', linked.display())
    print('search 20:', linked.search(20), 'delete 20:', linked.delete(20),
          'display:', linked.display())


def playground():
    """Accept user-selected operations and string values."""
    choices = {'1': (Stack, ['push', 'pop', 'peek', 'isEmpty']),
               '2': (Queue, ['enqueue', 'dequeue', 'front', 'isEmpty']),
               '3': (Deque, ['addFront', 'addRear', 'removeFront',
                             'removeRear', 'isEmpty']),
               '4': (LinkedList, ['insert', 'delete', 'search', 'display'])}
    choice = input('1 Stack  2 Queue  3 Deque  4 LinkedList: ').strip()
    if choice not in choices:
        print('Invalid selection.')
        return
    cls, operations = choices[choice]
    structure = cls()
    while True:
        print('Operations:', ', '.join(operations), '| back')
        operation = input('Operation: ').strip()
        if operation == 'back':
            return
        if operation not in operations:
            print('Use an operation listed above.')
            continue
        try:
            method = getattr(structure, operation)
            if operation in ['push', 'enqueue', 'addFront', 'addRear',
                             'insert', 'delete', 'search']:
                result = method(input('Value: '))
            else:
                result = method()
            print('Result:', result, '| Current values:', structure.display())
        except IndexError:
            print('The structure is empty. Add a value first.')


def main():
    while True:
        choice = input('\n1 Sample operations  2 Problem examples  '
                       '3 Try your own values  0 Quit: ').strip()
        if choice == '0':
            return
        if choice == '1':
            sample_demo()
        elif choice == '2':
            run_examples()
        elif choice == '3':
            playground()
        else:
            print('Choose 0, 1, 2, or 3.')


if __name__ == '__main__':
    main()
