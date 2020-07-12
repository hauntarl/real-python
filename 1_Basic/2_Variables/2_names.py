print('VARIABLE NAMES:')
# Variable names in Python can be any length and can consist 
# of uppercase and lowercase letters (A-Z, a-z), digits (0-9), 
# and the underscore character (_). An additional restriction is that, 
# although a variable name can contain digits, the first character of a 
# variable name cannot be a digit.
# One of the additions to Python 3 was full Unicode support, 
# which allows for Unicode characters in a variable name as well.
name = 'Bob'
Age = 54
has_W2 = True
print(name, Age, has_W2)
# 1099_filed = False  # invalid

# Note that case is significant. Lowercase and uppercase letters are not the same. 
# Use of the underscore character is significant as well.
numberofcollegegraduates = 2500  # harder to read
NUMBEROFCOLLEGEGRADUATES = 2500  # harder to read
numberOfCollegeGraduates = 2500  # camelCase
NumberOfCollegeGraduates = 2500  # PascalCase
number_of_college_graduates = 2500  # snake_case
# snake_casae should be used for functions and variable names.
# PascalCase should be used for class names.
# Naming convention: https://www.python.org/dev/peps/pep-0008/#naming-conventions
# Refer: https://www.python.org/dev/peps/pep-0008/


print('\nRESERVED KEYWORDS:')
# Language reserves a small set of keywords that designate special language functionality.
print(help('keywords'))  # see all the reserved keywords
print(help('None'))  # while running press 'q' to exit the blocking state
