# # When Executing this file main thread starts executing
#
import threading, time  # time is used to keep the execution in sleep or you can delay

def task1(k):
    print(f"\n Thread : {k}")
    global thread1
    print(f"\nThread is Alive : {thread1.is_alive()}")
    print("Thread is working \n")

# Creating thread
# Thread_Syntax: [Thread_name] = threading.Thread(target=[functional_reference], daemon=True or False, args=(args1,...))
# Daemon threads die when the main program exits. if daemon=False then thread die after completing the task
thread1 = threading.Thread(target=task1, daemon=False, args=("Cherry",)) # Main thread creates child thread
print("main thread finished")
thread1.start() # Child Thread starts Executing and Main thread also Executes Simultaneously
# join() is used to tell Main thread to wait until Child thread is finished
# thread1.join() # Using join() tells the main thread to wait until its function is completed or else both executed at the same time
# task1(thread1) # If join() not used thread1 and Main thread that Executes Task1(thread1) will print simultaneously
#
#
def delay():
    import time
    print(f" Thread is active")
    time.sleep(3) # it waits fo 10 sec
    print("Completed")

# thread2 = threading.Thread(target=delay, daemon=True)
# thread2.start()
# thread2.join()
# time.sleep(3) # sleeps for 5 seconds
# thread2.start() # This thread will die immediately after completing the task because It is not daemon thread

# Creating multiple threads
# threads = []
# for i in range(5):
#     t = threading.Thread(target=delay)
#     threads.append(t)
#     t.start()
#
# print(threads)
#
# for t in threads:
#     t.join()

#
# from threading import Thread
# # import time
#
# class A(Thread):
#     def run(self):
#         print(f"Thread A is active")
#         print("Thread A is sleeping")
#         time.sleep(3)
#
# class B(Thread):
#     def run(self):
#         print(f"Thread B is active")
#         print("Thread B is sleeping")
#         time.sleep(3)
#
#
# for i in range(5):
#     t4 = A()
#     t5 = B()
#     t4.start()
#     t5.start()
#     # t4.join()
#     # t5.join()



# import threading
# import time
#
# def worker(name, delay):
#     for i in range(3):
#         time.sleep(delay)
#         print(f"[{name}] Iteration {i}")
#
# # Create two threads targeting the worker() function
# t1 = threading.Thread(target=worker, name="Thread-A", args=("Thread-A", 1),daemon=False)
# t2 = threading.Thread(target=worker, name="Thread-B", args=("Thread-B", 1.5), daemon=True)
#
# # Start threads
# t1.start()
# t2.start()
#
# # Main thread waits for workers to finish
# # t1.join()
# # t2.join()
#
# print("All threads have finished.")
# print(t1.is_alive())


















