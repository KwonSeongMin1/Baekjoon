a = [1,2,3,4,5]
size = len(a)-1
for i in range(100):
    if size == -1:
        size = len(a)-1
    print(a[size])
    size -= 1
    
