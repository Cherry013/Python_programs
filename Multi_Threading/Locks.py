# Using Locks to void Race conditions
import threading

x=0
def increment():
    global x
    for _ in range(100000000000000):
        x+=1
    print(x)
increment()
print(x) # Output: 0


# x=0
# lock = threading.Lock()
# sea = threading.Semaphore(1)
# def increment1():
#     global x
#     for _ in range(10000000):
#         lock.acquire()
#         x+=1
#         lock.release()
#         # print(x,end=" ",flush=True)
#     print(x)
# #
# thread1 = threading.Thread(target=increment1)
# thread1.start()
# thread1.join()
# thread2 = threading.Thread(target=increment1)
# thread2.start()
# thread2.join()
#
#
# print(x) # Output: 0