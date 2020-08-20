"""We would like to have the new thread finish before the main thread"""

import time
import threading


def func(name):
    print(f'func started with arg {name}')
    time.sleep(2)
    print('func ended')


if __name__ == '__main__':
    print('main started')
    t = threading.Thread(target=func, args=['realpython'])
    t.start()
    print('\nCalling join to wait for thread execution')
    # by using the join() method of the t thread, we tell Python to wait for all
    # the threads to finish execution before proceeding
    t.join()
    print('main ended')
