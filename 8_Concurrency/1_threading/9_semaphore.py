import threading
import time
import random
import concurrent.futures

sem = threading.Semaphore()
print(dir(sem))
"""
Semaphore has a release and acquire method, which is very similar to what
we've seen before.

One of the greatest use case of semaphore is an atomic counter. Atomic meaning
it gurantees that the cpu won't execute any other instructions in between the
time it takes to increment/decrement the counter.
"""
sem = threading.Semaphore(value=50)
print()
print(sem._value)
sem.acquire()
sem.acquire()
sem.acquire()
print(sem._value)
sem.release()
print(sem._value)
"""
the _value here is atomic. This comes in handy when you are dealing with
limited resources, eg. a connection pool in a database, with limited resources
you want to be sure that only a certain number of machines are able to access
those resources.
"""


def welcome(semaphore, reached_max_users):
    visitor_number = 1
    while True:
        while not reached_max_users.is_set():
            print(f'Welcome visitor #{visitor_number}')
            semaphore.acquire()
            visitor_number += 1
            time.sleep(random.random())


def monitor(semaphore, reached_max_users):
    while True:
        print(f'[monitor] semaphore={semaphore._value}')
        time.sleep(3)
        if semaphore._value == 0:
            reached_max_users.set()
            print('[monitor] reached max users!')
            print('[monitor] kicking out a user...')
            semaphore.release()
            time.sleep(0.05)
            reached_max_users.clear()


if __name__ == '__main__':
    print()
    number_of_users = 20
    reached_max_users = threading.Event()
    semaphore = threading.Semaphore(value=number_of_users)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as exec:
        exec.submit(welcome, semaphore, reached_max_users)
        exec.submit(monitor, semaphore, reached_max_users)
