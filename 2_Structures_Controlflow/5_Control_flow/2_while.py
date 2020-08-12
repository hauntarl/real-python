# while loop is a python control structure for indeifinite loop
# while <expr>:
#   <statement(s)>

n = 5
while n >= 0:
    n -= 1
    print(n, end=' ')

print()
a = ['foo', 'bar', 'baz']
while a:
    print(a.pop(), end=' ')


# breal and continue statements
print()
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n, end=' ')
print('Loop ended.')

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n, end=' ')
print('Loop ended.')


# else clause in while loop
# When <additional_statement(s)> are placed in an else clause, they will be 
# executed only if the loop terminates “by exhaustion”—that is, if the loop 
# iterates until the controlling condition becomes false. If the loop is exited 
# by a break statement, the else clause won’t be executed.
n = 5
while n > 0:
    n -= 1
    print(n, end=' ')
else:
    print('Loop terminated by exhaustion')
print('follow-up statements...')

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n, end=' ')
else:
    print('Loop terminated using break statement')
print('\nfollow-up statements...')
# Refer: https://realpython.com/python-while-loop/
