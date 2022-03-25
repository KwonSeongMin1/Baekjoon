#https://www.acmicpc.net/problem/15722

from tkinter import Y


n = int(input())

x,y=0,0
count = 1;

for i in range(n):
    if x == y and x > 0:
        count = -count
    if x == y and x < 0:
        count = abs(count)
        count = count + 1
    if y != count:
        if count > 0:
            y = y + 1
        else:
            y = y - 1
    elif x != count:
        if count > 0:
            x = x + 1
        else:
            x = x - 1
        
print(x,y)