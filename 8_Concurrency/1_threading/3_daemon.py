"""
In the previous example we saw that our main thread didn't wait for the new
thread to finish. Sometimes we do want our main thread to wait for all of our 
threads to finish before we hit that final line of code, one way we can do that
is by using daemon threads.

Daemon - refers to background process, something that hums along silently in the
background while you are doing something else.
"""


import time
import threading


def func(name):
    print(f'func started with arg {name}')
    time.sleep(2)
    print('func ended')


if __name__ == '__main__':
    print('main started')
    # this time we are going to add one more argument while creating the Thread
    t = threading.Thread(target=func, args=['realpython'], daemon=True)
    t.start()
    print('\nmain ended')
"""
This time the multi function didn't get a chance to finish before the program
exited. Setting the daemon property to True, we explicitly specify the task to
be a background one and the main thread doesn't necessarily need to wait until
that particular thread finishes its execution.
"""
