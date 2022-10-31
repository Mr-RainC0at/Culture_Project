li = [354, 65, 874, 124, 32, 50, 177, 195, 78, 94]

for i in range(len(li)-1):
    minId = i
    for k in range(i+1, len(li)):
        if li[minId] > li[k]:
            minId = k
    tmp = li[i]
    li[i] = li[minId]
    li[minId] = tmp
    print(li)
