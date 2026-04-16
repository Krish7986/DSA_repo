# Unit Testing Quick Reference

## Files Created

### 📚 Learning Material
- **UNIT_TESTING_GUIDE.md** - Complete guide with concepts and examples

### 🧪 Test Files Created

**Two Sum Tests:**
- `test_two_sum_pytest.py` - Using pytest (simpler syntax)
- `test_two_sum_unittest.py` - Using unittest (verbose)

**Three Sum Tests:**
- `test_threesum_pytest.py` - Using pytest
- `test_threesum_unittest.py` - Using unittest

**Move Zeroes Tests:**
- `test_moves_zeros_pytest.py` - Using pytest
- `test_moves_zeros_unittest.py` - Using unittest

---

## Quick Start

### Option 1: Using pytest (Recommended for Beginners)

**Install pytest:**
```bash
pip install pytest
```

**Run all tests:**
```bash
pytest test_two_sum_pytest.py -v
pytest test_threesum_pytest.py -v
pytest test_moves_zeros_pytest.py -v
```

**Run specific test:**
```bash
pytest test_two_sum_pytest.py::test_two_sum_basic_case -v
```

**Run all tests in folder:**
```bash
pytest Two_Pointers/ -v
```

---

### Option 2: Using unittest (Built-in Python)

**No installation needed - built into Python!**

**Run all tests:**
```bash
python test_two_sum_unittest.py -v
python test_threesum_unittest.py -v
python test_moves_zeros_unittest.py -v
```

**Run specific test:**
```bash
python test_two_sum_unittest.py TestTwoSum.test_two_sum_basic_case
```

---

## Test Coverage Per Problem

### Two Sum - 8 test cases
- ✅ Basic example
- ✅ Pair at edges
- ✅ Minimum array size
- ✅ Duplicate numbers
- ✅ Negative numbers
- ✅ Large array
- ✅ Return type validation
- ✅ Index count validation

### Three Sum - 10 test cases
- ✅ Basic example
- ✅ No valid triplets
- ✅ All zeros
- ✅ Single triplet
- ✅ With duplicates
- ✅ Negative numbers
- ✅ Return type validation
- ✅ Triplet size validation
- ✅ Sum constraint validation
- ✅ No duplicate triplets

### Move Zeroes - 11 test cases
- ✅ Basic example
- ✅ No zeros
- ✅ All zeros
- ✅ Single zero
- ✅ Zero at beginning
- ✅ Zero at end
- ✅ Multiple zeros scattered
- ✅ Order preservation
- ✅ Zero count preservation
- ✅ Negative numbers
- ✅ Return type and length validation

---

## Understanding Test Structure

### pytest Style
```python
def test_function_name():
    # Arrange: Set up test data
    nums = [2, 7, 11, 15]
    target = 9
    
    # Act: Call the function
    result = solution.two_pointers(nums, target)
    
    # Assert: Check the result
    assert result == [1, 2]
```

### unittest Style
```python
class TestName(unittest.TestCase):
    def setUp(self):
        # Set up test data (runs before each test)
        self.solution = Solution()
    
    def test_function_name(self):
        # Arrange
        nums = [2, 7, 11, 15]
        target = 9
        
        # Act
        result = self.solution.two_pointers(nums, target)
        
        # Assert
        self.assertEqual(result, [1, 2])
```

---

## Why These Tests Are Important

### 1. **Test Different Scenarios**
   - Normal cases (happy path)
   - Edge cases (empty, single element, max size)
   - Boundary cases (first, last, middle)

### 2. **Test Data Types**
   - Correct return type
   - Correct structure

### 3. **Test Constraints**
   - Verify all constraints from problem are satisfied
   - e.g., triplets should sum to 0, no duplicates in result

### 4. **Catch Regressions**
   - If you change code later, tests will alert you if something breaks

---

## Common Assertions Comparison

| Purpose | pytest | unittest |
|---------|--------|----------|
| Equal | `assert a == b` | `self.assertEqual(a, b)` |
| Not equal | `assert a != b` | `self.assertNotEqual(a, b)` |
| True | `assert x` | `self.assertTrue(x)` |
| False | `assert not x` | `self.assertFalse(x)` |
| In list | `assert a in b` | `self.assertIn(a, b)` |
| Type | `assert isinstance(x, list)` | `self.assertIsInstance(x, list)` |
| Greater than | `assert a > b` | `self.assertGreater(a, b)` |
| List length | `assert len(a) == 5` | `self.assertEqual(len(a), 5)` |

---

## Next Steps

1. **Run the tests** to see them pass ✅
2. **Study the test code** to understand patterns
3. **Modify tests** - make one test fail intentionally to see the output
4. **Write your own tests** for new problems
5. **Run tests regularly** when developing code

---

## Pro Tips

### ✅ Writing Better Tests
- One assertion per test (when possible)
- Clear, descriptive test names
- Test edge cases, not just happy path
- Document WHY with docstrings

### ✅ Running Tests Efficiently
```bash
# Run tests and show coverage
pytest --cov=Two_Pointers test_*.py

# Stop after first failure
pytest -x

# Show print statements
pytest -s

# Run only failed tests
pytest --lf

# Run tests matching a name pattern
pytest -k "basic" -v
```

### ✅ Keep Tests Maintainable
- Group related tests in one file
- Use setUp() for common initialization
- Don't make tests depend on each other
- Use descriptive variable names

