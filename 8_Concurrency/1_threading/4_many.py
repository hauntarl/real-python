import time
import threading


def func(name, seconds):
    print(f'func started with args: name={name}, seconds={seconds}')
    time.sleep(seconds)
    print('func ended')


if __name__ == '__main__':
    print('main started')
    t1 = threading.Thread(target=func, args=['foo', 3])
    t2 = threading.Thread(target=func, args=['bar', 2])
    t3 = threading.Thread(target=func, args=['baz', 1])
    t1.start()
    t2.start()
    t3.start()
    t3.join()
    print('joined t3')
    t2.join()
    print('joined t2')
    t1.join()
    print('joined t1')
    print('main ended')
"""
This type of repetitive nature of starting and waiting for thread to finish can
get a bit cumbersome.
"""
