# to open a file: file = open('path/to/file.extension')
# to close a file: file.close()
file = open('D:/real_python/7_File_handling/file.txt')
file.close()


# to ensure file has closed even if an error occurs, use try: finally: block
file = open('D:/real_python/7_File_handling/file.txt')
try:
    print('processing contents of file')
    x = 1 / 0
    print('file was successfully')
except:
    print('oops an error occured')
finally:
    print('closing the file')
    file.close()


# another way to ensure file is properly closed is to use with: context manager
print()
with open('D:/real_python/7_File_handling/file.txt') as file:
    print('processing file in with context')
# file gets automatically closed once you exit the with context
# This is the most commonly used syntax for opening and closing files
