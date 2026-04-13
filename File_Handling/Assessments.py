# PROJECT 1: TRANSACTION DATA PIPELINE
def process_transactions(file):
    total = 0
    valid = 0
    invalid = 0
    revenue = 0
    category_revenue = {}

    with open(file, "r") as f, \
         open("clean.txt", "w") as clean, \
         open("error.log", "a", buffering=1) as log:

        header = f.readline()

        for line in f:
            total += 1
            line = line.strip()

            parts = line.split(",")

            if len(parts) != 3:
                log.write(f"{line} -> Invalid format\n")
                log.flush()
                invalid += 1
                continue

            user, amount, category = parts

            if amount == "":
                log.write(f"{line} -> Missing amount\n")
                log.flush()
                invalid += 1
                continue

            try:
                amount = float(amount)


                if amount < 0:
                    raise ValueError("Negative amount")

                clean.write(f"{user},{amount},{category}\n")

                revenue += amount
                category_revenue[category] = category_revenue.get(category, 0) + amount

                valid += 1

            except:
                log.write(f"{line} -> Non-numeric or invalid amount\n")
                log.flush()
                invalid += 1

    with open("clean.txt", "r") as f:
        print("Clean file size (bytes):", f.tell())  # will be 0 initially
        f.seek(0, 2)  # move to end
        print("Final position (file length):", f.tell())


    with open("report.txt", "w") as r:
        r.write(f"Total Records: {total}\n")
        r.write(f"Valid Records: {valid}\n")
        r.write(f"Invalid Records: {invalid}\n")
        r.write(f"Total Revenue: {revenue}\n\n")

        r.write("Category-wise Revenue:\n")
        for cat, amt in category_revenue.items():
            r.write(f"{cat}: {amt}\n")

#PROJECT 2: FILE-BASED RAG SYSTEM
def build_index(file):

    with open(file, "r") as f, open("vector_store.txt", "w") as vs:
        chunk = []
        for line in f:
            chunk.append(line.strip())

            if len(chunk) == 2:
                combined = " ".join(chunk)
                vs.write(combined + "\n")
                chunk = []

        if chunk:
            vs.write(" ".join(chunk) + "\n")
def query_system():

    while True:
        query = input("\nAsk (type 'exit'): ")

        if query.lower() == "exit":
            break

        best_match = ""
        max_score = 0

        with open("vector_store.txt", "r") as vs:

            vs.seek(0)

            for line in vs:
                line_lower = line.lower()
                score = 0

                for word in query.lower().split():
                    if word in line_lower:
                        score += 1

                if score > max_score:
                    max_score = score
                    best_match = line.strip()

        print("Answer:", best_match if best_match else "No match found")



if __name__ == "__main__":
    print("Transaction Pipeline")
    process_transactions("transactions.txt")
    print("Build Index")
    build_index("knowledge.txt")
    print("Query System")
    query_system()

# import os
# import sys
from contextlib import contextmanager
#
#
# def secure_opener(path, flags):
#     return os.open(path, flags, 0o600)
#
#
#
# class CustomFileManager:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         print("Opening file (Custom Manager)")
#         self.file = open(self.filename, self.mode, encoding="utf-8")
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Closing file (Custom Manager)")
#         if self.file:
#             self.file.close()
#
#
#
# @contextmanager
# def managed_file(filename, mode):
#     print("Opening file (Decorator Manager)")
#     f = open(filename, mode, encoding="utf-8")
#     try:
#         yield f
#     finally:
#         print("Closing file (Decorator Manager)")
#         f.close()
#
#
#
# def file_handling_demo():
#
#
#
#
#     f = open(
#         "demo.txt",
#         mode="w+",
#         buffering=1,
#         encoding="utf-8",
#         errors="strict",
#         newline="\n"
#     )
#
#     # WRITE METHODS
#     f.write("Line 1\n")
#     f.writelines(["Line 2\n", "Line 3\n"])
#
#     f.flush()
#
#     print("Current position:", f.tell())
#     f.seek(0)
#
#
#     print("Read all:", f.read())
#
#     f.seek(0)
#     print("Readline:", f.readline())
#
#     f.seek(0)
#     print("Readlines:", f.readlines())
#
#     # TRUNCATE
#     f.truncate(10)
#
#     f.close()
#
#
#
#     with open("print_output.txt", "w") as f:
#         print("Hello from print()", file=f)
#
#
#
#     sys.stdin = open("print_output.txt", "r")
#     print("Input read:", input())
#
#     sys.stdin.close()
#
#
#
#     fd = os.open("fd_demo.txt", os.O_WRONLY | os.O_CREAT)
#     f = open(fd, "w", closefd=True)
#     f.write("Written using file descriptor\n")
#     f.flush()
#     os.fsync(f.fileno())
#     f.close()
#
#
#
#     with open("secure.txt", "w", opener=secure_opener) as f:
#         f.write("Secure file with 600 permission")
#
#
#
#     with CustomFileManager("custom.txt", "w") as f:
#         f.write("Using class-based context manager\n")
#
#
#
#     with managed_file("decorator.txt", "w") as f:
#         f.write("Using decorator-based context manager\n")
#
#
#
#     with open("state.txt", "w+") as f:
#         print("Readable:", f.readable())
#         print("Writable:", f.writable())
#         print("Seekable:", f.seekable())
#
#         f.write("Testing state\n")
#         f.seek(0)
#         print("Content:", f.read())
#
#
#
#     with open("demo.txt", "r") as f:
#         for line in f:
#             print("Iter:", line.strip())


