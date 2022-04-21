#https://www.acmicpc.net/problem/1769

def converter(num,count):
    if len(num) > 1:
        sum = 0
        for i in num:
            sum += int(i)
        converter(str(sum),count+1)
    else:
        print(count)
        if int(num)%3==0:
            print("YES")
        else:
            print("NO")

converter(input(),0)