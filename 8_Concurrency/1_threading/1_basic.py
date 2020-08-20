"""
Terminologies:

- CPU     - Piece of hardware that executes code
- OS      - Handles the scheduling of when the CPU can be used
- PROCESS - A program that is been executed
- THREAD  - A part of the program that is using the CPU, some programs are very
            very simple and they only do one thing so they really need only one
            thread. Whereas other more complex programs require more 
            functionalities and efficiency so they might use many threads.
"""
import time
import threading


# Issues with single threaded programs.
def single(name):
    print(f"single started with arg {name}")
    # assume this to be some sort of a complex calculation which takes time to
    # process
    time.sleep(2)
    print('single ended')


"""
__name__ holds the context when this module is getting initialized or 
executed, there are basically 2 ways a file gets executed:
1. we are runnning this file in the terminal, in this case the __name__ holds
   value of '__main__'.
2. some other file is importing this, in this case the __name__ holds the 
   file name.

this simple distinction helps us write code in such a way that we can execute
functionalities provided by the module and see the output as well as being able
to export those functionalities without executing them at the same time.
"""
if __name__ == '__main__':
    print('main started')
    single('realpython')
    print('main ended')
"""
When we call the function, the program gets stuck for a while until the function
does return something back, meanwhile we are not able to interact with the
program.
"""


def func(name):
    print(f'func started with arg {name}')
    time.sleep(2)
    print('func ended')


if __name__ == '__main__':
    print()
    print('main started')
    # we are creating a new Thread using the Thread class from threading module,
    # we are also associating that thread with a target function that needs to
    # be executed in a multithreaded environment.
    t = threading.Thread(target=func, args=['realpython'])
    # to start the thread we call the method start() on the created object
    t.start()
    print('\nmain ended')
"""This way we can create a non-blocking code"""
