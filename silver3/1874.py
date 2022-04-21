stack = []  #스택을 쌓아줄 배열
num = []    #입력받은 배열
res = []    #결과값 배열
judge = []  #+,- 출력시키는 것을 도와줄 배열

n = int(input())

for _ in range(n):
    i = int(input())
    num.append(i)

i = 0   #입력받은 배열의 위치를 지정해 줄 변수
count = 0   #
while len(res) != n:    #결과값 배열이 완전히 차기 전 까진 계속 반복
    if num[i] > count:
        count += 1
    else:
        res.append(stack.pop())
        judge.append(0)
        i += 1
        continue
    stack.append(count)
    judge.append(1)

if num != res:
    print("NO")
else:
    for i in range(len(judge)):
        if judge[i]:
            print("+")
        else:
            print("-")
