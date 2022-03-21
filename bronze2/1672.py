# n = int(input())
# dna = input()
# list = {"AA":"A","AG":"C","AC":"A","AT":"G","GA":"C","GG":"G","GC":"T","GT":"A","CA":"A","CG":"T"
#         ,"CC":"C","CT":"G","TA":"G","TG":"A","TC":"G","TT":"T"}
# while len(dna) != 1:
#     dna = dna[0:-2] + list[dna[-2:]]
# print(dna)

import sys
input = sys.stdin.readline

n = int(input())
dna = list(input().rstrip())
list = {"AG":"C", "AC":"A", "AT":"G", "GC":"T", "GT":"A", "CT":"G", "GA":"C", "CA":"A", "TA":"G", "CG":"T", "TG":"A","TC":"G"}

a,b = "", dna.pop()
for _ in range(n-1):
    a = dna.pop()
    if a == b:
        continue
    b = list[a+b]
    print("a = ",a)
    print("b = ",b)