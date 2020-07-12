# if <expr>:
#   <statement>
# the most basic type of if statement
x = 0
y = 5

if x < y:
    print('x < y')
if y < x:
    print('y > x')
if x:
    print('x is Falsy')
if y:
    print('y is Truthy')
if x or y:
    print('x or y is Truthy')
if x and y:
    print('x and y is Falsy')
if 'aul' in 'grault':
    print('aul in grault')

print()
if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional')

print()
if 'foo' in ['foo', 'bar', 'baz']:
    print('Outer condition is true')

    if 10 > 20:
        print('Inner condition 1')

    print('Between inner conditions')

    if 10 < 20:
        print('Inner condition 2')

    print('End of outer condition')
print('After outer condition')


# if <expr>:
#   <statement(s)>
# else:
#   <statement(s)>
# the if-else block
print()
if x < 50:
    print('first suite')  # blocks are often refered to as suite in Python
    print('x < 50')
else:
    print('second suite')
    print('y >= x')


# if <expr>:
#   <statement(s)>
# elif <expr>:
#   <statement(s)>
# elif <expr>:
#   <statement(s)>
#   ...
# else:
#   <statement(s)>
# branching the execution based on several altrnatives, if-elif-else
print()
name = 'Joe'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Joe':
    print('Hello Joe')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")
# NOTE: Using a lengthy if/elif/else series can be a little inelegant,
# especially when the actions are simple statements like print().
# In many cases, there may be a more Pythonic way to accomplish the same thing.

# Possible alternative:
print()
names = {
    'Fred': 'Hello Fred',
    'Xander': 'Hello Xander',
    'Joe': 'Hello Joe',
    'Arnold': 'Hello Arnold'
}
print(names.get('Fred'))
print('Fred' in names and names['Fred'])
print(names.get('Rick'))
print('Rick' in name and names['Rick'])


# one-line if statements:
# if <expr>: <statement>
# if <expr>: <statement_1>; <statement_2>; ...; <statement_n>
# NOTE: The semicolon separating the <statements> has higher precedence than the
# colon following <expr>—in computer lingo, the semicolon is said to bind more
# tightly than the colon. Thus, the <statements> are treated as a suite, and
# either all of them are executed, or none of them are.
print()
if 'f' in 'foo':
    print('1')
    print('2')
    print('3')
if 'f' not in 'foo':
    print('1')
    print('2')
    print('3')

x = 2
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')
# NOTE: While all of this works, and the interpreter allows it, it is generally
# discouraged on the grounds that it leads to poor readability, particularly
# for complex if statements.
# On the other hand, If an if statement is simple enough, though, putting it
# all on one line may be reasonable. Something like this probably wouldn’t
# raise anyone’s hackles too much.


def foo():
    print('Did someone say foo?')


print()
debugging = True
if debugging:
    print('Calling function foo')
foo()


# Conditional Expressions in Python:
# Python does not support ternary operators like 'exp1 ? exp2 : exp3'
# Instead: <expr1> if <conditional_expr> else <expr2>
# NOTE: This is different from the if statement forms listed above because it
# is not a control structure that directs the flow of program execution. It
# acts more like an operator that defines an expression. In the above example,
# <conditional_expr> is evaluated first. If it is true, the expression
# evaluates to <expr1>. If it is false, the expression evaluates to <expr2>.
print()
raining = False
print('Lets go to the', 'beach' if not raining else 'library')
raining = True
print('Lets go to the', 'library' if raining else 'beach')

age = 15
person = 'minor' if age < 18 else 'adult'
print(person)
# NOTE: the conditional expression behaves like an expression syntactically.
# It can be used as part of a longer expression. The conditional expression has
# lower precedence than virtually all the other operators, so parentheses are
# needed to group it by itself.
print()
x = y = 40
print(1 + x if x < y else y + 2)  # both evaluate to 42
print((1 + x) if x < y else (y + 2))  # and are the same expressions
print(1 + (x if x < y else y) + 2)  # evaluates to 43
# they also use short-circuit evaluation

# they can also be used as a sort of an alternative to if-elif-else
x = 3
s = (
    'foo' if x == 1 else
    'bar' if x == 2 else
    'baz'
)
print(s)


# pass statement in Python: https://realpython.com/python-conditional-statements/#the-python-pass-statement
print()
super_complex_expression = 'meh'
if super_complex_expression is 'meh':
    pass
print('Using pass statement to create code stub')
# This is necessary when you don't have any implementation ready for a
# particular block and want to leave it empty for a while, but in Python,
# compiler will get angry at you if you do not provide atleast a single
# statement in the if block
