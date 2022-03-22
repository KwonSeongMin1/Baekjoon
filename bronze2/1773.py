#https://www.acmicpc.net/problem/1773
N, C = map(int, input().split())
c = [0] * (C+1)
for _ in range(N):
    num = int(input())
    if num == 1:
        print(C)
        quit()
    for k in range(num,C+1,num):
        c[k] = 1
print(sum(c))

# In = sys.stdin.readline


# def solution():
#     N, C = map(int, In().split())
#     times = [0] * (C+1)
#     for _ in range(N):
#         f = int(In())
#         if f == 1:
#             return C
#         for i in range(f, C+1, f):
#             times[i] = 1
#     answer = sum(times)
#     return answer


# if __name__ == "__main__":
#     print(solution())
