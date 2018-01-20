# Python Programming: Inheritance

## Purpose
* Why use Inheritance
* Learn and implement Inheritance
* Learn what a `subclass` is
* Learn what a `superclass` is
* How instance `attribute`s are accessed using Inheritance
* How to override a `method` or `attribute` inherited from the base class
* How to define a `class` with multiple base classes

## Files

| File Name | File Description |
| --------- | ---------------- |
| 0-lookup.py | Function that returns the list of available attributes and methods of an object |
| 1-my\_list.py | Defines a `class` MyList that inherits from `list` |
| 2-is\_same\_class.py | Function that returns `True` if an object is exactly an instance of a specified `class` ; otherwise `False` |
| 3-is\_kind\_of\_class.py | Function that returns `True` if an object is an instance of, or if the object is an instance of a `class` that inherited from, a specified `class` ; otherwise `False` |
| 4-inherits\_from.py | Function that returns `True` if the object is an instance of a `class` that inherited (directly or indirectly) from the specified `class` ; otherwise `False`
| 5-base\_geometry.py | Defines an empty class `BaseGeometry` |
| 6-base\_geometry.py | Builds off `5-base_geometry.py` to include a public instance method `area` |
| 7-base\_geometry.py | Builds off `6-base_geometry.py` to include `integer_validator` |
| 8-rectangle.py | Defines a class `Rectangle` that inherits from `BaseGeometry` and includes `width` and `height` |
| 9-rectangle.py | Builds off `8-rectangle.py` to include a more defined `area` and `__str__` |
| 10-square.py | Defines a class `Square` that inherits from `Rectangle` |
| 11-square.py | Builds off `10-square.py` to include `__str__` for Squares |
| 100-my\_int.py | Defines a class `MyInt` that inherits from `int` and inverts `==` and `!=` operators |
| tests/1-my\_list.txt | Tests for `1-my_list.py` |
| tests/7-base\_geometry.txt | Tests for `7-base_geometry.py` |

## Directories

| Directory Name | Directory Description |
| -------------- | --------------------- |
| tests/ | Contains doctest files for certain files |
