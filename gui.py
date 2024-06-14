import tkinter as tk
from tkinter import messagebox
from Sudoku_game import *


class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.entries = [[None for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.frame, width=2, font=('Arial', 18, 'bold'), justify='center')
                entry.grid(row=i, column=j)
                self.entries[i][j] = entry
                # Add thick black lines between each 3x3 grid
                if j == 2 or j == 5:
                    entry.grid(padx=(0, 7))
                if i == 2 or i == 5:
                    entry.grid(pady=(0, 7))
                    
        self.generate_button = tk.Button(self.master, text="Generate Puzzle", command=self.generate_puzzle)
        self.generate_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.solve_button = tk.Button(self.master, text="Solve Puzzle", command=self.solve_puzzle)
        self.solve_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.consistency_button = tk.Button(self.master, text="Check Consistency", command=self.check_consistency)
        self.consistency_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create difficulty of puzzle
        self.difficulty = tk.IntVar()
        self.difficulty.set(1)
        self.difficulty_label = tk.Label(self.master, text="Difficulty:")
        self.difficulty_label.pack(side=tk.LEFT, padx=5, pady=5)
        self.easy_radio = tk.Radiobutton(self.master, text="Easy", variable=self.difficulty, value=3)
        self.easy_radio.pack(side=tk.LEFT, padx=5, pady=5)
        self.medium_radio = tk.Radiobutton(self.master, text="Medium", variable=self.difficulty, value=2)
        self.medium_radio.pack(side=tk.LEFT, padx=5, pady=5)
        self.hard_radio = tk.Radiobutton(self.master, text="Hard", variable=self.difficulty, value=1)
        self.hard_radio.pack(side=tk.LEFT, padx=5, pady=5)


        self.solver = SudokuSolver()

    def generate_puzzle(self):
        self.solver.generate_puzzle(self.difficulty.get())
        self.update_entries()

    def update_entries(self):
        for i in range(9):
            for j in range(9):
                value = self.solver.grid[i][j]
                if value != 0:
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(value))
                else:
                    self.entries[i][j].delete(0, tk.END)

    def get_input_grid(self):
        input_grid = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                if value.isdigit():
                    input_grid[i][j] = int(value)
                else:
                    input_grid[i][j] = 0
        return input_grid

    def solve_puzzle(self):
        input_grid = self.get_input_grid()
        self.solver.grid = input_grid
        if self.solver.solve():
            self.update_entries()
        else:
            messagebox.showerror("Error", "No solution exists for the given puzzle.")

    def check_consistency(self):
        input_grid = self.get_input_grid()
        self.solver.grid = input_grid
        self.solver.print_consistency()

def main():
    root = tk.Tk()
    sudoku_gui = SudokuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()