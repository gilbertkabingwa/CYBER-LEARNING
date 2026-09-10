#What is a data type?
"""a data type is a classification that tells the computer what kind of value a variable holds and what operations can be performed on it"""

""""Python uses **data types** to define what kind of value a variable contains.

## 1. String — `str`

Used for text.

```python
name = "Gilbert"
country = "Rwanda"
```

* Text must be inside `" "` or `' '`.
* Strings can contain letters, numbers and symbols.

```python
print(name)
```

---

## 2. Integer — `int`

Used for whole numbers.

```python
age = 25
money = 1000
```

No decimal point.

```python
x = 10
```

---

## 3. Float — `float`

Used for numbers with decimals.

```python
price = 19.99
height = 160.5
```

---

## 4. Boolean — `bool`

Used for **True / False** values.

```python
is_student = True
is_raining = False
```

Important:

```python
True
False
```

Capital letters matter.

---

# Checking a Data Type

Use `type()`:

```python
name = "Gilbert"
age = 25
height = 160.5
student = True

print(type(name))
print(type(age))
print(type(height))
print(type(student))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

---

# Type Conversion

You can convert values from one type to another.

### String → Integer

```python
age = "25"
age = int(age)
```

### Integer → String

```python
age = 25
age = str(age)
```

### Integer → Float

```python
number = 10
number = float(number)
```

### Float → Integer

```python
number = 10.9
number = int(number)
```

 Converting `10.9` to `int` gives:

```text
10
```

The decimal part is removed.

---

# Important Difference

```python
age = 25
```

is an integer.

```python
age = "25"
```

is a string.

They may look similar, but Python treats them differently.

For example:

```python
print(25 + 5)
```

→ `30`

But:

```python
print("25" + "5")
```

→ `"255"`

Because Python joins two strings together.

---

# Main Data Types to Remember

| Data Type | Example   | Meaning        |
| --------- | --------- | -------------- |
| `str`     | `"Hello"` | Text           |
| `int`     | `25`      | Whole number   |
| `float`   | `25.5`    | Decimal number |
| `bool`    | `True`    | True/False     |

### Memorize:

**`str` = text**
**`int` = whole number**
**`float` = decimal number**
**`bool` = True/False**

These four are the most important basic Python data types to know first.
"""