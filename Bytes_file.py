b_data = b"Hello, World!"
print(f"Bytes literal: {b_data}")
print(f"Type: {type(b_data)}")

# Create a bytes object from a list of integers (0 to 255)
b_list = bytes([72, 101, 108, 108, 111])
print(f"Bytes from list: {b_list}")

# Accessing individual bytes (returns an integer)
print(f"First byte (ASCII value): {b_data[0]}")

# Attempting to modify a bytes object raises a TypeError
try:
    b_data[0] = 77
except TypeError as e:
    print(f"Error modifying bytes: {e}")

# Byte Array ==> bytearray(string, encoding like "utf-8")
ba_data = bytearray("Hello", "utf-8")
print(f"Original bytearray: {ba_data}")

# Modify individual bytes (using integer ASCII values)
# ASCII for 'M' is 77, 'a' is 97
ba_data[0] = 77  # Changes 'H' to 'M'
ba_data[1] = ord('a') # Changes 'e' to 'a'
print(f"Modified bytearray: {ba_data}")

# Append bytes to the bytearray
ba_data.extend(b", World!")
print(f"Extended bytearray: {ba_data}")

# # Changing data from Storage
# Create a bytearray (mutable)
data = bytearray(b"foo-bar-baz")
print(f"Original data: {data}")

# Create a memoryview of the bytearray
mv = memoryview(data)
print(mv)

section1 = mv[:3] # view of "foo"
section2 = mv[-3:] # view of "baz"
print(section1,section2)

# Modify the data through the memoryview slices
# Assigning a new bytes object to the slice updates the original 'data' bytearray
section1[:] = b"###"
section2[:] = b"***"

print(section1,section2)

print(f"Modified data via memoryview: {data}") # Modified data via memoryview: bytearray(b'###-bar-***')


# You can also create a memoryview of a bytes object (immutable)
b_data = b"immutable"
mv_b = memoryview(b_data)
print(f"Memoryview of bytes: {mv_b}")
# Attempting to modify a memoryview of immutable data will raise an error
try:
    mv_b[0] = 65
except TypeError as e:
    print(f"Error modifying immutable memoryview: {e}")


# To use different type of encoding like UTF-8,16 and 32. The UTF-64 encoding is not a standard or supported encoding in Python.
# Output will be in BOM(Byte Order Mark) Format it mean raw byte representations
s = "café"

# Encode to UTF-8 (default)
b_utf8 = s.encode("utf-8")
print(f"UTF-8: {b_utf8} (Length: {len(b_utf8)} bytes)")

# Encode to UTF-16 (usually includes a Byte Order Mark (BOM))
b_utf16 = s.encode("utf-16")
print(f"UTF-16: {b_utf16} (Length: {len(b_utf16)} bytes)")

# Encode to UTF-32 (fixed 4 bytes per character + BOM)
b_utf32 = s.encode("utf-32")
print(f"UTF-32: {b_utf32} (Length: {len(b_utf32)} bytes)")


s = "Hello"

# Create a bytearray using UTF-16 encoding
ba_utf16 = bytearray(s, "utf-16")
print(f"Bytearray UTF-16: {ba_utf16}")

# Create a bytearray using UTF-32 encoding
ba_utf32 = bytearray(s, "utf-32")
print(f"Bytearray UTF-32: {ba_utf32}")

# You can modify this mutable bytearray
ba_utf16[2] = 65 # Changes the byte value at index 2 (changes 'H' to 'A' in the byte stream)
print(f"Modified Bytearray UTF-16: {ba_utf16}")