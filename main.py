num1 = int(input('enter first num->'))
num2 = int(input('enter second num->'))
num3 = int(input('enter third num->'))

print('| min -> minimum\n| max -> maximum\n| avr -> average ')
op = input('->')
res = ''
if op == 'min':
    if num1 < num2 and num1 < num3:
        res = num1
    elif num2 < num1 and num2 < num3:
        res = num2
    elif num3 < num1 and num3 < num2:
        res = num3
    else:
        res = 'the numbers are equal'
elif op == 'max':
    if num1 > num2 and num1 > num3:
        res = num1
    elif num2 > num1 and num2 > num3:
        res = num2
    elif num3 > num1 and num3 > num2:
        res = num3
    else:
        res = ' the numbers are equal'
elif op == 'avr':
    res = (num1+num2+num3)/3
print(f'res = {res}')
