import random
class SudokuSolver:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]

    def print_grid(self):
        for row in self.grid:
            print(row)

    def is_safe(self, row, col, num):
        # Check if the number is not repeated in the row
        if num in self.grid[row]:
            return False

        # Check if the number is not repeated in the column
        if num in [self.grid[i][col] for i in range(9)]:
            return False

        # Check if the number is not repeated in the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True  # Sudoku solved successfully
        row, col = empty_cell

        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.grid[row][col] = num
                if self.solve():
                    return True
                self.grid[row][col] = 0  # Backtrack
        return False

    def find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None

    def generate_puzzle(self,difficulty):
            # Fill random places of the puzzle while ensuring solvability
        for _ in range(random.randint(17*difficulty, 24*difficulty)):  # Number of filled cells
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
            if self.is_safe(row, col, num):
                self.grid[row][col] = num
            else:
                self.grid[row][col] = 0

    def print_consistency(self):
        # Check consistency between pairs in the same row
        print("Row Consistency:")
        for row in self.grid:
            print(" ".join("False" if row.count(cell) > 1 else "True" for cell in row))

        # Check consistency between pairs in the same column
        print("\nColumn Consistency:")
        for col in range(9):
            column_values = [self.grid[row][col] for row in range(9)]
            print(" ".join(["False" if column_values.count(cell) > 1 else "True" for cell in column_values]))

        # Check consistency between pairs in the same 3x3 grid
        print("\nGrid Consistency:")
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grid_values = [self.grid[r][c] for r in range(i, i + 3) for c in range(j, j + 3)]
                print(" ".join(["False" if grid_values.count(cell) > 1 else "True" for cell in grid_values]))
        
        # Check domain of each cell
        print("\nDomain of each cell:")
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    domain = set(range(1, 10))
                    domain -= set(self.grid[i])  # Remove row elements
                    domain -= set(self.grid[r][j] for r in range(9))
                    start_row, start_col = 3 * (i // 3), 3 * (j // 3)
                    domain -= set(self.grid[r][c] for r in range(start_row, start_row + 3) for c in range(start_col, start_col + 3))
                    print(f"({i}, {j}): {domain}")
