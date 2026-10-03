# 🧩 Problem 2: Palindrome Number

- **Platform**: [LeetCode #9](https://leetcode.com/problems/palindrome-number/)
- **Difficulty**: `🟢 Easy`
- **Topics**: `Math`, `Two Pointers`
- **Solution File**: [`main.js`](./main.js)
- **Navigation**: [⬅️ Previous Problem: Two Sum](../1%20-%20Two%20Sum/Readme.md) | [🏠 Problem Index](../Readme.md) | [Next Problem: Roman to Integer ➡️](../3%20-%20Roman%20to%20Integer/README.md)

---

## 📖 Problem Statement

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

An integer is a **palindrome** when it reads the same forward and backward.
- For example, `121` is a palindrome, while `123` is not.

> **Follow-up**: Could you solve it without converting the integer to a string?

---

### Examples

#### Example 1:
- **Input**: `x = 121`
- **Output**: `true`
- **Explanation**: `121` reads as `121` from left to right and from right to left.

#### Example 2:
- **Input**: `x = -121`
- **Output**: `false`
- **Explanation**: From left to right, it reads `-121`. From right to left, it becomes `121-`. Therefore it is not a palindrome.

#### Example 3:
- **Input**: `x = 10`
- **Output**: `false`
- **Explanation**: Reads `01` from right to left. Therefore it is not a palindrome.

---

### Constraints

- $-2^{31} \le x \le 2^{31} - 1$ (32-bit signed integer range)

---

## 💡 Intuition & Core Concept

### 1. Identifying Instant Disqualifiers (Edge Cases)
- **Negative Numbers ($x < 0$)**:
  Any negative number starts with a minus sign `-`. Reversing `-121` yields `121-`, which is never identical to the original negative value. All negative numbers are immediately `false`.
- **Numbers Ending in Zero ($x \% 10 === 0 \text{ and } x \ne 0$)**:
  If a number ends in `0`, its reversed version would have to start with `0`. The only number that starts and ends with `0` is `0` itself. Any other number ending in `0` (e.g., `10`, `200`, `1230`) is immediately `false`.

### 2. Avoiding String Conversion & Integer Overflow
Converting the integer to a string is simple, but:
1. It allocates extra memory $\mathcal{O}(n)$.
2. It ignores the follow-up requirement.

Reversing the *entire* integer mathematically can cause **integer overflow** when reversing values close to $2^{31} - 1$.

### 3. The Revert-Half Insight 🌟
Instead of reversing the entire number:
- We can **reverse only the second half of the digits**.
- As we extract digits from the back of `x` and append them to `rev`, `x` shrinks and `rev` grows.
- When `x <= rev`, we have reached or crossed the middle point of the number!

---

## 🚀 Approaches

### Approach 1: Convert to String & Compare (Naive)

#### Concept
Convert the integer to a string and check if the string equals its reverse.

#### JavaScript Implementation
```javascript
function isPalindromeString(x) {
    if (x < 0) return false;
    const str = x.toString();
    return str === str.split('').reverse().join('');
}
```

#### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(d)$ — Where $d = \log_{10}(x)$ is the number of digits. Creating and reversing the string takes linear time relative to digit count.
- **Space Complexity**: $\mathcal{O}(d)$ — Creates auxiliary strings and arrays in memory.

---

### Approach 2: Reverting Half the Number (Optimal) 🌟

#### Concept
Extract the last digits of `x` using modulo arithmetic (`% 10`) and construct the reversed half (`rev * 10 + lastDigit`) while reducing `x` (`Math.floor(x / 10)`). Stop as soon as `x <= rev`.

#### Step-by-Step Algorithm
1. Check edge cases: if `x < 0` or (`x % 10 === 0 && x !== 0`), return `false`.
2. Initialize `rev = 0`.
3. Loop while `x > rev`:
   - Extract last digit: `lastDigit = x % 10`.
   - Append to reversed number: `rev = rev * 10 + lastDigit`.
   - Drop last digit from original: `x = Math.floor(x / 10)`.
4. Check palindrome condition:
   - **Even number of digits** (e.g. `1221`): `x === rev` (`12 === 12`).
   - **Odd number of digits** (e.g. `12321`): The middle digit is stored as the last digit in `rev` (`x = 12`, `rev = 123`). We discard it using `Math.floor(rev / 10)` and check `x === Math.floor(rev / 10)` (`12 === 12`).

#### Step-by-Step Dry Run

##### Trace 1: `x = 1221` (Even length)

| Iteration | `x` (before) | `lastDigit = x % 10` | `rev = rev * 10 + lastDigit` | `x = Math.floor(x / 10)` | Condition `x > rev` |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Init** | `1221` | - | `0` | - | `1221 > 0` (True) |
| **1** | `1221` | `1` | `0 * 10 + 1 = 1` | `122` | `122 > 1` (True) |
| **2** | `122` | `2` | `1 * 10 + 2 = 12` | `12` | `12 > 12` (**False** → Loop terminates) |

- **Final Check**: `x === rev` $\rightarrow$ `12 === 12` $\rightarrow$ **`true`** ✅

---

##### Trace 2: `x = 12321` (Odd length)

| Iteration | `x` (before) | `lastDigit = x % 10` | `rev = rev * 10 + lastDigit` | `x = Math.floor(x / 10)` | Condition `x > rev` |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Init** | `12321` | - | `0` | - | `12321 > 0` (True) |
| **1** | `12321` | `1` | `0 * 10 + 1 = 1` | `1232` | `1232 > 1` (True) |
| **2** | `1232` | `2` | `1 * 10 + 2 = 12` | `123` | `123 > 12` (True) |
| **3** | `123` | `3` | `12 * 10 + 3 = 123` | `12` | `12 > 123` (**False** → Loop terminates) |

- **Final Check**: `x === Math.floor(rev / 10)` $\rightarrow$ `12 === Math.floor(123 / 10)` $\rightarrow$ `12 === 12` $\rightarrow$ **`true`** ✅

---

#### JavaScript Implementation
```javascript
function Palindromex(x) {
    // Negative numbers and non-zero numbers ending in 0 cannot be palindromes
    if (x < 0 || (x % 10 === 0 && x !== 0)) return false;

    let rev = 0;
    while (x > rev) {
        let lastDigit = x % 10;
        rev = rev * 10 + lastDigit;
        x = Math.floor(x / 10);
    }

    // Even digits: x === rev
    // Odd digits:  x === Math.floor(rev / 10) (drops middle digit)
    return (x === rev || x === Math.floor(rev / 10));
}

// Example usage:
console.log(Palindromex(121));   // true
console.log(Palindromex(-121));  // false
console.log(Palindromex(10));    // false
console.log(Palindromex(11));    // true
```

#### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(\log_{10}(n))$ — We divide the input by $10$ in every iteration. Since we only process half the digits, the loop runs $\approx \frac{\log_{10}(n)}{2}$ times.
- **Space Complexity**: $\mathcal{O}(1)$ — Constant space. Only primitive numbers are used without any string or array allocations.

---

## ⚖️ Complexity Comparison

| Approach | Time Complexity | Space Complexity | Avoids Overflow? | No String Conversion? |
| :--- | :---: | :---: | :---: | :---: |
| **String Conversion** | $\mathcal{O}(\log_{10}(n))$ | $\mathcal{O}(\log_{10}(n))$ | Yes | ❌ (Allocates string) |
| **Reverse Entire Number** | $\mathcal{O}(\log_{10}(n))$ | $\mathcal{O}(1)$ | ❌ (Risk of 32-bit overflow) | ✅ |
| **Revert Half Number (Optimal)** | $\mathcal{O}(\log_{10}(n))$ | $\mathcal{O}(1)$ | ✅ | ✅ |

---

## 💻 How to Run

Run the solution directly using Node.js:

```bash
# From workspace root
node "2 - Palindrome Number/main.js"

# Or navigate into the folder
cd "2 - Palindrome Number"
node main.js
```

---

## 🔑 Key Takeaways

1. **Reversing Half Prevents Overflow**: Reversing only half the digits naturally caps the reversed number at $\le \sqrt{n}$ digits, completely eliminating the danger of integer overflow.
2. **Modulo and Division (`% 10`, `/ 10`)**: The foundational pattern for mathematical digit extraction without strings.
3. **Handling Parity (Even vs Odd)**: Using `Math.floor(rev / 10)` cleanly ignores the middle digit for odd-length numbers since the middle digit is always self-symmetric.

---

## 🧭 Navigation

- [⬅️ Previous Problem: Two Sum](../1%20-%20Two%20Sum/Readme.md)
- [🏠 Repository Index](../Readme.md)
- [Next Problem: Roman to Integer ➡️](../3%20-%20Roman%20to%20Integer/README.md)
