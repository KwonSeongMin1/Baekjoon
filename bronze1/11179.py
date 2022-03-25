#https://www.acmicpc.net/problem/11179

n=int(input())
digit_n=[]
rev_n = 0
while n != 0:
    digit_n.append(n%2)
    n = n // 2
for i in range(len(digit_n)):
    rev_n = rev_n + digit_n[len(digit_n)-1-i] * 2**i
    
print(rev_n)