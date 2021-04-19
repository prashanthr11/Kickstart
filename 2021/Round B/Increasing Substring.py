def solve():
    c = input()
    s = input()
    '''
    T.C: O(N)
    S.C: O(N)
    
    cnt = 1
    last = 'z'
    ret = list()
    
    for i in s:
        if i > last:
            cnt += 1
        else:
            cnt = 1
            
        last = i
        ret.append(cnt)
        
    print(*ret)
    '''
    
    cnt = 1
    print(cnt, end = ' ')
    for i in range(1, len(s)):
        if s[i] > s[i - 1]:
            cnt += 1
        else:
            cnt = 1
        print(cnt, end = ' ')
        
    print()
    
    
if __name__ == '__main__':
    for i in range(int(input())):
        print("Case{0}: ".format(i + 1), end = '')
        solve()
