# OS Module Learning Guide (Python)

## 📌 1. Introduction to OS Module

The `os` module in Python provides a way to interact with the operating
system.

### Key Uses:

-   File and directory handling
-   Process management
-   Environment variables
-   Low-level file operations

------------------------------------------------------------------------

## 📂 2. File Handling (High-Level vs Low-Level)

### High-Level (`open`)

``` python
with open("file.txt", "w") as f:
    f.write("Hello World")
```

### Low-Level (`os.open`)

``` python
import os

fd = os.open("file.txt", os.O_WRONLY | os.O_CREAT)
os.write(fd, b"Hello World")
os.close(fd)
```

------------------------------------------------------------------------

## 🔑 3. File Descriptors

-   Integer returned by `os.open`
-   Used to read/write files

### Example:

``` python
fd = os.open("file.txt", os.O_RDONLY)
data = os.read(fd, 100)
os.close(fd)
```

------------------------------------------------------------------------

## ⚙️ 4. Flags in os.open

  Flag          Meaning
  ------------- --------------
  os.O_RDONLY   Read only
  os.O_WRONLY   Write only
  os.O_RDWR     Read & Write
  os.O_CREAT    Create file
  os.O_APPEND   Append mode

### Example:

``` python
fd = os.open("file.txt", os.O_WRONLY | os.O_CREAT | os.O_APPEND)
```

------------------------------------------------------------------------

## 🔐 5. File Permissions

Permissions use octal format.

  Value   Meaning
  ------- -----------------------
  0o600   Owner: read/write
  0o644   Owner: rw, others: r
  0o777   Everyone: full access

### Example:

``` python
fd = os.open("secure.txt", os.O_WRONLY | os.O_CREAT, 0o600)
```

------------------------------------------------------------------------

## 📁 6. Working with Directories

### Create Directory

``` python
os.mkdir("test_folder")
```

### Remove Directory

``` python
os.rmdir("test_folder")
```

### List Files

``` python
files = os.listdir(".")
print(files)
```

------------------------------------------------------------------------

## 🌍 7. Environment Variables

### Get Variable

``` python
print(os.environ.get("PATH"))
```

### Set Variable

``` python
os.environ["MY_VAR"] = "Hello"
```

------------------------------------------------------------------------

## 🔄 8. Working Directory

### Get Current Directory

``` python
print(os.getcwd())
```

### Change Directory

``` python
os.chdir("..")
```

------------------------------------------------------------------------

## 🧪 9. Practical Example: Secure File Creator

``` python
import os

def secure_opener(path):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT, 0o600)
    os.write(fd, b"Sensitive Data")
    os.close(fd)

secure_opener("secure.txt")
```

------------------------------------------------------------------------

## 🧠 10. Concepts to Master

-   File Descriptor vs File Object
-   Bitwise Operators (`|`)
-   Permissions System
-   OS-Level File Handling
-   Difference between high-level and low-level APIs

------------------------------------------------------------------------

## 🚀 Next Steps

-   Learn `pathlib` (modern file handling)
-   Learn `tempfile`
-   Practice mini projects:
    -   Log file system
    -   Secure data storage
    -   File analyzer
