"""
. This is an implemention of Stack data structure which is a LIFO - last in
  first out
. A stack has two important methods, push() and pop()
"""


class Stack:
    def __init__(self):
        self._trace = []

    def __len__(self):
        return len(self._trace)

    def push(self, data):
        self._trace.append(data)

    def pop(self):
        data = self._trace[len(self._trace)-1]
        self._trace = self._trace[:len(self._trace) - 1]
        return data
