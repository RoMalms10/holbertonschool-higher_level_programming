# Python Programming: Everything is an object

## Purpose
* Learn about Immutable Objects
  - `int`, `float`, `decimal`, `complex`, `bool`, `string`, `tuple`, `range`, `frozenset`, and `byte`
* Learn about Mutable objects
  - `list`, `set`, `dict`, `bytearray`, and user defined `class`
* Learn how Python interacts with differently with each
  - The `+` operator calls `__add__`
  - The `+=` operator call `__iadd__`

## Files

| File Name | File Description |
| --------- | ---------------- |
| 0-answer.txt | The function to print out the type of an object |
| 1-answer.txt | The function to get the variable identifier |
| 2-answer.txt | Do `a` and `b` point to the same object? `a = 89` `b = 100` |
| 3-answer.txt | Do `a` and `b` point to the same object? `a = 89` `b = 89` |
| 4-answer.txt | Do `a` and `b` point to the same object? `a = 89` `b = a` |
| 5-answer.txt | Do `a` and `b` point to the same object? `a = 89` ` b = a + 1` |
| 6-answer.txt | What does this print? `s1 = "Holberton"` `s2 = s1` `print(s1 == s2)` |
| 7-answer.txt | What does this print? `s1 = "Holberton"` `s2 = s1` `print(s1 is s2)` |
| 8-answer.txt | What does this print? `s1 = "Holberton"` `s2 = "Holberton"` `print(s1 == s2)` |
| 9-answer.txt | What does this print? `s1 = "Holberton"` `s2 = s1` `print(s1 is s2)` |
| 10-answer.txt | What does this print? `l1 = [1, 2, 3]` `l2 = [1, 2, 3]` `print(l1 == l2)` |
| 11-answer.txt | What does this print? `l1 = [1, 2, 3]` `l2 = [1, 2, 3]` `print(l1 is l2)` |
| 12-answer.txt | What does this print? `l1 = [1, 2, 3]` `l2 = l1` `print(l1 == l2)` |
| 13-answer.txt | What does this print? `l1 = [1, 2, 3]` `l2 = l1` `print(l1 is l2)` |
| 14-answer.txt | What does this print? `l1 = [1, 2, 3]` `l2 = l1` `l1.append(4)` `print(l2)` |
| 15-answer.txt | What does this print? `l1 = [1, 2, 3]` `l2 = l1` `l1 = l1 +[4]` `print(l2)` |
| 16-answer.txt | What does this print? `def increment(n): n += 1` `a = 1` `increment(a)` `print(a)` |
| 17-answer.txt | What does this print? `def increment(n): n.append(4)` `l = [1, 2, 3]` `increment(l)` `print(l)` |
| 18-answer.txt | What does this print? `def assign_value(n, v): n = v` `l1 = [1, 2, 3]` `l2 = [4, 5, 6]` `increment(l1, l2)` `print(l1)` |
| 19-copy_list.py | Function that returns the copy of a list |
| 20-answer.txt | Is `a` a tuple? `a = ()` |
| 21-answer.txt | Is `a` a tuple? `a = (1, 2)` |
| 22-answer.txt | Is `a` a tuple? `a = (1)` |
| 23-answer.txt | Is `a` a tuple? `a = (1, )` |
| 24-answer.txt | What does this print? `a = (1)` `b = (1)` `a is b` |
| 25-answer.txt | What does this print? `a = (1, 2)` `b = (1, 2)` `a is b` |
| 26-answer.txt | What does this print? `a = ()` `b = ()` `a is b` |
| 27-answer.txt | Will the id be the same? `id(a)` `a = [1, 2, 3, 4]` `a = a + 5` `id(a)` |
| 28-answer.txt | Will the id be the same? `a = [1, 2, 3]` `id(a)` `a += [4]` `id(a)` |

## Extra
<a href="https://medium.com/@romalms10/whats-a-python-object-fed55e83a3fc">Blog Post</a> about Immutable and Mutable objects in Python
