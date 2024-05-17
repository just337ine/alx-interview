# 0x09 island_perimeter


## Introduction
This README file explains the concepts and techniques required to solve the problem of calculating the perimeter of an island represented in a 2D array (matrix). The island is defined as a group of connected land cells (1s) in the matrix, surrounded by water cells (0s). 

## 2D Arrays (Matrices)
### Accessing and Iterating Over Elements in a 2D Array
A 2D array, or matrix, is a grid of elements where each element is accessed using two indices: row and column.

Example of a 2D array:
```python
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
```

To iterate over each element in a 2D array, nested loops are used:
```python
for row in range(len(grid)):
    for col in range(len(grid[row])):
        # Access the element using grid[row][col]
```

### Navigating Through Adjacent Cells
To check the adjacent cells (horizontally and vertically) of a specific cell at `grid[row][col]`, use the following indices:
- Left: `grid[row][col - 1]`
- Right: `grid[row][col + 1]`
- Top: `grid[row - 1][col]`
- Bottom: `grid[row + 1][col]`

Boundary conditions should be checked to avoid accessing elements outside the grid.

## Conditional Logic
### Determining Cell Contribution to the Perimeter
A cell contributes to the island's perimeter if it is a land cell (`1`) and it is adjacent to a water cell (`0`) or is at the boundary of the grid. Use conditional statements to determine if a cell contributes to the perimeter:
```python
if grid[row][col] == 1:
    # Check all four directions
    if row == 0 or grid[row - 1][col] == 0:  # Top
        perimeter += 1
    if row == len(grid) - 1 or grid[row + 1][col] == 0:  # Bottom
        perimeter += 1
    if col == 0 or grid[row][col - 1] == 0:  # Left
        perimeter += 1
    if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:  # Right
        perimeter += 1
```

## Counting Techniques
### Counting Edges Contributing to the Perimeter
Initialize a perimeter counter to zero and increment it based on the conditions checked for each land cell. This way, you can count all the edges that contribute to the island's perimeter.

## Problem-Solving Strategies
### Breaking Down the Problem
1. **Identify Land Cells:** Iterate through the grid to find cells with a value of `1`.
2. **Calculate Contribution to Perimeter:** For each land cell, check its adjacent cells to determine how many edges contribute to the perimeter.
3. **Sum Up Contributions:** Accumulate the contributions to get the total perimeter.

## Python Programming
### Nested Loops for Iterating Over Grid Cells
Use nested loops to iterate through each cell in the grid:
```python
for row in range(len(grid)):
    for col in range(len(grid[row])):
        # Process each cell
```

### Conditional Statements to Check Adjacent Cells
Use conditional statements to ensure you only access valid cells within the grid boundaries:
```python
if row > 0 and grid[row - 1][col] == 0:  # Check top cell
    perimeter += 1
if row < len(grid) - 1 and grid[row + 1][col] == 0:  # Check bottom cell
    perimeter += 1
if col > 0 and grid[row][col - 1] == 0:  # Check left cell
    perimeter += 1
if col < len(grid[row]) - 1 and grid[row][col + 1] == 0:  # Check right cell
    perimeter += 1
```

## Complete Python Code Example
Here is a complete example of the island perimeter calculation:
```python
def island_perimeter(grid):
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:  # Top
                    perimeter += 1
                if row == len(grid) - 1 or grid[row + 1][col] == 0:  # Bottom
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:  # Left
                    perimeter += 1
                if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:  # Right
                    perimeter += 1
    return perimeter

# Example usage:
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
print(island_perimeter(grid))  # Output: 16
```

## Resources:
1. Python Official Documentation: [Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)
2. Python Multi-dimensional Arrays: [Python Lists](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/)
3. TutorialsPoint: [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)
