n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

if k == 0:
    if arr[0] > 1:
        print(arr[0] - 1)
    else:
        print(-1)
else:
    numX = arr[k-1]
    count = 0
    for num in arr:
        if num <= numX:
            count += 1
    if count == k:
        print(numX)
    else:
        print(-1)