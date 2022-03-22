#https://www.acmicpc.net/problem/1718
passwd = input()
key = input()
ans = []
for i in range(0,len(passwd),1):
    if passwd[i] != " ":
        num = ord(passwd[i]) - ord(key[i%len(key)])+96
        if num < 97:
            num = num + 26
        ans.append(chr(num))
    else:
        ans.append(" ")
for j in ans:
    print(j, end="")