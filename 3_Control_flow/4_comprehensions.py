# Calculating the squares using the for loop
squares = []
for x in range(10):
    squares.append(x * x)
print(squares)

# Calculating the squares using list comprehension
squares = [x * x for x in range(10)]
print(squares)
# Pattern: (values) = [(expression) for (value) in (collection)]

# you can expand the above pattern to use filtering
# calculating even squares using traditional for loop
print()
even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x * x)
print(even_squares)

# calculating even squares using list comprehension
even_squares = [x * x for x in range(10) if x % 2 == 0]
print(even_squares)
# Pattern: (values) = [(expression) for (value) in (collection) if (condition)]

print()
# set comprehension:
squares_set = {x * x for x in range(-9, 10)}
print(squares_set)
# dict comprehension:
squares_dict = {x: x * x for x in range(5)}
print(squares_dict)
# Refer: https://dbader.org/blog/list-dict-set-comprehensions-in-python
