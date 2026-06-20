# Python - More Classes and Objects

## Description

This project is part of the Holberton / ALX Higher-Level Programming
curriculum. It covers more advanced Object-Oriented Programming concepts
in Python, building on the basics of classes and objects.

In this project, we focus on:

- Building a complete `Rectangle` class step by step
- Using private/protected attributes with getters and setters
- Implementing special (dunder) methods: `__init__`, `__str__`, `__repr__`, `__del__`
- Tracking instances with class attributes
- Using static methods and class inheritance (`Square` inherits from `Rectangle`)

The main goal of this project is to understand how Python classes work
internally and how to design clean, well-encapsulated objects.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<username>/holbertonschool-higher_level_programming.git
   ```
2. Move into the project directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-more_classes
   ```
3. Make the files executable:
   ```bash
   chmod +x *.py
   ```
4. Run any file using:
   ```bash
   ./0-rectangle.py
   ```

## Requirements

- Ubuntu 20.04 LTS
- Python 3 (version 3.8.5)
- `pycodestyle` (version 2.8.*)
- All files must start with `#!/usr/bin/python3`
- All files must be executable
- All modules, classes, and functions must have documentation (docstrings)

## Examples

```python
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)
```

## Testing

You can test each class by creating a `*-main.py` file (e.g. `0-main.py`)
and running it with `python3`. Do not include the main test files in the
final repository submission unless specified.

## Files

| File | Description |
|------|--------------|
| `0-rectangle.py` | Empty `Rectangle` class |
| `1-rectangle.py` | `Rectangle` class with private width/height, getters and setters |
| `2-rectangle.py` | Adds `area()` and `perimeter()` methods |
| `3-rectangle.py` | Adds `__str__` method |
| `4-rectangle.py` | Adds `__repr__` method |
| `5-rectangle.py` | Adds `__del__` method |
| `6-rectangle.py` | Adds `number_of_instances` class attribute |
| `7-rectangle.py` | Adds `print_symbol` class attribute |
| `8-rectangle.py` | Adds `bigger_or_equal` static method |
| `9-rectangle.py` | Adds `Square` class that inherits from `Rectangle` |
| `10-rectangle.py` | Improves `Square` with `size` getter/setter and `__str__` |
| `101-nqueens.py` | Solves the N queens puzzle (Advanced) |

## Authors
Rahaf alabdalh — Holberton School student
