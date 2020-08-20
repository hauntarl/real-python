import random
import time
import threading
import concurrent.futures
import queue


# our pipeline needs to inherit from queue module, one of the features of the
# Queue class is that it handles the locking automatically
class Pipeline(queue.Queue):
    def __init__(self):
        # we don't require the capacity argument for our pipeline now, as Queue
        # class supports a maxsize argument to determine the size of queue.
        # setting the maxsize to 0 will set the maxsize to the maximum value
        # your system can allow
        super().__init__(maxsize=10)

    def set_message(self, message):
        self.put(message)
        print(f'Producing message of {message}')

    def get_message(self):
        message = self.get()
        print(f'Consuming message of {message}')
        return message


producer_pipeline = []
consumer_pipeline = []


def producer(pipeline, event):
    # is_set() of event, is getter for the current value of event flag
    while not event.is_set():
        message = random.randint(1, 100)
        producer_pipeline.append(message)
        pipeline.set_message(message)


def consumer(pipeline, event):
    # empty() method comes from the queue module
    while not pipeline.empty() or not event.is_set():
        print(f'queue size is {pipeline.qsize()}')
        message = pipeline.get_message()
        consumer_pipeline.append(message)
        time.sleep(random.random())


if __name__ == '__main__':
    pipeline = Pipeline()
    # instead of using the FINISH variable to recognise the end. We should use
    # event from the threading package.
    event = threading.Event()
    # flag that has 2 values, true or false. Its like a boolean flag that any
    # thread that has access to the event will have access to this flag. It has
    # 2 methods associated with it, .set() to set the event to true and .clear()
    # to set if back to false.

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as exe:
        exe.submit(producer, pipeline, event)
        exe.submit(consumer, pipeline, event)
        exe.submit(consumer, pipeline, event)
        exe.submit(consumer, pipeline, event)
        time.sleep(0.5)
        event.set()
    print(f'producer: {producer_pipeline}')
    print(f'consumer: {consumer_pipeline}')
"""
NOTE: when your code is utilizing threads, you won't get clear and concise 
error messages.
"""
