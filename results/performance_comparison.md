# Performance comparison

Measured microseconds per operation; medians of seven batches of 100 calls.
Fixtures and method lookup are excluded. Loop/call overhead is included.
n is the initial size; successful mutations change size by up to 100.
Linked-list search/delete use an absent value and traverse the full list.
Failed delete measures traversal, not a successful unlink.
Append batches can include allocation; individual timings do not prove Big O.
Small differences may be noise. Results depend on hardware and Python.

| Structure | Operation | Expected cost | n=100 | n=1,000 | n=10,000 | n=50,000 |
|---|---|---|---:|---:|---:|---:|
| Stack | push | O(1) amortized | 0.043 | 0.046 | 0.071 | 0.090 |
| Stack | pop | O(1) | 0.048 | 0.047 | 0.053 | 0.066 |
| Stack | peek | O(1) | 0.041 | 0.042 | 0.044 | 0.061 |
| Stack | isEmpty | O(1) | 0.036 | 0.037 | 0.038 | 0.050 |
| Queue | enqueue | O(1) amortized | 0.045 | 0.045 | 0.069 | 0.062 |
| Queue | dequeue | O(n) | 0.059 | 0.106 | 1.841 | 11.141 |
| Queue | front | O(1) | 0.037 | 0.038 | 0.042 | 0.054 |
| Queue | isEmpty | O(1) | 0.037 | 0.038 | 0.044 | 0.055 |
| Deque | addFront | O(n) | 0.086 | 0.248 | 3.646 | 17.718 |
| Deque | addRear | O(1) amortized | 0.042 | 0.053 | 0.066 | 0.064 |
| Deque | removeFront | O(n) | 0.056 | 0.099 | 1.696 | 13.726 |
| Deque | removeRear | O(1) | 0.046 | 0.046 | 0.048 | 0.067 |
| Deque | isEmpty | O(1) | 0.038 | 0.036 | 0.037 | 0.054 |
| LinkedList | insert | O(1) | 0.150 | 0.166 | 0.183 | 0.205 |
| LinkedList | delete | O(n) absent | 4.718 | 48.884 | 543.722 | 2926.200 |
| LinkedList | search | O(n) absent | 3.400 | 52.699 | 515.272 | 2647.654 |
| LinkedList | display | O(n) | 5.248 | 98.263 | 588.094 | 2881.627 |

## Interpretation

Front insertion/removal in the list queue/deque shifts remaining references.
Linked-list absent search/delete and display grow with traversal length.
Stack end operations avoid shifting. A single append may resize the list:
its worst case is O(n), while its amortized cost is O(1).
All four structures require O(n) storage; linked nodes add reference/object overhead.
See environment.json for the measured environment and CSV for all ranges.