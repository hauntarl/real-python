import time
import threading


def func(name):
    print(f'func started with arg {name}')
    time.sleep(2)
    print('func ended')


if __name__ == '__main__':
    print('main started')
    # we are creating a new Thread using the Thread class from threading module,
    # we are also associating that thread with a target function that needs to
    # be executed in a multithreaded environment.
    t = threading.Thread(target=func, args=['realpython'])
    # to start the thread we call the method start() on the created object
    t.start()
    print('\nmain ended')
"""This way we can create a non-blocking code"""
