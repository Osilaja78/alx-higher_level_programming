#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.
"""
import sys


def solve_nqueens(n):
    """
    Solve the N-queens problem and print all possible solutions.

    Args:
        n (int): The size of the chessboard and the number of queens.

    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        """
        Check if it's safe to place a queen at the given position.

        Args:
            board (list): The current state of the chessboard.
            row (int): The row index.
            col (int): The column index.

        Returns:
            bool: True if it's safe to place a queen, False otherwise.

        """
        # Check the row
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check the upper diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check the lower diagonal
        i, j = row, col
        while i < n and j >= 0:
            if board[i][j] == 1:
                return False
            i += 1
            j -= 1

        return True

    def solve(board, col, solutions):
        """
        Recursive function to solve the N-queens problem.

        Args:
            board (list): The current state of the chessboard.
            col (int): The current column index.
            solutions (list): List to store the valid solutions.

        """
        if col >= n:
            solution = []
            for i in range(n):
                row_str = "".join(str(board[i][j]) for j in range(n))
                solution.append(row_str)
            solutions.append(solution)
            return

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                solve(board, col + 1, solutions)
                board[i][col] = 0

    # Create an empty chessboard
    board = [[0] * n for _ in range(n)]
    solutions = []

    # Solve the N-queens problem
    solve(board, 0, solutions)

    # Print the solutions
    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Solve the N-queens problem
    solve_nqueens(N)
