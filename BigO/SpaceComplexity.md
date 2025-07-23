# Which Code is Best?

The best code is the one that balances the **3 pillars of programming**:
1. **Readable**: Easy to understand and maintain.
2. **Memory (Space Complexity)**: Efficient use of system memory.
3. **Speed (Time Complexity)**: Fast execution time.

Most code solutions involve a **trade-off between speed and memory**. For example, increasing speed often requires sacrificing memory, and vice versa. Let’s explore these pillars in detail.

---

## 1. **Readable Code**
Readable code is easy to understand, follow, and maintain. It uses meaningful variable names, proper indentation, and comments where necessary.

### Example:
```javascript
// Bad: Unreadable code
function x(a) {
    let b = 0;
    for (let i = 0; i < a.length; i++) b += a[i];
    return b;
}

// Good: Readable code
function calculateSum(numbers) {
    let sum = 0;
    for (let i = 0; i < numbers.length; i++) {
        sum += numbers[i];
    }
    return sum;
}
```
- **Why it’s better**: The second function uses descriptive names (`calculateSum`, `numbers`, `sum`) and proper formatting, making it easier to understand.

---

## 2. **Memory (Space Complexity)**
Space Complexity refers to the amount of memory a program uses during execution. Programs use two main memory spaces:
- **Heap**: Stores variables and data structures.
- **Stack**: Keeps track of function calls.

### What Causes Space Complexity?
- **Variables**: Storing values in memory.
- **Data Structures**: Arrays, objects, and other structures consume memory.
- **Function Calls**: Each function call adds a new frame to the stack.
- **Allocations**: Dynamic memory allocation (e.g., `new Array(100)`).

### Example:
```javascript
// High Space Complexity: Creates a new array of size `n`
function createLargeArray(n) {
    const arr = new Array(n); // Allocates memory for `n` elements
    return arr;
}

// Low Space Complexity: Uses a single variable
function calculateSum(numbers) {
    let sum = 0; // Only one variable is stored in memory
    for (let i = 0; i < numbers.length; i++) {
        sum += numbers[i];
    }
    return sum;
}
```
- **Why it matters**: The first function allocates memory for a large array, while the second function uses minimal memory.

---

## 3. **Speed (Time Complexity)**
Time Complexity refers to how long a program takes to execute. Faster code is often preferred, but it may require more memory.

### Example:
```javascript
// Faster: Uses a hash map for O(1) lookups
function findDuplicates(arr) {
    const seen = new Set();
    const duplicates = [];
    for (const num of arr) {
        if (seen.has(num)) {
            duplicates.push(num);
        } else {
            seen.add(num);
        }
    }
    return duplicates;
}

// Slower: Uses nested loops for O(n²) lookups
function findDuplicatesSlow(arr) {
    const duplicates = [];
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[i] === arr[j]) {
                duplicates.push(arr[i]);
            }
        }
    }
    return duplicates;
}
```
- **Why it matters**: The first function uses a `Set` for fast lookups, while the second function uses nested loops, which are much slower for large inputs.

---

## Trade-Offs Between Speed and Memory
In programming, there’s often a trade-off between speed and memory. For example:
- **Caching**: Increases speed by storing results in memory, but uses more memory.
- **Recursion**: Can make code more readable but may increase stack usage.
- **Precomputation**: Speeds up queries by precomputing results, but requires more memory.

### Example:
```javascript
// Faster but uses more memory: Caching results
function fibonacciWithCache(n, cache = {}) {
    if (n <= 1) return n;
    if (cache[n]) return cache[n]; // Return cached result if available
    cache[n] = fibonacciWithCache(n - 1, cache) + fibonacciWithCache(n - 2, cache);
    return cache[n];
}

// Slower but uses less memory: No caching
function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```
- **Why it matters**: The first function uses caching to speed up calculations but consumes more memory. The second function is slower but uses less memory.

---

## Balancing the 3 Pillars
The best code balances readability, memory usage, and speed. Here’s how to achieve this balance:

1. **Prioritize Readability**: Write clean, well-documented code that others (or your future self) can understand.
2. **Optimize for Memory**: Use data structures and algorithms that minimize memory usage, especially for large inputs.
3. **Optimize for Speed**: Use efficient algorithms and techniques to reduce runtime, but avoid unnecessary memory usage.

### Example:
```javascript
// Balanced: Readable, efficient, and uses reasonable memory
function findDuplicatesBalanced(arr) {
    const seen = new Set();
    const duplicates = new Set(); // Avoids duplicate entries in the result
    for (const num of arr) {
        if (seen.has(num)) {
            duplicates.add(num);
        } else {
            seen.add(num);
        }
    }
    return Array.from(duplicates);
}
```
- **Why it’s balanced**: This function is readable, uses a `Set` for fast lookups (speed), and avoids unnecessary memory usage by storing only unique duplicates.

---

## Summary

| Pillar           | Description                                                                 | Example                                                                 |
|------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Readable**     | Easy to understand and maintain.                                            | Use descriptive variable names and proper formatting.                   |
| **Memory**       | Efficient use of system memory (Heap and Stack).                            | Avoid unnecessary allocations and large data structures.                |
| **Speed**        | Fast execution time (Time Complexity).                                      | Use efficient algorithms like hash maps for O(1) lookups.               |

---

By balancing these 3 pillars, you can write code that is **efficient, maintainable, and scalable**. Always consider the trade-offs between speed and memory, and prioritize readability to ensure your code stands the test of time.
