# Python - Test-driven development

## Holberton School - Higher Level Programming

This project introduces test-driven development (TDD) in Python, using doctests and unittest to write and validate functions before/while implementing them.

## Requirements
- Ubuntu 20.04 LTS, Python 3 (version 3.4.3)
- All files end with a new line
- First line of all files: `#!/usr/bin/python3`
- Code follows pycodestyle (version 2.7.*)
- All files must be executable
- All modules and functions must have documentation
- All functions and modules tested with unittests/doctests

## Tasks

### 0. Integers addition
File: `0-add_integer.py`, `tests/0-add_integer.txt`
Adds two integers (or floats cast to int), raises `TypeError` with specific messages for invalid types.

### 1. Divide a matrix
File: `matrix_divided.py`, `tests/matrix_divided.txt`
Divides all elements of a matrix, with validation for matrix shape, element types, and division by zero.

### 2. Say my name
File: `say_my_name.py`, `tests/say_my_name.txt`
Prints "My name is <first name> <last name>", validating that names are strings.

### 3. Print square
File: `print_square.py`, `tests/print_square.txt`
Prints a square with the character `#`, validating size as a positive integer.

### 4. Text indentation
File: `text_indentation.py`, `tests/text_indentation.txt`
Prints text with 2 new lines after each `.`, `?`, and `:` characters.

### 5. Max integer - Unittest
File: `max_integer.py`, `tests/test_max_integer.py`
Finds the biggest integer in a list, tested using `unittest`.

### 6. Matrix multiplication (Advanced)
File: `matrix_mul.py`, `tests/matrix_mul.txt`
Multiplies two matrices, with full validation of dimensions and types.

### 7. Lazy matrix multiplication (Advanced)
File: `lazy_matrix_mul.py`
Multiplies two matrices using `numpy`.

## Author
Rahaf Alabdalh
