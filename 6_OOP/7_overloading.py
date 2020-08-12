"""
If you’ve used the + or * operator on a str object in Python, you must have
noticed its different behavior when compared to int or float objects.
This is called operator overloading or function overloading.


- Scenario:
you have a class representing an online order having a cart (a list) and a 
customer (a str or instance of another class which represents a customer).

In such a case, it is quite natural to want to obtain the length of the cart 
list. Someone new to Python might decide to implement a method called 
get_cart_len() in their class to do this. But you can configure the built-in 
len() in such a way that it returns the length of the cart list when given our 
object.

In another case, we might want to append something to the cart. Again, someone 
new to Python would think of implementing a method called append_to_cart() that 
takes an item and appends it to the cart list. But you can configure the + 
operator in such a way that it appends a new item to the cart.

Python does all this using special methods. These special methods have a naming 
convention, where the name starts with two underscores, followed by an 
identifier and ends with another pair of underscores. Essentially, each 
built-in function or operator has a special method corresponding to it. For 
example, there’s __len__(), corresponding to len(), and __add__(), 
corresponding to the + operator.

By default, most of the built-ins and operators will not work with objects of 
your classes. You must add the corresponding special methods in your class 
definition to make your object compatible with built-ins and operators.


- The Internals of Operations Like len() and []:
Every class in Python defines its own behavior for built-in functions and 
methods. When you pass an instance of some class to a built-in function or use 
an operator on the instance, it is actually equivalent to calling a special 
method with relevant arguments.

If there is a built-in function, func(), and the corresponding special method 
for the function is __func__(), Python interprets a call to the function as 
obj.__func__(), where obj is the object. In the case of operators, if you have 
an operator opr and the corresponding special method for it is __opr__(), 
Python interprets something like obj1 <opr> obj2 as obj1.__opr__(obj2).

So, when you’re calling len() on an object, Python handles the call as 
obj.__len__(). When you use the [] operator on an iterable to obtain the value 
at an index, Python handles it as itr.__getitem__(index), where itr is the 
iterable object and index is the index you want to obtain.
"""
a = 'Real Python'
b = ['Real', 'Python']
print(len(a), a.__len__())
print(b[0], b.__getitem__(0))
"""
As you can see, when you use the function or its corresponding special method, 
you get the same result. In fact, when you obtain the list of attributes and 
methods of a str object using dir(), you’ll see these special methods in the 
list in addition to the usual methods available on str objects.
"""
print(dir(a))
# NOTE: If the behavior of a built-in function or operator is not defined in
# the class by the special method, then you will get a TypeError.


# Overloading Built-in Functions:
class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return len(self.cart)

    def __bool__(self):
        return len(self) > 0

    def __add__(self, other):
        new_cart = self.cart.copy()
        new_cart.append(other)
        # NOTE: __class__ is not a special method but a class attribute which
        # is present by default. It has a reference to the class. By using it
        # here, we are obtaining that and then calling the constructor in the
        # usual manner. In other words, this is equivalent to
        # CustomComplex(real, imag). This is done here to avoid refactoring the
        # code if the name of the class changes someday.
        return self.__class__(new_cart, self.customer)

    def __radd__(self, other):
        new_cart = self.cart.copy()
        new_cart.insert(0, other)
        return self.__class__(new_cart, self.customer)

    def __getitem__(self, key):
        return self.cart[key]


order = Order(['banana', 'apple', 'mango'], 'Real Python')
print()
print(len(order))
print(bool(order))
print(bool(Order([], 'Empty')))
"""
As you can see, you can now use len() to directly obtain the length of the cart.
Moreover, it makes more intuitive sense to say “length of order” rather than 
calling something like order.get_cart_len(). Your call is both Pythonic and 
more intuitive. When you don’t have the __len__() method defined but still call 
len() on your object, you get a TypeError.

But, when overloading len(), you should keep in mind that Python requires the 
function to return an integer. If your method were to return anything other 
than an integer, you would get a TypeError. This, most probably, is to keep it 
consistent with the fact that len() is generally used to obtain the length of a 
sequence, which can only be an integer.

Note: When the __bool__() special method is not implemented in a class, the 
value returned by __len__() is used as the truth value, where a non-zero value 
indicates True and a zero value indicates False. In case both the methods are 
not implemented, all instances of the class are considered to be True.
"""


class Vector:
    def __init__(self, x_comp, y_comp):
        self.x_comp = x_comp
        self.y_comp = y_comp

    # NOTE: their is no restriction on the return type for the __abs__ method
    # unlike __len__.
    def __abs__(self):
        return (self.x_comp ** 2 + self.y_comp ** 2) ** 0.5


vector = Vector(3, 4)
print()
print(abs(vector))


"""
- Overloading Built-in Operators:
Changing the behavior of operators is just as simple as changing the behavior 
of functions. You define their corresponding special methods in your class, and 
the operators work according to the behavior defined in these methods.

These are different from the above special methods in the sense that they need 
to accept another argument in the definition other than self, generally 
referred to by the name other. Let’s look at a few examples.

- Making Your Objects Capable of Being Added Using +
The special method corresponding to the + operator is the __add__() method. 
Adding a custom definition of __add__() changes the behavior of the operator. 
It is recommended that __add__() returns a new instance of the class instead of 
modifying the calling instance itself.

Similarly, you have the __sub__(), __mul__(), and other special methods which
define the behavior of -, *, and so on. These methods should return a new
instance of the class as well.

While defining the __add__(), __sub__(), __mul__(), and similar special methods 
allows you to use the operators when your class instance is the left-hand side 
operand, the operator will not work if the class instance is the right-hand 
side operand.

If the operators work only when the instance is the left operand, we are 
violating the fundamental principle of commutativity in many cases. Therefore, 
to help you make your classes mathematically correct, Python provides you with 
reverse special methods such as __radd__(), __rsub__(), __rmul__(), and so on
"""
print()
print(order.cart)
order += 'orange'
print(order.cart)
order = 'grapes' + order
print(order.cart)

"""
- Indexing and Slicing Your Objects Using []
The [] operator is called the indexing operator and is used in various contexts 
in Python such as getting the value at an index in sequences, getting the value 
associated with a key in dictionaries, or obtaining a part of a sequence 
through slicing. You can change its behavior using the __getitem__() special 
method.

Note: There is a similar __setitem__() special method that is used to define 
the behavior of obj[x] = y. This method takes two arguments in addition to self,
generally called key and value, and can be used to change the value at key to 
value.
"""
print()
print(order[3])
print(order[::-1])
# NOTE: As long as you’re using data structures that support slicing (lists,
# tuples, strings, and so on), you can configure your objects to directly slice
# the structure.

# A Complete Example
# REFER: https://realpython.com/operator-function-overloading/#a-complete-example
