"""Measure public operations; fixture construction is outside timing."""
import csv
import json
import platform
import statistics
import time
from pathlib import Path
from stack import Stack
from queue import Queue
from deque import Deque
from linked_list import LinkedList

SIZES = (100, 1000, 10000, 50000)
REPEATS = 7
BATCH = 100


def make_linked(n):
    linked = LinkedList()
    for value in range(n):
        linked.insert(value)
    return linked


def main():
    rows = []
    cases = [
        ('Stack', Stack, 'push', lambda n: -1, 'O(1) amortized'),
        ('Stack', Stack, 'pop', None, 'O(1)'),
        ('Stack', Stack, 'peek', None, 'O(1)'),
        ('Stack', Stack, 'isEmpty', None, 'O(1)'),
        ('Queue', Queue, 'enqueue', lambda n: -1, 'O(1) amortized'),
        ('Queue', Queue, 'dequeue', None, 'O(n)'),
        ('Queue', Queue, 'front', None, 'O(1)'),
        ('Queue', Queue, 'isEmpty', None, 'O(1)'),
        ('Deque', Deque, 'addFront', lambda n: -1, 'O(n)'),
        ('Deque', Deque, 'addRear', lambda n: -1, 'O(1) amortized'),
        ('Deque', Deque, 'removeFront', None, 'O(n)'),
        ('Deque', Deque, 'removeRear', None, 'O(1)'),
        ('Deque', Deque, 'isEmpty', None, 'O(1)'),
        ('LinkedList', make_linked, 'insert', lambda n: -1, 'O(1)'),
        ('LinkedList', make_linked, 'delete', lambda n: -1, 'O(n) absent'),
        ('LinkedList', make_linked, 'search', lambda n: -1, 'O(n) absent'),
        ('LinkedList', make_linked, 'display', None, 'O(n)'),
    ]
    for name, factory, operation, arg, complexity in cases:
        for n in SIZES:
            samples = []
            # Untimed warm-up with a separate fixture.
            warm = factory(n) if name == 'LinkedList' else factory(range(n))
            method = getattr(warm, operation)
            method() if arg is None else method(arg(n))
            for _ in range(REPEATS):
                obj = factory(n) if name == 'LinkedList' else factory(range(n))
                method = getattr(obj, operation)
                value = None if arg is None else arg(n)
                start = time.perf_counter_ns()
                for _ in range(BATCH):
                    method() if arg is None else method(value)
                samples.append((time.perf_counter_ns() - start) / BATCH / 1000)
            rows.append([name, operation, n, complexity,
                         round(statistics.median(samples), 6),
                         round(min(samples), 6), round(max(samples), 6)])
    out = Path(__file__).parent / 'results'
    out.mkdir(exist_ok=True)
    with (out / 'performance_results.csv').open('w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['structure', 'operation', 'initial_n', 'expected_cost',
                         'median_us', 'min_us', 'max_us'])
        writer.writerows(rows)
    metadata = {'python': platform.python_version(), 'platform': platform.platform(),
                'processor': platform.processor(), 'sizes': SIZES,
                'repeats': REPEATS, 'operations_per_sample': BATCH,
                'clock': 'perf_counter_ns', 'timestamp_utc':
                time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    (out / 'environment.json').write_text(json.dumps(metadata, indent=2))
    lines = ['# Performance comparison', '',
             'Measured microseconds per operation; medians of seven batches of 100 calls.',
             'Fixtures and method lookup are excluded. Loop/call overhead is included.',
             'n is the initial size; successful mutations change size by up to 100.',
             'Linked-list search/delete use an absent value and traverse the full list.',
             'Failed delete measures traversal, not a successful unlink.',
             'Append batches can include allocation; individual timings do not prove Big O.',
             'Small differences may be noise. Results depend on hardware and Python.', '',
             '| Structure | Operation | Expected cost | n=100 | n=1,000 | n=10,000 | n=50,000 |',
             '|---|---|---|---:|---:|---:|---:|']
    for i in range(0, len(rows), len(SIZES)):
        group = rows[i:i+len(SIZES)]
        lines.append('| ' + ' | '.join([group[0][0], group[0][1], group[0][3]] +
                     [f'{r[4]:.3f}' for r in group]) + ' |')
    lines += ['', '## Interpretation', '',
              'Front insertion/removal in the list queue/deque shifts remaining references.',
              'Linked-list absent search/delete and display grow with traversal length.',
              'Stack end operations avoid shifting. A single append may resize the list:',
              'its worst case is O(n), while its amortized cost is O(1).',
              'All four structures require O(n) storage; linked nodes add reference/object overhead.',
              'See environment.json for the measured environment and CSV for all ranges.']
    (out / 'performance_comparison.md').write_text('\n'.join(lines))
    print('Saved 68 measured operation/size combinations to', out)


if __name__ == '__main__':
    main()
