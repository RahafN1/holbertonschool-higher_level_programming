# Python - Everything is Object

## Description
This project explores how Python handles objects, references, and variables under the hood. In Python, everything is an object — including integers, strings, lists, functions, and classes.

In this project, we focus on:
- Understanding the difference between an object and an instance
- Understanding mutable vs immutable types
- Understanding references, aliases, and assignments
- Understanding how variable identity (`id()`) and equality (`==`) differ
- Understanding how Python passes variables to functions

The main goal of this project is to deeply understand how Python manages objects in memory, so that unexpected behaviors (like two variables unintentionally pointing to the same object) become predictable and explainable.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/<your-username>/holbertonschool-higher_level_programming.git
   ```
2. Move into the project directory:
   ```
   cd holbertonschool-higher_level_programming/python-everything_is_object
   ```
3. Run any script using:
   ```
   ./0-answer.txt
   ```
   or view the answer files directly (they contain one-line answers, not executable code).

## Requirements
- Ubuntu 20.04 LTS
- python3 (version 3.8.5)
- pycodestyle (version 2.7.*)
- All Python files start with `#!/usr/bin/python3`
- All files end with a new line
- All files must be executable
- A `README.md` file at the root of the project is mandatory
- Answer (`.txt`) files contain only one line, with no shebang, and no leading/trailing spaces

## Examples
```python
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
```

```python
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
```

## Testing
You can test your understanding by opening the Python interpreter (`python3`) and experimenting with variables, `id()`, `is`, and `==` — but only **after** reading the documentation and reasoning through the answers on your own.

## Files
| Task | File | Description |
| --- | --- | --- |
| 0 | `0-answer.txt` | Who am I? — function used to print the type of an object |
| 1 | `1-answer.txt` | Where are you? — function used to print the identifier of an object |
| 2 | `2-answer.txt` | Right count — result of a reference count question |
| 3 | `3-answer.txt` | Right count = — result after an assignment |
| 4 | `4-answer.txt` | Right count = — result after a second assignment |
| 5 | `5-answer.txt` | Right count =+ — result after an augmented assignment |
| 6 | `6-answer.txt` | Is equal — whether two variables are equal |
| 7 | `7-answer.txt` | Is the same — whether two variables are the same object |
| 8 | `8-answer.txt` | Is really equal — whether two variables are really equal |
| 9 | `9-answer.txt` | Is really the same — whether two variables are really the same object |
| 10 | `10-answer.txt` | And with a list, is it equal |
| 11 | `11-answer.txt` | And with a list, is it the same |
| 12 | `12-answer.txt` | And with a list, is it really equal |
| 13 | `13-answer.txt` | And with a list, is it really the same |
| 14 | `14-answer.txt` | List append |
| 15 | `15-answer.txt` | List add |
| 16 | `16-answer.txt` | Integer incrementation |
| 17 | `17-answer.txt` | List incrementation |
| 18 | `18-answer.txt` | List assignation |
| 19 | `19-copy_list.py` | Copy a list object |
| 20 | `20-answer.txt` | Tuple or not? |
| 21 | `21-answer.txt` | Tuple or not? |
| 22 | `22-answer.txt` | Tuple or not? |
| 23 | `23-answer.txt` | Tuple or not? |
| 24 | `24-answer.txt` | Who I am? |
| 25 | `25-answer.txt` | Tuple or not |
| 26 | `26-answer.txt` | Empty is not empty |
| 27 | `27-answer.txt` | Still the same? |
| 28 | `28-answer.txt` | Same or not? |
| 29 | `100-python_is_object.py` | Python3: Mutable, Immutable... everything is object! |
| 30 (Advanced) | `101-*` | #pythonic |
| 31 (Advanced) | `102-*` | Low memory cost |
| 32 (Advanced) | `103-*` | int 1/3 |
| 33 (Advanced) | `104-*` | int 2/3 |
| 34 (Advanced) | `105-*` | int 3/3 |
| 35 (Advanced) | `106-*` | Clear strings |

## Authors
Rahaf Alabdalh 
