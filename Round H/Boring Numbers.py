from collections import Counter as di, defaultdict as dt, deque as dq
from itertools import permutations as perv, combinations as comb
from math import ceil as cl, floor as fl, sqrt, log


def boring(a):
    a = str(a)
    l = list(map(str, a))
    for i in range(len(l)):
        if i % 2:
            if int(l[i]) % 2:
                return False
        else:
            if not int(l[i]) % 2:
                return False
    return True

def solve():
    a, b = list(map(int, input().split()))
    cnt = 0
    for i in range(a, b + 1):
        if boring(i):
            cnt += 1
    return cnt


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print("Case #{0}: {1}".format(i + 1, solve()))
