# 0x08 making_change

## Introduction

This README provides an in-depth exploration of algorithms suitable for solving the coin change problem.

## Greedy Algorithms

### How Greedy Algorithms Work

Greedy algorithms build up a solution piece by piece, always choosing the next piece that offers the most immediate benefit. In the context of the coin change problem, a greedy algorithm selects the largest coin denomination that is less than or equal to the remaining amount to be changed until the amount is zero.

### Suitability for the Coin Change Problem

Greedy algorithms are straightforward and can be very efficient. They work well for the coin change problem when the coin denominations allow a greedy choice to lead to an optimal solution. For example, with U.S. coins (1, 5, 10, 25), a greedy approach works perfectly.

### Limitations

Greedy algorithms do not always provide the optimal solution for all sets of coin denominations. For example, with denominations {1, 3, 4}, a greedy algorithm trying to make change for 6 would choose {4, 1, 1} instead of the optimal {3, 3}.

## Dynamic Programming

### Basic Principles

Dynamic programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems. It is particularly effective for optimization problems where the solution can be constructed from solutions to overlapping subproblems.

### Overlapping Subproblems and Optimal Substructure

In the coin change problem, the optimal solution for a given amount depends on the optimal solutions for smaller amounts. For instance, if we know the minimum coins needed for amounts smaller than the target, we can build the solution for the target amount.

## Algorithmic Complexity

### Time Complexity

Analyzing the time complexity involves understanding how the number of operations grows with input size. For greedy algorithms in the coin change problem, the time complexity is typically O(n) where n is the amount to be changed. For dynamic programming solutions, it is O(n * m) where m is the number of different coin denominations.

### Space Complexity

Space complexity refers to the amount of memory used by the algorithm. For DP solutions, the space complexity is often O(n), as it requires storage for the solutions to subproblems.

## Problem-Solving Strategies

### Breaking Down the Problem

The coin change problem can be broken down into smaller subproblems, each representing a smaller amount of change to be made. This is central to the dynamic programming approach.

### Iterative vs Recursive Approaches

- **Iterative Approach**: Constructs the solution in a bottom-up manner, starting from the smallest subproblems.
- **Recursive Approach**: Solves the problem in a top-down manner, starting from the target amount and recursively solving for smaller amounts. Often combined with memoization to store intermediate results and avoid redundant calculations.

## Python Programming

### Manipulating Lists and Using List Comprehensions

Python lists are versatile for implementing DP solutions. List comprehensions provide a concise way to create lists and perform operations.

### Efficient Looping and Conditional Statements

Efficient loops and conditionals are crucial for performance. Using range-based loops and minimizing unnecessary checks can improve the efficiency of your algorithm.

### Example: Dynamic Programming for Coin Change

```python
def coin_change(coins, amount):
    # Initialize the DP table with a value higher than any possible solution
    dp = [float('inf')] * (amount + 1)
    # Base case: 0 coins are needed to make 0 amount
    dp[0] = 0
    
    # Fill the DP table
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] != float('inf'):
                dp[x] = min(dp[x], dp[x - coin] + 1)
    
    # Return the result for the amount or -1 if no solution was found
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))  # Output: 3 (5 + 5 + 1)
```

## Resources

1. Python Official Documentation: [Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
2. GeeksforGeeks Articles:
   * [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
   * [Greedy Algorithm](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
