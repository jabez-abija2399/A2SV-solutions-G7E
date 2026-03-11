n, s = map(int,input().split())
segment = list(map(int,input().split()))

sumSeg = 0
maxCount = float('-inf')
left = 0

for right in range(n):
    sumSeg += segment[right]
    while sumSeg > s:
        sumSeg -= segment[left]
        left += 1
    maxCount = max(maxCount, right - left + 1)

print(maxCount)
