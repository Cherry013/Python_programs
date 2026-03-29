import os

print(os.path)
fd = os.open("Demo.txt",os.O_RDONLY,0o600)
print(fd)
print(os.read(fd,25))

print(os.environ.get("PATH").split(";"))