# Python - Inheritance

A project covering the concept of **inheritance** in Python as part of the Holberton School Higher Level Programming curriculum.

---

## Description

This project explores one of the fundamental pillars of Object-Oriented Programming (OOP) — **Inheritance**. You will learn how to create class hierarchies, override methods, validate data, and build reusable code using base classes.

---

## Requirements

- Ubuntu 20.04 LTS
- Python 3.8.5
- All files must be executable
- First line of all files: `#!/usr/bin/python3`
- Code must follow `pycodestyle` (version 2.8.*)
- All modules, classes, and functions must have documentation

---

## How It Works

1. Define a base class with shared attributes and methods.
2. Create subclasses that inherit from the base class.
3. Override or extend methods as needed.
4. Use built-in functions like `isinstance`, `issubclass`, `type`, and `super` to inspect class relationships.

---

## Tasks

### 0. Lookup
Write a function that returns the list of available attributes and methods of an object.
- **File:** `0-lookup.py`
- **Prototype:** `def lookup(obj):`

### 1. My list
Write a class `MyList` that inherits from `list` with a method that prints the list sorted.
- **File:** `1-my_list.py`
- **Prototype:** `def print_sorted(self):`

### 2. Exact same object
Write a function that returns `True` if the object is exactly an instance of the specified class.
- **File:** `2-is_same_class.py`
- **Prototype:** `def is_same_class(obj, a_class):`

### 3. Same class or inherit from
Write a function that returns `True` if the object is an instance of, or inherited from, the specified class.
- **File:** `3-is_kind_of_class.py`
- **Prototype:** `def is_kind_of_class(obj, a_class):`

### 4. Only sub class of
Write a function that returns `True` if the object is an instance of a class that inherited from the specified class.
- **File:** `4-inherits_from.py`
- **Prototype:** `def inherits_from(obj, a_class):`

### 5. Geometry module
Write an empty class `BaseGeometry`.
- **File:** `5-base_geometry.py`

### 6. Improve Geometry
Improve `BaseGeometry` by adding a public instance method `area()` that raises an Exception.
- **File:** `6-base_geometry.py`

### 7. Integer validator
Add an `integer_validator` method to `BaseGeometry` that validates integer values.
- **File:** `7-base_geometry.py`
- **Prototype:** `def integer_validator(self, name, value):`

### 8. Rectangle
Write a class `Rectangle` that inherits from `BaseGeometry`.
- **File:** `8-rectangle.py`

### 9. Full rectangle
Improve `Rectangle` by implementing the `area()` method and `__str__` representation.
- **File:** `9-rectangle.py`

### 10. Square #1
Write a class `Square` that inherits from `Rectangle`.
- **File:** `10-square.py`

### 11. Square #2
Improve `Square` by adding a custom `__str__` method.
- **File:** `11-square.py`

### 12. My integer *(Advanced)*
Write a class `MyInt` that inherits from `int` with `==` and `!=` operators inverted.
- **File:** `100-my_int.py`

### 13. Can I? *(Advanced)*
Write a function that adds a new attribute to an object if possible; raises `TypeError` if not.
- **File:** `101-add_attribute.py`
- **Prototype:** `def add_attribute(obj, name, value):`

---

## Examples

**Lookup:**
```python
lookup = __import__('0-lookup').lookup

class MyClass(object):
    my_attr = 3
    def my_meth(self):
        pass

print(lookup(MyClass))
# ['__class__', '__dict__', ..., 'my_attr', 'my_meth']
```

**My list:**
```python
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(3)
my_list.append(1)
my_list.append(2)
my_list.print_sorted()
# [1, 2, 3]
```

**Integer validator:**
```python
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()
bg.integer_validator("my_int", 12)   # OK
bg.integer_validator("age", 0)       # ValueError: age must be greater than 0
```

---

## Files

| File | Description |
|------|-------------|
| `0-lookup.py` | Returns list of attributes and methods of an object |
| `1-my_list.py` | Class `MyList` inheriting from `list` |
| `2-is_same_class.py` | Checks if object is exactly an instance of a class |
| `3-is_kind_of_class.py` | Checks if object is an instance or inherited from a class |
| `4-inherits_from.py` | Checks if object is instance of a subclass only |
| `5-base_geometry.py` | Empty class `BaseGeometry` |
| `6-base_geometry.py` | `BaseGeometry` with `area()` method |
| `7-base_geometry.py` | `BaseGeometry` with `integer_validator` method |
| `8-rectangle.py` | Class `Rectangle` inheriting from `BaseGeometry` |
| `9-rectangle.py` | `Rectangle` with `area()` and `__str__` |
| `10-square.py` | Class `Square` inheriting from `Rectangle` |
| `11-square.py` | `Square` with `__str__` method |
| `100-my_int.py` | Class `MyInt` with inverted `==` and `!=` |
| `101-add_attribute.py` | Adds attribute to object if possible |

---

## Learning Objectives

- What is a superclass, base class, or parent class
- What is a subclass
- How to list all attributes and methods of a class or instance
- How to inherit a class from another
- How to define a class with multiple base classes
- What is the default class every class inherits from
- How to override a method or attribute inherited from a base class
- What are `isinstance`, `issubclass`, `type`, and `super` built-in functions

---

## Author

**Rahaf Alabdalh**