#
# # Question 1
# with open("sample.txt", "r") as file:
#     content = file.read()
#     print("Number of characters:", len(content))
#
#
#
#
#
#
#
# with open("sample.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         if len(line.strip()) > 10:
#             print(line.strip())
#
#
# with open("sample.txt", "w") as file:
#     file.write("Line 1\n")
#     file.write("Line 2\n")
#     file.write("Line 3\n")
#
#
# with open("sample.txt", "a") as file:
#     file.write("Line 4\n")
#     file.write("Line 5\n")
#
#
# with open("sample.txt", "r") as file:
#     print(file.read())
#
# with open("sample.txt", "r") as file:
#     first_part = file.read(10)
#     print("First 10 characters:", first_part)
#
#     position = file.tell()
#     print("Cursor position after reading 10 chars:", position)
#
#     file.seek(0)
#     print("Cursor moved to beginning.")
#
#     full_content = file.read()
#     print("Full content:\n", full_content)
#
# class FileManager:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(self.filename, "w")
#         self.file.write("This is written inside __enter__\n")
#         return self.file
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.file:
#             self.file.close()
#
#         if exc_type:
#             print("Exception occurred:")
#             print("Type:", exc_type)
#             print("Value:", exc_value)
#         return False
#
#
#
# with FileManager("sample.txt") as f:
#     f.write("Writing more data inside with block\n")
#
#
# from contextlib import contextmanager
#
# @contextmanager
# def open_file(filename, mode):
#     file = open(filename, mode)
#     try:
#         yield file
#     finally:
#         file.close()
#         print("File closed safely.")
#
#
#
# with open_file("sample.txt", "r") as f:
#     print(f.read())
#
#
# with open("sample.txt", "r") as file:
#     while True:
#         chunk = file.read(5)
#         if not chunk:
#             break
#         print("Chunk:", chunk)
#         print("Cursor position:", file.tell())
#
#     file.seek(10)
#     print("\nMoved cursor to position 10\n")
#     while True:
#         chunk = file.read(5)
#         if not chunk:
#             break
#         print("Chunk after seek:", chunk)
#         print("Cursor position:", file.tell())
#
#




# Question 1
# open a file using context manager

# with open("test.txt", "r") as t:
#     print(t.read())
#     t.seek(0)
#     # print(t.readline(10))
#     c=0
#     for i in t.readlines():
#         c+=len(i)
#     print(c)
#     t.seek(0)
#     print(len(t.read()))

# with open("test.txt",'r') as f:
#     for i in f.readlines():
#         if len(i)>10:
#             print(i[:-2])
# with open("demo.txt",'w+') as f:
#     f.write("hello world\n")
#     f.writelines(["how are you\n", "thinnara\n"])
#     f.seek(0)
#     print(f.read())

# class open_file:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode=mode
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         print("File opened successfully")
#         return self.file
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#         print("File closed successfully")
#
#
# with open_file("test.txt", "w+") as f:
#     f.write("Hello World")
#     f.seek(0)
#     print(f.read())

# @contextmanager
# def open_file(fn, mode):
#     print("opening file")
#     with open(fn, mode) as f:
#         yield f
#         print("intermediate file")
#
#     print("outside open")
#     print("closing file")
#
#
#
# with open_file("test.txt", "w+") as f:
#     print(f)