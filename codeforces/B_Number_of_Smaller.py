n, m = map(int, input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

first = 0
result = []

for second in range(len(arr2)):
    while first < len(arr1) and  arr1[first] < arr2[second]:
        first += 1  
    result.append(first)
print(*result)
