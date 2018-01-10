# Python Programming: More Objects and Classes

## Purpose
* Become more familiar with classes and objects
  - `self` versus `cls`
  - when to reference `self`
  - `__init__`
* Learn the magic methods
  - `__str__`
  - `__repr__`
  - `__del__`
* Learn and implement class attributes
  - How to initialize them
  - How to reassign them inside and outside of the `class`
* Learn and implement `staticmethods` and `classmethods`
* Learn about `eval()`

## Files
| File Name | File Description |
| --------- | ---------------- |
| 0-rectangle.py | Defines an empty class `Rectangle` that defines a rectangle |
| 1-rectangle.py | Builds off `0-rectangle.py` to include setters and getters for `width` and `height` |
| 2-rectangle.py | Builds off `1-rectangle.py` to include `area` and `perimeter` |
| 3-rectangle.py | Builds off `2-rectangle.py` to include an \"informal\" string representation of the rectangle using `#` in `__str__` |
| 4-rectangle.py | Builds off `3-rectangle.py` to include a \"formal\" string representation of the rectangle in (i.e. `Rectangle(2, 4)`  `__repr__` |
| 5-rectangle.py | Builds off `4-rectangle.py` to include a message when an instance of `Rectangle` is deleted in `__del__` |
| 6-rectangle.py | Builds off `5-rectangle.py` to include a public class attribute that keeps track of how many Rectangles there are (using `__init__` and `__del__`) |
| 7-rectangle.py | Builds off `6-rectangle.py` to include a public class attribute that stores the representation of the square as a symbol |
| 8-rectangle.py | Builds off `7-rectangle.py` to include a `@staticmethod` for comparing rectangles |
| 9-rectangle.py | Builds off `8-rectangle.py` to include a `@classmethod` for making a square |
