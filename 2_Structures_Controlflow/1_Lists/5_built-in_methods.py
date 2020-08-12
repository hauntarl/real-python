# most string methods return a new string object that is modifed
# leaving the original string object unchanged

# most list methods will modify the target list in place and do not
# return anything typically

a = [1, 2, 3]
print(f'a = {a}')
a.append(345)
print(f'after appending 345 to a, a = {a}')  # list got modifed
print(f'a + [3, 4, 5] = {a + [3, 4, 5]}')  # returned new modified list
print(f'a = {a}')
print(f'a.append([3, 4, 5]) returns {a.append([3, 4, 5])}')
print(f'a = {a}')

# to get the behavior of concatenation operator without returning anything
# but modifying the target list in-place use extend
a = [1, 2]
print(f'\na = {a}')
print(f'a.extend([3, 4, 5]) returns {a.extend([3, 4, 5])}')
print(f'a = {a}')

# method insert: inserts the object at a specified location and shifts others
# to the right
a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
print(f'\na = {a}')
print(f'a.insert(3, 3.14) returns {a.insert(3, 3.14)}')
print(f'a = {a}')

# remove method removes object from the list, but raises ValueError if the
# object is missing
print(f'a.remove(3.14) returns {a.remove(3.14)}')
print(f'a = {a}')

# clear method empties the list completely
print(f'a.clear() returns {a.clear()}')
print(f'a = {a}')

# sort method sorts the list in ascending order by default
# but can take 2 additional parameters (key: func, reverse: bool)
a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
print(f'\na = {a}')
print(f'a.sort() returns {a.sort()}')
print(f'a = {a}')
print(f'a.sort(reverse=True) returns {a.sort(reverse=True)}')
print(f'a = {a}')

a += ['Apple', 'Zebra']
print(f'\na = {a}')
print(f'a.sort() returns {a.sort()}')  # the issue of unicode values
print(f'a = {a}')
# to counter it we can use the key parameter in sort method
print(f'a.sort(key=str.upper) returns {a.sort(key=str.upper)}')
print(f'a = {a}')
# NOTE: sort method will only work if the objects are of same type
# else it raises TypeError
# Refer: https://realpython.com/python-sort/

# reverse method reverses the list in place
a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
print(f'\na = {a}')
print(f'a.reverse() returns {a.reverse()}')
print(f'a = {a}')
print(f'a[::-1] returns {a[::-1]}')  # returns a copy of modified list
print(f'a = {a}')  # but doesn't affect the targeted list


# list methods with return values
# pop method removes the object at specified index, default: -1 (last)
a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
print(f'\na = {a}')
print(f'a.pop(3) returns {a.pop(3)}')
print(f'a = {a}')

# index method returns the index for given object if present,
# else raises a ValueError
print(f"a.index('bacon') returns {a.index('bacon')}")
print(f"a.index('bacon', 1, 3) returns {a.index('bacon', 1, 3)}")
# print(f"a.index('bacon', 3) returns {a.index('bacon', 3)}")  # raises error

# method count: returns the occurrences of an object in the list

# copy method returns shallow copy of the list
a = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(f'a = {a}')
b = a.copy()
print(f'b = a.copy(), b = {b}')
print(f'Is a == b? {a == b}')
print(f'If a is b? {a is b}')
b[0] = 'b'
print('b[0] = \'b\'')
print(f'a = {a}')
print(f'b = {b}')
b[1][2] = 'zz'
print('b[1][2] = \'zz\'')
print(f'a = {a}')
print(f'b = {b}')
# NOTE: shallow copy means a new list gets generated but the underlying complex
# objects still refer to the same memory, unlike strings which are immutables
# to reassigning str objects doesn't reflect in the original list
# the same behavior is noticed when we use slicing techniques
# Refer: https://realpython.com/copying-python-objects/
c = a[:]
print(f'\nc = a[:], c = {c}')
print(f'Is a == c? {a == c}')
print(f'If a is c? {a is c}')
c[3][1] = 'slice'
print('c[3][1] = \'slice\'')
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
# NOTE: need to be cautious when using lists with sublists and using copy operations
