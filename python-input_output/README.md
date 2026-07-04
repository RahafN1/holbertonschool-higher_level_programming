# Python - Input/Output

## Description
This project is an implementation of basic and advanced File I/O and JSON handling in Python. It focuses on reading and writing text files, serializing and deserializing Python objects to and from JSON, and manipulating files as part of common real-world tasks.

In this project, we focus on:
- Reading from and writing to text files
- Appending content to existing files
- Converting Python data structures to JSON strings and back
- Saving and loading objects from JSON files
- Working with classes and serializing/deserializing custom objects
- Solving classic problems such as Pascal's Triangle
- Parsing and processing log files

The main goal of this project is to understand how Python handles file operations and how to use the `json` module to persist and exchange data.

## Installation
1. Clone the repository:
   `git clone https://github.com/RahafN1/holbertonschool-higher_level_programming.git`
2. Move into the project directory:
   `cd holbertonschool-higher_level_programming/python-input_output`
3. Make the scripts executable:
   `chmod +x *.py`
4. Run a script directly:
   `./0-main.py`

## Requirements
- Ubuntu 20.04 LTS
- Python 3 (`python3`, version 3.4.3 or higher)
- All files interpreted/compiled on Ubuntu 20.04 LTS using `python3`
- All code follows the `pycodestyle` style (version 2.5.*)
- All files must be executable
- All modules and functions must be documented

## Examples
```python
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")
```

```python
#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

my_list = [1, 2, 3]
filename = "my_list.json"
save_to_json_file(my_list, filename)
```

## Testing
You can test each function by creating a `X-main.py` file and running it with `./X-main.py`. Do not include the main test files in the repository.

## Files

| File | Description |
| --- | --- |
| `0-read_file.py` | Reads a text file (UTF8) and prints it to stdout |
| `1-write_file.py` | Writes a string to a text file (UTF8) and returns the number of characters written |
| `2-append_write.py` | Appends a string at the end of a text file (UTF8) and returns the number of characters added |
| `3-to_json_string.py` | Returns the JSON representation of an object (string) |
| `4-from_json_string.py` | Returns an object (Python data structure) represented by a JSON string |
| `5-save_to_json_file.py` | Writes an Object to a text file, using a JSON representation |
| `6-load_from_json_file.py` | Creates an Object from a JSON file |
| `7-add_item.py` | Adds all arguments to a Python list, and saves them to a file |
| `8-class_to_json.py` | Returns the dictionary description with simple data structure for JSON serialization of an object |
| `9-student.py` | Defines a `Student` class with a `to_json` method |
| `10-student.py` | Updates the `Student` class to allow `to_json` to retrieve only specific attributes |
| `11-student.py` | Updates the `Student` class with a `reload_from_json` method |
| `12-pascal_triangle.py` | Returns a list of lists of integers representing Pascal's Triangle |
| `100-append_after.py` | Inserts a line of text to a file after each line containing a specific string |
| `101-stats.py` | Reads stdin line by line and computes metrics (log parsing) |

## Author
Rahaf Alabdalh
