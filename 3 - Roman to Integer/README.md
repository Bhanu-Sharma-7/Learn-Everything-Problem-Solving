# 🧩 Problem 3: Roman to Integer

- **Platform**: [LeetCode #13](https://leetcode.com/problems/roman-to-integer/)
- **Difficulty**: `🟢 Easy`
- **Topics**: `Hash Table`, `Math`, `String`
- **Solution File**: [`main.js`](./main.js)
- **Navigation**: [⬅️ Previous Problem: Palindrome Number](../2%20-%20Palindrome%20Number/README.md) | [🏠 Problem Index](../Readme.md)

---

## 📖 Problem Statement

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D`, and `M`.

| Symbol | Value |
| :---: | :---: |
| **I** | 1 |
| **V** | 5 |
| **X** | 10 |
| **L** | 50 |
| **C** | 100 |
| **D** | 500 |
| **M** | 1000 |

For example:
- `2` is written as `II` in Roman numeral, just two ones added together.
- `12` is written as `XII`, which is simply `X + II`.
- `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`.

There are six instances where subtraction is used:
- `I` can be placed before `V` (5) and `X` (10) to make `4` and `9`. 
- `X` can be placed before `L` (50) and `C` (100) to make `40` and `90`. 
- `C` can be placed before `D` (500) and `M` (1000) to make `400` and `900`.

Given a roman numeral, convert it to an integer.

---

### Examples

#### Example 1:
- **Input**: `s = "III"`
- **Output**: `3`
- **Explanation**: `III = 3`.

#### Example 2:
- **Input**: `s = "LVIII"`
- **Output**: `58`
- **Explanation**: `L = 50`, `V = 5`, `III = 3`. `50 + 5 + 3 = 58`.

#### Example 3:
- **Input**: `s = "MCMXCIV"`
- **Output**: `1994`
- **Explanation**: `M = 1000`, `CM = 900`, `XC = 90` and `IV = 4`. `1000 + 900 + 90 + 4 = 1994`.

---

### Constraints

- $1 \le \text{s.length} \le 15$
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is **guaranteed** that `s` is a valid roman numeral in the range $[1, 3999]$.

---

## 💡 Intuition & Core Concept

In Roman numerals:
1. **Additive Order**: Normally, symbols are listed from largest to smallest ($M \rightarrow D \rightarrow C \rightarrow L \rightarrow X \rightarrow V \rightarrow I$). When a symbol is followed by one of equal or smaller value, its value is **added** to the running total.
2. **Subtractive Rule**: Whenever a symbol with a **smaller** value appears **before a symbol with a larger value**, it means the smaller value is being subtracted from the larger value.
   - For example, in `"IV"`, $I < V$ ($1 < 5$), so we subtract $1$: $-1 + 5 = 4$.
   - In `"IX"`, $I < X$ ($1 < 10$), so we subtract $1$: $-1 + 10 = 9$.
   - In `"XL"`, $X < L$ ($10 < 50$), so we subtract $10$: $-10 + 50 = 40$.

### The Lookahead Rule
When inspecting character $s[i]$:
- If the next symbol $s[i+1]$ exists and has a **greater value** than $s[i]$, we **subtract** the current value:
  $$\text{total} \mathrel{-}= \text{value}(s[i])$$
- Otherwise, we **add** the current value:
  $$\text{total} \mathrel{+}= \text{value}(s[i])$$

When $i$ reaches the last character, there is no next character (`undefined`), so it will always be added to the total.

---

## 🚀 Approaches

### Approach 1: Left-to-Right Lookahead (Optimal) 🌟

#### Concept
Store the values of Roman characters in a Hash Map / JavaScript object. Iterate through the string from left to right. At each index, compare the value of the current symbol with the value of the next symbol.

#### Step-by-Step Algorithm
1. Create a dictionary/map `symbols` mapping each Roman character to its integer value.
2. Initialize `total = 0`.
3. Loop `i` from `0` to `s.length - 1`:
   - Let `currentNumber = symbols[s[i]]`.
   - Let `nextNumber = symbols[s[i + 1]]`.
   - If `nextNumber > currentNumber`, subtract `currentNumber` from `total`.
   - Else, add `currentNumber` to `total`.
4. Return `total`.

#### Step-by-Step Dry Run

##### Trace: `s = "MCMXCIV"` (Expected Output: `1994`)

| Step | Index ($i$) | Char ($s[i]$) | Current Value | Next Char ($s[i+1]$) | Next Value | Condition (`next > curr`) | Action | Running Total |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Init** | - | - | - | - | - | - | Initialize `total = 0` | `0` |
| **1** | `0` | `'M'` | `1000` | `'C'` | `100` | `100 > 1000` (False) | Add `1000` | `0 + 1000 = 1000` |
| **2** | `1` | `'C'` | `100` | `'M'` | `1000` | `1000 > 100` (**True**) | Subtract `100` | `1000 - 100 = 900` |
| **3** | `2` | `'M'` | `1000` | `'X'` | `10` | `10 > 1000` (False) | Add `1000` | `900 + 1000 = 1900` |
| **4** | `3` | `'X'` | `10` | `'C'` | `100` | `100 > 10` (**True**) | Subtract `10` | `1900 - 10 = 1890` |
| **5** | `4` | `'C'` | `100` | `'I'` | `1` | `1 > 100` (False) | Add `100` | `1890 + 100 = 1990` |
| **6** | `5` | `'I'` | `1` | `'V'` | `5` | `5 > 1` (**True**) | Subtract `1` | `1990 - 1 = 1989` |
| **7** | `6` | `'V'` | `5` | `undefined` | `undefined` | `undefined > 5` (False) | Add `5` | `1989 + 5 = 1994` |

- **Result**: `1994` ✅

---

#### JavaScript Implementation

```javascript
function roman(s) {
    const symbols = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    };

    let total = 0;

    for (let i = 0; i < s.length; i++) {
        const currentNumber = symbols[s[i]];
        const nextNumber = symbols[s[i + 1]];

        if (nextNumber > currentNumber) {
            total -= currentNumber;
        } else {
            total += currentNumber;
        }
    }

    return total;
}

