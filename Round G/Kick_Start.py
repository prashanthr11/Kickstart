from collections import Counter as di, defaultdict as dt, deque as dq
from itertools import permutations as perv, combinations as comb
from math import ceil as cl, floor as fl, sqrt, log

def solve():
    s = input()
    ans, cnt = 0, 0
    st, en = 'KICK', 'START'
    
    for i in range(len(s) - len(st)):
        if s[i:i + len(st)] == st:
            cnt += 1
        if s[i:i + len(en)] == en:
            ans += cnt
    return ans



if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print("Case #{0}: {1}".format(i + 1, solve()))
