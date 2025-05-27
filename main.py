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

def load_puzzle(path: str):
    with open(path, 'r') as f:
        raw_lines = [line.strip() for line in f if line.strip()]
    grid = SudokuGrid.from_text(raw_lines)
    return grid, raw_lines

def main():
    args = parse_args()

    try:
        puzzle, raw_lines = load_puzzle(args.puzzle_file)
    except Exception as e:
        print(f"error: nie udało się wczytać puzzle: {e}", file=sys.stderr)
        sys.exit(1)

    solver = NaiveSudokuSolver()
    try:
        solution = solver.solve(puzzle, args.timeout)
    except TimeoutError:
        # wymagana dokładnie ta fraza i exit code 2
        print("TIMEOUT")
        sys.exit(2)

    if solution is None:
        puzzle_str = "".join(raw_lines)
        # używamy tabulatorów przed i po myślniku, żeby CI je złapało
        print(f"INFEASIBLE\t-\tpuzzle grid:{puzzle_str}")
        sys.exit(1)

    # w pozostałych przypadkach po prostu drukujemy rozwiązanie
    print(solution)

if __name__ == "__main__":
    main()