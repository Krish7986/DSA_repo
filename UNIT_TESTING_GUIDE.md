# Unit Testing Guide - Python

## What is Unit Testing?
A **unit test** is an automated test that checks if a single function or method works correctly. Instead of running code manually and checking output, you write tests that verify:
- ✅ Correct output for valid inputs
- ✅ Correct behavior for edge cases
- ✅ Error handling for invalid inputs

## Why Unit Test?
1. **Find bugs early** - Catch errors before production
2. **Refactor safely** - Change code without breaking it
3. **Documentation** - Tests show how code should behave
4. **Confidence** - Know your code works

---

## Approach 1: unittest (Built-in Python Framework)

### Basic Structure
```python
import unittest

class TestMyFunction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(expected, actual)  # Check equality
    
    def test_case_2(self):
        self.assertTrue(condition)  # Check if True
    
    def test_case_3(self):
        self.assertRaises(ValueError, function, args)  # Check exception

if __name__ == '__main__':
    unittest.main()
```

### Common Assertions
```python
self.assertEqual(a, b)           # a == b
self.assertNotEqual(a, b)        # a != b
self.assertTrue(x)               # x is True
self.assertFalse(x)              # x is False
self.assertIn(a, b)              # a in b
self.assertGreater(a, b)         # a > b
self.assertRaises(Exception, func) # func raises Exception
```

### Example with unittest
```python
import unittest

class Solution:
    def add(self, a, b):
        return a + b

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_positive_numbers(self):
        result = self.solution.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_negative_numbers(self):
        result = self.solution.add(-2, -3)
        self.assertEqual(result, -5)
    
    def test_mixed_numbers(self):
        result = self.solution.add(5, -3)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
```

**Run with:** `python test_file.py`

---

## Approach 2: pytest (Simpler, Popular)

### Basic Structure
```python
def test_case_1():
    assert expected == actual

def test_case_2():
    assert condition

def test_case_3():
    with pytest.raises(ValueError):
        function(args)
```

### Common Assertions
```python
assert a == b              # equality
assert a != b              # not equal
assert x                   # x is True
assert not x               # x is False
assert a in b              # a in b
assert a > b               # a greater than b
```

### Example with pytest
```python
import pytest

class Solution:
    def add(self, a, b):
        return a + b

solution = Solution()

def test_positive_numbers():
    assert solution.add(2, 3) == 5

def test_negative_numbers():
    assert solution.add(-2, -3) == -5

def test_mixed_numbers():
    assert solution.add(5, -3) == 2
```

**Install:** `pip install pytest`
**Run with:** `pytest test_file.py` or `pytest test_file.py -v` (verbose)

---

## Comparison: unittest vs pytest

| Feature | unittest | pytest |
|---------|----------|--------|
| **Setup** | Built-in | Install needed |
| **Class required** | Yes (usually) | No (functions work) |
| **Assertions** | `self.assertEqual()` | `assert` keyword |
| **Simplicity** | More boilerplate | More concise |
| **Learning curve** | Steeper | Gentler |
| **Large projects** | Good | Excellent |

**Recommendation for beginners:** Start with `pytest` (simpler syntax)

---

## Best Practices

### 1. Name Tests Clearly
```python
✅ def test_two_sum_with_valid_input():
❌ def test_1():
```

### 2. Test One Thing Per Test
```python
✅ def test_returns_correct_index():
❌ def test_everything():
```

### 3. Test Edge Cases
```python
# Normal case
test_with_regular_input()

# Edge cases
test_with_empty_input()
test_with_single_element()
test_with_duplicates()
test_with_negative_numbers()
```

### 4. Use Descriptive Assertions
```python
✅ self.assertEqual(result, [1, 2], "Should return indices 1 and 2")
❌ self.assertEqual(result, [1, 2])
```

---

## File Organization
```
project/
├── solution.py          # Your code
├── test_solution.py     # Your tests
└── test_data/           # Test data (optional)
```

**Convention:** Test file name = `test_` + source file name

---

## Running Tests

### pytest
```bash
pytest test_file.py                 # Run all tests
pytest test_file.py -v              # Verbose (show each test)
pytest test_file.py::test_function  # Run specific test
pytest --tb=short                   # Shorter error messages
```

### unittest
```bash
python test_file.py                           # Run all tests
python test_file.py TestClassName.test_name   # Run specific test
python -m unittest -v                         # Verbose mode
```

