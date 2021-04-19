from collections import Counter as di, defaultdict as dt, deque as dq
from itertools import permutations as perv, combinations as comb
from math import ceil as cl, floor as fl, sqrt, log

def solve():
    a, b, c = list(map(int, input().split()))
    ans = b - 1
    ans += min((b - c) + 1 + (a - c), 1 + a) 
    return ans



if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print("Case #{0}: {1}".format(i + 1, solve()))
