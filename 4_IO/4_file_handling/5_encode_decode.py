# the open() function also supports an encoding parameter, which specifies the
# type of character. eg. ascii, utf-8 (python default), utf-16
with open('4_IO/4_file_handling/uni.txt', 'w', encoding='utf-8') as file:
    print('file opened in write mode with utf-8 encoding')
    file.write('Ͷ, Θ, Ξ, Ψ, Ω')
# NOTE: if the encoding is changed to ascii, then it raises UnicodeEncodeError

with open('4_IO/4_file_handling/uni.txt', 'r') as file:
    print('\nfile opened in read mode with utf-8 encoding')
    data = file.readline()
    print(data)
