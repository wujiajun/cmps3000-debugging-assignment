# CMPS-3000 Debugging Assignment

Group 3 code for Assignment 3: Error Identification, Testing and Debugging (CMPS-3000-BSA, SAIT).

In this assignment we found and fixed errors in a small Python program, tracked each bug on a Trello board, and wrote tests for the fixed code.

## About the Program

The program is a small order management system. An `Order` has a customer name and a list of items. Each item is a tuple: `(item_name, quantity, price)`.

An order can:

- calculate the total price (`calculate_total`)
- add an item (`add_item`)
- remove all items with a given name (`remove_item`)
- print a summary (`print_summary`)
- return a discount rate for a discount code (`apply_discount`)

## Bugs We Fixed

| Bug | Type | Method | Problem | Fix |
| --- | --- | --- | --- | --- |
| #1a | Syntax Error | `add_item()` | Missing colon at the end of the `def` line | Added `:` |
| #1b | Syntax Error | `print_summary()` | Missing closing parenthesis in the last `print` line | Added `)` |
| #2 | Runtime Error | `print_summary()` | `self.itemz` does not exist (AttributeError) | Changed to `self.items` |
| #3 | Logic Error | `calculate_total()` | Quantity and price were added (`+`), so the total was wrong | Changed to `*` |
| #4 | Logic Error | `remove_item()` | Items were removed while looping over the same list, so some items were skipped | Made a new list without the removed items |
| #5 | Logic Error | `calculate_total()` | An empty order returned the text "Empty Order" instead of a number | Removed the check, so the method always returns a number (0 for an empty order) |

Each bug has a card on our Trello board with steps to reproduce, expected and actual results, and screenshots.

The original code with all the bugs is in the first commit: [`1ec6eed`](https://github.com/wujiajun/cmps3000-debugging-assignment/commit/1ec6eedf603ad2bf9239472720ccd71e3b6d67e4).

## Project Structure

```
cmps3000-debugging-assignment/
├── pyproject.toml
├── uv.lock
├── README.md
└── src/
    └── cmps3000_debugging_assignment/
        ├── __init__.py
        ├── buggy_code.py          # the fixed code
        └── tests/
            └── test_buggy_code.py # tests (Part B)
```

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/) to manage the project
- pytest (installed as a development dependency by `uv sync`)

## How to Run

Set up the project. This also installs pytest:

```bash
uv sync
```

Run the program:

```bash
uv run python src/cmps3000_debugging_assignment/buggy_code.py
```

It prints an order summary and a discount rate.

## How to Run the Tests

The tests are in `src/cmps3000_debugging_assignment/tests/`. They are written with pytest. Run all tests from the project folder:

```bash
uv run pytest -v
```

There are 14 tests: 13 unit tests and 1 integration test. All of them pass.

- Unit tests check one method at a time (`add_item`, `remove_item`, `calculate_total`, `print_summary`, `apply_discount`), including edge cases such as an empty order and a name that is not in the order.
- The integration test runs `main()` and checks the printed output, so it uses all the methods together.

## Assignment Parts

| Part | Topic |
| --- | --- |
| A | Find bugs (syntax, runtime, logic), fix them, and report each one on Trello |
| B | Write unit tests and an integration test for the fixed code |
| C | Describe the debugging strategy and draw a diagram that shows how we traced one bug |
| D | Individual reflection |

## Links

- GitHub repository: https://github.com/wujiajun/cmps3000-debugging-assignment
- Trello board: https://trello.com/b/UyzhnbUG/assignment-3

## Team

Group 3: Jaylene, Noah, Ian, Jiao, Jason