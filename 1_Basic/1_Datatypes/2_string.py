print('STRINGS:')
# Strings are sequences of character data. The string type in Python is called str.
print('I am a string', type('I am a string'))
# A string in Python can contain as many characters as you wish.

# \ character - also known as escape character
# print('This string contains a single quote (') character.') # error
print('This string contains a single quote (\') character.')
# Refer: https://realpython.com/python-data-types/#strings

# raw strings - escape sequences are not translated
print(r"can't\nescape")

# triple quoted strings: Escape sequences still work in triple-quoted strings,
# but single quotes, double quotes, and newlines can be included without escaping them
print('''This string has a single (') and a double (") quote.''')
# with this we can have multi-line strings
print("""This is a
string that spans
across several lines""")
# triple-quoted strings can be used to add an explanatory comment to Python code
