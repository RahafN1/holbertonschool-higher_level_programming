# Python - Serialization

## Description
This project covers the concept of serialization and deserialization in Python — the process of converting Python objects into a format that can be stored or transmitted (such as JSON, Pickle, CSV, or XML), and rebuilding those objects back from that format without losing information.

In this project, we focus on:
- Basic serialization and deserialization using the `json` module
- Pickling and unpickling custom Python classes with the `pickle` module
- Converting CSV data into JSON format
- Serializing and deserializing Python objects using XML

The main goal of this project is to understand the different serialization formats available in Python, when to use each one, and how to safely convert data between them.

## Installation
1. Clone the repository:
   `git clone https://github.com/RahafN1/holbertonschool-higher_level_programming.git`
2. Move into the project directory:
   `cd holbertonschool-higher_level_programming/python-serialization`
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
serialize_and_save_to_file = __import__('0-basic_serialization').serialize_and_save_to_file

my_dict = {
    'name': "John",
    'age': 27,
    'city': "San Francisco"
}
serialize_and_save_to_file(my_dict, "data.json")
```

```python
#!/usr/bin/python3
import pickle
Student = __import__('1-pickle_defined_class').Student

student = Student("John", 25, "Computer Science")

with open("student.pkl", "wb") as file:
    pickle.dump(student, file)
```

## Testing
You can test each function by creating a `X-main.py` file and running it with `./X-main.py`. Do not include the main test files in the repository.

## Files

| File | Description |
| --- | --- |
| `0-basic_serialization.py` | Serializes a Python dictionary to a JSON file and deserializes it back |
| `1-pickle_defined_class.py` | Defines a `Student` class and pickles/unpickles instances of it |
| `2-csv_to_json.py` | Converts data from a CSV file to a JSON file |
| `3-xml_serialization.py` | Serializes and deserializes a Python dictionary using XML |

## Author
Rahaf Alabdalh
