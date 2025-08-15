print("Enter first number:")
fnum = float(input())

print("Enter operator(+, -, *, /):")
ope = input()

print("Enter second number:")
snum = float(input())

if ope == '+':
    result = fnum + snum
    print(result)
    
elif ope == '-':
    result = fnum - snum
    print(result)

elif ope == '*':
    result= fnum * snum
    print(result)

elif ope == '/':
    if fnum != 0:
        result = fnum / snum
        print(result)
    else:
     print("Invalid can't divide with zero")
    
