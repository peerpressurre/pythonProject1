num = int(input('enter number->'))

print('mi -> mile\nin -> inch\nyd -> yard')
op = input('->')
res = ''
if op == 'mi':
    res = int(num*0.000621371)
elif op == 'in':
    res = int(num*39.370)
elif op == 'yd':
    res = int(num*1.0936)

print(f'res = {res}')
