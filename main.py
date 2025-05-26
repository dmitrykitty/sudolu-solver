import sys
import argparse
from timeit import default_timer as timer

from src.model.grid import SudokuGrid
from src.solvers.naive_solver import NaiveSudokuSolver

def parse_args():
    p = argparse.ArgumentParser(prog="sudoku")
    p.add_argument("puzzle_file", help="Ścieżka do pliku z sudoku (wiersze jako CSV)")
    p.add_argument(
        "-t", "--timeout",
        type=float,
        default=5.0,
        help="Limit czasu (w sekundach)"
    )
    return p.parse_args()

def load_puzzle(path: str) -> SudokuGrid:
    with open(path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    return SudokuGrid.from_text(lines)

def main():
    args = parse_args()

    try:
        puzzle = load_puzzle(args.puzzle_file)
    except Exception as e:
        print(f"error: nie udało się wczytać puzzle: {e}", file=sys.stderr)
        sys.exit(1)

    solver = NaiveSudokuSolver()
    try:
        solution = solver.solve(puzzle, args.timeout)
    except TimeoutError:
        print("timeout")
        sys.exit(1)

    if solution is None:
        print("no solution")
        sys.exit(1)

    # wbudowane __str__ da ASCII-art
    print(solution)

if __name__ == "__main__":
    main()