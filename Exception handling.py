a = int(input('Enter a number'))
b = int(input('Enter a number'))

try:
    c = a/b
    print(c)

except Exception as e:
    print('Division by zero not possible',e)

finally:
    print('Save the Code')