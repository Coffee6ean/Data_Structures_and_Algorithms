# What is Good Code?

Good code is the foundation of efficient, maintainable, and scalable software. It is not just about making the code work but ensuring it works well under various conditions and is understandable by others (or your future self). Below are the key qualities to evaluate what good code is:

---

## 1. **Readable**
Readable code is easy to understand, follow, and maintain. It adheres to consistent naming conventions, proper indentation, and includes meaningful comments where necessary. Readability ensures that other developers (or you in the future) can quickly grasp the logic and purpose of the code.

### Tips for Writing Readable Code:
- Use descriptive variable and function names (e.g., `calculateTotalPrice` instead of `calc`).
- Follow a consistent coding style (e.g., camelCase, snake_case).
- Avoid overly complex one-liners; prioritize clarity over cleverness.
- Add comments to explain *why* something is done, not *what* is being done (the code should speak for itself).

---

## 2. **Scalable**
Scalable code can handle increased workloads efficiently as the input size grows. Scalability is often measured using **Big O Notation**, which describes how the runtime or resource requirements of an algorithm grow as the input size increases.

### What is Big O Notation?
Big O Notation is a mathematical concept used to describe the performance or complexity of an algorithm. It answers the question: *"How does the runtime or space requirements of an algorithm grow as the input size grows?"*

Here’s the updated section with **code examples** added to each of the common Big O notations. You can copy and paste this into your `.md` file.

---

### Common Big O Notations:

#### **O(1)**: Constant Time
The algorithm takes the same amount of time regardless of the input size.

##### Example:
```javascript
function getFirstElement(arr) {
    return arr[0]; // Accessing the first element of an array
}
```
- **Explanation**: No matter how large the array is, accessing the first element always takes the same amount of time.

---

#### **O(log n)**: Logarithmic Time
The runtime grows logarithmically as the input size increases. Commonly seen in divide-and-conquer algorithms.

##### Example:
```javascript
function binarySearch(arr, target) {
    let left = 0;
    let right = arr.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] === target) return mid; // Found the target
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1; // Target not found
}
```
- **Explanation**: In binary search, the input size is halved with each iteration, leading to a logarithmic runtime.

---

#### **O(n)**: Linear Time
The runtime grows linearly with the input size.

##### Example:
```javascript
function printArrayElements(arr) {
    for (let i = 0; i < arr.length; i++) {
        console.log(arr[i]); // Print each element
    }
}
```
- **Explanation**: The loop runs once for each element in the array, so the runtime scales linearly with the input size.

---

#### **O(n log n)**: Linearithmic Time
Common in efficient sorting algorithms like Merge Sort and Quick Sort.

##### Example:
```javascript
function mergeSort(arr) {
    if (arr.length <= 1) return arr;

    const mid = Math.floor(arr.length / 2);
    const left = mergeSort(arr.slice(0, mid)); // Recursively sort left half
    const right = mergeSort(arr.slice(mid)); // Recursively sort right half

    return merge(left, right); // Merge the two sorted halves
}

function merge(left, right) {
    let result = [];
    let i = 0, j = 0;

    while (i < left.length && j < right.length) {
        if (left[i] < right[j]) {
            result.push(left[i]);
            i++;
        } else {
            result.push(right[j]);
            j++;
        }
    }
    return result.concat(left.slice(i)).concat(right.slice(j));
}
```
- **Explanation**: Merge Sort divides the array into halves (log n) and then merges them in linear time (n), resulting in \( O(n \log n) \).

---

#### **O(n²)**: Quadratic Time
The runtime grows exponentially with the input size. Commonly seen in nested loops.

##### Example:
```javascript
function printAllPairs(arr) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length; j++) {
            console.log(arr[i], arr[j]); // Print all pairs
        }
    }
}
```
- **Explanation**: For each element in the array, the inner loop runs \( n \) times, resulting in \( n \times n = n^2 \) operations.

---

#### **O(2^n)**: Exponential Time
The runtime doubles with each additional input. Commonly seen in recursive algorithms that solve problems by breaking them into smaller subproblems.

##### Example:
```javascript
function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2); // Recursively calculate Fibonacci
}
```
- **Explanation**: Each call to `fibonacci` results in two more calls, leading to exponential growth in the number of operations.

---

### Summary of Common Big O Notations with Examples

| Big O Notation | Description                     | Example Code                                                                 |
|----------------|---------------------------------|------------------------------------------------------------------------------|
| **O(1)**       | Constant time                   | Accessing an array element by index.                                         |
| **O(log n)**   | Logarithmic time                | Binary search.                                                               |
| **O(n)**       | Linear time                     | Iterating through an array.                                                  |
| **O(n log n)** | Linearithmic time               | Merge Sort, Quick Sort.                                                      |
| **O(n²)**      | Quadratic time                  | Nested loops (e.g., printing all pairs in an array).                         |
| **O(2^n)**     | Exponential time                | Recursive Fibonacci.                                                         |

---

This section now includes **code examples** for each Big O notation, making it easier to understand how these complexities manifest in real-world algorithms. Let me know if you need further clarification or additional examples!

#### Why Big O Matters:
Understanding Big O helps developers choose the most efficient algorithm for a given problem, especially when dealing with large datasets.

---

## 3. **Algorithm Efficiency**
Algorithm efficiency refers to how well an algorithm performs in terms of time and space complexity. It is closely tied to Big O Notation and scalability.

### Key Metrics for Algorithm Efficiency:
- **Time Complexity**: How much time does the algorithm take to complete as the input size grows?
- **Space Complexity**: How much memory does the algorithm use as the input size grows?

### Example:
Consider a function that sums all numbers in an array:

```js
// O(n) time complexity
function sumArray(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}
```