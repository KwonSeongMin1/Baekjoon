while True:
    num = input()
    if num == '0': break
    if len(num) == 1:
        print("yes")
    elif len(num) <= 3 and num[0] == num[-1]:
        print("yes")
    elif len(num) > 3 and num[0] == num[-1] and num[1] == num[-2]:
        print("yes")
    else:
        print("no")