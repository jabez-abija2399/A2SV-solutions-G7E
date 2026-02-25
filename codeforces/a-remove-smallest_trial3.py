t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    possible = True
    for i in range(n-1):
        if abs(int(nums[i]) -  int(nums[i+1])) > 1:
            possible = False
            break
            
        
    if possible:
        print("YES")
    else:
        print("NO")
