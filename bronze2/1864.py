def getops(c,x):
    num=0
    if x == '-':
        num = num + 0*(8**c)
    if x == '\\':
        num = num + 1*(8**c)
    if x == '(':
        num = num + 2*(8**c)
    if x == '@':
        num = num + 3*(8**c)
    if x == '?':
        num = num + 4*(8**c)
    if x == '>':
        num = num + 5*(8**c)
    if x == '&':
        num = num + 6*(8**c)
    if x == '%':
        num = num + 7*(8**c)
    if x == '/':
        num = num + -1*(8**c)
    c = c + 1
    if(c > 3):
        c = 0
    return num

while True:
    ops = input()
    if ops == '#': break
    res = 0
    count = 0
    if len(ops) > 8:    
        for i in range(7, -1, -1):
            res = res + getops(count, ops[i])
            count = count + 1
    else:
        for i in range(len(ops)-1,-1,-1):
            res = res + getops(count, ops[i])
            count = count + 1
    print(res)
    
