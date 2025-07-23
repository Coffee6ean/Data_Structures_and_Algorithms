# Why Does, for Example \( 4 + 5n \) Simplify to \( O(n) \)?

Big O Notation is used to describe the **upper bound** of an algorithm's runtime or resource usage as the input size (\( n \)) grows toward infinity. It focuses on the **dominant term** and ignores constants and lower-order terms that become insignificant for large inputs. Let’s break this down step by step.

---

## 1. **What is Big O Notation?**
Big O Notation describes how an algorithm's runtime or resource usage scales as the input size (\( n \)) grows. It ignores constant factors and lower-order terms because they become negligible for large inputs.

---

## 2. **Simplifying \( 4 + 5n \):**
The function \( 4 + 5n \) consists of two terms:
- **\( 4 \)**: A constant term (does not depend on \( n \)).
- **\( 5n \)**: A linear term (scales directly with \( n \)).

### Step 1: Identify the Dominant Term
- As \( n \) grows larger, the term \( 5n \) dominates the function because it grows linearly with \( n \), while the constant term \( 4 \) remains the same regardless of \( n \).
- For example:
  - If \( n = 1 \), \( 4 + 5n = 9 \).
  - If \( n = 1000 \), \( 4 + 5n = 5004 \).
  - If \( n = 1,000,000 \), \( 4 + 5n = 5,000,004 \).

  As \( n \) increases, the \( 5n \) term becomes the primary contributor to the function's value, while the \( 4 \) becomes negligible.

### Step 2: Drop the Constant Coefficient
- The coefficient \( 5 \) in \( 5n \) is a constant factor. In Big O Notation, we ignore constant coefficients because they do not affect the **rate of growth** of the function.
- For example:
  - \( 5n \) grows at the same rate as \( n \), just 5 times faster. However, Big O Notation is concerned with the **general trend** (linear growth), not the specific multiplier.

### Step 3: Write the Simplified Big O
- After dropping the constant term (\( 4 \)) and the coefficient (\( 5 \)), the function \( 4 + 5n \) simplifies to \( O(n) \).

---

## 3. **Why Do We Ignore Constants and Lower-Order Terms?**
Big O Notation focuses on the **asymptotic behavior** of a function, meaning how it behaves as \( n \) approaches infinity. Constants and lower-order terms become insignificant in this context because:
- **Constants**: A constant like \( 4 \) or a coefficient like \( 5 \) does not change the **rate of growth** of the function. Whether the function is \( n \) or \( 5n \), it still grows linearly.
- **Lower-Order Terms**: Terms like \( 4 \) (constant) or \( n^2 \) (quadratic) in a function like \( n^2 + 5n + 4 \) are overshadowed by the dominant term (\( n^2 \)) as \( n \) grows.

---

## 4. **Mathematical Explanation**
Big O Notation is defined using limits. For a function \( f(n) = 4 + 5n \), we can say:
\[
f(n) = O(g(n))
\]
if there exists a constant \( C > 0 \) and a value \( n_0 \) such that:
\[
f(n) \leq C \cdot g(n) \quad \text{for all} \quad n \geq n_0.
\]

For \( f(n) = 4 + 5n \), we can choose \( g(n) = n \), \( C = 6 \), and \( n_0 = 1 \):
\[
4 + 5n \leq 6n \quad \text{for all} \quad n \geq 1.
\]
This satisfies the definition of \( O(n) \).

---

## 5. **Example Comparison**
Let’s compare \( 4 + 5n \) with \( n \) for different values of \( n \):

| \( n \) | \( 4 + 5n \) | \( n \) | Ratio (\( \frac{4 + 5n}{n} \)) |
|---------|--------------|---------|-------------------------------|
| 1       | 9            | 1       | 9                             |
| 10      | 54           | 10      | 5.4                           |
| 100     | 504          | 100     | 5.04                          |
| 1000    | 5004         | 1000    | 5.004                         |

As \( n \) grows, the ratio \( \frac{4 + 5n}{n} \) approaches \( 5 \), which is a constant. This shows that \( 4 + 5n \) grows **linearly** with \( n \), and the constant \( 4 \) becomes insignificant.

---

## 6. **General Rule for Simplifying Big O**
When simplifying a function for Big O Notation:
1. **Keep the dominant term**: The term that grows the fastest as \( n \) increases.
2. **Drop constants**: Coefficients and lower-order terms do not affect the growth rate.
3. **Write the result**: Express the simplified function in Big O Notation.

For example:
- \( 4 + 5n \) → \( O(n) \)
- \( 3n^2 + 2n + 10 \) → \( O(n^2) \)
- \( 7n^3 + 100n^2 + 50 \) → \( O(n^3) \)

---

## 7. **Conclusion**
The function \( 4 + 5n \) simplifies to \( O(n) \) because:
1. The linear term \( 5n \) dominates as \( n \) grows.
2. The constant \( 4 \) becomes insignificant for large \( n \).
3. The coefficient \( 5 \) is dropped because it does not affect the growth rate.

This simplification allows us to focus on the **scalability** of the algorithm, which is the primary purpose of Big O Notation.
