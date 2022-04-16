n = int(input())
count = 0
for i in range(666,1000000000): #666부터 반복
    if "666" in str(i): #만약 숫자 안에 666이 포함되면
        count += 1 #666 ,1666 ,2666 ... 의 숫자 번호 count
        if count == n:  #내가 찾는 번호의 숫자이면? break
            print(i)
            break