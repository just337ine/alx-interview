# 0x0A Primegame

## Prime Numbers

### Understanding Prime Numbers
Prime numbers are natural numbers greater than 1 that have no positive divisors other than 1 and themselves. In other words, a prime number is a number that cannot be formed by multiplying two smaller natural numbers. The first few prime numbers are: 2, 3, 5, 7, 11, 13, etc.

### Efficient Algorithms for Identifying Prime Numbers Within a Range
To identify prime numbers within a given range, you can use several algorithms. The simplest method is trial division, where you check divisibility by all integers up to the square root of the number. However, more efficient algorithms exist, such as the Sieve of Eratosthenes.

## Sieve of Eratosthenes

### Overview
The Sieve of Eratosthenes is an efficient algorithm for finding all prime numbers up to a specified limit. It works by iteratively marking the multiples of each prime number starting from 2.

### Algorithm Steps
1. Create a boolean array `is_prime` of size `n+1` and initialize all entries to `True`.
2. Set `is_prime[0]` and `is_prime[1]` to `False`, as 0 and 1 are not prime.
3. For each number `p` from 2 to the square root of `n`:
   - If `is_prime[p]` is `True`, mark all multiples of `p` as `False`.
4. The remaining `True` values in `is_prime` indicate prime numbers.

### Implementation in Python
```python
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(n + 1) if is_prime[p]]

# Example usage
print(sieve_of_eratosthenes(30))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

## Game Theory

### Basic Principles of Competitive Games
In competitive games, players take turns making moves, with each move potentially leading to a win or loss. Understanding optimal play involves analyzing the game's win conditions and strategies that maximize a player's chances of winning.

### Understanding Win Conditions and Strategies
Win conditions are the scenarios where a player wins the game. Strategies are plans or methods employed by players to reach these win conditions while preventing their opponents from doing so.

## Dynamic Programming/Memoization

### Concept
Dynamic programming (DP) is a method for solving problems by breaking them down into simpler subproblems and storing the results of these subproblems to avoid redundant calculations. Memoization is a specific type of dynamic programming where you store the results of expensive function calls and reuse them when the same inputs occur again.

### Application in Games
In the context of game theory, dynamic programming can optimize solutions across multiple rounds of a game by reusing previously calculated results.

## Python Programming

### Loops and Conditional Statements
Loops (for, while) and conditional statements (if, else) are fundamental in implementing game logic and algorithms.

### Example of Using Loops and Conditional Statements
```python
# Simple loop example
for i in range(10):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
```

### Arrays and Lists for Storing Data
Arrays (lists in Python) are used to store integers and track removed numbers during gameplay or algorithm execution.

### Example of Using Lists
```python
# List example
numbers = [1, 2, 3, 4, 5]
removed_numbers = []
for number in numbers:
    if number % 2 == 0:
        removed_numbers.append(number)

print("Removed numbers:", removed_numbers)  # Output: Removed numbers: [2, 4]
```

## Resources:
1. Prime Numbers and Sieve of Eratosthenes:
  * [Khan Academy:Prime Numbers](https://www.khanacademy.org/math/cc-fourth-grade-math/imp-factors-multiples-and-patterns/imp-prime-and-composite-numbers/v/prime-numbers)
  * [Sieve of Eratosthenes in Python](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)
Game Theory Basics: [Game Theory Introduction](https://www.investopedia.com/terms/g/gametheory.asp)
2. Dynamic Programming:[What Is Dynamic Programming With Python Examples](https://skerritt.blog/dynamic-programming/)
3. Python Official Documentation:[Python Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
