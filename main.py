num1 = int(input('enter first num->'))
num2 = int(input('enter second num->'))
num3 = int(input('enter third num->'))

print('| + -> sum\n| * -> mul')
op = input('->')
res = ''
if op == '+':
    res = num1+num2+num3
elif op == '*':
    res = num1*num2*num3

print(f'res = {res}')