# Advanced OS & File Handling (Next Step)

## 🎯 Goal

Move from basic OS usage → advanced, real-world system-level
understanding.

------------------------------------------------------------------------

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

## 🚀 Next Step

After this, move to: - pathlib (modern replacement for os.path) -
tempfile module - NumPy basics (arrays, operations)
