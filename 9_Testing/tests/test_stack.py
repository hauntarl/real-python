"""
. This file is responsible for performing tests on our Stack data structure
. When using pytest, any file that you want to test has to be prefixed with the
  word 'test_'
"""

from ds.stack import Stack
from pytest import fixture, raises

# any function which represents a test should also be prefixed with 'test_'


def test_constructor():
    s = Stack()  # creation of object via constructor
    # assert command results in a boolean where you compare your test results
    # with an expected output, if assert returns false, the test fails
    # assert 1 == 2  # try me
    assert isinstance(s, Stack)

    # in a test driven development, you will first write the tests, then modify
    # the functionality of your code such that it passes the tests
    assert len(s) == 0  # to pass this test, Stack needs to implement __len__()
    # in order to return the correct length of the stack, you'll also need to
    # create a internal structure which will represent the innner workings of a
    # stack


# test to check the push operation on stack
# there are 2 ways to go from here, creating another stack object using the
# constructor, but when you have a whole bunch of tests, it gets tedious
# to write create operations over and over again, instead we could do what's
# called a 'fixture'
# 'stack' parameter has the same name as our fixture, what this essentially does
# is calls the stack() which returns a brand new Stack object, inject that
# object into this function
def test_push(stack):
    stack.push(3)  # need to implement push() method
    assert len(stack) == 1

    stack.push(5)
    assert len(stack) == 2


@fixture  # this will create a fixture
def stack():
    return Stack()


def test_pop(stack):
    stack.push('hello')
    stack.push('world')

    assert stack.pop() == 'world'
    assert stack.pop() == 'hello'
    # to catch an expected exception from your function, use 'raises'
    with raises(IndexError):
        stack.pop()
