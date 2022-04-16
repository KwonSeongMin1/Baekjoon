word = []
length = 1
for i in range(int(input())):
    w = input()
    if w not in word:
        word.append(w)
word.sort()
while len(word):
    flag = 1
    for i in range(len(word)):
        if len(word[i]) == length:
            print(word[i])
            word.pop(word.index(word[i]))
            flag = 0
            break
    if flag:
        length += 1
