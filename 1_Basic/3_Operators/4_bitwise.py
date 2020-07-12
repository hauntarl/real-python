# Bitwise operators treat operands as sequences
# of binary digits and operate on them bit by bit.
# list of operators...
# & - AND
# | - OR
# ~ - NOT
# ^ - XOR
# >> - SHIFT_RIGHT
# << - SHIFT_LEFT

print('0b{:04b}'.format(0b1100 & 0b1010))
print('0b{:04b}'.format(0b1100 | 0b1010))
print('0b{:04b}'.format(0b1100 ^ 0b1010))
print('0b{:04b}'.format(0b1100 >> 2))
print('0b{:04b}'.format(0b0011 << 2))
