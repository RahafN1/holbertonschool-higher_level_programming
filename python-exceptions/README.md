# Python - Exceptions

## Holberton School - Higher Level Programming

This project covers exception handling in Python: how to catch, handle, and raise exceptions to write more robust and safe code.

## Requirements
- Ubuntu 20.04 LTS, Python 3 (version 3.4.3)
- All files end with a new line
- First line of all files: `#!/usr/bin/python3`
- Code follows pycodestyle (version 2.7.*)
- All files must be executable
- All modules, classes, and functions must have documentation

## Tasks

### 0. Safe list printing
File: `0-safe_print_list.py`
Prints `x` elements of a list, using `try/except` to handle out-of-range access, and returns the real number of elements printed.

### 1. Safe printing of an integers list
File: `1-safe_print_list_integers.py`
Prints only the integer elements of a list, using `try/except` to skip non-integers.

### 2. Print and count integers
File: `2-safe_print_integer_err.py`
Prints an integer with a message, returns `True` if printed successfully, `False` otherwise.

### 3. Integers division with debug
File: `3-safe_print_division.py`
Divides two integers and prints the result, with a debug message printed in all cases.

### 4. Divide a list
File: `4-list_division.py`
Divides element by element a list by another list, handling division by zero, type errors, and list length differences.

### 5. Raise exception
File: `5-raise_exception_score.py`
Returns `42`, only to demonstrate uncaught exception behavior.

### 6. Raise a message
File: `6-raise_exception_def.py`
Returns a function pointer that raises an Exception with a given message.

### 7. Safe integer print with error message (Advanced)
File: `100-safe_print_integer.py`
Prints an integer with a specified format, returns `True`/`False` depending on success.

### 8. Safe function (Advanced)
File: `101-safe_function.py`
Executes a function safely, returning `[None, error]` if an exception is raised, using `sys.exc_info()`.

### 9. ByteCode -> Python #4 (Advanced)
File: `102-magic_calculation.py`
Reverse-engineers Python bytecode into an equivalent function.

## Author
Rahaf Alabdalh
