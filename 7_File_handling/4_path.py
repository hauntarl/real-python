# Files are located via file paths, a string that represents the location of a
# file. File paths are broken up in 3 major paths:
# 1. path
# 2. file name
# 3. extension

# There are to types of paths:
# 1. Relative paths - for windows
# my_file.py - file in current directory
# data\info.txt - file in subdirectory from current directory
# ..\peers\folder\data\config.txt - .. go one level up in directory tree
# NOTE: Relative path for other OS are same as that of windows but with one
# exception, instead of back slash they use forward slash
# 2. Absolute paths
# for windows - it will begin with a drive letter like 'C'
# C:\Users\anony\Downloads
# for mac and linux - they contain only folder names

# dealing with different separators, the os module will create system specific
# separators based on current operating system
import os


# building relative path
file_path = os.path.join('real_python', '7_File_handling', 'file.txt')
print(file_path)  # windows will give back slashes

# building absolute file path
file_path = os.path.join('D:', os.sep, 'real_python',
                         '7_File_handling', 'file.txt')
print(file_path)

with open(file_path) as file:
    print('\nopening file in read mode')
    data = file.readlines()
    print(data)
