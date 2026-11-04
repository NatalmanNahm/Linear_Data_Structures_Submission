# Linear Data Structures Submission

Python 3.10 or later. The runnable suite uses only the standard library.
No installation or pip commands are needed. The Word analysis is for reading.

## Run on macOS or Windows

Extract this ZIP, open Terminal in the extracted folder, then run:

```bash
python3 demo.py
python3 -m unittest -v
python3 examples.py
python3 benchmark.py
```

On Windows, use `py` instead of `python3` if needed.
On macOS, type `cd ` then drag the extracted folder into Terminal and press Enter.
The demo menu offers sample operations, problem examples, and your own values.
Choose 0 to quit; use `back` to leave the operation playground.
Values entered in the playground are strings. Required camelCase methods are
retained exactly as assigned; other function names follow Python conventions.

## Deliverable map

- stack.py: Stack with push, pop, peek, isEmpty.
- queue.py: Queue with enqueue, dequeue, front, isEmpty.
- deque.py: Deque with addFront, addRear, removeFront, removeRear, isEmpty.
- linked_list.py: LinkedList with insert, delete, search, display.
- demo.py: sample operations and interactive user input.
- test_structures.py: seven automated test methods with multiple assertions.
- examples.py: bracket matching, request processing, palindrome checking, tasks.
- Linear_Data_Structures_Analysis.docx: two-page comparison and use cases.
- benchmark.py: reproducible operation timing and comparison report generation.
- results/performance_results.csv: 68 operation/size combinations.
- results/performance_comparison.md: readable timing table and methodology.
- results/environment.json: execution environment and timing settings.

## Behavior and assumptions

Front is list index 0; stack top and deque rear are the last index.
Empty pop/peek/dequeue/front/removal raises IndexError; the UI handles it.
LinkedList.insert prepends, so insertion order is reversed in display.
LinkedList.delete removes the first match and returns True, or False if absent.
search returns a Boolean. display returns a list snapshot rather than printing;
the demo prints it. Duplicates and None are supported. No thread safety is claimed.
Queue dequeue and deque front operations shift list references and cost O(n).
A list-backed deque must not be confused with Python's collections.deque.
Benchmark results were actually measured in the recorded environment.
Rerunning replaces the three generated results files with your own timings.
