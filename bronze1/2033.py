#https://www.acmicpc.net/problem/20362

digit = 10
h_digit = 5
num = int(input())
while True:

    if num % digit >= h_digit and num > digit:
        num = (((num//digit)+1)*digit)
        digit = digit * 10
        h_digit = h_digit * 10
    elif num % digit < h_digit and num > digit:
        num = (num//digit)*digit
        digit = digit * 10
        h_digit = h_digit * 10
    else:
        break
print(num)