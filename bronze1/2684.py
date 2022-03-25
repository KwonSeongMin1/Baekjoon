#https://www.acmicpc.net/problem/2684

P = int(input())
case_1 = "TTT"
case_2 = "TTH"
case_3 = "THT"
case_4 = "THH"
case_5 = "HTT"
case_6 = "HTH"
case_7 = "HHT"
case_8 = "HHH"
for _ in range(P):
    res = [0] * 8
    case = input()
    for i in range(38):
        if case[i] + case[i+1] + case[i+2] == case_1:
            res[0] = res[0] + 1
        if case[i] + case[i+1] + case[i+2] == case_2:
            res[1] = res[1] + 1
        if case[i] + case[i+1] + case[i+2] == case_3:
            res[2] = res[2] + 1
        if case[i] + case[i+1] + case[i+2] == case_4:
            res[3] = res[3] + 1
        if case[i] + case[i+1] + case[i+2] == case_5:
            res[4] = res[4] + 1
        if case[i] + case[i+1] + case[i+2] == case_6:
            res[5] = res[5] + 1
        if case[i] + case[i+1] + case[i+2] == case_7:
            res[6] = res[6] + 1
        if case[i] + case[i+1] + case[i+2] == case_8:
            res[7] = res[7] + 1
    print(' '.join(map(str,res)))