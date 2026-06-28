# Python - Abstract Classes and Interfaces

A project covering **Abstract Classes**, **Interfaces**, and **Duck Typing** in Python as part of the Holberton School Higher Level Programming curriculum.

---

## Description

This project explores how to define and use abstract classes and interfaces in Python using the `abc` module. You will learn how to enforce method implementation in subclasses, apply duck typing, use mixins, and work with multiple inheritance.

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

1. Define abstract base classes using the `abc` module.
2. Force subclasses to implement specific methods using `@abstractmethod`.
3. Apply duck typing to work with objects based on behavior, not type.
4. Use mixins to add reusable functionality across multiple classes.
5. Explore multiple inheritance and method resolution order (MRO).

---

## Tasks

### 0. Abstract Animal Class and its Subclasses
Create an abstract class `Animal` with an abstract method `sound()`. Implement two subclasses `Dog` and `Cat` that override the method.
- **File:** `task_00_abc.py`

### 1. Shapes, Interfaces, and Duck Typing
Create an abstract class `Shape` with abstract methods `area()` and `perimeter()`. Implement `Circle` and `Rectangle` subclasses. Write a function `shape_info()` that uses duck typing.
- **File:** `task_01_duck_typing.py`

### 2. Extending the Python List with Notifications
Create a class `VerboseList` that inherits from `list` and prints a notification message every time an item is added or removed.
- **File:** `task_02_verboselist.py`

### 3. CountedIterator - Keeping Track of Iteration
Create a class `CountedIterator` that extends the built-in iterator and keeps track of how many items have been iterated over.
- **File:** `task_03_countediterator.py`

### 4. The Enigmatic FlyingFish - Exploring Multiple Inheritance
Create a `FlyingFish` class that inherits from both `Fish` and `Bird`. Override methods to demonstrate multiple inheritance and explore the MRO.
- **File:** `task_04_flyingfish.py`

### 5. The Mystical Dragon - Mastering Mixins
Create two mixin classes `SwimMixin` and `FlyMixin`, then create a `Dragon` class that inherits from both mixins to demonstrate the power of mixins.
- **File:** `task_05_dragon.py`

---

## Examples

**Abstract Animal:**
```python
from task_00_abc import Dog, Cat

dog = Dog()
cat = Cat()
print(dog.sound())  # Bark
print(cat.sound())  # Meow
```

**Duck Typing:**
```python
from task_01_duck_typing import Circle, Rectangle, shape_info

c = Circle(5)
r = Rectangle(4, 6)
shape_info(c)
shape_info(r)
```

**VerboseList:**
```python
from task_02_verboselist import VerboseList

vl = VerboseList([1, 2, 3])
vl.append(4)        # Added [4] to the list.
vl.remove(2)        # Removed [2] from the list.
```

**CountedIterator:**
```python
from task_03_countediterator import CountedIterator

data = [1, 2, 3, 4]
counted = CountedIterator(data)
for item in counted:
    print(item, "- count:", counted.get_count())
```

**FlyingFish:**
```python
from task_04_flyingfish import FlyingFish

ff = FlyingFish()
ff.swim()   # The flying fish is swimming!
ff.fly()    # The flying fish is soaring!
```

**Dragon:**
```python
from task_05_dragon import Dragon

d = Dragon()
d.swim()    # The dragon is swimming!
d.fly()     # The dragon is flying!
d.roar()    # The dragon is roaring!
```

---

## Files

| File | Description |
|------|-------------|
| `task_00_abc.py` | Abstract `Animal` class with `Dog` and `Cat` subclasses |
| `task_01_duck_typing.py` | Abstract `Shape` class with `Circle` and `Rectangle` |
| `task_02_verboselist.py` | `VerboseList` class extending Python list |
| `task_03_countediterator.py` | `CountedIterator` class tracking iteration count |
| `task_04_flyingfish.py` | `FlyingFish` class using multiple inheritance |
| `task_05_dragon.py` | `Dragon` class using `SwimMixin` and `FlyMixin` |

---

## Learning Objectives

- What is an abstract class and how to define one using the `abc` module
- What is the `@abstractmethod` decorator and how to use it
- What is duck typing and how it applies in Python
- How to extend built-in classes like `list` and iterators
- How to use multiple inheritance and understand MRO
- What are mixins and how to use them for reusable functionality

---

## Author

**Rahaf Alabdalh**
