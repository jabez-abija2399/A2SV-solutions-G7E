n,m = map(int, input().split())

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

fir = 0
sec = 0
result = []
while fir < n and sec < m:
    if num1[fir] < num2[sec]:
        result.append(num1[fir]) 
        fir += 1
    else:
        result.append(num2[sec]) 
        sec += 1
result.extend(num1[fir:])
result.extend(num2[sec:])
print(*result)
