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

[//]: # (## 🚀 Next Steps)

[//]: # ()
[//]: # (-   Learn `pathlib` &#40;modern file handling&#41;)

[//]: # (-   Learn `tempfile`)

[//]: # (-   Practice mini projects:)

[//]: # (    -   Log file system)

[//]: # (    -   Secure data storage)

[//]: # (    -   File analyzer)


# Advanced OS & File Handling


## 📌 1. os.read(), os.write() Deep Dive

### os.read

Reads bytes from file descriptor.

``` python
import os

fd = os.open("file.txt", os.O_RDONLY)
data = os.read(fd, 50)
print(data)
os.close(fd)
```

### os.write

Writes bytes (must be in bytes format)

``` python
fd = os.open("file.txt", os.O_WRONLY)
os.write(fd, b"Hello Advanced OS")
os.close(fd)
```

------------------------------------------------------------------------

## ⚠️ 2. Important Concept: Bytes vs String

-   os.read → returns bytes
-   os.write → accepts bytes

### Convert:

``` python
text = "Hello"
b = text.encode()

data = b"Hello"
text = data.decode()
```

------------------------------------------------------------------------

## 🔐 3. File Modes & Security

### Flags Combination Example

``` python
fd = os.open("secure.txt", os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
```

-   O_EXCL → prevents overwriting existing file
-   Used for secure systems

------------------------------------------------------------------------

## 📊 4. os.stat (File Metadata)

``` python
import os

info = os.stat("file.txt")
print(info.st_size)   # file size
print(info.st_mode)   # permissions
```

------------------------------------------------------------------------

## 📁 5. Path Handling with os.path

``` python
import os

print(os.path.exists("file.txt"))
print(os.path.isfile("file.txt"))
print(os.path.isdir("folder"))
print(os.path.join("folder", "file.txt"))
```

------------------------------------------------------------------------

## 🔄 6. File Copy (Manual Implementation)

``` python
import os

src = os.open("source.txt", os.O_RDONLY)
dest = os.open("dest.txt", os.O_WRONLY | os.O_CREAT, 0o644)

while True:
    data = os.read(src, 1024)
    if not data:
        break
    os.write(dest, data)

os.close(src)
os.close(dest)
```

------------------------------------------------------------------------

## 🧪 7. Mini Project 1: Secure File Writer

``` python
import os

def secure_write(filename, content):
    fd = os.open(filename, os.O_WRONLY | os.O_CREAT, 0o600)
    os.write(fd, content.encode())
    os.close(fd)

secure_write("secret.txt", "My Password")
```

------------------------------------------------------------------------

## 🧪 8. Mini Project 2: Simple Logger

``` python
import os

def logger(message):
    fd = os.open("log.txt", os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    os.write(fd, (message + "\n").encode())
    os.close(fd)

logger("Program started")
logger("Error occurred")
```

------------------------------------------------------------------------

## 🧠 9. Concepts to Master

-   Byte handling (encode/decode)
-   File descriptor lifecycle
-   Secure file creation
-   Efficient file reading (chunks)
-   OS-level vs Python-level file handling

------------------------------------------------------------------------
