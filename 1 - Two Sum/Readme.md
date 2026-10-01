# 🧩 Problem 1: Two Sum

- **Platform**: [LeetCode #1](https://leetcode.com/problems/two-sum/)
- **Difficulty**: `🟢 Easy`
- **Topics**: `Array`, `Hash Table`
- **Solution File**: [`main.js`](./main.js)
- **Navigation**: [🏠 Problem Index](../Readme.md) | [Next Problem: Palindrome Number ➡️](../2%20-%20Palindrome%20Number/README.md)

---

## 📖 Problem Statement

Given an array of integers `nums` and an integer `target`, return **indices of the two numbers such that they add up to `target`**.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

---

### Examples

#### Example 1:
- **Input**: `nums = [2, 7, 11, 15]`, `target = 9`
- **Output**: `[0, 1]`
- **Explanation**: Because `nums[0] + nums[1] == 2 + 7 == 9`, we return `[0, 1]`.

#### Example 2:
- **Input**: `nums = [3, 2, 4]`, `target = 6`
- **Output**: `[1, 2]`
- **Explanation**: Because `nums[1] + nums[2] == 2 + 4 == 6`, we return `[1, 2]`.

#### Example 3:
- **Input**: `nums = [3, 3]`, `target = 6`
- **Output**: `[0, 1]`
- **Explanation**: Because `nums[0] + nums[1] == 3 + 3 == 6`, we return `[0, 1]`.

---

### Constraints

- $2 \le \text{nums.length} \le 10^4$
- $-10^9 \le \text{nums}[i] \le 10^9$
- $-10^9 \le \text{target} \le 10^9$
- **Only one valid answer exists.**

---

## 💡 Intuition & Core Concept

We need to find two distinct indices $i$ and $j$ such that:

$$\text{nums}[i] + \text{nums}[j] = \text{target}$$

Rearranging this formula gives the **complement**:

$$\text{complement} = \text{target} - \text{nums}[i]$$

For every number `x` we inspect, we simply need to know:
> *"Have we already seen `target - x` earlier in the array?"*

---

## 🚀 Approaches

### Approach 1: Brute Force (Nested Loops)

#### Concept
Check every possible pair $(i, j)$ in the array and see if their sum matches `target`.

#### Algorithm
1. Loop $i$ from $0$ to $\text{length} - 1$.
2. Loop $j$ from $i + 1$ to $\text{length} - 1$.
3. Check if `nums[i] + nums[j] === target`. If true, return `[i, j]`.

#### JavaScript Implementation
```javascript
function twoSumBruteForce(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }
    return [];
}
```

#### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n^2)$ — Two nested loops iterate over the array of length $n$.
- **Space Complexity**: $\mathcal{O}(1)$ — No additional auxiliary memory is allocated.

---

### Approach 2: One-Pass Hash Map (Optimal) 🌟

#### Concept
Instead of repeatedly scanning the array to find the complement, we can use a Hash Map (or JavaScript `Map` / `Object`) to store each number and its index as we iterate. Looking up a key in a Hash Map takes $\mathcal{O}(1)$ on average.

#### Step-by-Step Walkthrough
1. Initialize an empty Hash Map: `seen = new Map()`.
2. Iterate through `nums` with index `i`:
   - Calculate `complement = target - nums[i]`.
   - If `seen.has(complement)`, return `[seen.get(complement), i]`.
   - Otherwise, store the current element: `seen.set(nums[i], i)`.
3. If no pair is found, return `[]`.

#### Dry Run Example
For `nums = [2, 7, 11, 15]` and `target = 9`:

| Step | Index ($i$) | Current Num | Complement ($9 - \text{num}$) | In Map? | Map State (`seen`) | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `0` | `2` | `7` | No | `{ 2 => 0 }` | Store `2` at index `0` |
| 2 | `1` | `7` | `2` | **Yes!** (at index `0`) | `{ 2 => 0 }` | **Return `[0, 1]`** |

#### JavaScript Implementation
```javascript
function twoSum(nums, target) {
    const seen = new Map();

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];

        if (seen.has(complement)) {
            return [seen.get(complement), i];
        }

        seen.set(nums[i], i);
    }

    return [];
}
```

#### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ — We traverse the list containing $n$ elements exactly once. Each hash table lookup takes $\mathcal{O}(1)$ average time.
- **Space Complexity**: $\mathcal{O}(n)$ — The map stores up to $n$ elements in the worst case.

---

## ⚖️ Complexity Comparison

| Approach | Time Complexity | Space Complexity | Best Used When |
| :--- | :---: | :---: | :--- |
| **Brute Force** | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | Memory is extremely constrained, or $n \le 100$. |
| **Hash Map (One-Pass)** | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | Optimal for interviews and production systems. |

---

## 💻 How to Run

Run the solution directly using Node.js:

```bash
# From workspace root
node "1 - Two Sum/main.js"

# Or navigate into the folder
cd "1 - Two Sum"
node main.js
```

---

## 🔑 Key Takeaways

1. **Hash Maps Trade Space for Time**: Moving from $\mathcal{O}(n^2)$ to $\mathcal{O}(n)$ by using an $\mathcal{O}(n)$ hash map is one of the most common optimization patterns in array problems.
2. **Complement Lookup Pattern**: Storing `target - current` simplifies pairwise sum checks to instant lookups.

---

## 🧭 Navigation

- [🏠 Repository Index](../Readme.md)
- [Next Problem: Palindrome Number ➡️](../2%20-%20Palindrome%20Number/README.md)