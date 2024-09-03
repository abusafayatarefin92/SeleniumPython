arithmatic_x = 25
arithmatic_y = 8

#Arithmetic Operators
print('Arithmetic Operators')
print(arithmatic_x + arithmatic_y) #add
print(arithmatic_x - arithmatic_y) #subtraction
print(arithmatic_x * arithmatic_y) #multiplication
print(arithmatic_x / arithmatic_y) #division
print(arithmatic_x % arithmatic_y) #modular operator (remainder)
print(arithmatic_x ** arithmatic_y) #exponentiation (power)
print(arithmatic_x // arithmatic_y) #round the result to the nearest whole number

#Assignment Operators
print('\n' + 'Assignment Operators')
assignment_x = 10
assignment_y = 3
assignment_x += assignment_y
print(assignment_x)
assignment_x -= assignment_y
print(assignment_x)
assignment_x *= assignment_y
print(assignment_x)
assignment_x **= assignment_y
print(assignment_x)
assignment_x /= assignment_y
print(assignment_x)
assignment_x //= assignment_y
print(assignment_x)
assignment_x %= assignment_y
print(assignment_x)

#Comparison Operators
print('\n' + 'Comparison Operators')
compairon_x = 10
comparison_y = 5
print(compairon_x == comparison_y)
print(compairon_x != comparison_y)
print(compairon_x > comparison_y)
print(compairon_x < comparison_y)
print(compairon_x <= comparison_y)
print(compairon_x >= comparison_y)

#Logical Operators
print('\n' + 'Logical Operators')
logical_x = 10
logical_y = 6
print(logical_x == logical_y and logical_x > logical_y)
print(logical_x == logical_y or logical_x > logical_y)

#Identity Operators
print('\n' + 'Identity Operators')
identity_x = ['academy', 'ok']
identity_y = ['academy', 'ok']
print(identity_x is identity_y)
print(identity_x is not identity_y)
print(identity_x == identity_y)

#Membership Operator
print('\n' + 'Membership Operator')
membership_x = ['academy', 'ok']
membership_y = ['academy', 'ok']
print('ok' in membership_x)
print('ok' not in membership_x)

#Bitwise Operators
print('\n' + 'Bitwise Operators')
print('& - AND')
print('| - OR')
print('~ - NOT')
print('^ - XOR')

print('\n' + 'Bitwise value')
print('0 - 00')
print('1 - 01')
print('2 - 10')
print('3 - 11')
print('4 - 100')
print('5 - 101')
print('6 - 110')
print('7 - 111')
print('8 - 1000')
print('9 - 1001')
print('10 - 1010')

print()

bitwise_x = 1
bitwise_y = 2
bitwise_z = ~bitwise_x
print(bitwise_x & bitwise_y)
print(bitwise_x | bitwise_y)
print(bitwise_z)
print(bitwise_x ^ bitwise_y)