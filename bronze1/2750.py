count = int(input())
list = []
for _ in range(count):
    num = input()
    list.append(int(num))
list.sort()
for _ in list:
    print(_)