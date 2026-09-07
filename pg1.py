n=int(input())
bin_string=bin(n)
binary=bin_string[2:]
b1=binary.replace('0','x')
b2=b1.replace('1','0')
b3=b2.replace('x','1')
result=int(b3,2)
print(result)
