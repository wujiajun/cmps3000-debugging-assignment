# CMPS-3000 Debugging Assignment

Group 3 code for Assignment 3: Error Identification, Testing and Debugging (CMPS-3000-BSA, SAIT).

In this assignment we find and fix errors in a small Python program, track each bug on a Trello board, write tests for the fixed code, and show how we traced one of the bugs.

## About the Program

The program is a small order management system. An `Order` has a customer name and a list of items. Each item is a tuple: `(item_name, quantity, price)`.

An order can:

- calculate the total price (`calculate_total`)
- add an item (`add_item`)
- remove an item by name (`remove_item`)
- print a summary (`print_summary`)
- return a discount rate for a discount code (`apply_discount`)

## Project Structure

```
cmps3000-debugging-assignment/
├── pyproject.toml
├── uv.lock
├── README.md
└── src/
    └── cmps3000_debugging_assignment/
        ├── __init__.py
        ├── buggy_code.py          # the original code with the bugs
        └── tests/
            └── test_buggy_code.py # tests (Part B)
```

The original `buggy_code.py` is kept as it is, so the bugs can be reproduced for the Trello cards and screenshots. The fixed version of the code will be added after the bugs are fixed.

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/) to manage the project
- pytest (installed as a development dependency by `uv sync`)

## How to Run

Set up the project. This also installs pytest:

```bash
uv sync
```

Run the original buggy code:

```bash
uv run python src/cmps3000_debugging_assignment/buggy_code.py
```

The original code does not run yet. It has errors that Python reports when it starts. This is expected.

## How to Run the Tests

The tests are in `src/cmps3000_debugging_assignment/tests/`. They are written with pytest (Part B). Run all tests from the project folder:

```bash
uv run pytest -v
```

## Assignment Parts

| Part | Topic |
| --- | --- |
| A | Find at least three bugs (syntax, runtime, logic), fix them, and report each one on Trello |
| B | Write unit tests and an integration test for the fixed code |
| C | Describe the debugging strategy and draw a diagram that shows how we traced one bug |
| D | Individual reflection |

## Links

- Trello board: https://trello.com/b/6ae16a294bad6b2b17ebcc12

## Team

Group 3: Jaylene, Noah, Ian, Jiao, Jason