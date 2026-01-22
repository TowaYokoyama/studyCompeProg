import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
#----------------------------------------#
import itertools
#----------------------------------------#
def dfs(idx, rem, u):
    if idx == n - 1:
        u.append(s[p[idx]])
        if 3 <= len("".join(u)) <= 16 and "".join(u) not in t:
            print("".join(u))
            exit()
        else: return
    nu = u + [s[p[idx]]] + ["_"]
    for k in range(rem + 1):
        dfs(idx + 1, rem - k, nu + ["_"] * k)
    return

n, m = map(int, input().split())
s = [input().strip() for _ in range(n)]
t = set(input().strip() for _ in range(m))
cnt = 16 - sum(len(s[i]) for i in range(n)) - n + 1
for p in itertools.permutations(list(range(n))):
    dfs(0, cnt, [])
print(-1)
