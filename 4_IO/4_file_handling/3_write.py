# to open a file in write mode, use 'w' flag, however you need to be cautious
# while performing this operation as it will overwrite any previous data
with open('4_IO/4_file_handling/new_file.txt', 'w') as file:
    print('file opened in write mode')
    data = 'Some text for my new file.\n'
    file.write(data)  # appends given data after current file pointer

    data = 'More text for my new file.\n'
    file.write(data)

    data = ['Line 1.\n', 'Line 3.\n', 'Line 3.\n']
    file.writelines(data)  # takes input as list of strings
    print('added content to the file')

with open('4_IO/4_file_handling/new_file.txt', 'r') as file:
    print('\nfile opened in read mode')
    data = file.readlines()
    print(data)


# reading from one file and writing it to other
with open('4_IO/4_file_handling/file.txt', 'r') as src, open('4_IO/4_file_handling/file_caps.txt', 'w') as dst:
    print('\nfile.txt opened in read mode')
    print('file_caps.txt opened in write mode')
    data = src.readlines()
    for d in data:
        dst.write(d.upper())
    print('converting data from file.txt to upper case and writing it to file_caps.txt')

with open('4_IO/4_file_handling/file_caps.txt', 'r') as file:
    print('\nfile_caps opened in read mode')
    data = file.readlines()
    print(data)


# opening file in append mode with 'a' allows adding new content to the end of
# existing file, same methods can be used in append mode as write mode, data is
# simple appended to the end of the pre-existing file
with open('4_IO/4_file_handling/new_file.txt', 'a') as file:
    print('\nnew_file opened in append mode')
    data = 'New ending for my file.\n'
    file.write(data)

with open('4_IO/4_file_handling/new_file.txt', 'r') as file:
    print('\nnew_file opened in read mode')
    data = file.readlines()
    print(data)
