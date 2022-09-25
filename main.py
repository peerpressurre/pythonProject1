number = int(input('number->')) #->1234
x1 = number%10 #123->4
number=int(number/10)
x2 = number%10 #12->3
number=int(number/10)
x3 = number%10 #1->2
number=int(number/10)
x4 = number #1
res = int(x1*1000+x2*100+x3*10+x4)

print(res)