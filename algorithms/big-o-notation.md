# Big O

Big O Notation:
:   A mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity.

- It is used to describe the performance of an algorithm.
- It helps us determine if an algorithm is going to scale well.

Time Complexity:
:   Time complexity is a concept in computer science and algorithm analysis that quantifies the amount of time an algorithm takes to run as a function of the input size. It helps us understand and compare the efficiency of algorithms in terms of their execution time as the input size grows. Time complexity is typically expressed using big O notation, which provides an upper bound on the growth rate of the algorithm's runtime relative to the input size.

## Common notations used in time complexity analysis

### O(1) - Constant Time

An algorithm is said to have constant time complexity if its runtime does not depend on the input size. It means the algorithm takes a fixed amount of time to complete, regardless of how large the input is.

### O(log n) - Logarithmic Time

Algorithms with logarithmic time complexity have runtimes that grow slowly as the input size increases. Common examples include binary search and many efficient tree-based data structures and algorithms.

### O(n) - Linear Time

Linear time complexity means that the algorithm's runtime is directly proportional to the input size. As the input size grows, the runtime also increases linearly.

### O(n log n) - Linearithmic Time

Algorithms with linearithmic time complexity are more efficient than purely linear algorithms but are not as fast as logarithmic ones. Merge sort and quicksort are examples of algorithms with this time complexity.

### O(n^2) - Quadratic Time

Quadratic time complexity means that the runtime of the algorithm grows with the square of the input size. Algorithms that involve nested loops are often associated with this time complexity.

### O(n^k) - Polynomial Time

Algorithms with polynomial time complexity have runtimes that grow with the input size raised to a constant power 'k'. For example, cubic time (O(n^3)) or quadratic time (O(n^2)).

### O(2^n) - Exponential Time

Algorithms with exponential time complexity have runtimes that grow rapidly with the input size, making them impractical for large inputs. Many brute-force algorithms exhibit exponential time complexity.

### O(n!) - Factorial Time

Factorial time complexity is the worst-case scenario, where the runtime grows factorially with the input size. Permutations and some brute-force algorithms have this time complexity.


## Why do we use time complexity analysis?
Time complexity analysis helps us make informed decisions about which algorithm to use for a particular problem based on the expected input size and available computational resources. It's an essential concept for designing efficient algorithms and optimizing the performance of software systems.