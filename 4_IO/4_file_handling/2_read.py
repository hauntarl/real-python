with open('4_IO/4_file_handling/file.txt') as file:
    data = file.read(10)  # reading 10 bytes from the file
    print(data)

    data = file.readline()  # reads a single line from current file pointer
    print(data)

    data = file.readlines()  # reads contents of file as a list
    print(data)

# the default mode for open() is read, which only permits reading from a file
# if file doesn't exists then it will throw an error. However it is possible to
# to explicitly provide the read argument to the function
with open('4_IO/4_file_handling/file.txt', 'r') as file:
    data = file.readlines()
    print(data)

# modes: r, w, a. for binary: rb, wb, ab
