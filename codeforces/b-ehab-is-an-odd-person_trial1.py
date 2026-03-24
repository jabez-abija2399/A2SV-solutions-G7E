

    n = int(input())
    arr = list(map(int, input().split()))
     
    odd = any(x % 2 == 1 for x in arr)
    even = any(x % 2 == 0 for x in arr)
     
    if odd and even:
        arr.sort()
     
    print(*arr)