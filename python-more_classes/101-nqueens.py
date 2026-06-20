#!/usr/bin/python3
"""Solves the N queens puzzle using backtracking."""
import sys


def solve_nqueens(n):
    """Find and print all solutions to the N queens puzzle."""
    queens = [-1] * n
    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        if row == n:
            print([[r, queens[r]] for r in range(n)])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            queens[row] = col
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtrack(row + 1)

            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
