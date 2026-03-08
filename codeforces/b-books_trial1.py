n, t = map(int, input().split())

books = list(map(int,input().split()))


maxCount = 0
left = 0
currentTime = 0

for right in range(n):
    currentTime += books[right]
    while currentTime > t:
        currentTime -= books[left]
        left += 1

    maxCount = max(maxCount, right - left + 1)

print(maxCount)