// Example usage:
console.log(roman("III"));     // 3
console.log(roman("LVIII"));   // 58
console.log(roman("MCMXCIV")); // 1994
console.log(roman("IV"));      // 4
```

#### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — We iterate over the input string of length $n$ once. Since $n \le 15$ by problem constraints, this operation takes strictly bounded constant time $\mathcal{O}(1)$.
- **Space Complexity**: $\mathcal{O}(1)$ — The dictionary contains a fixed size of 7 Roman symbols. No extra dynamically sized memory is allocated.

---

### Approach 2: Right-to-Left Traversal (Alternative)

#### Concept
Traverse the string backward from right to left. Keep track of the maximum value seen so far or the previous value. If the current value is less than the previous value, subtract it; otherwise, add it.

#### JavaScript Implementation

```javascript
function romanToIntRightToLeft(s) {
    const symbols = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    };

    let total = 0;
    let prevValue = 0;

    for (let i = s.length - 1; i >= 0; i--) {
        const currValue = symbols[s[i]];

        if (currValue < prevValue) {
            total -= currValue;
        } else {
            total += currValue;
        }

        prevValue = currValue;
    }

    return total;
}
```

#### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — Single pass from right to left.
- **Space Complexity**: $\mathcal{O}(1)$ — Fixed memory usage.

---

## ⚖️ Complexity Comparison

| Approach | Time Complexity | Space Complexity | Code Simplicity | Lookahead Required? |
| :--- | :---: | :---: | :---: | :---: |
| **Left-to-Right Lookahead** | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Very High | Yes ($s[i+1]$) |
| **Right-to-Left Pass** | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | High | No (Tracks `prev`) |

---

## 💻 How to Run

Run the solution directly using Node.js:

```bash
# From workspace root
node "3 - Roman to Integer/main.js"

# Or navigate into the folder
cd "3 - Roman to Integer"
node main.js
```

---

## 🔑 Key Takeaways

1. **Subtractive Principle**: A smaller numeral preceding a larger numeral always represents subtraction, avoiding the need for multi-character token parsing (like treating `"IV"` or `"CM"` as special composite symbols).
2. **Graceful Lookahead Handling**: In JavaScript, accessing `s[i + 1]` at the last character yields `undefined`. Evaluating `undefined > currentNumber` evaluates to `false`, which naturally falls into the addition branch without needing an out-of-bounds guard check.
3. **$\mathcal{O}(1)$ Constant Footprint**: Because the Roman numeral alphabet is finite (7 characters) and valid numbers cannot exceed 3999 ($s.length \le 15$), Roman numeral conversion is an $\mathcal{O}(1)$ operation in practical terms.

---

## 🧭 Navigation

- [⬅️ Previous Problem: Palindrome Number](../2%20-%20Palindrome%20Number/README.md)
- [🏠 Repository Index](../Readme.md)
