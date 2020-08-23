def solve():
    n = int(input())
    l = list(map(int, input().split()))
    diff = list()
    for i in range(1, len(l)):
        diff.append(l[i] - l[i - 1])
        
        
    maxi = 0
    cnt = 1
    
    for i in range(1, len(diff)):
        if diff[i] == diff[i - 1]:
            cnt += 1
        else:
            maxi = max(maxi, cnt)
            cnt = 1
    
    return max(maxi, cnt) + 1


n = int(input())
for i in range(n):
    print("Case #{0}: {1}".format(i + 1, solve()))
