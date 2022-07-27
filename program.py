print('Hello, World!', end=' | ')
print(100, end=' | ')
print(5 + 5)

name = 'Josue'
age = 24
print('My name is ' + name)
print(f'I am {age} years old.')

# This is a comment

'''This is another comment
that goes on
and on
and on...'''

# Strings has indexes
name = 'Josue'

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# Slicing in string
print(name[0:3])

# Lenght of my name
print(len(name))

print('python is awesome'.capitalize())
print('python is awesome'.upper())
print('PYTHON IS AWESOME'.lower())

print('PYTHON IS AWESOME'.islower())
print('PYTHON IS AWESOME'.isupper())

print('python is awesome'.replace('python', 'freeCodeCamp'))

# Split and Join strings
print('python is awesome'.split(' '))
print(' '.join(['python', 'is', 'awesome']))

# Working with numbers
a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)  # 2.0

a = 10
b = 5

print(a//b)  # 2

name = input('What is your name? ')
print(f'Your name is {name}')

# If else statement
a = float(input('First: '))
b = float(input('Second: '))
op = input('Operation (sum/sub/mul/div): ')

if op == 'sum':
    print(f'a + b = {a+b}')
elif op == 'sub':
    print(f'a - b = {a-b}')
elif op == 'mul':
    print(f'a * b = {a*b}')
elif op == 'div':
    print(f'a / b = {a/b}')
else:
    print('Invalid Operation!')


a = float(input('First: '))
b = float(input('Second: '))
op = input('Operation (sum/sub/mul/div): ')

match op:
    case 'sum':
        print(f'a + b = {a+b}')
    case 'sub':
        print(f'a - b = {a-b}')
    case 'mul':
        print(f'a * b = {a*b}')
    case 'div':
        print(f'a / b = {a/b}')
    case _:
        print('Invalid Operation!')
