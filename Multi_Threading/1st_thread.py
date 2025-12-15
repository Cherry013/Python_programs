# When Executing this file main thread starts executing

import threading, time  # time is used to keep the execution in sleep or you can delay

def task1(k):
    print(f"\n Thread : {k}")
    global thread1
    print(f"\nThread is Alive : {thread1.is_alive()}")
    print("Thread is working \n")

# Creating thread
# Thread_Syntax: [Thread_name] = threading.Thread(target=[functional_reference], daemon=True or False, args=(args1,...))
# Daemon threads die when the main program exits. if daemon=False then thread die after completing the task
thread1 = threading.Thread(target=task1, daemon=True, args=("Cherry",)) # Main thread creates child thread
thread1.start() # Child Thread starts Executing and Main thread also Executes Simultaneously
# join() is used to tell Main thread to wait until Child thread is finished
thread1.join() # Using join() tells the main thread to wait until its function is completed or else both executed at the same time
task1(thread1) # If join() not used thread1 and Main thread that Executes Task1(thread1) will print simultaneously


def delay():
    import time
    print(f" Thread is active")
    time.sleep(10) # it waits fo 10 sec
    print("Completed")

thread2 = threading.Thread(target=delay)
thread2.start()
thread2.join()
time.sleep(5) # sleeps for 5 seconds
thread2.start() # This thread will die immediately after completing the task because It is not daemon thread

# Creating multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=delay)
    threads.append(t)
    t.start()

print(threads)

for t in threads:
    t.join()


