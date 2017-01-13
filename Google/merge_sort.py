def mergesort(x):
    result = []
    if len(x) < 2: return x
    mid = len(x)/2
    left = mergesort(x[:mid])
    right = mergesort(x[mid:])
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result += left[i:]
    result += right[j:]