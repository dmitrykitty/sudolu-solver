# Sudoku Solver 101

This project aims to produce a solver for the general [sudoku puzzle](https://en.wikipedia.org/wiki/Sudoku). The general variant is basically the sudoku with no specific size. Classically, the sudoku uses `9`x`9` grid, but in general it can any size divisible into equal blocks, e.g., `4`x`4`, `16`x`16`, `25`x`25`, etc.

You will also learn how to use `uv` to maintain an application project.

## TODO: 

There are several tasks to complete:
- [ ] install [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [ ] initialize project using uv:
    - check `uv init --help`
    - use following options:
      - project name: `sudolver`
      - project description: `A sudoku solver.`
      - do not create the `README`
      - it should be an `app` project
      - it should not be a package
      - use python: `3.13`
      - make `uv` install the python for you — python preference should be `only-managed`
- [ ] add dependencies:
    - check `uv add --help`
    - add following packages:
        - `numpy`
        - `mypy` (only to the `development` dependency group)
        - `ruff` (only to the `development` dependency group)
        - `pytest-mock` (only to the `development` dependency group)
- [ ] run your `main.py` with `uv run`, it will:
    - install the python 3.13
    - create a `venv` in `.venv` 
    - install required packages 
    - later you can still use `uv run` or just activate the `.venv` via `source .venv/bin/activate` and use `python`
- [ ] add missing code in `src/model/grid.py` according to the `#TODO` comments
- [ ] add missing code in `src/solvers/naive_solver.py` according to the `#TODO` comments
- [ ] modify the `main.py` file, so:
    - [ ] it parses arguments as in the output of `python main.py --help`:

    ```
    usage: python main.py -t <timeout> <path_to_puzzle>

    Sudolver - yet another sudoku solver.

    positional arguments:
    puzzle_path           path to the file containing a sudoku puzzle

    options:
    -h, --help            show this help message and exit
    --time-limit, -t TIME_LIMIT
                            time limit for the solver (in seconds)
    ```

    - [ ] it solves the given puzzle using a naive solver from `src/solvers/naive_solver.py`:
      - [ ] if solver finds a solution, print the solution
      - [ ] if solver times out, print `TIMEOUT` and exit with code `2` — use [`sys.exit` ](https://docs.python.org/3/library/sys.html#sys.exit)
      - [ ] if solver does not find a solution, print `INFEASIBLE` and exit with code `1`
- [ ] keep your code tidy by running `ruff format` and `ruff check` or using vs code `ruff` extension
    - bobot won't give points if your file is not well formatted 

Extra materials:
- [uv usage guide](https://docs.astral.sh/uv/guides/projects/) 
- [numpy documentation](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [how to solve sudoku via backtracking](https://www.geeksforgeeks.org/sudoku-backtracking-7/)

## Grading

* [ ] Make sure, you have a **private** group
  * [how to create a group](https://docs.gitlab.com/ee/user/group/#create-a-group)
* [ ] Fork this project into your private group
  * [how to create a fork](https://docs.gitlab.com/ee/user/project/repository/forking_workflow.html#creating-a-fork)
* [ ] Add @bobot-is-a-bot as the new project's member (role: **maintainer**)
  * [how to add an user](https://docs.gitlab.com/ee/user/project/members/index.html#add-a-user)

## How To Submit Solutions

* [ ] Clone repository: git clone:
    ```bash
    git clone <repository url>
    ```
* [ ] Solve the exercises
    * use WebIDE, whatever
* [ ] Commit your changes
    ```bash
    git add <path to the changed files>
    git commit -m <commit message>
    ```
* [ ] Push changes to the gitlab master branch
    ```bash
    git push 
    ```

The rest will be taken care of automatically. You can check the `GRADE.md` file for your grade / test results. Be aware that it may take some time (up to one hour) till this file appears.


## Project Structure

    .
    ├── puzzles                     # contains puzzles of various sizes
    ├── src                         # source directory
    │   ├── model                   # - directory with the problem model 
    │   │   └── grid.py             # TODO: representation of the sudoku grid
    │   └── solvers                 # - directory with the sudoku solvers
    │       └── naive_solver.py     # TODO: a naive sudoku solver
    ├── main.py                     # TODO: create this file with `uv init`
    ├── pyproject.toml              # TODO: create this file with `uv init`
    └── README.md                   # the README you are reading now
    