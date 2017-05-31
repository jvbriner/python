n = int(input())
a = list(map(int, input().split()))

def partitionInPlace(a, start, end):
    pivot = a[end]
    i = start - 1    
    for j in range(start, end):
        if a[j] <= pivot:
            i += 1
            if i != j:
                a[i], a[j] = a[j], a[i]
    a[i+1], a[end] = a[end], a[i+1]
    return i + 1

def qsortInPlace(a, start, end, indent = ""):
    if end - start < 1:
        return
    
    pivotLoc = partitionInPlace(a, start, end)
    
    qsortInPlace(a,start, pivotLoc-1)
    qsortInPlace(a,pivotLoc+1, end)
    
    return

qsortInPlace(a, 0, len(a) - 1)
print(*a)
