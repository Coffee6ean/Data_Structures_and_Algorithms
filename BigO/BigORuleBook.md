# Big O Rules Explained

Big O Notation is a fundamental concept in computer science used to describe the performance or complexity of an algorithm. It helps us understand how an algorithm scales as the input size grows. Below are the **four key rules** of Big O Notation, explained with theory and examples.

---

## Rule 1: **Worst Case**
Big O Notation always considers the **worst-case scenario** when analyzing an algorithm's performance. This means we focus on the maximum amount of time or resources an algorithm could take, regardless of the input.

### Example:
Consider a function that searches for a specific value in an array:

```javascript
function findValue(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) {
            return i; // Return the index if found
        }
    }
    return -1; // Return -1 if not found
}
```

- **Best Case**: The target is the first element (\( O(1) \)).
- **Worst Case**: The target is the last element or not in the array (\( O(n) \)).
- **Big O**: We use \( O(n) \) because we always consider the worst case.

---

## Rule 2: **Remove Constants**
When analyzing Big O, we **ignore constant factors** because they do not affect the growth rate of the algorithm as the input size increases.

### Example:
Consider the following function:

```javascript
function processArray(arr) {
    arr.forEach(item => console.log(item)); // O(n)
    arr.forEach(item => console.log(item)); // O(n)
}
```

- The function has two loops, each running \( n \) times.
- Total operations: \( 2n \).
- **Big O**: We drop the constant \( 2 \), so the complexity is \( O(n) \).

---

## Rule 3: **Different Terms for Inputs**
If an algorithm has multiple inputs, we use **different terms** to represent each input. We do not combine them into a single term unless they are directly related.

### Example:
Consider a function that processes two arrays:

```javascript
function processTwoArrays(arr1, arr2) {
    arr1.forEach(item => console.log(item)); // O(a)
    arr2.forEach(item => console.log(item)); // O(b)
}
```

- The first loop runs \( a \) times (size of `arr1`).
- The second loop runs \( b \) times (size of `arr2`).
- **Big O**: \( O(a + b) \), because the inputs are independent.

---

## Rule 4: **Drop Non-Dominants**
When analyzing Big O, we focus on the **dominant term** (the term that grows the fastest as the input size increases) and drop all non-dominant terms.

### Example:
Consider the following function:

```javascript
function processAndSquare(arr) {
    arr.forEach(item => console.log(item)); // O(n)
    arr.forEach(item => {
        arr.forEach(innerItem => console.log(item + innerItem)); // O(n^2)
    });
}
```

- The first loop runs \( n \) times (\( O(n) \)).
- The nested loop runs \( n \times n \) times (\( O(n^2) \)).
- Total complexity: \( O(n + n^2) \).
- **Big O**: We drop the non-dominant term \( n \), so the complexity is \( O(n^2) \).

---

## Summary of Big O Rules

| Rule                  | Description                                                                 | Example                          | Big O        |
|-----------------------|-----------------------------------------------------------------------------|----------------------------------|--------------|
| **Worst Case**        | Always consider the worst-case scenario.                                    | Searching an array for a value   | \( O(n) \)   |
| **Remove Constants**  | Ignore constant factors in the complexity.                                  | Two loops of \( n \) operations  | \( O(n) \)   |
| **Different Terms**   | Use separate terms for different inputs.                                    | Processing two arrays            | \( O(a + b) \) |
| **Drop Non-Dominants**| Focus on the dominant term and drop non-dominant terms.                     | \( O(n + n^2) \)                 | \( O(n^2) \) |

---

## Practical Example

Let’s analyze the following function using all four rules:

```javascript
function exampleFunction(arr1, arr2) {
    // Rule 3: Different terms for inputs
    arr1.forEach(item => console.log(item)); // O(a)

    // Rule 3: Different terms for inputs
    arr2.forEach(item => console.log(item)); // O(b)

    // Rule 4: Drop non-dominants
    arr1.forEach(item => {
        arr2.forEach(innerItem => console.log(item + innerItem)); // O(a * b)
    });

    // Rule 2: Remove constants
    for (let i = 0; i < 1000; i++) {
        console.log("Constant operation"); // O(1)
    }
}
```

- **Step 1**: Identify the terms:
  - \( O(a) \) (first loop)
  - \( O(b) \) (second loop)
  - \( O(a \times b) \) (nested loop)
  - \( O(1) \) (constant loop)
- **Step 2**: Apply Rule 2 (remove constants) to the \( O(1) \) term.
- **Step 3**: Apply Rule 4 (drop non-dominants) to focus on \( O(a \times b) \).
- **Final Big O**: \( O(a \times b) \).

---

## Conclusion
Understanding these four rules of Big O Notation is essential for analyzing and comparing the efficiency of algorithms. By focusing on the **worst case**, **removing constants**, **using different terms for inputs**, and **dropping non-dominant terms**, we can simplify complexity analysis and make better decisions when designing algorithms.
