n,m = map(int,input().split())
chess = []  #체스 배열
result = [] #결과값 저장용
for _ in range(n):
    chess.append(list(input())) #체스판 만들기

for i in range(n-7):    
    for j in range(m-7):
        #8x8 체스판이 들어갈 수 있는만큼 반복
        count1 = 0
        count2 = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                #8x8 체스판 부위별로 파악
                if (x+y) % 2 == 0:
                    #첫 번째 부위가 흰색일 때와 검은색일 때로 나눠서 판별
                    if chess[x][y] != 'W':
                        count1 += 1
                    if chess[x][y] != 'B':
                        count2 += 1
                else:
                    if chess[x][y] != 'W':
                        count2 += 1
                    if chess[x][y] != 'B':
                        count1 += 1
        result.append(count1)
        result.append(count2)
print(min(result))
