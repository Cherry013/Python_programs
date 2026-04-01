# NumPy Basics – Complete Guide

---

## 📌 What is NumPy?

NumPy stands for **Numerical Python**. It is a powerful Python library used for performing mathematical and numerical operations efficiently.

### Why NumPy is Important?

- Faster than Python lists (implemented in C)
- Uses less memory
- Supports vectorized operations (no need for loops)
- Widely used in Data Science, Machine Learning, and Scientific Computing

---

## 📦 Installation

```bash
pip install numpy
```

---

## 📥 Importing NumPy

```python
import numpy as np
```

### Explanation:

- `numpy` is the library name
- `np` is an alias (short name) used by convention

---

## 🔢 Creating Arrays

### 1️⃣ 1D Array

```python
arr = np.array([1, 2, 3, 4])
print(arr)
```

### Explanation:

- `np.array()` converts a Python list into a NumPy array
- This creates a **1-dimensional array**

---

### 2️⃣ 2D Array

```python
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
```

### Explanation:

- Nested lists represent rows and columns
- This creates a **2-dimensional array (matrix)**

---

### Check Type

```python
print(type(arr))
```

### Explanation:

- Output will be: `<class 'numpy.ndarray'>`
- All NumPy arrays belong to `ndarray` class

---

## 📊 Array Properties

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
```

### Explanation:

- `ndim` → Number of dimensions (2 for matrix)
- `shape` → (rows, columns)
- `size` → Total number of elements
- `dtype` → Data type (int, float, etc.)

---

## 🧱 Special Arrays

```python
np.zeros((2,3))
np.ones((2,3))
np.eye(3)
np.arange(0,10)
np.linspace(0,1,5)
```

### Explanation:

- `zeros((2,3))` → 2x3 matrix filled with 0
- `ones((2,3))` → 2x3 matrix filled with 1
- `eye(3)` → Identity matrix (diagonal = 1)
- `arange(0,10)` → Values from 0 to 9
- `linspace(0,1,5)` → 5 evenly spaced values between 0 and 1

---

## 🔍 Indexing & Slicing

### 1D Example

```python
arr = np.array([10, 20, 30, 40])

print(arr[0])
print(arr[1:3])
```

### Explanation:

- `arr[0]` → First element
- `arr[1:3]` → Elements from index 1 to 2

---

### 2D Example

```python
arr = np.array([[1,2,3],[4,5,6]])

print(arr[0,1])
print(arr[:,1])
```

### Explanation:

- `arr[0,1]` → Row 0, Column 1
- `arr[:,1]` → All rows, Column 1

---

## ⚡ Vectorized Operations

```python
arr = np.array([1,2,3])

print(arr + 10)
print(arr * 2)
```

### Explanation:

- `arr + 10` → Adds 10 to each element
- `arr * 2` → Multiplies each element by 2
- No loops required → faster execution

---

## ➕ Basic Mathematical Functions

```python
np.sum(arr)
np.mean(arr)
np.max(arr)
np.min(arr)
np.std(arr)
```

### Explanation:

- `sum()` → Total of elements
- `mean()` → Average value
- `max()` → Largest value
- `min()` → Smallest value
- `std()` → Standard deviation (spread of data)

---

## 🔄 Reshaping Arrays

```python
arr = np.arange(6)

print(arr.reshape(2,3))
```

### Explanation:

- `arange(6)` → [0,1,2,3,4,5]
- `reshape(2,3)` → Converts into 2 rows and 3 columns
- Total elements must match

---

## 🧪 Practice Tasks

1. Create an array from 1 to 20
2. Reshape it into (4,5)
3. Print:
   - Shape
   - First row
   - Last column
4. Add 100 to all elements

5. Create a 3x3 matrix using `np.arange()` and reshape it
   - Find the sum of all elements
   - Find the maximum value
   - Find the mean of the matrix

6. Create an array from 10 to 50 with a step of 5
   - Slice the array to get middle elements
   - Multiply all elements by 3
   - Convert the array into a 2D array of shape (2, ?)
