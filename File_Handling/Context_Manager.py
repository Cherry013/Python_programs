# Context managers are a fundamental design pattern in Python that provide a structured approach to resource management.
# They ensure that resources are acquired, used properly, and then finally released or cleaned up, even with errors or exceptions.
# Using 'with' it will automatically call '__enter__' to start a process and it calls '__exit__' to End the process at the End of the block.
# Those two methods contains logic to start and end the process

# with open('Hello.txt','r') as f:
#     print(f.read())

# Custom Context Manager
# This is custom context manager Instead of open() U created your own way you can write logic on your own inside the '__enter__' and '__exit__' for starting and exiting
# Note: Need to return the value from '__enter__' method to send to corresponding alias value like a in the below context manager
class A:
    def __init__(self,value,mode):
        print("Initializing")
        self.value = value
        self.mode = mode
    def __enter__(self):
        print("Starting")
        self.value = open(self.value,self.mode)
        return self.value
    def __exit__(self,exc_type,exc_value,traceback):
        print(exc_type,exc_value,traceback,sep='\n')
        print("Closing")
        self.value.close()

with A('Hello.txt','r') as a:
    print(a.read())
    print(a.tell())
    print(a.seek(6))
    print(a.tell())

obj = A('Demo.txt','r')
with obj as obj:
    print(obj.read())


